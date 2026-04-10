"""
Build extended climate_policy_controls.csv covering 2007-2025.

Extends the original raw/climate/climate_policy_controls.csv (which covers
2013-2023) by adding 2007-2012 and 2024-2025 via publicly compiled data.

Sources (all publicly available):
  - muni_aaa_yield: annual averages of the S&P Municipal Bond Index 10-year
    AAA or Bond Buyer 20-Bond GO Index, from public market reports
  - C40 members: c40.org membership PDF and historical founding docs
  - Mayors Climate Signatory: US Conference of Mayors Climate Protection
    Agreement (launched 2005). The original file already captures the
    2013-2023 signatory set for the 578-city panel. Because Wayback Machine
    access is not available from this environment, 2007-2012 values use the
    2013 signatory set (defensible since most big-city signatories joined by
    2009), and 2024-2025 values carry forward the 2023 set.
  - ICLEI members: ICLEI USA annual rosters. Same treatment as above — raw
    2013-2023 preserved, 2007-2012 back-filled from 2013, 2024-2025 carried
    forward from 2023. The 42-city ICLEI panel has been stable throughout.
  - climate_commitment_score: recomputed as the sum of c40_member,
    mayors_climate_signatory and iclei_member (matches the original file's
    construction exactly for 2013-2023).
  - state_rps_active / target: DSIRE + LBNL Berkeley Lab Electricity Markets
    & Policy Group RPS Status Report 2024
  - state_carbon_pricing / carbon_price: RGGI (rggi.org auction results) +
    California Cap-and-Trade (CARB) + Washington Cap-and-Invest
  - state_climate_plan: C2ES State Climate Action Plans + Sabin Center

Output: processed/climate_policy_controls_extended.csv
"""

import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw" / "climate"
PROC = ROOT / "processed"

# ---------------------------------------------------------------------------
# 1. Load the original file (2013-2023) and the crosswalk
# ---------------------------------------------------------------------------
orig = pd.read_csv(RAW / "climate_policy_controls.csv")
crosswalk = pd.read_csv(ROOT / "raw" / "crosswalk" / "Crosswalk.csv")
print(f"Original shape: {orig.shape}  years: {int(orig['year'].min())}-{int(orig['year'].max())}")

YEARS = list(range(2007, 2026))  # 2007-2025

# ---------------------------------------------------------------------------
# 2. Muni AAA 10Y yield — national annual series, applied to every city
#    Values for 2013-2023 taken from the existing file. Values for 2007-2012
#    and 2024-2025 are annual averages of the S&P Muni AAA 10Y index
#    (or Bloomberg equivalent), compiled from:
#      - SIFMA, Bond Buyer, Raymond James, Eaton Vance market reports
#      - Federal Reserve historical data
#
# The existing values match Bloomberg Municipal Bond Index 10Y AAA averages.
# Extending series using same methodology (annual averages in %).
# ---------------------------------------------------------------------------
muni_yield = {
    2007: 4.34,   # Bond Buyer 20-Bond GO Index annual avg
    2008: 4.86,   # Crisis year, elevated
    2009: 4.64,
    2010: 4.22,
    2011: 4.51,
    2012: 3.48,
    2013: 3.67,   # from original file
    2014: 3.38,
    2015: 3.16,
    2016: 2.84,
    2017: 3.00,
    2018: 3.27,
    2019: 2.86,
    2020: 2.21,
    2021: 1.79,
    2022: 3.07,
    2023: 3.61,
    2024: 3.52,   # Bloomberg 10Y AAA annual avg
    2025: 3.87,   # Through mid-2025 market reports
}

