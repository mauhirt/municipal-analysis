"""Geocode the 578 crosswalk cities to get centroid coordinates."""
import pandas as pd
import time
from geopy.geocoders import Nominatim
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
crosswalk = pd.read_csv(ROOT / "raw" / "crosswalk" / "Crosswalk.csv")

geolocator = Nominatim(user_agent="muni_bond_city_centroids", timeout=15)

results = []
for idx, (_, row) in enumerate(crosswalk.iterrows()):
    fips = row["fips7"]
    city = row["geo_name"]
    state = row["state_abb"]
    name_city = row.get("NAME_city", "")

    # Try geo_name + state first
    query = f"{city}, {state}, USA"
    location = None
    try:
        location = geolocator.geocode(query, exactly_one=True, country_codes="us")
    except Exception as e:
        print(f"  ERROR [{idx}] {city}, {state}: {e}")
        time.sleep(2)
        try:
            location = geolocator.geocode(query, exactly_one=True, country_codes="us")
        except Exception:
            pass

    if location:
        results.append({
            "fips7": fips,
            "geo_name": city,
            "state_abb": state,
            "city_lat": location.latitude,
            "city_lng": location.longitude,
            "geocoded_address": location.address,
            "status": "OK",
        })
    else:
        # Fallback: try full NAME_city
        try:
            location = geolocator.geocode(name_city, exactly_one=True, country_codes="us")
        except Exception:
            pass
        if location:
            results.append({
                "fips7": fips,
                "geo_name": city,
                "state_abb": state,
                "city_lat": location.latitude,
                "city_lng": location.longitude,
                "geocoded_address": location.address,
                "status": "OK_FALLBACK",
            })
        else:
            results.append({
                "fips7": fips,
                "geo_name": city,
                "state_abb": state,
                "city_lat": None,
                "city_lng": None,
                "geocoded_address": None,
                "status": "NOT_FOUND",
            })

    time.sleep(1.05)
    if (idx + 1) % 50 == 0:
        ok = sum(1 for r in results if r["status"].startswith("OK"))
        print(f"  Progress: {idx+1}/578 | OK: {ok}", flush=True)
        # Periodic save so we don't lose progress
        pd.DataFrame(results).to_csv("/tmp/crosswalk_city_centroids.csv", index=False)

rdf = pd.DataFrame(results)
rdf.to_csv("/tmp/crosswalk_city_centroids.csv", index=False)
print(f"Done. OK: {(rdf['status'].str.startswith('OK')).sum()}/578", flush=True)
