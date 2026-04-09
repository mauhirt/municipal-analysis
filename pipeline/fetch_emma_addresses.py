"""
Fetch issuer addresses from MSRB EMMA for municipal bond issuers.

Workflow:
1. Load Bloomberg issuer CSV
2. Fetch all EMMA issuer IDs by state (from state pages)
3. Match Bloomberg issuers to EMMA issuers by name
4. Fetch each matched issuer's EMMA detail page for address info
5. Save results to CSV
"""

import csv
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "raw"
BLOOMBERG_CSV = RAW_DIR / "bloomberg" / "All_US_Municipal_Bond_Issuers.csv"
OUTPUT_DIR = RAW_DIR / "emma"
EMMA_ISSUERS_CACHE = OUTPUT_DIR / "emma_issuers_by_state.json"
OUTPUT_CSV = OUTPUT_DIR / "issuer_addresses.csv"
PROGRESS_FILE = OUTPUT_DIR / "fetch_progress.json"

EMMA_BASE = "https://emma.msrb.org"

US_STATES = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY",
    "DC", "PR", "VI", "GU", "AS", "MP",
]


def make_session():
    """Create a requests session with EMMA cookies."""
    session = requests.Session()
    session.headers.update({
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
    })
    session.cookies.set("Disclaimer6", "msrborg", domain="emma.msrb.org", path="/")
    return session


def fetch_state_issuers(session, state, retries=3):
    """Fetch all issuers for a state from the EMMA state page."""
    url = f"{EMMA_BASE}/IssuerHomePage/State?state={state}"
    for attempt in range(retries):
        try:
            r = session.get(url, timeout=30)
            r.raise_for_status()
            match = re.search(r"var issuers = (\[.*?\]);", r.text, re.DOTALL)
            if match:
                return json.loads(match.group(1))
            return []
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2 ** (attempt + 1))
            else:
                print(f"  ERROR fetching {state}: {e}")
                return []


def fetch_all_state_issuers(session):
    """Fetch issuer lists for all states. Uses cache if available."""
    if EMMA_ISSUERS_CACHE.exists():
        print(f"Loading cached EMMA issuers from {EMMA_ISSUERS_CACHE}")
        with open(EMMA_ISSUERS_CACHE) as f:
            return json.load(f)

    all_issuers = {}
    for i, state in enumerate(US_STATES):
        print(f"  [{i+1}/{len(US_STATES)}] Fetching issuers for {state}...", end="", flush=True)
        issuers = fetch_state_issuers(session, state)
        all_issuers[state] = issuers
        print(f" {len(issuers)} issuers")
        time.sleep(0.5)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(EMMA_ISSUERS_CACHE, "w") as f:
        json.dump(all_issuers, f)
    print(f"Cached {sum(len(v) for v in all_issuers.values())} issuers to {EMMA_ISSUERS_CACHE}")
    return all_issuers


def normalize_name(name):
    """Normalize issuer name for matching."""
    name = name.upper().strip()
    # Remove common suffixes/noise
    name = re.sub(r"\s+", " ", name)
    # Remove punctuation except ampersand
    name = re.sub(r"[,.'\"()]", "", name)
    return name


def build_emma_lookup(all_issuers):
    """Build a lookup dict: (state, normalized_name) -> issuer record."""
    lookup = {}
    for state, issuers in all_issuers.items():
        for iss in issuers:
            key = (state, normalize_name(iss["nm"]))
            lookup[key] = iss
    return lookup