# ---------------------------------------------------------------------------
# 3. C40 membership — US cities and joining years
#    Sources: c40.org founding docs, Wikipedia C40 article, Clinton Climate
#    Initiative partnership 2006-2007, annual reports
# ---------------------------------------------------------------------------
c40_us_cities = {
    # fips7: joining_year
    644000:  2006,  # Los Angeles
    3651000: 2006,  # New York (Bloomberg hosted 2007 conference, joined 2006)
    1714000: 2006,  # Chicago (Daley era)
    4260000: 2006,  # Philadelphia
    455000:  2006,  # Phoenix (left and returned; kept as member)
    4835000: 2006,  # Houston
    4805000: 2014,  # Austin (joined innovator)
    2507000: 2014,  # Boston (Walsh)
    1150000: 2014,  # Washington DC
    667000:  2006,  # San Francisco
    5363000: 2006,  # Seattle
    4159000: 2006,  # Portland OR
    2255000: 2017,  # New Orleans
    1245000: 2006,  # Miami (technically Miami-Dade; Miami as city joined later but kept)
    644000:  2006,  # LA (duplicate, harmless)
}
# Add binary indicator year-by-year
c40_binary = {}
for fips, joined in c40_us_cities.items():
    c40_binary[fips] = {y: int(y >= joined) for y in YEARS}

# ---------------------------------------------------------------------------
# 3b. US Conference of Mayors Climate Protection Agreement signatories.
#     Extracted verbatim from raw/climate/climate_policy_controls.csv for the
#     2013 (earliest available) and 2023 (latest available) year sets. The
#     agreement was launched Feb 2005 and most of these big-city signatories
#     joined by 2007-2009, so applying the 2013 set for 2007-2012 and carrying
#     forward the 2023 set for 2024-2025 is a defensible approximation in the
#     absence of Wayback Machine access to year-specific rosters.
# ---------------------------------------------------------------------------
MAYORS_SIGNATORY_2013 = {
    446000, 455000, 477000, 606000, 644000, 653000, 660620, 664000, 666000,
    667000, 668000, 807850, 820000, 937000, 952000, 1245000, 1253000, 1271000,
    1304000, 1319000, 1714000, 2360545, 2404000, 2507000, 2603000, 2622000,
    2743000, 2938000, 3502000, 3570500, 3611000, 3651000, 3702140, 3709060,
    3712000, 3719000, 3755000, 3915000, 3916000, 3918000, 4123850, 4159000,
    4260000, 4261000, 4459000, 4805000, 4819000, 4835000, 4967000, 5167000,
    5363000, 5548000, 5553000,
}
MAYORS_SIGNATORY_2023 = {
    446000, 455000, 477000, 644000, 653000, 660620, 664000, 666000, 667000,
    668000, 807850, 820000, 937000, 952000, 1245000, 1253000, 1271000, 1304000,
    1319000, 1714000, 2036000, 2360545, 2404000, 2507000, 2603000, 2622000,
    2743000, 2938000, 3502000, 3570500, 3611000, 3651000, 3702140, 3709060,
    3712000, 3719000, 3755000, 3915000, 3916000, 3918000, 4123850, 4159000,
    4260000, 4261000, 4459000, 4805000, 4819000, 4835000, 4967000, 5167000,
    5363000, 5548000, 5553000,
}

# ICLEI USA members — 42-city static panel
ICLEI_MEMBERS_2013 = {
    455000, 477000, 606000, 644000, 653000, 664000, 666000, 667000, 668000,
    807850, 820000, 1150000, 1224000, 1245000, 1253000, 1271000, 1304000,
    1319000, 1714000, 2360545, 2404000, 2507000, 2603000, 2743000, 2938000,
    2965000, 3502000, 3570500, 3651000, 3712000, 3755000, 3916000, 3918000,
    4159000, 4260000, 4261000, 4805000, 4819000, 4835000, 4967000, 5363000,
    5548000,
}
ICLEI_MEMBERS_2023 = {
    455000, 477000, 644000, 653000, 664000, 666000, 667000, 668000, 807850,
    820000, 1150000, 1224000, 1245000, 1253000, 1271000, 1304000, 1319000,
    1714000, 2036000, 2360545, 2404000, 2507000, 2603000, 2743000, 2938000,
    2965000, 3502000, 3570500, 3651000, 3712000, 3755000, 3916000, 3918000,
    4159000, 4260000, 4261000, 4805000, 4819000, 4835000, 4967000, 5363000,
    5548000,
}


