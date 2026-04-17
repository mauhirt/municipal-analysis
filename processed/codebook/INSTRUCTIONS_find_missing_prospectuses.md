## Task: Find Missing Bond Prospectus URLs on EMMA

### What you need to do

Open `processed/codebook/emma_lookup_uncovered_issuances.csv`. This file has **139 rows**, each representing a municipal bond issuance that is missing its Official Statement (prospectus) PDF. Your job is to find the direct PDF download URL for each one on MSRB's EMMA platform.

### How to look up each row

1. Open the `emma_search` URL for the row (e.g. `https://emma.msrb.org/Search/Search.aspx?criteria=015343AA4`). This searches EMMA by the lead CUSIP.
2. Navigate to the security's details page and find the **Official Statement** document link.
3. Copy the direct PDF URL — it will look like `https://emma.msrb.org/P21963220-P21497913-P21950218.pdf`.
4. If no Official Statement was submitted, write `NO OS SUBMITTED`.

### How to record your results

Add a `prospectus_url` column to the file `raw/bloomberg/Missing_Green_Prospectuses_URLS.csv`, following the existing format:

```
Row,Issuer_Name,Issue_Date,lead_CUSIP,emma_security_details_url,prospectus_url
```

**Important:** Each row is a unique **(Issuer, Issue Date)** pair — one bond issuance that needs one prospectus. The same issuer can appear multiple times with different issue dates. Each date needs its own lookup.

### Key columns in the lookup file

| Column | Use |
|---|---|
| `Issuer_Name` | Who issued the bond |
| `Issue_Date` | When (each date = separate prospectus) |
| `lead_CUSIP` | Use this to search on EMMA |
| `emma_search` | Clickable EMMA search URL |
| `all_CUSIPs` | All CUSIPs in this issuance (semicolon-separated) |

### After you're done

The download and processing pipeline will run automatically:
- `pipeline/06_download_missing_prospectuses.py` downloads the PDFs
- `pipeline/02_convert_prospectuses_to_text.py` extracts text
- Coverage is recomputed on `raw/bloomberg/cusip_with_assignment_matched.csv`
