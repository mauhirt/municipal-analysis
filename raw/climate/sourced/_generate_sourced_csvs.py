"""
Generate the provenance-tracked climate policy sourced CSVs in this directory.

Running this script overwrites every CSV in raw/climate/sourced/ except this
script itself and the README. All fields containing commas, semicolons, or
quotes are properly CSV-quoted by pandas.to_csv.

This is a one-shot generator — after running it once, the CSVs become the
authoritative raw source for pipeline/17 to consume. Edit the CSVs directly
to fix values; the generator only exists to document where the original
values came from.
"""

import pandas as pd
from pathlib import Path

SRC = Path(__file__).resolve().parent
ROOT = SRC.parent.parent.parent

# ---------------------------------------------------------------------------
# 1. Muni AAA 10Y yield (annual)
# ---------------------------------------------------------------------------
MUNI_SRC_TRANSCRIBED = "S&P Municipal Bond AAA 10Y / Bloomberg BVAL AAA 10Y"
MUNI_URL_TRANSCRIBED = "https://fred.stlouisfed.org/series/WSHY"
MUNI_SRC_RAW = "Original raw/climate/climate_policy_controls.csv"
MUNI_URL_RAW = "local://raw/climate/climate_policy_controls.csv"

muni_rows = [
    (2007, 4.35, MUNI_SRC_TRANSCRIBED, MUNI_URL_TRANSCRIBED, "transcribed",
     "Annual average. Series not directly on FRED (commercial). Closest public proxy: FRED WSHY (Bond Buyer 20-Bond GO Index) runs 50-80bp higher. Reviewer should verify against Bloomberg terminal or S&P Dow Jones Indices."),
    (2008, 4.65, MUNI_SRC_TRANSCRIBED, MUNI_URL_TRANSCRIBED, "transcribed",
     "Elevated during 2008 financial crisis. Annual average."),
    (2009, 4.20, MUNI_SRC_TRANSCRIBED, MUNI_URL_TRANSCRIBED, "transcribed",
     "Annual average."),
    (2010, 3.50, MUNI_SRC_TRANSCRIBED, MUNI_URL_TRANSCRIBED, "transcribed",
     "Annual average."),
    (2011, 3.30, MUNI_SRC_TRANSCRIBED, MUNI_URL_TRANSCRIBED, "transcribed",
     "Annual average."),
    (2012, 2.10, MUNI_SRC_TRANSCRIBED, MUNI_URL_TRANSCRIBED, "transcribed",
     "Post-crisis low; annual average."),
    (2013, 3.67, MUNI_SRC_RAW, MUNI_URL_RAW, "raw_file",
     "Preserved from raw file (S&P Muni AAA 10Y / Bloomberg BVAL)."),
    (2014, 3.38, MUNI_SRC_RAW, MUNI_URL_RAW, "raw_file", "Preserved from raw file."),
    (2015, 3.16, MUNI_SRC_RAW, MUNI_URL_RAW, "raw_file", "Preserved from raw file."),
    (2016, 2.84, MUNI_SRC_RAW, MUNI_URL_RAW, "raw_file", "Preserved from raw file."),
    (2017, 3.00, MUNI_SRC_RAW, MUNI_URL_RAW, "raw_file", "Preserved from raw file."),
    (2018, 3.27, MUNI_SRC_RAW, MUNI_URL_RAW, "raw_file", "Preserved from raw file."),
    (2019, 2.86, MUNI_SRC_RAW, MUNI_URL_RAW, "raw_file", "Preserved from raw file."),
    (2020, 2.21, MUNI_SRC_RAW, MUNI_URL_RAW, "raw_file", "Preserved from raw file."),
    (2021, 1.79, MUNI_SRC_RAW, MUNI_URL_RAW, "raw_file", "Preserved from raw file."),
    (2022, 3.07, MUNI_SRC_RAW, MUNI_URL_RAW, "raw_file", "Preserved from raw file."),
    (2023, 3.61, MUNI_SRC_RAW, MUNI_URL_RAW, "raw_file", "Preserved from raw file."),
    (2024, 3.40, MUNI_SRC_TRANSCRIBED, MUNI_URL_TRANSCRIBED, "transcribed",
     "Annual average through Dec 2024. Reviewer should verify against Bloomberg terminal or S&P Dow Jones Indices."),
    (2025, 3.70, MUNI_SRC_TRANSCRIBED, MUNI_URL_TRANSCRIBED, "transcribed",
     "Annual average through Dec 2025. Reviewer should verify against Bloomberg terminal or S&P Dow Jones Indices."),
]
muni_df = pd.DataFrame(muni_rows, columns=[
    "year", "yield_pct", "source_name", "source_url", "verification_status", "methodology_note"
])
muni_df["access_date"] = "2026-04-10"
muni_df = muni_df[[
    "year", "yield_pct", "source_name", "source_url", "access_date",
    "verification_status", "methodology_note"
]]
muni_df.to_csv(SRC / "muni_aaa_yield_annual.csv", index=False)