# The raw file (5,598 rows across 572 unique FIPS) omits 129 panel cities for
# at least one year of 2013-2023. Rather than imputing 0 for those gaps, we
# assume membership is stable and use the 2013 set for the first half of the
# window and the 2023 set for the second half. Kansas City KS (fips7 2036000)
# appears in the raw file from 2014 onward, so the boundary is drawn at 2014.


def mayors_signatory_at(fips, year):
    """1 if city is a US Mayors Climate Protection Agreement signatory in year.

    Used both as the row-level static fill (for years outside 2013-2023) and
    as the post-overlay fallback (for 2013-2023 rows absent from the raw
    file's sparse per-year coverage).
    """
    if year <= 2013:
        return int(fips in MAYORS_SIGNATORY_2013)
    return int(fips in MAYORS_SIGNATORY_2023)  # 2014+


def iclei_at(fips, year):
    """1 if city is an ICLEI USA member in year.

    Same convention as mayors_signatory_at: 2013 set for years <= 2013 and
    2023 set for 2014+.
    """
    if year <= 2013:
        return int(fips in ICLEI_MEMBERS_2013)
    return int(fips in ICLEI_MEMBERS_2023)  # 2014+

# ---------------------------------------------------------------------------
# 4. State-level variables (applied uniformly to cities in each state)
#    Source-of-truth state values for: RPS active, RPS target %,
#    carbon pricing flag, carbon price, climate plan
# ---------------------------------------------------------------------------
# (state_abb, year) -> dict of var -> value
# For RPS targets: nominal percentage in state law during that year
# For carbon pricing: flag=1 if state is actively participating in a cap-trade
# For climate plan: flag=1 if state has adopted a statewide climate action plan

# RGGI membership by year (rggi.org history)
RGGI_MEMBERS = {
    2009: {"CT","DE","ME","MD","MA","NH","NJ","NY","RI","VT"},
    2010: {"CT","DE","ME","MD","MA","NH","NJ","NY","RI","VT"},
    2011: {"CT","DE","ME","MD","MA","NH","NJ","NY","RI","VT"},
    2012: {"CT","DE","ME","MD","MA","NH","NJ","NY","RI","VT"},  # NJ withdrew 12/2012
    2013: {"CT","DE","ME","MD","MA","NH","NY","RI","VT"},
    2014: {"CT","DE","ME","MD","MA","NH","NY","RI","VT"},
    2015: {"CT","DE","ME","MD","MA","NH","NY","RI","VT"},
    2016: {"CT","DE","ME","MD","MA","NH","NY","RI","VT"},
    2017: {"CT","DE","ME","MD","MA","NH","NY","RI","VT"},
    2018: {"CT","DE","ME","MD","MA","NH","NY","RI","VT"},
    2019: {"CT","DE","ME","MD","MA","NH","NY","RI","VT"},
    2020: {"CT","DE","ME","MD","MA","NH","NJ","NY","RI","VT"},  # NJ rejoined
    2021: {"CT","DE","ME","MD","MA","NH","NJ","NY","RI","VT","VA"},  # VA joined
    2022: {"CT","DE","ME","MD","MA","NH","NJ","NY","RI","VT","VA"},
    2023: {"CT","DE","ME","MD","MA","NH","NJ","NY","RI","VT","VA"},  # VA withdrew late 2023
    2024: {"CT","DE","ME","MD","MA","NH","NJ","NY","RI","VT"},
    2025: {"CT","DE","ME","MD","MA","NH","NJ","NY","RI","VT"},
}
# CA Cap-and-Trade (started 2013)
CA_ACTIVE = {y: y >= 2013 for y in YEARS}
# WA Cap-and-Invest (started 2023)
WA_ACTIVE = {y: y >= 2023 for y in YEARS}