def load_bloomberg_issuers():
    """Load the Bloomberg CSV."""
    issuers = []
    with open(BLOOMBERG_CSV, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            issuers.append(row)
    return issuers


def match_issuers(bloomberg_issuers, emma_lookup):
    """Match Bloomberg issuers to EMMA issuers by state + name."""
    matched = []
    unmatched = []
    for row in bloomberg_issuers:
        state = row["State"].strip()
        name = row["Issuer Name"].strip()
        key = (state, normalize_name(name))
        emma_rec = emma_lookup.get(key)
        if emma_rec:
            matched.append({
                "state": state,
                "bloomberg_name": name,
                "issuer_type": row.get("Issuer Type", ""),
                "emma_id": emma_rec["id"],
                "emma_type": emma_rec["tp"],
                "emma_name": emma_rec["nm"],
            })
        else:
            unmatched.append(row)
    return matched, unmatched


def parse_address_from_page(html):
    """Extract address info from an EMMA issuer detail page."""
    soup = BeautifulSoup(html, "lxml")
    result = {
        "issuer_display_name": "",
        "contact_name": "",
        "address_line1": "",
        "address_line2": "",
        "city": "",
        "address_state": "",
        "zip_code": "",
        "phone": "",
        "email": "",
        "website": "",
    }

    # Extract displayed issuer name (e.g., "CITY OF DOTHAN, ALABAMA (AL)")
    h3 = soup.find("h3", string=re.compile(r"\(\w{2}\)\s*$"))
    if h3:
        result["issuer_display_name"] = h3.get_text(strip=True)

    # Find contact info section
    contact_h4 = soup.find("h4", string=re.compile(r"Contact Information", re.I))
    if not contact_h4:
        return result

    card_body = contact_h4.find_parent("div", class_="card-body")
    if not card_body:
        return result

    # Get contact list items
    contact_ul = card_body.find("ul", class_="fs14")
    if contact_ul:
        items = [li.get_text(strip=True) for li in contact_ul.find_all("li")]
        _parse_contact_items(items, result)

    # Get website
    website_div = card_body.find("div", class_="issuer-info-websites")
    if website_div:
        link = website_div.find("a")
        if link:
            result["website"] = link.get_text(strip=True)

    return result


def _parse_contact_items(items, result):
    """Parse the list of contact info items into structured fields."""
    address_lines = []

    for item in items:
        item = item.strip()
        if not item:
            continue

        # Phone pattern
        if re.match(r"^\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}", item):
            result["phone"] = item
            continue

        # Email pattern
        if re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", item):
            result["email"] = item
            continue

        # City, State ZIP pattern (e.g., "Boston, MA 02108")
        city_match = re.match(
            r"^(.+?),\s*([A-Z]{2})\s+(\d{5}(?:-\d{4})?)$", item
        )
        if city_match:
            result["city"] = city_match.group(1).strip()
            result["address_state"] = city_match.group(2)
            result["zip_code"] = city_match.group(3)
            continue

        # Otherwise it's either a contact name or address line
        address_lines.append(item)

    # First non-address-looking line is likely the contact name
    # Address lines typically contain numbers or street words
    street_pattern = re.compile(
        r"\d|Street|St\b|Avenue|Ave\b|Boulevard|Blvd\b|Drive|Dr\b|"
        r"Road|Rd\b|Lane|Ln\b|Suite|Ste\b|Floor|P\.?O\.?\s*Box|Way\b|"
        r"Circle|Court|Ct\b|Place|Pl\b|Highway|Hwy\b|Plaza",
        re.I,
    )

    name_assigned = False
    addr_idx = 0
    for line in address_lines:
        if not name_assigned and not street_pattern.search(line):
            result["contact_name"] = line
            name_assigned = True
        else:
            if addr_idx == 0:
                result["address_line1"] = line
            else:
                result["address_line2"] = line
            addr_idx += 1


def fetch_issuer_address(session, emma_id, emma_type, retries=3):
    """Fetch an issuer's detail page and extract address info."""
    url = f"{EMMA_BASE}/IssuerHomePage/Issuer?id={emma_id}&type={emma_type}"
    for attempt in range(retries):
        try:
            r = session.get(url, timeout=30)
            r.raise_for_status()
            return parse_address_from_page(r.text)
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2 ** (attempt + 1))
            else:
                print(f"  ERROR fetching issuer {emma_id}: {e}")
                return None


def load_progress():
    """Load set of already-fetched issuer IDs."""
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE) as f:
            return set(json.load(f))
    return set()