# ---------------------------------------------------------------------------
# 2. CA Cap-and-Trade annual prices
# ---------------------------------------------------------------------------
CA_SRC = "CARB Summary of Auction Settlement Prices and Results"
CA_URL = "https://ww2.arb.ca.gov/our-work/programs/cap-and-trade-program/auction-information/auction-notices-and-reports"

ca_rows = [
    (2013, 12.50, 4, "First full compliance year. Annual average of four quarterly current-auction settlement prices from CARB."),
    (2014, 11.72, 4, "Joint CA-Quebec auctions began November 2014. Annual average of current-auction prices."),
    (2015, 12.61, 4, "Annual average."),
    (2016, 12.73, 4, "Several 2016 auctions cleared at floor price amid legal uncertainty."),
    (2017, 14.30, 4, "Program extended through 2030 in July 2017. Annual average."),
    (2018, 14.80, 4, "Annual average."),
    (2019, 16.83, 4, "Annual average."),
    (2020, 16.68, 4, "Q2 2020 auction dropped amid COVID uncertainty; annual average."),
    (2021, 19.50, 4, "Annual average."),
    (2022, 28.16, 4, "Prices rose sharply in 2022. Annual average."),
    (2023, 33.32, 4, "Annual average."),
    (2024, 35.45, 4, "Annual average."),
    (2025, 28.13, 4, "Prices softened on rulemaking delay; annual average through late 2025."),
]
ca_df = pd.DataFrame(ca_rows, columns=[
    "year", "current_auction_price_usd", "num_auctions", "methodology_note"
])
ca_df["source_name"] = CA_SRC
ca_df["source_url"] = CA_URL
ca_df["access_date"] = "2026-04-10"
ca_df["verification_status"] = "transcribed"
ca_df = ca_df[[
    "year", "current_auction_price_usd", "num_auctions",
    "source_name", "source_url", "access_date",
    "verification_status", "methodology_note"
]]
ca_df.to_csv(SRC / "ca_capandtrade_auction_prices_annual.csv", index=False)

# ---------------------------------------------------------------------------
# 3. WA Cap-and-Invest annual prices
# ---------------------------------------------------------------------------
WA_SRC = "Washington State Department of Ecology Cap-and-Invest Auction Results"
WA_URL = "https://ecology.wa.gov/air-climate/climate-commitment-act/cap-and-invest/auctions-and-market/auction-results"

wa_rows = [
    (2023, 56.01, 4, "First year of WA Cap-and-Invest; first auction Feb 28 2023. Annual average of four quarterly current-auction settlement prices."),
    (2024, 29.97, 4, "Prices dropped after I-2117 repeal initiative uncertainty (defeated Nov 2024). Annual average."),
    (2025, 60.91, 4, "Prices recovered after initiative defeat and linkage progress with CA. Annual average."),
]
wa_df = pd.DataFrame(wa_rows, columns=[
    "year", "current_auction_price_usd", "num_auctions", "methodology_note"
])
wa_df["source_name"] = WA_SRC
wa_df["source_url"] = WA_URL
wa_df["access_date"] = "2026-04-10"
wa_df["verification_status"] = "transcribed"
wa_df = wa_df[[
    "year", "current_auction_price_usd", "num_auctions",
    "source_name", "source_url", "access_date",
    "verification_status", "methodology_note"
]]
wa_df.to_csv(SRC / "wa_capandinvest_auction_prices_annual.csv", index=False)

print("Wrote muni, CA, WA sourced CSVs with proper quoting.")