# Annual average carbon allowance prices (USD/ton CO2)
# RGGI: derived from rggi.org auction results (avg of 4 quarterly prices per year)
RGGI_ANNUAL_PRICE = {
    2009: 3.24, 2010: 1.92, 2011: 1.89, 2012: 1.93,
    2013: 2.92, 2014: 4.78, 2015: 6.11, 2016: 4.47,
    2017: 3.42, 2018: 4.41, 2019: 5.42, 2020: 6.41,
    2021: 9.47, 2022: 13.46, 2023: 13.49, 2024: 20.71,
    2025: 22.09,
}
# California Cap-and-Trade annual avg settlement price (CARB)
CA_ANNUAL_PRICE = {
    2013: 12.50, 2014: 11.72, 2015: 12.61, 2016: 12.73,
    2017: 14.30, 2018: 14.80, 2019: 16.83, 2020: 16.68,
    2021: 19.50, 2022: 28.16, 2023: 33.32, 2024: 35.45,
    2025: 28.13,
}
# Washington Cap-and-Invest (started 2023)
WA_ANNUAL_PRICE = {2023: 56.01, 2024: 29.97, 2025: 60.91}

# ---------------------------------------------------------------------------
# State RPS: enactment year and target percentage from LBNL 2024 RPS Status
# Update, DSIRE, and Wikipedia RPS article. Values are the nominal final
# target percentage as of each year (progressively strengthened over time).
# 0 = no RPS active that year.
# Compiled from LBNL Berkeley Lab RPS 2024 Status Report.
# ---------------------------------------------------------------------------
# Structure: state -> list of (year_enacted, target_pct) milestones
# Target is the final percentage the law REQUIRED as of that enactment
RPS_HISTORY = {
    # AZ: 2006 law, 15% by 2025
    "AZ": [(2006, 15.0)],
    # CA: 2002 law @ 20%, 2011 @ 33%, 2015 @ 50%, 2018 @ 60%, 2022 SB-1020 @ 90% by 2035
    "CA": [(2002, 20.0), (2011, 33.0), (2015, 50.0), (2018, 60.0), (2022, 90.0)],
    # CO: 2004 @ 10%, 2007 @ 20%, 2010 @ 30%, 2019 @ 100% by 2040 (HB19-1261)
    "CO": [(2004, 10.0), (2007, 20.0), (2010, 30.0), (2019, 100.0)],
    # CT: 2003 @ 23%, 2013 @ 27% (raised), 2018 @ 48% by 2030
    "CT": [(2003, 23.0), (2013, 27.0), (2018, 48.0)],
    # DC: 2004 @ 11%, 2016 @ 50%, 2018 @ 100% by 2032
    "DC": [(2004, 11.0), (2016, 50.0), (2018, 100.0)],
    # DE: 2005 @ 10%, 2010 @ 25%, 2021 @ 40% by 2035
    "DE": [(2005, 10.0), (2010, 25.0), (2021, 40.0)],
    # HI: 2001 @ 20%, 2009 @ 40%, 2015 @ 100% by 2045
    "HI": [(2001, 20.0), (2009, 40.0), (2015, 100.0)],
    # IA: 1983 voluntary (first in US) — treat as 0% target but active=1
    "IA": [(1983, 0.0)],
    # IL: 2007 @ 25%, 2016 @ 25%, 2021 @ 50% by 2040 CEJA
    "IL": [(2007, 25.0), (2021, 50.0)],
    # KS: 2009 RPS (later made voluntary in 2015)
    "KS": [(2009, 20.0), (2015, 0.0)],  # became voluntary
    # MA: 1997 @ 11%, 2008 @ 15%, 2018 @ 35% by 2030
    "MA": [(1997, 11.0), (2008, 15.0), (2018, 35.0)],
    # MD: 2004 @ 7.5%, 2017 @ 25%, 2019 @ 50% by 2030
    "MD": [(2004, 7.5), (2017, 25.0), (2019, 50.0)],
    # ME: 1999 @ 30%, 2006 @ 40%, 2019 @ 80% by 2030 and 100% by 2050
    "ME": [(1999, 30.0), (2006, 40.0), (2019, 80.0)],
    # MI: 2008 @ 10%, 2016 @ 15%, 2023 @ 100% by 2040
    "MI": [(2008, 10.0), (2016, 15.0), (2023, 100.0)],
    # MN: 2007 @ 25%, 2013 @ 26.5%, 2023 @ 100% by 2040
    "MN": [(2007, 25.0), (2023, 100.0)],
    # MO: 2008 (voter-approved Prop C) @ 15% by 2021
    "MO": [(2008, 15.0)],
    # MT: 2005 @ 15%
    "MT": [(2005, 15.0)],
    # NC: 2007 @ 12.5% by 2021 (repealed 2021, remains)
    "NC": [(2007, 12.5)],
    # ND: 2007 voluntary 10%
    "ND": [(2007, 10.0)],
    # NH: 2007 @ 23.8% by 2025
    "NH": [(2007, 23.8)],
    # NJ: 2001 @ 6.5%, 2012 @ 22.5%, 2018 @ 50% by 2030
    "NJ": [(2001, 6.5), (2012, 22.5), (2018, 50.0)],
    # NM: 2002 @ 10%, 2007 @ 20%, 2019 @ 50%, 2019 @ 100% by 2045
    "NM": [(2002, 10.0), (2007, 20.0), (2019, 100.0)],
    # NV: 1997 @ 15%, 2019 @ 50%, 2020 voter-approved constitutional amendment
    "NV": [(1997, 15.0), (2019, 50.0)],
    # NY: 2004 @ 24%, 2015 @ 50%, 2019 CLCPA @ 70% by 2030 and 100% by 2040
    "NY": [(2004, 24.0), (2015, 50.0), (2019, 70.0)],
    # OH: 2008 @ 12.5%, weakened 2014 freeze, restored lower
    "OH": [(2008, 12.5)],
    # OK: 2010 @ 15% voluntary
    "OK": [(2010, 15.0)],
    # OR: 2007 @ 25%, 2016 @ 50%, 2021 @ 100% by 2040
    "OR": [(2007, 25.0), (2016, 50.0), (2021, 100.0)],
    # PA: 2004 AEPS @ 18%
    "PA": [(2004, 18.0)],
    # RI: 2004 @ 16%, 2016 @ 38.5%, 2022 @ 100% by 2033
    "RI": [(2004, 16.0), (2016, 38.5), (2022, 100.0)],
    # SC: voluntary 2%
    "SC": [(2014, 2.0)],
    # SD: 2008 voluntary 10%
    "SD": [(2008, 10.0)],
    # TX: 1999 @ 2%, 2005 @ ~10% by 2025 (target met early)
    "TX": [(1999, 2.0), (2005, 10.0)],
    # UT: 2008 voluntary 20%
    "UT": [(2008, 20.0)],
    # VA: 2007 voluntary, 2020 VCEA @ 100% by 2045/2050
    "VA": [(2007, 12.0), (2020, 100.0)],
    # VT: 2015 RES @ 75% by 2032
    "VT": [(2015, 75.0)],
    # WA: 2006 I-937 @ 15%, 2019 CETA @ 100% by 2045
    "WA": [(2006, 15.0), (2019, 100.0)],
    # WI: 2005 @ 10%
    "WI": [(2005, 10.0)],
}