def save_progress(done_ids):
    """Save set of fetched issuer IDs."""
    with open(PROGRESS_FILE, "w") as f:
        json.dump(list(done_ids), f)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    session = make_session()

    # --- Step 1: Fetch all EMMA issuer IDs by state ---
    print("=" * 60)
    print("Step 1: Fetching EMMA issuer lists by state")
    print("=" * 60)
    all_issuers = fetch_all_state_issuers(session)
    total_emma = sum(len(v) for v in all_issuers.values())
    print(f"Total EMMA issuers across all states: {total_emma}")

    # --- Step 2: Match Bloomberg issuers to EMMA ---
    print("\n" + "=" * 60)
    print("Step 2: Matching Bloomberg issuers to EMMA")
    print("=" * 60)
    bloomberg_issuers = load_bloomberg_issuers()
    print(f"Bloomberg issuers: {len(bloomberg_issuers)}")

    emma_lookup = build_emma_lookup(all_issuers)
    matched, unmatched = match_issuers(bloomberg_issuers, emma_lookup)
    print(f"Matched: {len(matched)}")
    print(f"Unmatched: {len(unmatched)}")

    # Deduplicate by emma_id (multiple Bloomberg names can map to same EMMA issuer)
    seen_ids = set()
    unique_matched = []
    for m in matched:
        if m["emma_id"] not in seen_ids:
            seen_ids.add(m["emma_id"])
            unique_matched.append(m)
    print(f"Unique EMMA issuers to fetch: {len(unique_matched)}")

    # Separate type M (managed/customized pages with addresses) from
    # type G (generic bond-level entries, no contact info on EMMA).
    type_m = [m for m in unique_matched if m["emma_type"] == "M"]
    type_g = [m for m in unique_matched if m["emma_type"] != "M"]
    print(f"  Type M (have EMMA pages with addresses): {len(type_m)}")
    print(f"  Type G (bond-level, no contact info):    {len(type_g)}")

    # --- Step 3: Fetch addresses for type M issuers ---
    print("\n" + "=" * 60)
    print("Step 3: Fetching issuer addresses from EMMA (type M only)")
    print("=" * 60)
    done_ids = load_progress()
    print(f"Already fetched: {len(done_ids)}")

    # Load existing results if resuming
    results = []
    if OUTPUT_CSV.exists() and done_ids:
        with open(OUTPUT_CSV, newline="") as f:
            reader = csv.DictReader(f)
            results = list(reader)
        print(f"Loaded {len(results)} existing results")

    to_fetch = [m for m in type_m if m["emma_id"] not in done_ids]
    print(f"Type M remaining to fetch: {len(to_fetch)}")

    fieldnames = [
        "state", "bloomberg_name", "issuer_type", "emma_id", "emma_type",
        "emma_name", "issuer_display_name", "contact_name",
        "address_line1", "address_line2", "city", "address_state",
        "zip_code", "phone", "email", "website",
    ]

    batch_size = 50
    for i in range(0, len(to_fetch), batch_size):
        batch = to_fetch[i : i + batch_size]
        print(f"\n  Batch {i // batch_size + 1} "
              f"({i+1}-{min(i+len(batch), len(to_fetch))} of {len(to_fetch)})")

        for j, m in enumerate(batch):
            addr = fetch_issuer_address(session, m["emma_id"], m["emma_type"])
            row = {**m}
            if addr:
                row.update(addr)
            results.append(row)
            done_ids.add(m["emma_id"])

            # Rate limit: ~1 request per second to avoid 403
            time.sleep(1.0)

            if (j + 1) % 10 == 0:
                print(f"    {j+1}/{len(batch)} done")

        # Save after each batch
        with open(OUTPUT_CSV, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(results)
        save_progress(done_ids)
        print(f"  Saved progress: {len(results)} type M rows")

    # --- Step 4: Add type G issuers (no address fetch needed) ---
    print("\n" + "=" * 60)
    print("Step 4: Adding type G issuers (no EMMA address available)")
    print("=" * 60)
    for m in type_g:
        row = {**m}
        # Leave address fields empty -- these issuers have not provided
        # contact information on EMMA.
        results.append(row)
    print(f"Added {len(type_g)} type G issuers")

    # Final save
    with open(OUTPUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(results)

    # --- Summary ---
    has_address = sum(1 for r in results if r.get("address_line1"))
    print("\n" + "=" * 60)
    print("DONE")
    print("=" * 60)
    print(f"Total results: {len(results)}")
    print(f"With address: {has_address}")
    print(f"Without address: {len(results) - has_address}")
    print(f"Output: {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