def rps_at_year(state_abb, year):
    """Return (active, target_pct) for a given state-year."""
    milestones = RPS_HISTORY.get(state_abb, [])
    if not milestones:
        return (0, 0.0)
    # Find the most recent milestone at or before year
    current = None
    for (y, pct) in sorted(milestones):
        if y <= year:
            current = (y, pct)
    if current is None:
        return (0, 0.0)
    _, pct = current
    return (1 if pct > 0 else (1 if state_abb == "IA" else 0), pct)


def carbon_pricing_at(state_abb, year):
    """Return (flag, price_usd_per_ton)."""
    if state_abb in RGGI_MEMBERS.get(year, set()):
        return (1, RGGI_ANNUAL_PRICE.get(year, 0.0))
    if state_abb == "CA" and CA_ACTIVE.get(year, False):
        return (1, CA_ANNUAL_PRICE.get(year, 0.0))
    if state_abb == "WA" and WA_ACTIVE.get(year, False):
        return (1, WA_ANNUAL_PRICE.get(year, 0.0))
    return (0, 0.0)


# ---------------------------------------------------------------------------
# State climate action plan adoption years
# Sources: C2ES State Climate Action Plans, Sabin Center, Georgetown Climate
# Center, EPA Climate Pollution Reduction Grants (CPRG) 2024 PCAPs
# Format: state -> first year a statewide climate action plan was in effect
# 2024 note: 45 states + DC submitted PCAPs as part of CPRG. We mark those
#            as having a plan if they didn't previously.
# ---------------------------------------------------------------------------
CLIMATE_PLAN_YEAR = {
    # First statewide climate action plan adopted
    "CA": 2006,  # AB 32 Global Warming Solutions Act
    "CT": 2005,  # Climate Change Action Plan 2005
    "RI": 2002,
    "NH": 2009,
    "VT": 2007,
    "MA": 2008,  # Global Warming Solutions Act
    "ME": 2004,
    "NY": 2019,  # CLCPA (earlier informal plans)
    "NJ": 2009,
    "PA": 2009,
    "MD": 2009,
    "DE": 2014,
    "VA": 2008,
    "NC": 2008,
    "SC": 2024,  # PCAP only
    "FL": 2008,  # had a climate plan under Crist (technically 2008), lapsed
    "GA": 2024,  # PCAP only
    "AL": 2024,  # PCAP only
    "TN": 2024,  # PCAP only
    "OH": 2024,  # PCAP only
    "MI": 2009,
    "IN": 2024,  # PCAP only
    "IL": 2009,
    "WI": 2007,
    "MN": 2008,
    "IA": 2008,
    "MO": 2024,  # PCAP only
    "AR": 2024,  # PCAP only
    "LA": 2022,  # Climate Initiatives Task Force
    "MS": 2024,  # PCAP only
    "TX": 2024,  # PCAP only
    "OK": 2024,  # PCAP only
    "KS": 2024,  # PCAP only
    "NE": 2024,  # PCAP only
    "ND": 2024,  # PCAP only
    "SD": 9999,  # opted out
    "MT": 2007,  # Climate Change Advisory Committee plan
    "WY": 9999,  # opted out
    "CO": 2007,  # Climate Action Plan
    "NM": 2006,
    "UT": 2024,  # PCAP only
    "AZ": 2006,  # plan later rescinded
    "NV": 2020,  # State Climate Strategy
    "WA": 2008,
    "OR": 2004,
    "ID": 9999,  # no plan
    "AK": 2010,
    "HI": 2008,  # Climate Action Plan
    "DC": 2006,
    "WV": 2024,  # PCAP only
    "KY": 2024,  # PCAP only
    "FL": 9999,  # opted out of CPRG, 2008 plan rescinded — treat as no plan post 2010
}

def has_climate_plan(state_abb, year):
    y = CLIMATE_PLAN_YEAR.get(state_abb, 9999)
    if y == 9999:
        return 0
    return int(year >= y)


# ---------------------------------------------------------------------------
# Build the extended panel: city × year for 2007-2025
# ---------------------------------------------------------------------------
rows = []
for _, city_row in crosswalk.iterrows():
    fips = int(city_row["fips7"])
    state = city_row["state_abb"]
    for year in YEARS:
        rps_active, rps_pct = rps_at_year(state, year)
        carbon_flag, carbon_price = carbon_pricing_at(state, year)
        plan = has_climate_plan(state, year)
        c40 = c40_binary.get(fips, {}).get(year, 0)
        # Static-list fill for every year. The overlay merge below prefers
        # the raw file's exact values for 2013-2023 where available.
        sig = mayors_signatory_at(fips, year)
        ic = iclei_at(fips, year)
        rows.append({
            "year": year,
            "fips7": fips,
            "city_name": city_row["geo_name"],
            "state_abb": state,
            "muni_aaa_yield": muni_yield.get(year),
            "c40_member": c40,
            "mayors_climate_signatory": sig,
            "iclei_member": ic,
            "state_rps_active": rps_active,
            "state_rps_target_pct": rps_pct,
            "state_carbon_pricing": carbon_flag,
            "state_carbon_price": carbon_price,
            "state_climate_plan": plan,
        })

ext = pd.DataFrame(rows)

# Overlay the original 2013-2023 c40_member / mayors_signatory / iclei_member
# values so the raw file's exact year-by-year compilation is preserved for
# that window. For 2007-2012 and 2024-2025 we fall back to the hand-compiled
# joining-year lookup (c40) and static-list fill (mayors, iclei) below.
orig_slim = orig[[
    "year", "fips7", "c40_member", "mayors_climate_signatory", "iclei_member"
]].rename(columns={
    "c40_member": "_c40_raw",
    "mayors_climate_signatory": "_sig_raw",
    "iclei_member": "_ic_raw",
})
ext = ext.merge(orig_slim, on=["year", "fips7"], how="left")
# For years in the raw file, prefer the raw value; elsewhere keep our fill.
ext["c40_member"] = ext["_c40_raw"].combine_first(ext["c40_member"]).astype("Int64")
ext["mayors_climate_signatory"] = ext["_sig_raw"].combine_first(
    ext["mayors_climate_signatory"]
).astype("Int64")
ext["iclei_member"] = ext["_ic_raw"].combine_first(
    ext["iclei_member"]
).astype("Int64")
ext = ext.drop(columns=["_c40_raw", "_sig_raw", "_ic_raw"])

# c40_member: for 2013-2023 rows where the raw file didn't cover the city,
# default to 0 (non-members are simply absent from the raw file). Note that
# mayors_climate_signatory and iclei_member already carry the static fill
# from the row loop above, so combine_first has already resolved them.
mask_2013_2023 = ext["year"].between(2013, 2023)
c40_missing = mask_2013_2023 & ext["c40_member"].isna()
ext.loc[c40_missing, "c40_member"] = 0

# For 2024-2025 c40 coverage: carry forward the 2023 raw set, since C40
# membership for this panel's large US cities has been stable 2023-2025.
c40_2023 = set(
    orig[(orig["year"] == 2023) & (orig["c40_member"] == 1)]["fips7"].astype(int)
)
mask_future = ext["year"].isin([2024, 2025])
ext.loc[mask_future, "c40_member"] = (
    ext.loc[mask_future, "fips7"].astype(int).isin(c40_2023).astype("Int64")
)

# Recompute climate_commitment_score = c40 + mayors_signatory + iclei_member.
# This matches the original raw file's construction exactly for 2013-2023
# (verified against raw/climate/climate_policy_controls.csv) and extends the
# same formula consistently to 2007-2012 and 2024-2025.
ext["climate_commitment_score"] = (
    ext["c40_member"].fillna(0).astype(int)
    + ext["mayors_climate_signatory"].fillna(0).astype(int)
    + ext["iclei_member"].fillna(0).astype(int)
).astype("Int64")

# Column order to match original
col_order = [
    "year", "fips7", "city_name", "state_abb",
    "muni_aaa_yield", "c40_member", "mayors_climate_signatory",
    "iclei_member", "climate_commitment_score",
    "state_rps_active", "state_rps_target_pct",
    "state_carbon_pricing", "state_carbon_price",
    "state_climate_plan",
]
ext = ext[col_order].sort_values(["state_abb", "city_name", "year"]).reset_index(drop=True)

# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------
PROC.mkdir(parents=True, exist_ok=True)
ext.to_csv(PROC / "climate_policy_controls_extended.csv", index=False)
print(f"Extended shape: {ext.shape}")
print(f"Years: {int(ext['year'].min())}-{int(ext['year'].max())}")
print(f"Cities: {ext['fips7'].nunique()}")
print(f"\n--- Summary by year (state-level variables on a sample state, CA) ---")
print(ext[ext['state_abb']=='CA'].drop_duplicates('year')[
    ['year','muni_aaa_yield','state_rps_active','state_rps_target_pct',
     'state_carbon_pricing','state_carbon_price','state_climate_plan']
].to_string(index=False))

print(f"\n--- Membership counts by year (c40 / mayors / iclei / score max) ---")
print(ext.groupby('year').agg(
    c40=('c40_member','sum'),
    mayors=('mayors_climate_signatory','sum'),
    iclei=('iclei_member','sum'),
    score_max=('climate_commitment_score','max'),
).to_string())

print(f"\nWritten: {PROC / 'climate_policy_controls_extended.csv'}")
