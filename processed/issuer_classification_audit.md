# Issuer Classification Audit

Comparison of jurisdiction types assigned in `bonds_with_issuer_classification.xlsx`
against the MSRB's official `Issuer Type` in `All_US_Municipal_Bond_Issuers.csv`.

## Summary

- **Total unique issuers analysed:** 960
- **MSRB entries searched:** 100,422

| Comparison outcome | Count |
|---|---|
| AGREES | 372 |
| AGREES_ALTERNATE_ENTRY | 215 |
| PLAUSIBLE_MSRB_USES_PARENT | 67 |
| DISCREPANCY | 21 |
| UNABLE_TO_COMPARE | 285 |

**Interpretation of categories:**

- **AGREES** — Your jurisdiction type directly maps to the MSRB Issuer Type of the best match.
- **AGREES_ALTERNATE_ENTRY** — The best MSRB match has a different type, but another high-scoring MSRB entry for the same entity has a type that matches yours. This commonly happens because MSRB creates separate entries for different bond programs (e.g., general obligation vs revenue bonds) and sometimes labels them differently.
- **PLAUSIBLE_MSRB_USES_PARENT** — You classified the entity as SCHOOL_DISTRICT, SPECIAL_DISTRICT, or MULTI_JURISDICTIONAL, but MSRB uses the parent jurisdiction's type (City/County/State). The MSRB has only four categories (City, County, State, Other) and often assigns subordinate entities to their parent jurisdiction.
- **DISCREPANCY** — A genuine disagreement between your classification and what MSRB records suggest, warranting review.
- **UNABLE_TO_COMPARE** — The fuzzy match quality was too low to make a reliable comparison, or no MSRB entries exist for the state.

## Cross-tabulation (Your type vs MSRB type)

For the 675 issuers with reliable MSRB matches:

| Your_Jurisdiction    |   City |   County |   Other |   State |   All |
|:---------------------|-------:|---------:|--------:|--------:|------:|
| CITY                 |    174 |       10 |      22 |       9 |   215 |
| COUNTY               |     20 |       25 |      12 |       0 |    57 |
| MULTI_JURISDICTIONAL |     43 |        5 |      19 |      14 |    81 |
| OTHER                |      1 |        0 |       0 |       0 |     1 |
| SCHOOL_DISTRICT      |     57 |        7 |      39 |      11 |   114 |
| SPECIAL_DISTRICT     |     35 |        8 |      22 |       5 |    70 |
| STATE                |     15 |        1 |      28 |      93 |   137 |
| All                  |    345 |       56 |     142 |     132 |   675 |

## Match quality distribution

| Quality | Count | Description |
|---|---|---|
| HIGH | 192 | Score >= 90 with shared specific words |
| MODERATE | 476 | Score 80-89 with shared specific words |
| FAIR | 7 | Score 70-79 with shared specific words |
| LOW | 277 | Score < 70 or no shared specific words |
| NO_STATE | 8 | No MSRB entries for the state |

## Key systematic patterns observed

### 1. MSRB classifies bond programs (not entities)

The MSRB database is organised around bond programs, not institutional entities. A single city may have dozens of MSRB entries — one for general obligation bonds (often typed as "City"), and many for revenue bonds (often typed as "Other"). For example, Tampa, FL has 47 MSRB entries: most are typed "Other" (revenue programs), not "City".

### 2. MSRB uses only four categories

The MSRB uses only **City, County, State, Other**. Your classification uses a richer taxonomy: CITY, COUNTY, STATE, SPECIAL_DISTRICT, MULTI_JURISDICTIONAL, SCHOOL_DISTRICT, OTHER. Anything that isn't cleanly a city, county, or state government in MSRB's view becomes "Other", including state authorities, public universities, financing authorities, transit authorities, etc.

### 3. Louisiana parishes are classified as "City" by MSRB

MSRB classifies Louisiana parishes (county-equivalents) as "City", not "County". Your classification of these as COUNTY is arguably more accurate.

### 4. District of Columbia

MSRB classifies DC as "State". Your classification as CITY is a reasonable alternative given DC functions as a city government. This is a definitional difference, not an error.

### 5. State authorities and universities

You classified state-created authorities (financing authorities, development corporations, public universities) as STATE. MSRB frequently classifies these as "Other" (e.g., MTA, NJ Infrastructure Bank, state universities). Both approaches have merit: yours reflects the controlling jurisdiction, MSRB's reflects that these are not the state government itself.

## Discrepancies requiring review (21 issuers)

These are cases where your classification and the MSRB classification clearly disagree, and no alternate MSRB entry has a matching type.

### Parish of Terrebonne LA Sales & Use Tax Revenue [LA]

- **Your classification:** COUNTY (Direct government)
- **MSRB best match:** TERREBONNE PARISH LA
- **MSRB type:** City
- **Match score:** 100 (HIGH)
- **MSRB type distribution across matches:** {'City': 15, 'Other': 2}
- **Analysis:** Louisiana parishes are county-equivalents. MSRB classifies parishes as City, likely treating them as the primary local government. Your COUNTY classification is arguably more accurate for jurisdictional analysis.

### Lower Colorado River Authority [TX]

- **Your classification:** STATE (State agency)
- **MSRB best match:** LOWER COLORADO RIVER AUTHORITY
- **MSRB type:** Other
- **Match score:** 100 (HIGH)
- **MSRB type distribution across matches:** {'Other': 1, 'City': 7, 'County': 2}
- **Analysis:** MSRB classifies state authorities/agencies as Other rather than State. Your STATE classification reflects the controlling jurisdiction. MSRB reserves State for the state government itself.

### Inlivian [NC]

- **Your classification:** CITY (Authority/Agency)
- **MSRB best match:** INLIVIAN N C MULTIFAMILY REV
- **MSRB type:** Other
- **Match score:** 100 (HIGH)
- **MSRB type distribution across matches:** {'Other': 2}
- **Analysis:** MSRB classifies this city entity's bond programs as Other (typically used for revenue bonds). Your CITY classification reflects the actual governmental jurisdiction. The MSRB category may reflect the bond type rather than the issuer type.

### District of Columbia Water & Sewer Authority [DC]

- **Your classification:** CITY (Authority/Agency)
- **MSRB best match:** DISTRICT OF COLUMBIA
- **MSRB type:** State
- **Match score:** 100 (HIGH)
- **MSRB type distribution across matches:** {'State': 1, 'Other': 12}
- **Analysis:** DC is a unique jurisdiction — it functions as both a city and a state. MSRB classifies it as State; your classification as CITY reflects its municipal government role. Definitional difference, not an error.

### District of Columbia [DC]

- **Your classification:** CITY (Direct government)
- **MSRB best match:** DISTRICT OF COLUMBIA
- **MSRB type:** State
- **Match score:** 100 (HIGH)
- **MSRB type distribution across matches:** {'State': 1, 'Other': 14}
- **Analysis:** DC is a unique jurisdiction — it functions as both a city and a state. MSRB classifies it as State; your classification as CITY reflects its municipal government role. Definitional difference, not an error.

### Warm Springs Reservation Confederated Tribe [OR]

- **Your classification:** OTHER (Tribal government)
- **MSRB best match:** WARM SPRINGS RESERVATION ORE CONFEDERATED TRIBES
- **MSRB type:** City
- **Match score:** 95 (HIGH)
- **MSRB type distribution across matches:** {'City': 4}
- **Analysis:** MSRB classifies tribal governments as City. Your OTHER classification more accurately reflects the unique sovereign status of tribal governments.

### Ward Two Water District of Livingston Parish [LA]

- **Your classification:** COUNTY (Special district)
- **MSRB best match:** LIVINGSTON PARISH LA
- **MSRB type:** City
- **Match score:** 92 (HIGH)
- **MSRB type distribution across matches:** {'City': 20}
- **Analysis:** Louisiana parishes are county-equivalents. MSRB classifies parishes as City, likely treating them as the primary local government. Your COUNTY classification is arguably more accurate for jurisdictional analysis.

### St Charles Parish Consolidated Waterworks & Wastewater District No 1 [LA]

- **Your classification:** COUNTY (Special district)
- **MSRB best match:** ST CHARLES PARISH LA
- **MSRB type:** City
- **Match score:** 92 (HIGH)
- **MSRB type distribution across matches:** {'City': 9, 'Other': 10}
- **Analysis:** Louisiana parishes are county-equivalents. MSRB classifies parishes as City, likely treating them as the primary local government. Your COUNTY classification is arguably more accurate for jurisdictional analysis.

### Livingston Parish Sewer District [LA]

- **Your classification:** COUNTY (Special district)
- **MSRB best match:** LIVINGSTON PARISH LA
- **MSRB type:** City
- **Match score:** 92 (HIGH)
- **MSRB type distribution across matches:** {'City': 24}
- **Analysis:** Louisiana parishes are county-equivalents. MSRB classifies parishes as City, likely treating them as the primary local government. Your COUNTY classification is arguably more accurate for jurisdictional analysis.

### Beauregard Parish Waterworks District No 3 [LA]

- **Your classification:** COUNTY (Special district)
- **MSRB best match:** BEAUREGARD PARISH LA
- **MSRB type:** City
- **Match score:** 92 (HIGH)
- **MSRB type distribution across matches:** {'City': 22}
- **Analysis:** Louisiana parishes are county-equivalents. MSRB classifies parishes as City, likely treating them as the primary local government. Your COUNTY classification is arguably more accurate for jurisdictional analysis.

### Hudson Yards Infrastructure Corp [NY]

- **Your classification:** CITY (Development corporation)
- **MSRB best match:** HUDSON YARDS INFRASTRUCTURE CORPORATION
- **MSRB type:** Other
- **Match score:** 92 (HIGH)
- **MSRB type distribution across matches:** {'Other': 8, 'County': 4}
- **Analysis:** MSRB classifies this city-controlled development entity as Other. Your CITY classification reflects the controlling jurisdiction. MSRB reserves City for the city government's direct bond programs.

### Town of Bedford NH [NH]

- **Your classification:** CITY (Town Government)
- **MSRB best match:** BEDFORD N H
- **MSRB type:** Other
- **Match score:** 86 (MODERATE)
- **MSRB type distribution across matches:** {'Other': 4}
- **Analysis:** New England towns are general-purpose local governments equivalent to cities. MSRB classifies them as Other. Your CITY classification is reasonable for jurisdictional analysis.

### Angelina & Neches River Authority [TX]

- **Your classification:** STATE (State agency)
- **MSRB best match:** ANGELINA & NECHES RIV AUTH TEX INDL DEV CORP IND L DEV REV
- **MSRB type:** City
- **Match score:** 86 (MODERATE)
- **MSRB type distribution across matches:** {'City': 9, 'County': 4}
- **Analysis:** MSRB has classified this entity under City, which may reflect local rather than state control. Your STATE classification assigns it to the controlling state. Review whether this entity truly operates at the state level.

### City of Manchester NH Sewer Revenue [NH]

- **Your classification:** CITY (Direct government)
- **MSRB best match:** MANCHESTER N H
- **MSRB type:** Other
- **Match score:** 86 (MODERATE)
- **MSRB type distribution across matches:** {'Other': 6}
- **Analysis:** MSRB classifies this city entity's bond programs as Other (typically used for revenue bonds). Your CITY classification reflects the actual governmental jurisdiction. The MSRB category may reflect the bond type rather than the issuer type.

### City of Charleston SC Waterworks & Sewer System Revenue [SC]

- **Your classification:** CITY (Direct government)
- **MSRB best match:** CHARLESTON CNTY S C
- **MSRB type:** County
- **Match score:** 86 (MODERATE)
- **MSRB type distribution across matches:** {'County': 10, 'Other': 4}
- **Analysis:** MSRB lists this under a county-level entry. Review whether the issuer is truly at the city level or operates at the county level.

### City & County of Honolulu HI [HI]

- **Your classification:** CITY (Direct government)
- **MSRB best match:** HONOLULU HAWAII CITY & CNTY BRD WTR SUPPLY WTR & CONS REVS
- **MSRB type:** County
- **Match score:** 86 (MODERATE)
- **MSRB type distribution across matches:** {'County': 14}
- **Analysis:** MSRB lists this under a county-level entry. Review whether the issuer is truly at the city level or operates at the county level.

### Morgantown Utility Board Inc [WV]

- **Your classification:** CITY (Public utility)
- **MSRB best match:** MORGANTOWN W VA
- **MSRB type:** Other
- **Match score:** 86 (MODERATE)
- **MSRB type distribution across matches:** {'Other': 2, 'State': 1}
- **Analysis:** MSRB classifies this city entity's bond programs as Other (typically used for revenue bonds). Your CITY classification reflects the actual governmental jurisdiction. The MSRB category may reflect the bond type rather than the issuer type.

### Sustainable Energy Utility Inc [DE]

- **Your classification:** STATE (State agency)
- **MSRB best match:** SUSTAINABLE ENERGY UTIL INC DEL ENERGY EFFICIENCY REV
- **MSRB type:** City
- **Match score:** 86 (MODERATE)
- **MSRB type distribution across matches:** {'City': 2}
- **Analysis:** MSRB has classified this entity under City, which may reflect local rather than state control. Your STATE classification assigns it to the controlling state. Review whether this entity truly operates at the state level.

### Private Colleges & Universities Authority [GA]

- **Your classification:** STATE (Financing authority)
- **MSRB best match:** PRIVATE COLLEGES & UNIVS AUTH GA IAM COML PAPER NTS 3/A2 EMORY UNIV
- **MSRB type:** Other
- **Match score:** 86 (MODERATE)
- **MSRB type distribution across matches:** {'Other': 5}
- **Analysis:** MSRB classifies state authorities/agencies as Other rather than State. Your STATE classification reflects the controlling jurisdiction. MSRB reserves State for the state government itself.

### Town of Salem NH [NH]

- **Your classification:** CITY (Direct government)
- **MSRB best match:** SALEM N H
- **MSRB type:** Other
- **Match score:** 86 (MODERATE)
- **MSRB type distribution across matches:** {'Other': 2}
- **Analysis:** MSRB classifies this city entity's bond programs as Other (typically used for revenue bonds). Your CITY classification reflects the actual governmental jurisdiction. The MSRB category may reflect the bond type rather than the issuer type.

### West County Facilities Financing Authority [CA]

- **Your classification:** COUNTY (Financing authority)
- **MSRB best match:** CITY OF SAN DIEGO - PUBLIC FACILITIES FINANCING AUTHORITY LEASE REVENUE COMMERCIAL PAPER (79729T) (CA)
- **MSRB type:** Other
- **Match score:** 86 (MODERATE)
- **MSRB type distribution across matches:** {'Other': 6, 'City': 5}
- **Analysis:** MSRB classifies this county entity as Other. Your COUNTY classification reflects the jurisdictional level. The MSRB category may reflect the special-purpose nature of the entity.

## Plausible differences — MSRB uses parent jurisdiction (67 issuers)

In these cases, you used a more specific jurisdiction type (SCHOOL_DISTRICT, SPECIAL_DISTRICT, or MULTI_JURISDICTIONAL) and MSRB used the parent jurisdiction (City, County, or State). Your more granular classification is reasonable and provides richer analytical detail.

| Issuer | State | Your Type | MSRB Type | MSRB Match | Score |
|---|---|---|---|---|---|
| Benton Washington Regional Public Water Authority | AR | MULTI_JURISDICTIONAL | City | BENTON ARK GEN REV | 86 |
| Conway County Regional Water Distribution District | AR | MULTI_JURISDICTIONAL | City | CONWAY ARK ELEC REV | 86 |
| James Fork Regional Water District | AR | MULTI_JURISDICTIONAL | City | JAMES FORK REGL WTR DIST ARK WTR REV | 79 |
| Lawrence County Regional Water District | AR | MULTI_JURISDICTIONAL | County | LAWRENCE CNTY ARK SCH DIST | 86 |
| San Diego Association of Governments | CA | MULTI_JURISDICTIONAL | City | CITY & COUNTY OF SAN FRANCISCO - CERTIFICATES OF PARTICIPATI | 86 |
| Cherokee Metropolitan District/CO | CO | MULTI_JURISDICTIONAL | City | CHEROKEE COLO WTR DIST | 86 |
| Triview Metropolitan District | CO | MULTI_JURISDICTIONAL | City | METROPOLITAN DENVER COLO SEW DISP DIST NO 001 | 86 |
| Windy Gap Firming Project Water Activity Enterprise | CO | MULTI_JURISDICTIONAL | City | WINDY GAP FIRMING PROJ WTR ACTIVITY ENTERPRISE COLO SR REV | 88 |
| Greater New Haven Water Pollution Control Authority | CT | MULTI_JURISDICTIONAL | City | CITY OF NEW HAVEN | 86 |
| Hartford County Metropolitan District Clean Water Project Revenue | CT | MULTI_JURISDICTIONAL | City | HARTFORD CONN | 86 |
| Mattabassett District | CT | MULTI_JURISDICTIONAL | City | MATTABASSETT DIST CONN | 84 |
| South Central Connecticut Regional Water Authority | CT | MULTI_JURISDICTIONAL | State | CONNECTICUT ST | 88 |
| Iowa Lakes Regional Water | IA | MULTI_JURISDICTIONAL | City | IOWA LAKES REGL WTR IOWA WTR REV | 86 |
| LaGrange County Regional Utility District | IN | MULTI_JURISDICTIONAL | County | LAGRANGE CNTY IND | 86 |
| Berkshire Wind Power Cooperative Corp | MA | MULTI_JURISDICTIONAL | County | BERKSHIRE CNTY MASS | 86 |
| Charles River Pollution Control District | MA | MULTI_JURISDICTIONAL | City | SALEM MASS POLLUTION CTL REV | 86 |
| Greater Lawrence Sanitation District/MA | MA | MULTI_JURISDICTIONAL | City | LAWRENCE MASS | 86 |
| Marthas Vineyard Land Bank | MA | MULTI_JURISDICTIONAL | City | MARTHAS VINEYARD MASS REFUSE DISP & RES RECOVERYDIST | 86 |
| Massachusetts Municipal Wholesale Electric Co | MA | MULTI_JURISDICTIONAL | State | MASSACHUSETTS ST | 90 |
| Upper Blackstone Water Pollution Abatement District | MA | MULTI_JURISDICTIONAL | City | UPPER BLACKSTONE WTR POLLUTN ABATEMENT DIST MASS | 87 |
| MBS International Airport Revenue | MI | MULTI_JURISDICTIONAL | City | INTERNATIONAL ELDERLY CARE INC MICH FIRST MTG HE ALTH FAC | 86 |
| Metropolitan Council | MN | MULTI_JURISDICTIONAL | City | METROPOLITAN COUNCIL MINN MINNEAPOLIS- ST PAUL AREA SPORTS F | 100 |
| Western Minnesota Municipal Power Agency | MN | MULTI_JURISDICTIONAL | State | SOUTHERN MINNESOTA MUNICIPAL POWER AGENCY | 94 |
| Missouri Joint Municipal Electric Utility Commission | MO | MULTI_JURISDICTIONAL | City | FB MISSOURI TR | 86 |
| Silver City Joint Utility System Revenue | NM | MULTI_JURISDICTIONAL | City | SILVER CITY N MEX | 86 |
| Mountain Regional Water Special Service District | UT | MULTI_JURISDICTIONAL | City | EAGLE MOUNTAIN UTAH SPL ASSMT | 86 |
| Wasatch Integrated Waste Management District | UT | MULTI_JURISDICTIONAL | County | WASATCH CNTY UTAH | 86 |
| Discovery Clean Water Alliance | WA | MULTI_JURISDICTIONAL | City | DISCOVERY CLEAN WTR ALLIANCE WASH SWR REV | 89 |
| Bardstown Independent School District Finance Corp | KY | SCHOOL_DISTRICT | City | BARDSTOWN KY | 86 |
| Berea Independent School District Finance Corp | KY | SCHOOL_DISTRICT | City | BEREA KY | 86 |
| Fort Thomas Independent School District Finance Corp | KY | SCHOOL_DISTRICT | City | FORT THOMAS KY | 88 |
| Frankfort Independent School District Finance Corp | KY | SCHOOL_DISTRICT | City | FRANKFORT KY | 86 |
| Owensboro Independent School District Finance Corp | KY | SCHOOL_DISTRICT | City | OWENSBORO KY | 86 |
| Anchor Bay School District | MI | SCHOOL_DISTRICT | City | BAY CITY MICH | 86 |
| Berrien Springs Public Schools | MI | SCHOOL_DISTRICT | County | BERRIEN CNTY MICH | 86 |
| Crestwood School District/MI | MI | SCHOOL_DISTRICT | City | CRESTWOOD MICH SCH DIST | 82 |
| Escanaba Area Public Schools | MI | SCHOOL_DISTRICT | City | ESCANABA MICH | 86 |
| Holt Public Schools | MI | SCHOOL_DISTRICT | City | HOLT MICH PUB SCHS | 70 |
| Lansing School District | MI | SCHOOL_DISTRICT | City | LANSING MICH | 86 |
| Monroe County Intermediate School District | MI | SCHOOL_DISTRICT | City | MONROE MICH | 86 |
| Morenci Area Schools | MI | SCHOOL_DISTRICT | City | BARAGA MICH AREA SCHS FORMERLY BARAGA TWP MICH SCH DIST TO 0 | 86 |
| North Muskegon Public Schools | MI | SCHOOL_DISTRICT | City | MUSKEGON MICH | 86 |
| Warren Woods Public Schools | MI | SCHOOL_DISTRICT | City | GROSSE POINTE WOODS MICH WTR SUPPLY & SEW DISP SYS REV | 86 |
| Westwood Heights Schools | MI | SCHOOL_DISTRICT | City | DEARBORN HEIGHTS MICH CITY SCH DIST NO 007 | 86 |
| Crystal City School District No 47 | MO | SCHOOL_DISTRICT | City | CRYSTAL CITY MO CTFS PARTN | 89 |
| North Kansas City School District No 74 | MO | SCHOOL_DISTRICT | City | NORTH KANSAS CITY MO | 92 |
| Cross County Rural Water System | AR | SPECIAL_DISTRICT | County | CROSS CNTY ARK RESIDENTIAL HSG FACS BRD SINGLE FAMILY MTG RE | 86 |
| Southside Public Water Authority | AR | SPECIAL_DISTRICT | City | SOUTHSIDE ARK PUB WTR AUTH WTR & SWR REV | 71 |
| Southwest Water Users Public Water Authority of the State of Arkansas | AR | SPECIAL_DISTRICT | State | ARKANSAS DEVELOPMENT FINANCE AUTHORITY | 86 |
| Warren Water District Service Area 6 | AR | SPECIAL_DISTRICT | City | WARREN ARK WTR & SWR REV | 86 |
| Portland Water District | ME | SPECIAL_DISTRICT | City | PORTLAND ME | 86 |
| Portland Water District Water System Revenue | ME | SPECIAL_DISTRICT | City | PORTLAND ME | 86 |
| Shell Rock River Watershed District | MN | SPECIAL_DISTRICT | City | DEER RIVER MINN | 86 |
| Old Gainesboro Road Utility District of Jackson & Putnam Counties | TN | SPECIAL_DISTRICT | City | GAINESBORO TENN | 86 |
| Bell County Municipal Utility District No 1 | TX | SPECIAL_DISTRICT | City | AVERY TEX RANCH RD DIST NO 1 | 86 |
| Buena Vista-Bethel Special Utiltiy District | TX | SPECIAL_DISTRICT | City | RIO VISTA TEX | 86 |
| Denton County Fresh Water Supply District No 7 | TX | SPECIAL_DISTRICT | County | DENTON CNTY TEX FRESH WTR SUPPLY DIST NO 7 | 89 |
| Denton County Levee Improvement District No 1 | TX | SPECIAL_DISTRICT | State | TEXAS TRANSPORTATION COMMISSION, STATE OF TEXAS HIGHWAY IMPR | 86 |
| Fort Bend County Levee Improvement District No 7 | TX | SPECIAL_DISTRICT | City | CITY OF FORT WORTH, TEXAS | 86 |
| Fort Bend County Municipal Utility District No 152 | TX | SPECIAL_DISTRICT | City | CITY OF FORT WORTH, TEXAS | 86 |
| Fort Bend County Municipal Utility District No 194 | TX | SPECIAL_DISTRICT | City | CITY OF FORT WORTH, TEXAS | 86 |
| Galveston County Municipal Utility District No 44 | TX | SPECIAL_DISTRICT | City | CITY OF GALVESTON | 86 |
| Harris County Municipal Utility District No 1 | TX | SPECIAL_DISTRICT | County | ARANSAS CNTY TEX NAV DIST NO 1 | 86 |
| Hays County Municipal Utility District No 4 | TX | SPECIAL_DISTRICT | City | AUSTIN TEX UTIL SYS REV TAXABLE DISC COML PAPERNTS 3/A2 YRS  | 86 |
| Kaufman County Fresh Water Supply District No 1-C | TX | SPECIAL_DISTRICT | County | KAUFMAN CNTY TEX FRESH WTR SUPPLY DIST NO 1-C | 89 |
| Northlake Municipal Management District No 1 | TX | SPECIAL_DISTRICT | City | ARCOLA TEX MUN MGMT DIST NO 1 | 86 |
| Central Valley Water Reclamation Facility | UT | SPECIAL_DISTRICT | City | CENTRAL VY WTR RECLAMATION FAC UTAH SWR REV | 78 |

## Agrees via alternate MSRB entry (215 issuers)

The best MSRB match had a different type, but another high-scoring MSRB entry for the same entity has a type consistent with your classification. These are not discrepancies.

| Issuer | State | Your Type | MSRB Best Type | MSRB Match | Score |
|---|---|---|---|---|---|
| Antelope Valley-East Kern Water Agency Financing Authority | CA | CITY | Other | MOJAVE WATER AGENCY | 86 |
| Hastings Campus Housing Finance Authority | CA | CITY | State | CALIFORNIA HOUSING FINANCE AGENCY (CALHFA) - AFFORDABLE HOUS | 86 |
| Lakeport Municipal Financing Agency | CA | CITY | State | CALIFORNIA HOUSING FINANCE AGENCY (CALHFA) - MUNICIPAL CERTI | 86 |
| San Rafael Joint Powers Financing Authority | CA | CITY | Other | CITY OF SAN DIEGO - CONVENTION CENTER EXPANSION FINANCING AU | 86 |
| Santa Clarita Public Finance Authority | CA | CITY | State | CALIFORNIA HOUSING FINANCE AGENCY (CALHFA) - AFFORDABLE HOUS | 86 |
| Woodland Finance Authority | CA | CITY | State | CALIFORNIA HOUSING FINANCE AGENCY (CALHFA) - AFFORDABLE HOUS | 86 |
| Board of Water Commissioners City & County of Denver/The | CO | CITY | County | DENVER WATER | 100 |
| City of Sheridan CO | CO | CITY | County | ARAPAHOE CNTY COLO SCH DIST NO 002 SHERIDAN | 86 |
| Denver Wastewater Management Division Department of Public Works | CO | CITY | County | DENVER WATER | 86 |
| City of Oakland Park FL Water & Sewer Revenue | FL | CITY | Other | OAKLAND PARK FLA | 86 |
| Town of Miami Lakes FL Stormwater Utility System Revenue | FL | CITY | Other | FORT PIERCE FLA STORMWATER UTIL REV | 86 |
| City & County Honolulu HI Wastewater System Revenue | HI | CITY | County | HONOLULU HAWAII CITY & CNTY WASTEWTR SYS REV | 86 |
| City of Rock Island IL | IL | CITY | County | ROCK ISLAND CNTY ILL | 86 |
| Lexington-Fayette Urban County Government | KY | CITY | County | LEXINGTON-FAYETTE URBAN CNTY GOVT KY | 86 |
| Louisville and Jefferson County Metropolitan Sewer District | KY | CITY | Other | LOUISVILLE/JEFFERSON COUNTY METROPOLITAN SEWER DISTRICT | 100 |
| Housing & Redevelopment Authority of The City of St Paul Minnesota | MN | CITY | State | MINNESOTA HOUSING | 100 |
| City of Minot ND | ND | CITY | Other | MINOT N D | 86 |
| Brick Township Municipal Utilities Authority/The | NJ | CITY | Other | WASHINGTON TOWNSHIP MUNICIPAL UTILITIES AUTHORITY | 88 |
| City of Wildwood NJ | NJ | CITY | Other | WILDWOOD N J | 86 |
| Jersey City Municipal Utilities Authority | NJ | CITY | Other | NEW JERSEY INFRASTRUCTURE BANK (NJIB) (FORMERLY KNOWN AS NEW | 86 |
| Township of Monroe NJ/Middlesex County | NJ | CITY | Other | MIDDLESEX N J | 86 |
| City of Albuquerque NM Refuse Removal & Disposal Revenue | NM | CITY | Other | ALBUQUERQUE N MEX | 86 |
| Buffalo Sewer Authority | NY | CITY | Other | BUFFALO N Y | 86 |
| City of Auburn NY | NY | CITY | State | $179,220,000 HOSPITAL FOR SPECIAL SURGERY TAXABLE BONDS SERI | 86 |
| Town of Murray NY | NY | CITY | Other | MURRAY TOWN N Y | 88 |
| Town of York NY | NY | CITY | State | $179,220,000 HOSPITAL FOR SPECIAL SURGERY TAXABLE BONDS SERI | 86 |
| Greene Township Municipal Authority | PA | CITY | County | GREENE CNTY PA | 86 |
| City of Columbia SC Stormwater System Revenue | SC | CITY | Other | COLUMBIA S C | 86 |
| City of Columbia SC Waterworks & Sewer System Revenue | SC | CITY | Other | COLUMBIA S C | 86 |
| Metropolitan Government of Nashville & Davidson County TN Water & Sewer Revenue | TN | CITY | County | THE METROPOLITAN GOVERNMENT OF NASHVILLE AND DAVIDSON COUNTY | 93 |
| City of Wheeling WV Waterworks & Sewerage System Revenue | WV | CITY | Other | WHEELING W VA | 86 |
| County of Cullman AL Water Revenue | AL | COUNTY | City | CULLMAN ALA | 86 |
| County of San Diego CA | CA | COUNTY | City | CITY & COUNTY OF SAN FRANCISCO - CERTIFICATES OF PARTICIPATI | 86 |
| Los Angeles County Development Authority | CA | COUNTY | City | CITY OF LOS ANGELES | 86 |
| Los Angeles County Public Works Financing Authority | CA | COUNTY | City | CITY OF LOS ANGELES | 86 |
| San Diego County Water Authority | CA | COUNTY | Other | SAN DIEGO COUNTY WATER AUTHORITY | 100 |
| San Luis Obispo County Financing Authority | CA | COUNTY | City | CITY & COUNTY OF SAN FRANCISCO BAYSHORE HESTER AD NO. 95-1 - | 86 |
| Brunswick & Glynn County Development Authority | GA | COUNTY | City | BRUNSWICK GA | 86 |
| County of Greene IA | IA | COUNTY | City | GREENE IOWA | 86 |
| DuPage County Forest Preserve District | IL | COUNTY | City | FOREST PK ILL | 86 |
| St Charles County Industrial Development Authority | MO | COUNTY | City | ST CHARLES MO | 87 |
| County of Grand Forks ND | ND | COUNTY | Other | GRAND FORKS N D | 87 |
| County of Passaic NJ | NJ | COUNTY | Other | PASSAIC N J | 86 |
| Passaic County Improvement Authority/The | NJ | COUNTY | Other | PASSAIC N J | 86 |
| Salem County Pollution Control Financing Authority | NJ | COUNTY | Other | SALEM N J | 86 |
| Saratoga County Water Authority | NY | COUNTY | Other | SARATOGA N Y | 86 |
| Western Nassau County Water Authority | NY | COUNTY | Other | NASSAU N Y | 86 |
| Dayton-Montgomery County Port Authority | OH | COUNTY | City | CITY OF DAYTON  | 86 |
| Toledo-Lucas County Port Authority | OH | COUNTY | Other | TOLEDO-LUCAS COUNTY PORT AUTHORITY | 100 |
| Warren County Port Authority | OH | COUNTY | Other | TOLEDO-LUCAS COUNTY PORT AUTHORITY | 86 |
| County of Lancaster PA | PA | COUNTY | City | LANCASTER PA | 100 |
| Lancaster County Solid Waste Management Authority | PA | COUNTY | City | LANCASTER PA | 86 |
| Fairfax County Economic Development Authority | VA | COUNTY | Other | FAIRFAX COUNTY WATER AUTHORITY | 89 |
| County of King WA | WA | COUNTY | Other | KING COUNTY FIRE PROTECTION DISTRICT NO. 27 | 86 |
| County of Okanogan WA | WA | COUNTY | City | KENT, WA | 86 |
| County of Milwaukee WI | WI | COUNTY | City | HOUSING AUTHORITY OF THE CITY OF MILWAUKEE | 86 |
| County of Portage WI | WI | COUNTY | City | PORTAGE WIS | 86 |
| Central Arkansas Water | AR | MULTI_JURISDICTIONAL | State | ARKANSAS NATURAL RESOURCES COMMISSION | 86 |
| California Municipal Finance Authority | CA | MULTI_JURISDICTIONAL | State | CALIFORNIA ST | 87 |
| California Public Finance Authority | CA | MULTI_JURISDICTIONAL | State | CALIFORNIA ST | 87 |
| California Statewide Communities Development Authority | CA | MULTI_JURISDICTIONAL | State | CALIFORNIA ST | 90 |
| Mendota Joint Powers Financing Authority | CA | MULTI_JURISDICTIONAL | City | MENDOTA CALIF | 86 |
| Monterey Regional Waste Management Authority | CA | MULTI_JURISDICTIONAL | City | MONTEREY CALIF | 86 |
| Peninsula Corridor Joint Powers Board Measure RR Sales Tax Revenue | CA | MULTI_JURISDICTIONAL | City | CITY OF SAN JOSE - SPECIAL HOTEL TAX BONDS | 86 |
| San Bernardino Associated Governments | CA | MULTI_JURISDICTIONAL | City | CITY & COUNTY OF SAN FRANCISCO - CERTIFICATES OF PARTICIPATI | 86 |
| Sonoma-Marin Area Rail Transit District | CA | MULTI_JURISDICTIONAL | City | CITY & COUNTY OF SAN FRANCISCO CFD NO. 2014-1 (TRANSBAY TRAN | 86 |
| South Bayside Waste Management Authority | CA | MULTI_JURISDICTIONAL | City | SOUTH BAYSIDE WASTE MGMT AUTH CALIF SOLID WASTEENTERPRISE R  | 86 |
| Southern California Public Power Authority | CA | MULTI_JURISDICTIONAL | State | CALIFORNIA ST | 87 |
| Upper Eagle Regional Water Authority | CO | MULTI_JURISDICTIONAL | City | EAGLE COLO | 86 |
| East Central Regional Wastewater Treatment Facilities Operation Board | FL | MULTI_JURISDICTIONAL | County | BREVARD CNTY FLA WTR & WASTEWATER UTIL REV | 86 |
| Gainesville & Hall County Development Authority | GA | MULTI_JURISDICTIONAL | City | GAINESVILLE GA | 88 |
| South Georgia Governmental Services Authority | GA | MULTI_JURISDICTIONAL | City | FB GEORGIA TR | 86 |
| Jackson & Williamson Counties Community High School District 165 Carbondale | IL | MULTI_JURISDICTIONAL | City | CARBONDALE ILL | 86 |
| Macoupin & Madison Counties Community Unit School District No 8 Bunker Hill | IL | MULTI_JURISDICTIONAL | State | KEWANEE COMMUNITY UNIT SCHOOL DISTRICT #229 | 86 |
| Madison Bond Etc Counties Community Unit School District No 5 Highland | IL | MULTI_JURISDICTIONAL | State | KEWANEE COMMUNITY UNIT SCHOOL DISTRICT #229 | 86 |
| Metropolitan Pier & Exposition Authority | IL | MULTI_JURISDICTIONAL | City | METROPOLITAN PIER & EXPOSITION AUTH ILL REV | 91 |
| Massachusetts Water Resources Authority | MA | MULTI_JURISDICTIONAL | State | MASSACHUSETTS ST | 90 |
| Eco Maine | ME | MULTI_JURISDICTIONAL | State | MAINE LEASE REV | 100 |
| Southern Ohio Port Authority | OH | MULTI_JURISDICTIONAL | City | CANTON OHIO | 86 |
| Port of Portland OR Airport Revenue | OR | MULTI_JURISDICTIONAL | City | PORT PORTLAND ORE | 87 |
| Allegheny Valley Joint Sewage Authority | PA | MULTI_JURISDICTIONAL | City | ALLEGHENY TWP PA | 86 |
| Burgettstown-Smith Township Joint Sewerage Authority | PA | MULTI_JURISDICTIONAL | City | BURGETTSTOWN AREA SCH DIST PA | 86 |
| Center-West Joint Sewer Authority | PA | MULTI_JURISDICTIONAL | City | CENTER TWP PA | 86 |
| Greater Greensburg Sewer Authority | PA | MULTI_JURISDICTIONAL | City | GREENSBURG PA | 87 |
| Millcreek-Richland Joint Authority | PA | MULTI_JURISDICTIONAL | City | RICHLAND TWP PA | 86 |
| Mountaintop Area Joint Sanitary Authority | PA | MULTI_JURISDICTIONAL | City | ALLENTOWN PA AREA HOSP AUTH REV | 86 |
| Shamokin-Coal Township Joint Sewer Authority | PA | MULTI_JURISDICTIONAL | City | TOWNSHIP OF UPPER ST. CLAIR | 86 |
| Wilkinsburg-Penn Joint Water Authority/The | PA | MULTI_JURISDICTIONAL | City | NORTH PENN PA WTR AUTH WTR REV | 86 |
| Horizon Regional Municipal Utility District | TX | MULTI_JURISDICTIONAL | City | HORIZON CITY TEX | 86 |
| Utah Associated Municipal Power Systems | UT | MULTI_JURISDICTIONAL | State | STATE OF UTAH | 86 |
| Northern Virginia Transportation Commission | VA | MULTI_JURISDICTIONAL | State | TRANSPORTATION PROGRAM AND REVENUE BONDS NORTHERN VIRGINIA T | 86 |
| Madison County Board of Education/AL | AL | SCHOOL_DISTRICT | City | MADISON ALA | 86 |
| Atwater Elementary School District | CA | SCHOOL_DISTRICT | City | ATWATER CALIF | 86 |
| Capistrano Unified School District | CA | SCHOOL_DISTRICT | City | POWAY UNIFIED SCHOOL DISTRICT | 88 |
| Corning Union Elementary School District | CA | SCHOOL_DISTRICT | City | CORNING CALIF REV | 86 |
| Dublin Unified School District | CA | SCHOOL_DISTRICT | City | POWAY UNIFIED SCHOOL DISTRICT | 88 |
| Esparto Unified School District | CA | SCHOOL_DISTRICT | City | POWAY UNIFIED SCHOOL DISTRICT | 88 |
| Fairfield-Suisun Unified School District | CA | SCHOOL_DISTRICT | City | POWAY UNIFIED SCHOOL DISTRICT | 88 |
| Hayward Unified School District | CA | SCHOOL_DISTRICT | City | POWAY UNIFIED SCHOOL DISTRICT | 88 |
| Lucia Mar Unified School District | CA | SCHOOL_DISTRICT | City | POWAY UNIFIED SCHOOL DISTRICT | 88 |
| Marysville Joint Unified School District | CA | SCHOOL_DISTRICT | City | POWAY UNIFIED SCHOOL DISTRICT | 88 |
| Red Bluff Union Elementary School District | CA | SCHOOL_DISTRICT | City | RED BLUFF CALIF | 86 |
| San Diego Unified School District/CA | CA | SCHOOL_DISTRICT | City | POWAY UNIFIED SCHOOL DISTRICT | 88 |
| Western Placer Unified School District | CA | SCHOOL_DISTRICT | City | POWAY UNIFIED SCHOOL DISTRICT | 88 |
| Westminster School District | CA | SCHOOL_DISTRICT | City | WESTMINSTER CALIF CTFS PARTN | 86 |
| Madison County School District/GA | GA | SCHOOL_DISTRICT | City | ACWORTH GA HSG AUTH REV | 86 |
| Greene County Community School District | IA | SCHOOL_DISTRICT | City | GREENE IOWA | 86 |
| Cook County Community Consolidated School District No 168 Sauk Village | IL | SCHOOL_DISTRICT | State | KEWANEE COMMUNITY UNIT SCHOOL DISTRICT #229 | 86 |
| Jackson County Community Consolidated School District No 140 Unity Point | IL | SCHOOL_DISTRICT | State | KEWANEE COMMUNITY UNIT SCHOOL DISTRICT #229 | 86 |
| Kane County School District No 129 West Aurora | IL | SCHOOL_DISTRICT | City | AURORA ILL | 86 |
| Madison County Community Unit School District No 7 Edwardsville | IL | SCHOOL_DISTRICT | City | EDWARDSVILLE ILL | 86 |
| Frankton-Lapel Community Schools | IN | SCHOOL_DISTRICT | City | FRANKTON IND SWR REV | 86 |
| South Ripley Community Multi-School Building Corp | IN | SCHOOL_DISTRICT | City | CITY OF SOUTH BEND, INDIANA | 86 |
| Covington Independent School District Finance Corp/KY | KY | SCHOOL_DISTRICT | City | COVINGTON KY | 100 |
| Essexville-Hampton Public Schools/MI | MI | SCHOOL_DISTRICT | City | ESSEXVILLE-HAMPTON MICH PUB SCHS | 88 |
| Flushing Community Schools | MI | SCHOOL_DISTRICT | City | FLUSHING MICH | 86 |
| Melvindale Northern Allen Park Public Schools | MI | SCHOOL_DISTRICT | City | ALLEN PARK MICH | 86 |
| Clearwater Reorganized School District No R-1 | MO | SCHOOL_DISTRICT | County | ADAIR CNTY MO R-1 SCH DIST LEASE CTFS PARTN | 86 |
| Dexter School District No R-11 Stoddard/MO | MO | SCHOOL_DISTRICT | City | DEXTER MO CTFS PARTN | 100 |
| Hayti Reorganized School District No 2 | MO | SCHOOL_DISTRICT | City | HARTVILLE MO R-2 SCH DIST | 86 |
| Hazelwood School District | MO | SCHOOL_DISTRICT | City | HAZELWOOD MO | 86 |
| Jackson County School District No R-IV Blue Springs | MO | SCHOOL_DISTRICT | City | BLUE SPRINGS MO | 89 |
| Lonedell R-XIV School District | MO | SCHOOL_DISTRICT | County | ANDREW CNTY MO PUB WTR SUPPLY DIST NO 1 WTRWKS R EV | 86 |
| Normandy Schools Collaborative | MO | SCHOOL_DISTRICT | County | NORMANDY SCHS COLLABORATIVE MO JT EXECUTIVE GOVERNIG BRD ST  | 86 |
| Pleasant Hill R-III School District | MO | SCHOOL_DISTRICT | City | PLEASANT HILL MO | 90 |
| Texas County R-IV School District Cabool | MO | SCHOOL_DISTRICT | County | ADAIR CNTY MO R-1 SCH DIST LEASE CTFS PARTN | 86 |
| Brick Township Board Of Education | NJ | SCHOOL_DISTRICT | State | LACEY TOWNSHIP BOARD OF EDUCATION | 90 |
| Cranford Township Board Of Education | NJ | SCHOOL_DISTRICT | State | LACEY TOWNSHIP BOARD OF EDUCATION | 90 |
| East Brunswick Township Board Of Education | NJ | SCHOOL_DISTRICT | State | LACEY TOWNSHIP BOARD OF EDUCATION | 90 |
| Florence Township Board of Education | NJ | SCHOOL_DISTRICT | State | LACEY TOWNSHIP BOARD OF EDUCATION | 90 |
| Gloucester City School District | NJ | SCHOOL_DISTRICT | City | GLOUCESTER CITY N J | 88 |
| Monroe Township Board of Education/Middlesex County | NJ | SCHOOL_DISTRICT | State | LACEY TOWNSHIP BOARD OF EDUCATION | 90 |
| Orange Township Board of Education | NJ | SCHOOL_DISTRICT | State | LACEY TOWNSHIP BOARD OF EDUCATION | 90 |
| Union Township Board of Education/Union County | NJ | SCHOOL_DISTRICT | State | LACEY TOWNSHIP BOARD OF EDUCATION | 90 |
| Upper Deerfield Township Board of Education | NJ | SCHOOL_DISTRICT | State | LACEY TOWNSHIP BOARD OF EDUCATION | 90 |
| Vernon Township Board of Education | NJ | SCHOOL_DISTRICT | State | LACEY TOWNSHIP BOARD OF EDUCATION | 90 |
| Yamhill County School District No 1 Yamhill-Carlton | OR | SCHOOL_DISTRICT | County | YAMHILL CNTY ORE SCH DIST NO 1 YAMHILL-CARLTON | 87 |
| Central Columbia School District | PA | SCHOOL_DISTRICT | City | COLUMBIA BORO PA | 86 |
| Ligonier Valley School District | PA | SCHOOL_DISTRICT | City | LIGONIER PA | 86 |
| Mcguffey School District | PA | SCHOOL_DISTRICT | City | MCGUFFEY SCH DIST PA | 77 |
| Penncrest School District | PA | SCHOOL_DISTRICT | City | PENNCREST SCH DIST PA | 78 |
| Richland County School District No 2/SC | SC | SCHOOL_DISTRICT | County | RICHLAND CNTY S C REC DIST | 86 |
| Arcadia School District | WI | SCHOOL_DISTRICT | City | ARCADIA WIS | 86 |
| Cambridge School District | WI | SCHOOL_DISTRICT | City | CAMBRIDGE WIS | 86 |
| Middleton-Cross Plains Area School District/WI | WI | SCHOOL_DISTRICT | City | MIDDLETON-CROSS PLAINS AREA SCH DIST WIS | 91 |
| Monona Grove School District/WI | WI | SCHOOL_DISTRICT | City | MONONA GROVE WIS SCH DIST | 86 |
| Oregon School District/WI | WI | SCHOOL_DISTRICT | City | OREGON WIS SCHOOL DISTRICT | 98 |
| Racine Unified School District | WI | SCHOOL_DISTRICT | City | RACINE WIS | 86 |
| Mid-Arkansas Utilities Public Water Authority | AR | SPECIAL_DISTRICT | State | ARKANSAS ST DEV FIN AUTH WTR REV | 86 |
| Imperial Irrigation District Electric System Revenue | CA | SPECIAL_DISTRICT | City | IMPERIAL CALIF CTFS PARTN | 86 |
| Los Angeles County Sanitation Districts Financing Authority | CA | SPECIAL_DISTRICT | City | CITY OF LOS ANGELES | 86 |
| Pajaro Valley Water Management Agency | CA | SPECIAL_DISTRICT | State | CALIFORNIA HOUSING FINANCE AGENCY (CALHFA) - AFFORDABLE HOUS | 86 |
| Sacramento Area Flood Control Agency | CA | SPECIAL_DISTRICT | State | CALIFORNIA HOUSING FINANCE AGENCY (CALHFA) - AFFORDABLE HOUS | 86 |
| Sacramento Municipal Utility District | CA | SPECIAL_DISTRICT | City | SACRAMENTO CALIF | 86 |
| San Francisco Bay Area Rapid Transit District | CA | SPECIAL_DISTRICT | City | CITY & COUNTY OF SAN FRANCISCO BAYSHORE HESTER AD NO. 95-1 - | 86 |
| San Francisco Bay Area Rapid Transit District Sales Tax Revenue | CA | SPECIAL_DISTRICT | City | SAN FRANCISCO CALIF BAY AREA RAPID TRAN DIST SALES TAX REV | 88 |
| San Joaquin Valley Clean Energy Authority | CA | SPECIAL_DISTRICT | City | CITY & COUNTY OF SAN FRANCISCO BAYSHORE HESTER AD NO. 95-1 - | 86 |
| Stockton-East Water District | CA | SPECIAL_DISTRICT | City | CITY OF STOCKTON | 86 |
| Three Rivers Levee Improvement Authority | CA | SPECIAL_DISTRICT | City | CITY & COUNTY OF SAN FRANCISCO BAYSHORE HESTER AD NO. 95-1 - | 86 |
| Trinity Public Utilities District | CA | SPECIAL_DISTRICT | County | TRINITY CNTY CALIF | 86 |
| Eagle River Water & Sanitation District Water Revenue | CO | SPECIAL_DISTRICT | City | EAGLE COLO | 86 |
| Seminole Improvement District | FL | SPECIAL_DISTRICT | County | SEMINOLE CNTY FLA | 86 |
| Metropolitan Water Reclamation District of Greater Chicago | IL | SPECIAL_DISTRICT | City | CHICAGO WATER | 100 |
| Yorkville-Bristol Sanitation District | IL | SPECIAL_DISTRICT | City | YORKVILLE ILL | 86 |
| Terrebonne Levee & Conservation District Sales Tax Revenue | LA | SPECIAL_DISTRICT | City | ABBEVILLE LA SALES & USE TAX REV | 86 |
| Howard Bend Levee District | MO | SPECIAL_DISTRICT | City | HOWARD BEND LEVEE DIST MO | 86 |
| Southern Sandoval County Arroyo Flood Control Authority | NM | SPECIAL_DISTRICT | County | SANDOVAL CNTY N MEX | 86 |
| Port of Morrow OR | OR | SPECIAL_DISTRICT | City | PORT MORROW ORE | 88 |
| Aliquippa Municipal Water Authority Water & Sewer Revenue | PA | SPECIAL_DISTRICT | City | ALIQUIPPA PA | 86 |
| Lakes Fresh Water Supply District of Denton County | TX | SPECIAL_DISTRICT | County | LAKES FRESH WTR SUPPLY DIST DENTON CNTY TEX | 86 |
| North Mission Glen Municipal Utility District/TX | TX | SPECIAL_DISTRICT | City | CITY OF SUGAR LAND, TX | 86 |
| Tattor Municipal Road District/TX | TX | SPECIAL_DISTRICT | City | TATTOR MUN RD DIST TEX | 86 |
| Upper Brushy Creek Water Control and Improvement District | TX | SPECIAL_DISTRICT | City | BRUSHY CREEK MUN UTIL DIST TEX | 86 |
| Central Utah Water Conservancy District | UT | SPECIAL_DISTRICT | City | CENTRAL UTAH WTR CONSERVANCY DIST | 92 |
| Jordan Valley Water Conservancy District | UT | SPECIAL_DISTRICT | City | JORDAN UTAH SCH DIST | 86 |
| Southeast Arkansas College | AR | STATE | City | SOUTHEAST ARK COLLEGE CTFS PARTN ARK | 89 |
| State of Arkansas | AR | STATE | City | ARKANSAS ST TEACHERS COLLEGE REVS NAME CHANGED T O STATE COL | 90 |
| University of Arkansas | AR | STATE | Other | BOARD OF TRUSTEES OF THE UNIVERSITY OF ARKANSAS FINANCIAL IN | 100 |
| Colorado School of Mines | CO | STATE | Other | COLORADO SCHOOL OF MINES | 100 |
| Colorado Water Resources & Power Development Authority | CO | STATE | Other | COLORADO WATER RESOURCES AND POWER DEVELOPMENT AUTHORITY | 100 |
| Colorado Water Resources & Power Development Authority State Revolving Fund | CO | STATE | Other | COLORADO WATER RESOURCES AND POWER DEVELOPMENT AUTHORITY | 96 |
| Illinois Finance Authority | IL | STATE | Other | CENTRAL ILLINOIS REGIONAL AIRPORT AUTHORITY | 86 |
| Northern Illinois University | IL | STATE | City | UNIVERSITY OF ILLINOIS | 93 |
| Indiana Finance Authority | IN | STATE | Other | INDIANA BOND BANK | 86 |
| Indiana University | IN | STATE | Other | INDIANA UNIVERSITY | 100 |
| Massachusetts State College Building Authority | MA | STATE | Other | MASSACHUSETTS STATE COLLEGE BUILDING AUTHORITY | 100 |
| University of Michigan | MI | STATE | Other | MICHIGAN STATE UNIVERSITY | 93 |
| State of Montana | MT | STATE | County | MONTANA ASSN OF CNTYS JT PWRS INS AUTH REV | 86 |
| North Dakota Public Finance Authority | ND | STATE | Other | ND PUBLIC FINANCE AUTHORITY | 94 |
| Williston State College | ND | STATE | Other | WILLISTON N D | 86 |
| New Hampshire Business Finance Authority | NH | STATE | Other | NEW HAMPSHIRE HOUSING FINANCE AUTHORITY | 91 |
| New Jersey Infrastructure Bank | NJ | STATE | Other | NEW JERSEY INFRASTRUCTURE BANK (NJIB) (FORMERLY KNOWN AS NEW | 100 |
| New Mexico Finance Authority | NM | STATE | Other | NEW MEXICO FINANCE AUTHORITY | 100 |
| Metropolitan Transportation Authority | NY | STATE | Other | METROPOLITAN TRANSPORTATION AUTHORITY | 100 |
| Metropolitan Transportation Authority Dedicated Tax Fund | NY | STATE | Other | METROPOLITAN TRANSPORTATION AUTHORITY | 100 |
| New York State Energy Research & Development Authority | NY | STATE | Other | NEW YORK STATE ENERGY RESEARCH AND DEVELOPMENT AUTHORITY (NY | 100 |
| Utility Debt Securitization Authority | NY | STATE | Other | UTILITY DEBT SECURITIZATION AUTH N Y | 90 |
| Ohio Air Quality Development Authority | OH | STATE | City | CANTON OHIO | 86 |
| Ohio Higher Educational Facility Commission | OH | STATE | City | CANTON OHIO | 86 |
| Ohio State University/The | OH | STATE | Other | THE OHIO STATE UNIVERSITY | 100 |
| Ohio Water Development Authority | OH | STATE | City | CANTON OHIO | 86 |
| Ohio Water Development Authority Water Pollution Control Loan Fund | OH | STATE | Other | CENTRAL OHIO TRANSIT AUTHORITY (COTA) | 86 |
| University of Cincinnati | OH | STATE | City | CINCINNATI OHIO UNIV REV NAME CHANGED TO UNIVERSITY CINCINNA | 93 |
| Oklahoma Development Finance Authority | OK | STATE | City | OKLAHOMA CITY | 86 |
| Board of Regents of the University of Texas System | TX | STATE | Other | BOARD OF REGENTS OF THE TEXAS TECH UNIVERSITY SYSTEM | 100 |
| Texas Water Development Board | TX | STATE | Other | BOARD OF REGENTS OF THE TEXAS TECH UNIVERSITY SYSTEM | 86 |
| University of Utah/The | UT | STATE | City | UNIVERSITY UTAH CTFS PARTN | 100 |
| Utah State University | UT | STATE | City | UNIVERSITY UTAH CTFS PARTN | 100 |
| University of Virginia | VA | STATE | Other | UNIVERSITY OF VIRGINIA | 100 |
| Virginia Resources Authority Clean Water Revolving Fund | VA | STATE | Other | VIRGINIA RESOURCES AUTHORITY | 100 |
| Virginia Small Business Financing Authority | VA | STATE | Other | VIRGINIA PORT AUTHORITY | 88 |
| Washington Economic Development Finance Authority | WA | STATE | City | FB WASHINGTON TR | 86 |
| Washington State Convention Center Public Facilities District | WA | STATE | Other | WASHINGTON STATE CONVENTION CENTER PUBLIC FACILITIES DISTRIC | 100 |
| Washington State University | WA | STATE | City | FB WASHINGTON TR | 86 |
| Western Washington University | WA | STATE | City | FB WASHINGTON TR | 86 |

## Direct agreement (372 issuers)

Your classification directly matches the MSRB best match type.

| Issuer | State | Your Type | MSRB Type | MSRB Match | Score |
|---|---|---|---|---|---|
| Calera Waterworks Board | AL | CITY | City | CALERA ALA | 86 |
| City of Trussville AL | AL | CITY | City | TRUSSVILLE ALA | 87 |
| City of Vestavia Hills AL | AL | CITY | City | VESTAVIA HILLS ALA | 88 |
| Fort Payne Waterworks Board | AL | CITY | City | FORT PAYNE ALA | 86 |
| Hanceville Waterworks & Sewer Board | AL | CITY | City | HANCEVILLE ALA | 86 |
| Hoover Industrial Development Board | AL | CITY | City | HOOVER ALA | 86 |
| Opelika Utilities Board | AL | CITY | City | OPELIKA ALA | 86 |
| Ozark Utilities Board | AL | CITY | City | OZARK ALA | 86 |
| Russellville Water Works & Sewer Board | AL | CITY | City | RUSSELLVILLE ALA | 86 |
| Arkadelphia Water & Sewer System | AR | CITY | City | ARKADELPHIA ARK | 86 |
| City of Centerton AR Water & Sewer Revenue | AR | CITY | City | CENTERTON ARK WTR & SWR REV | 86 |
| City of Dardanelle AR Water & Sewer Revenue Sales & Use Tax | AR | CITY | City | DARDANELLE ARK SALES & USE TAX | 92 |
| City of El Dorado AR Water & Sewer Revenue | AR | CITY | City | EL DORADO ARK WTR & SWR REV | 86 |
| City of Heber Springs AR Water & Sewer Revenue | AR | CITY | City | CITY OF HOT SPRINGS | 88 |
| City of Hot Springs AR Wastewater Revenue | AR | CITY | City | CITY OF HOT SPRINGS | 100 |
| City of Hot Springs AR Waterworks Revenue | AR | CITY | City | CITY OF HOT SPRINGS | 100 |
| City of Little Rock AR Water Reclamation System Revenue | AR | CITY | City | LITTLE ROCK | 100 |
| City of Mountain Home AR Water & Sewer Revenue | AR | CITY | City | MOUNTAIN HOME ARK | 87 |
| City of Osceola AR Electric Water & Sewer Revenue | AR | CITY | City | OSCEOLA ARK CTFS PARTN | 86 |
| City of Osceola AR Sales & Use Tax | AR | CITY | City | OSCEOLA ARK SALES & USE TAX | 91 |
| City of Prairie Grove AR Water & Sewer Revenue | AR | CITY | City | PRAIRIE GROVE ARK | 87 |
| City of Russellville AR Water & Sewer Revenue | AR | CITY | City | RUSSELLVILLE ARK SWR REV | 86 |
| City of Ward AR Water & Sewer Revenue | AR | CITY | City | WARD ARK WTR & SWR REV | 86 |
| City of Wynne AR Water & Sewer Revenue | AR | CITY | City | WYNNE ARK WTR & SWR REV | 86 |
| Gilbert Water Resource Municipal Property Corp | AZ | CITY | City | GILBERT ARIZ | 86 |
| Alameda Community Facilities District | CA | CITY | City | CITY OF SAN JOSE - COMMUNITY FACILITIES DISTRICT BONDS | 88 |
| Chula Vista Municipal Financing Authority | CA | CITY | City | CHULA VISTA CALIF | 86 |
| City & County of San Francisco CA | CA | CITY | City | CITY & COUNTY OF SAN FRANCISCO - CERTIFICATES OF PARTICIPATI | 95 |
| City & County of San Francisco CA Community Facilities District No 2014-1 | CA | CITY | City | CITY OF SAN JOSE - COMMUNITY FACILITIES DISTRICT BONDS | 94 |
| City of Foster City CA | CA | CITY | City | FOSTER CITY CALIF | 88 |
| City of Long Beach CA Harbor Revenue | CA | CITY | City | CITY OF LONG BEACH, CA | 100 |
| City of Los Angeles CA Wastewater System Revenue | CA | CITY | City | CITY OF LOS ANGELES | 100 |
| City of Los Angeles Department of Airports | CA | CITY | City | CITY OF LOS ANGELES | 100 |
| City of Los Angeles Department of Airports Customer Facility Charge Revenue | CA | CITY | City | CITY OF LOS ANGELES | 100 |
| City of Napa CA Solid Waste Revenue | CA | CITY | City | NAPA CALIF SOLID WASTE REV | 86 |
| City of San Francisco CA Public Utilities Commission Water Revenue | CA | CITY | City | SAN FRANCISCO PUBLIC UTILITIES COMMISSION | 100 |
| City of Santa Clara CA Sewer Revenue | CA | CITY | City | CITY OF SANTA CLARA | 100 |
| Los Angeles Department of Water & Power | CA | CITY | City | LOS ANGELES DEPARTMENT OF WATER AND POWER | 100 |
| Port of Los Angeles | CA | CITY | City | PORT OF LOS ANGELES | 100 |
| San Francisco City & County Public Utilities Commission Power Revenue | CA | CITY | City | SAN FRANCISCO PUBLIC UTILITIES COMMISSION | 100 |
| San Francisco City & County Public Utilities Commission Wastewater Revenue | CA | CITY | City | SAN FRANCISCO PUBLIC UTILITIES COMMISSION | 100 |
| San Francisco Municipal Transportation Agency | CA | CITY | City | CITY & COUNTY OF SAN FRANCISCO BAYSHORE HESTER AD NO. 95-1 - | 86 |
| San Jose Financing Authority | CA | CITY | City | CITY OF SAN JOSE - SJ-SC CLEAN WATER FINANCING AUTHORITY SEW | 100 |
| San Mateo Foster City Public Financing Authority | CA | CITY | City | CITY OF SAN JOSE FINANCING AUTHORITY - LEASE REVENUE BONDS | 88 |
| City of Arvada CO Wastewater Revenue | CO | CITY | City | ARVADA COLO | 86 |
| City of Arvada CO Water Revenue | CO | CITY | City | ARVADA COLO | 86 |
| City of Aurora CO Sewer Revenue | CO | CITY | City | AURORA COLO SWR REV | 86 |
| City of Aurora CO Water Revenue | CO | CITY | City | AURORA COLO | 86 |
| City of Boulder CO Water & Sewer Revenue | CO | CITY | City | CITY OF BOULDER | 100 |
| City of Northglenn CO Wastewater System Revenue | CO | CITY | City | NORTHGLENN COLO WASTEWATER REV | 89 |
| City of Derby CT | CT | CITY | City | DERBY CONN | 86 |
| City of Groton CT | CT | CITY | City | GROTON LONG PT ASSOC INC CONN | 86 |
| City of Stamford CT Water Pollution Control System & Facility Revenue | CT | CITY | City | STAMFORD CONN | 86 |
| City of Atlanta GA Airport Passenger Facility Charge | GA | CITY | City | ATLANTA GA | 100 |
| City of Atlanta GA Department of Aviation | GA | CITY | City | ATLANTA GA | 100 |
| City of Atlanta GA Water & Wastewater Revenue | GA | CITY | City | ATLANTA GA | 100 |
| City of Iowa Falls IA Sewer Revenue | IA | CITY | City | CITY OF IOWA CITY | 100 |
| City of Iowa Falls IA Water Revenue | IA | CITY | City | CITY OF IOWA CITY | 100 |
| City of Boise City ID Water Renewal Revenue | ID | CITY | City | BOISE CITY IDAHO WTR RENEWAL REV | 90 |
| City of Hailey ID Wastewater Revenue | ID | CITY | City | HAILEY IDAHO | 86 |
| City of Chicago Heights IL | IL | CITY | City | CITY OF CHICAGO | 100 |
| City of Decatur IL | IL | CITY | City | DECATUR ILL | 86 |
| City of Marseilles IL | IL | CITY | City | MARSEILLES ILL | 87 |
| City of Naperville IL | IL | CITY | City | NAPERVILLE ILL | 87 |
| Village of Antioch IL | IL | CITY | City | ANTIOCH ILL | 86 |
| Village of Bensenville IL | IL | CITY | City | BENSENVILLE ILL | 87 |
| Village of Kenilworth IL | IL | CITY | City | KENILWORTH ILL | 87 |
| Village of Oak Lawn IL Regional Water System Revenue | IL | CITY | City | VILLAGE OF JOHNSBURG | 86 |
| Village of Park Forest IL | IL | CITY | City | PARK FOREST ILL | 87 |
| City of Bedford IN Sewage Works Revenue | IN | CITY | City | BEDFORD IND | 86 |
| City of Bedford IN Waterworks Revenue | IN | CITY | City | BEDFORD IND | 86 |
| City of Bloomington IN | IN | CITY | City | BLOOMINGTON IND DOWNTOWN PKG DEV CORP | 86 |
| City of Bloomington IN Sewage Works Revenue | IN | CITY | City | BLOOMINGTON IND | 86 |
| City of Bloomington IN Waterworks Revenue | IN | CITY | City | BLOOMINGTON IND | 86 |
| City of Columbia City IN | IN | CITY | City | COLUMBIA CITY IND | 89 |
| City of Decatur IN | IN | CITY | City | DECATUR IND | 86 |
| City of Elkhart IN Sewage Works Revenue | IN | CITY | City | ELKHART IND | 86 |
| City of Fort Wayne IN Sewage Works Revenue | IN | CITY | City | FORT WAYNE IND | 86 |
| City of Jeffersonville IN Sewage Works Revenue | IN | CITY | City | JEFFERSONVILLE IND | 88 |
| City of Lawrence IN Waterworks Revenue | IN | CITY | City | CITY OF ANDERSON, IN  | 86 |
| City of Mishawaka IN Sewage Works Revenue | IN | CITY | City | CITY OF ANDERSON, IN  | 86 |
| City of Mishawaka IN Waterworks Revenue | IN | CITY | City | CITY OF ANDERSON, IN  | 86 |
| City of West Lafayette IN Sewer Revenue | IN | CITY | City | WEST LAFAYETTE IND | 88 |
| Indianapolis Local Public Improvement Bond Bank | IN | CITY | City | INDIANAPOLIS LOCAL PUBLIC IMPROVEMENT BOND BANK | 100 |
| Town of Schererville IN Sewage Works Revenue | IN | CITY | City | SCHERERVILLE IND | 86 |
| City of Fredonia KS | KS | CITY | City | CITY OF LAWRENCE, KS WATER AND SEWER | 86 |
| City of Girard KS | KS | CITY | City | CITY OF LAWRENCE, KS WATER AND SEWER | 86 |
| City of Lawrence KS | KS | CITY | City | CITY OF LAWRENCE | 100 |
| City of Liberal KS | KS | CITY | City | CITY OF LAWRENCE, KS WATER AND SEWER | 86 |
| City of Mission KS | KS | CITY | City | CITY OF LAWRENCE, KS WATER AND SEWER | 86 |
| City of St Marys KS | KS | CITY | City | CITY OF LAWRENCE, KS WATER AND SEWER | 86 |
| City of Wamego KS | KS | CITY | City | CITY OF LAWRENCE, KS WATER AND SEWER | 86 |
| City of Henderson KY | KY | CITY | City | HENDERSON KY | 100 |
| City of Hopkinsville KY | KY | CITY | City | HOPKINSVILLE KY | 100 |
| Town of Albany LA Water & Sewer System Revenue | LA | CITY | City | ALBANY WTR & SWR REV LA | 86 |
| Town of Franklinton LA Water & Sewer Revenue | LA | CITY | City | FRANKLINTON LA | 100 |
| Boston Water & Sewer Commission | MA | CITY | City | BOSTON MASS | 86 |
| City of Boston MA | MA | CITY | City | BOSTON MASS | 86 |
| City of Everett MA | MA | CITY | City | EVERETT MASS | 86 |
| City of Malden MA | MA | CITY | City | MALDEN MASS | 86 |
| Town of Ashland MA | MA | CITY | City | ASHLAND MASS | 86 |
| Town of Eastham MA | MA | CITY | City | EASTHAM MASS | 86 |
| Town of Norton MA | MA | CITY | City | NORTON MASS | 86 |
| Town of Otis MA | MA | CITY | City | OTIS MASS | 86 |
| Town of South Hadley MA | MA | CITY | City | HADLEY MASS | 86 |
| Town of Wareham MA | MA | CITY | City | WAREHAM MASS | 86 |
| Town of Watertown MA | MA | CITY | City | TOWN OF WATERTOWN, MA | 100 |
| City of Portland ME General Airport Revenue | ME | CITY | City | PORTLAND ME | 100 |
| City of Warren MI Water & Sewer System Revenue | MI | CITY | City | CITY OF WARREN, MICHIGAN | 86 |
| City of Bloomington MN | MN | CITY | City | BLOOMINGTON MINN HEALTH CARE FACS REV | 86 |
| City of White Bear Lake MN | MN | CITY | City | WHITE BEAR LAKE MINN | 86 |
| Fergus Falls Housing & Redevelopment Authority | MN | CITY | City | FERGUS FALLS MINN | 86 |
| City of Caruthersville MO | MO | CITY | City | CARUTHERSVILLE MO | 100 |
| City of Pleasant Hill MO Water & Sewerage System Revenue | MO | CITY | City | PLEASANT HILL MO | 100 |
| St Louis Clean Energy Development Board | MO | CITY | City | LAKE ST LOUIS MO | 86 |
| St Louis Municipal Finance Corp | MO | CITY | City | ST LOUIS MO | 86 |
| City of Laurel MS Water & Sewer System Revenue | MS | CITY | City | LAUREL MISS WTR & SWR SYS REV | 86 |
| City of Starkville MS Water & Sewer System Revenue | MS | CITY | City | STARKVILLE MISS | 86 |
| Village of Firth NE | NE | CITY | City | FIRTH NEB | 86 |
| City of Santa Fe NM Wastewater Utility System Revenue | NM | CITY | City | CITY OF SANTA FE, NM | 100 |
| Trust for Cultural Resources of The City of New York/The | NY | CITY | City | CITY OF NEW YORK (NYC) | 89 |
| City of Hamilton OH Wastewater System Revenue | OH | CITY | City | CITY OF HAMILTON, OHIO | 86 |
| City of North Olmsted OH | OH | CITY | City | NORTH OLMSTED OHIO CITY SCH DIST | 86 |
| City of Springfield OH | OH | CITY | City | CITY OF SPRINGFIELD OHIO | 96 |
| Hamilton Community Authority | OH | CITY | City | HAMILTON TWP OHIO | 86 |
| Village of Granville OH | OH | CITY | City | GRANVILLE OHIO | 86 |
| City of Bend OR Sewer Revenue | OR | CITY | City | CITY OF BEND | 100 |
| City of Boardman OR | OR | CITY | City | BOARDMAN ORE | 86 |
| City of Gresham OR | OR | CITY | City | CITY OF GRESHAM | 100 |
| City of Portland OR | OR | CITY | City | CITY OF PORTLAND, OREGON | 91 |
| Blythe Township Solid Waste Authority | PA | CITY | City | BLYTHE TWP PA | 86 |
| Borough of Grove City PA | PA | CITY | City | BOROUGH OF GROVE CITY | 100 |
| Borough of Stockertown PA | PA | CITY | City | STOCKERTOWN BORO PA | 86 |
| Brighton Township Municipal Authority | PA | CITY | City | NEW BRIGHTON PA | 86 |
| Economy Borough Municipal Authority | PA | CITY | City | ECONOMY PA | 86 |
| Ephrata Borough Authority | PA | CITY | City | EPHRATA BORO PA | 86 |
| Franklin Township Municipal Sanitary Authority | PA | CITY | City | FRANKLIN PA | 86 |
| Franklin Township Sewer Authority | PA | CITY | City | FRANKLIN PA | 86 |
| Mccandless Township Sanitation Authority | PA | CITY | City | MCCANDLESS PA | 87 |
| Monroeville Municipal Authority | PA | CITY | City | MONROEVILLE PA | 88 |
| North Sewickley Township Sewer Authority | PA | CITY | City | SEWICKLEY PA | 86 |
| North Sewickley Township Water Authority | PA | CITY | City | SEWICKLEY PA | 86 |
| South Middleton Township Municipal Authority | PA | CITY | City | TOWNSHIP OF UPPER ST. CLAIR | 86 |
| Township of Radnor PA | PA | CITY | City | LOWER PAXTON TOWNSHIP, DAUPHIN COUNTY | 86 |
| Washington Township Municipal Authority/Franklin County PA | PA | CITY | City | FRANKLIN PA | 100 |
| West Mifflin Sanitary Sewer Municipal Authority | PA | CITY | City | WEST MIFFLIN PA | 89 |
| City of Burkburnett TX Water & Sewer Revenue | TX | CITY | City | CITY OF SUGAR LAND, TX | 86 |
| City of Elmendorf TX | TX | CITY | City | ELMENDORF TEX | 86 |
| Mission Economic Development Corp | TX | CITY | City | CLEBURNE TEX 4B ECONOMIC DEVELOPMENT CORP SALESTAX REV | 86 |
| City of Spanish Fork City UT Sewer Revenue | UT | CITY | City | SPANISH FORK CITY UTAH SWR REV | 87 |
| Alexandria Sanitation Authority | VA | CITY | City | ALEXANDRIA VA | 87 |
| City of Emporia VA | VA | CITY | City | EMPORIA VA | 100 |
| City of Hampton VA | VA | CITY | City | HAMPTON VA | 100 |
| City of Norfolk VA | VA | CITY | City | NORFOLK VA CTFS PARTN | 100 |
| City of Virginia Beach VA | VA | CITY | City | VIRGINIA BEACH VA CTFS PARTN | 100 |
| Town of Vienna VA | VA | CITY | City | VIENNA VA | 100 |
| City of Burlington VT Electric System Revenue | VT | CITY | City | BURLINGTON VT | 100 |
| City of Anacortes WA Utility System Revenue | WA | CITY | City | CITY OF EVERETT, WA | 86 |
| City of Cashmere WA Water & Sewer Revenue | WA | CITY | City | CITY OF EVERETT, WA | 86 |
| City of Edmonds WA Water & Sewer Revenue | WA | CITY | City | CITY OF EVERETT, WA | 86 |
| City of Longview WA | WA | CITY | City | KENT, WA | 86 |
| City of Richland WA Electric Revenue | WA | CITY | City | CITY OF EVERETT, WA | 86 |
| City of Seattle WA Municipal Light & Power Revenue | WA | CITY | City | CITY OF SEATTLE | 100 |
| City of Seattle WA Water System Revenue | WA | CITY | City | CITY OF SEATTLE | 100 |
| City of Spokane WA Water & Wastewater Revenue | WA | CITY | City | CITY OF EVERETT, WA | 86 |
| City of Tacoma WA Electric System Revenue | WA | CITY | City | CITY OF EVERETT, WA | 86 |
| City of Tacoma WA Regional Water Supply System Revenue | WA | CITY | City | CITY OF EVERETT, WA | 86 |
| City of Tacoma WA Solid Waste Utility Revenue | WA | CITY | City | TACOMA WASH SOLID WASTE REV | 88 |
| City of Gillett WI | WI | CITY | City | GILLETT WIS | 86 |
| City of Madison WI | WI | CITY | City | CITY OF MADISON  | 100 |
| City of Milwaukee WI Sewerage System Revenue | WI | CITY | City | CITY OF MILWAUKEE | 100 |
| Milwaukee Metropolitan Sewerage District | WI | CITY | City | CITY OF MILWAUKEE | 86 |
| Milwaukee Redevelopment Authority | WI | CITY | City | CITY OF MILWAUKEE | 86 |
| Village of Fox Point WI | WI | CITY | City | FOX POINT WIS | 86 |
| Cherokee County Water & Sewer Authority/AL | AL | COUNTY | County | CHEROKEE CNTY ALA | 86 |
| Covington County Water Authority | AL | COUNTY | County | COVINGTON CNTY ALA | 86 |
| Sumter County Industrial Development Authority/AL | AL | COUNTY | County | SUMTER CNTY ALA WTR AUTH WTR REV | 86 |
| County of Pinal AZ | AZ | COUNTY | County | COUNTY OF PINAL | 100 |
| County of Pueblo CO | CO | COUNTY | County | PUEBLO CITY-CNTY LIBR DIST COLO CTFS PARTN | 86 |
| County of Hillsborough FL | FL | COUNTY | County | HILLSBOROUGH COUNTY BOCC | 88 |
| County of Carroll KY | KY | COUNTY | County | CARROLL CNTY KY | 86 |
| County of Montgomery MD Water Quality Protection Charge Revenue | MD | COUNTY | County | MONTGOMERY CNTY MD WTR QUALITY PROTN CHARGE REV | 88 |
| Montgomery County Housing Opportunities Commission | MD | COUNTY | County | MONTGOMERY CNTY MD | 86 |
| County of Douglas MN | MN | COUNTY | County | DOUGLAS CNTY MINN HSG & REDEV AUTH | 86 |
| County of Lowndes MS | MS | COUNTY | County | LOWNDES CNTY MISS POLLUTION CTL REV | 86 |
| County of Hudson NJ | NJ | COUNTY | County | HUDSON CNTY N J CORRECTIONAL FAC CTFS PARTN | 86 |
| Mercer County Improvement Authority/The | NJ | COUNTY | County | MERCER CNTY N J IMPT AUTH | 86 |
| Union County Improvement Authority | NJ | COUNTY | County | SPRINGFIELD TWP N J FOR FUTURE SPRINGFIELD TWP NJ BURLINGTON | 86 |
| County of Westchester NY | NY | COUNTY | County | WESTCHESTER CNTY N Y | 86 |
| Jefferson County Industrial Development Agency | NY | COUNTY | County | JEFFERSON CNTY N Y | 86 |
| Rockland County Solid Waste Management Authority | NY | COUNTY | County | ROCKLAND CNTY N Y | 86 |
| Westchester County Industrial Development Agency | NY | COUNTY | County | WESTCHESTER CNTY N Y | 86 |
| Cleveland-Cuyahoga County Port Authority | OH | COUNTY | County | CUYAHOGA COUNTY, OHIO | 86 |
| Lehigh County Industrial Development Authority | PA | COUNTY | County | LEHIGH CNTY PA INDL DEV AUTH REV | 86 |
| County of Williamson TN | TN | COUNTY | County | WILLIAMSON CNTY TENN HOSP INC HOSP FACS REV | 86 |
| Berkeley County Building Commission | WV | COUNTY | County | BERKELEY CNTY W VA LEASE REV | 86 |
| Berkeley County Public Service District | WV | COUNTY | County | BERKELEY CNTY W VA LEASE REV | 86 |
| Berkeley County Public Service Sewer District | WV | COUNTY | County | BERKELEY CNTY W VA LEASE REV | 86 |
| Greenbrier Public Service District No 1 | WV | COUNTY | County | GREENBRIER CNTY W VA REV | 86 |
| Los Angeles County Metropolitan Transportation Authority Sales Tax Revenue | CA | MULTI_JURISDICTIONAL | Other | ORANGE COUNTY TRANSPORTATION AUTHORITY | 90 |
| San Diego County Regional Transportation Commission | CA | MULTI_JURISDICTIONAL | Other | ALAMEDA COUNTY TRANSPORTATION COMMISSION | 89 |
| Transbay Joint Powers Authority | CA | MULTI_JURISDICTIONAL | Other | TRANSBAY JOINT POWERS AUTHORITY | 100 |
| Upper Santa Ana River Watershed Infrastructure Financing Auth & San Bernadino | CA | MULTI_JURISDICTIONAL | Other | UPPER SANTA ANA RIV WATERSHED INFRASTRUCTURE FING AUTH & SAN | 86 |
| Washington Metropolitan Area Transit Authority Dedicated Revenue | DC | MULTI_JURISDICTIONAL | Other | METROPOLITAN WASHINGTON AIRPORTS AUTHORITY | 88 |
| Metropolitan Atlanta Rapid Transit Authority | GA | MULTI_JURISDICTIONAL | Other | MARTA - METROPOLITAN ATLANTA RAPID TRANSIT AUTHORITY | 100 |
| Peoria Tazewell Etc Counties Community College District No 514 | IL | MULTI_JURISDICTIONAL | Other | AUGUSTANA COLLEGE | 86 |
| White Gallatin Etc Counties Community College Dist No 533 Southeastern Illinois | IL | MULTI_JURISDICTIONAL | Other | AUGUSTANA COLLEGE | 86 |
| Washington Suburban Sanitary Commission | MD | MULTI_JURISDICTIONAL | Other | WASHINGTON SUBURBAN SANITARY DISTRICT | 86 |
| Upper Mohawk Valley Regional Water Finance Authority | NY | MULTI_JURISDICTIONAL | Other | MOHAWK N Y | 86 |
| American Municipal Power Inc | OH | MULTI_JURISDICTIONAL | Other | AMERICAN MUNICIPAL POWER, INC. | 100 |
| Columbus-Franklin County Finance Authority | OH | MULTI_JURISDICTIONAL | Other | COLUMBUS-FRANKLIN COUNTY FINANCE AUTHORITY | 100 |
| Stark Metropolitan Housing Authority | OH | MULTI_JURISDICTIONAL | Other | CUYAHOGA METROPOLITAN HOUSING AUTHORITY | 91 |
| Easton Area Joint Sewer Authority/The | PA | MULTI_JURISDICTIONAL | Other | ADMIRAL PEARY PA AREA VOCATIONAL TECHNICAL SCH BLDG AUTH REV | 86 |
| University Area Joint Authority Sewer Revenue | PA | MULTI_JURISDICTIONAL | Other | DUQUESNE UNIVERSITY | 86 |
| Narragansett Bay Commission | RI | MULTI_JURISDICTIONAL | Other | NARRAGANSETT R I | 86 |
| Upper Trinity Regional Water District | TX | MULTI_JURISDICTIONAL | Other | NORTH TEXAS MUNICIPAL WATER DISTRICT - REGIONAL SOLID WASTE  | 86 |
| Utah Transit Authority | UT | MULTI_JURISDICTIONAL | Other | UTAH TRANSIT AUTHORITY | 100 |
| Central Puget Sound Regional Transit Authority | WA | MULTI_JURISDICTIONAL | Other | CENTRAL PUGET SOUND REGIONAL TRANSIT AUTHORITY (SOUND TRANSI | 100 |
| Maricopa County School District No 83-Cartwright Elementary | AZ | SCHOOL_DISTRICT | Other | BUCKEYE ELEMENTARY SCHOOL DISTRICT #33 | 86 |
| Chicago Board of Education | IL | SCHOOL_DISTRICT | Other | BOARD OF EDUCATION OF THE CITY OF CHICAGO | 100 |
| Ida Public Schools | MI | SCHOOL_DISTRICT | Other | VICKSBURG COMMUNITY SCHOOLS | 86 |
| Center School District No 58/MO | MO | SCHOOL_DISTRICT | Other | CENTER MO SCH DIST NO 058 CTFS PARTN | 86 |
| Bayonne School District | NJ | SCHOOL_DISTRICT | Other | BAYONNE N J | 86 |
| Buena Regional School District | NJ | SCHOOL_DISTRICT | Other | BUENA N J | 86 |
| Clearview Regional High School District | NJ | SCHOOL_DISTRICT | Other | HIGH BRIDGE BORO N J | 86 |
| Eatontown Board of Education | NJ | SCHOOL_DISTRICT | Other | EATONTOWN N J | 86 |
| Elmwood Park Board of Education | NJ | SCHOOL_DISTRICT | Other | ELMWOOD PARK N J | 86 |
| Glen Rock School District | NJ | SCHOOL_DISTRICT | Other | GLEN ROCK N J | 86 |
| Hackensack Board of Education | NJ | SCHOOL_DISTRICT | Other | HACKENSACK N J | 86 |
| Long Branch Board of Education | NJ | SCHOOL_DISTRICT | Other | LONG BRANCH N J | 86 |
| Manasquan Board of Education | NJ | SCHOOL_DISTRICT | Other | MANASQUAN N J | 86 |
| Plainfield Board of Education | NJ | SCHOOL_DISTRICT | Other | PLAINFIELD N J | 86 |
| Sayreville School District | NJ | SCHOOL_DISTRICT | Other | SAYREVILLE N J | 86 |
| Trenton Public Schools School District | NJ | SCHOOL_DISTRICT | Other | TRENTON N J | 86 |
| Vineland Board of Education | NJ | SCHOOL_DISTRICT | Other | VINELAND N J | 86 |
| West Windsor-Plainsboro Regional School District/NJ | NJ | SCHOOL_DISTRICT | Other | EAST WINDSOR N J REGL SCH DIST | 86 |
| Willingboro Township School District | NJ | SCHOOL_DISTRICT | Other | WILLINGBORO TWP N J | 86 |
| Albany City School District/NY | NY | SCHOOL_DISTRICT | Other | ALBANY N Y | 86 |
| Binghamton City School District | NY | SCHOOL_DISTRICT | Other | BINGHAMTON N Y | 86 |
| Cazenovia Central School District | NY | SCHOOL_DISTRICT | Other | CAZENOVIA N Y | 86 |
| East Rockaway Union Free School District | NY | SCHOOL_DISTRICT | Other | EAST ROCKAWAY N Y | 87 |
| Honeoye Falls-Lima Central School District | NY | SCHOOL_DISTRICT | Other | HONEOYE FALLS N Y | 87 |
| West Genesee Central School District | NY | SCHOOL_DISTRICT | Other | BRIDGEWATER LEONARDSVILLE WEST WINFIELD N Y CENT SCH DIST | 86 |
| Windsor Central School District | NY | SCHOOL_DISTRICT | Other | NEW WINDSOR N Y | 86 |
| Upper Sandusky Exempted Village School District | OH | SCHOOL_DISTRICT | Other | BRADFORD EXEMPTED VILLAGE SCHOOL DISTRICT | 88 |
| Xenia Community School District | OH | SCHOOL_DISTRICT | Other | SYCAMORE COMMUNITY CITY SCHOOL DISTRICT | 89 |
| Charleroi Area School District | PA | SCHOOL_DISTRICT | Other | GALETON AREA SCHOOL DISTRICT | 86 |
| Forest Area School District | PA | SCHOOL_DISTRICT | Other | ADMIRAL PEARY PA AREA VOCATIONAL TECHNICAL SCH | 86 |
| Huntingdon Area School District | PA | SCHOOL_DISTRICT | Other | HUNTINGDON AREA SCHOOL DISTRICT | 100 |
| Indiana Area School District | PA | SCHOOL_DISTRICT | Other | ADMIRAL PEARY PA AREA VOCATIONAL TECHNICAL SCH | 86 |
| Mid Valley School District | PA | SCHOOL_DISTRICT | Other | ALLEGHENY VALLEY PA SCH AUTH SCH BLDG REV FORMER LY ALLEGHEN | 86 |
| Millville Area School District | PA | SCHOOL_DISTRICT | Other | ADMIRAL PEARY PA AREA VOCATIONAL TECHNICAL SCH | 86 |
| School District of Philadelphia/The | PA | SCHOOL_DISTRICT | Other | THE SCHOOL DISTRICT OF PHILADELPHIA | 100 |
| Orangeburg County School District | SC | SCHOOL_DISTRICT | Other | ORANGEBURG S C CTFS PARTN | 86 |
| Tri-Valley School District | SD | SCHOOL_DISTRICT | Other | BRANDON VALLEY S D INDPT SCH DIST NO 150 | 86 |
| Edgewood Independent School District/Bexar County | TX | SCHOOL_DISTRICT | Other | AUSTIN INDEPENDENT SCHOOL DISTRICT | 89 |
| Fort Bend Independent School District | TX | SCHOOL_DISTRICT | Other | AUSTIN INDEPENDENT SCHOOL DISTRICT | 89 |
| Coachella Valley Water District Stormwater System Revenue | CA | SPECIAL_DISTRICT | Other | COACHELLA VALLEY WATER DISTRICT | 100 |
| Cosumnes Community Services District | CA | SPECIAL_DISTRICT | Other | COSUMNES CMNTY SVCS DIST CTFS PARTN | 86 |
| Crescenta Valley Water District | CA | SPECIAL_DISTRICT | Other | SCOTTS VALLEY WATER DISTRICT | 86 |
| East Bay Municipal Utility District Wastewater System Revenue | CA | SPECIAL_DISTRICT | Other | EAST BAY MUNICIPAL UTILITY DISTRICT (EBMUD) | 92 |
| East Bay Municipal Utility District Water System Revenue | CA | SPECIAL_DISTRICT | Other | EAST BAY MUNICIPAL UTILITY DISTRICT (EBMUD) | 92 |
| McKinleyville Community Service District | CA | SPECIAL_DISTRICT | Other | EASTERN MUNICIPAL WATER DISTRICT - COMMUNITY FACILITIES DIST | 86 |
| San Lorenzo Valley Water District | CA | SPECIAL_DISTRICT | Other | SCOTTS VALLEY WATER DISTRICT | 86 |
| Santa Clara Valley Water District Safe Clean Water Revenue | CA | SPECIAL_DISTRICT | Other | SCOTTS VALLEY WATER DISTRICT | 86 |
| Regional Transportation District Sales Tax Revenue | CO | SPECIAL_DISTRICT | Other | REGIONAL TRANSPORTATION DISTRICT | 100 |
| Hyde Park Community Development District No 1 | FL | SPECIAL_DISTRICT | Other | AVON PARK FLA WTR & SWR REV | 86 |
| Lakewood Ranch Stewardship District Utility Revenue | FL | SPECIAL_DISTRICT | Other | LAKEWOOD RANCH STEWARDSHIP DIST FLA UTIL REV | 87 |
| Albuquerque Metropolitan Arroyo Flood Control Authority | NM | SPECIAL_DISTRICT | Other | ALBUQUERQUE N MEX | 86 |
| Metro/OR | OR | SPECIAL_DISTRICT | Other | OREGON METRO | 86 |
| Tualatin Hills Park & Recreation District | OR | SPECIAL_DISTRICT | Other | BEND PARK & RECREATION DISTRICT | 91 |
| Inman Campobello Water District | SC | SPECIAL_DISTRICT | Other | INMAN-CAMPOBELLO S C WTR DIST WTRWKS SYS IMPT REV | 74 |
| North Texas Municipal Water District | TX | SPECIAL_DISTRICT | Other | NORTH TEXAS MUNICIPAL WATER DISTRICT - REGIONAL SOLID WASTE  | 100 |
| North Texas Municipal Water District Water System Revenue | TX | SPECIAL_DISTRICT | Other | NORTH TEXAS MUNICIPAL WATER DISTRICT - REGIONAL SOLID WASTE  | 100 |
| South Dallas Water Authority Inc | TX | SPECIAL_DISTRICT | Other | DALLAS CONVENTION CENTER HOTEL DEVELOPMENT CORPORATION HOTEL | 86 |
| Grant County Public Utility District No 2 Electric Revenue | WA | SPECIAL_DISTRICT | Other | PUBLIC UTILITY DISTRICT NO. 2 OF GRANT COUNTY | 96 |
| Grant County Public Utility District No 2 Priest Rapids Hydroelectric Project | WA | SPECIAL_DISTRICT | Other | PUBLIC UTILITY DISTRICT NO. 2 OF GRANT COUNTY | 96 |
| Pend Oreille County Public Utility District No 1 Box Canyon | WA | SPECIAL_DISTRICT | Other | PUBLIC UTILITY DISTRICT NO 1 OF SKAGIT COUNTY | 88 |
| Huntington Storm Water District | WV | SPECIAL_DISTRICT | Other | HUNTINGTON W VA | 86 |
| Arkansas Development Finance Authority | AR | STATE | State | ARKANSAS DEVELOPMENT FINANCE AUTHORITY | 100 |
| Arizona Board of Regents | AZ | STATE | State | ARIZONA BRD REGENTS CTFS PARTN | 88 |
| Arizona Industrial Development Authority | AZ | STATE | State | ARIZONA INDUSTRIAL DEVELOPMENT AUTHORITY | 100 |
| Arizona State University | AZ | STATE | State | ARIZONA STATE UNIVERSITY | 100 |
| University of Arizona/The | AZ | STATE | State | UNIVERSITY OF ARIZONA | 100 |
| California Community Choice Financing Authority | CA | STATE | State | CALIFORNIA ST | 87 |
| California Educational Facilities Authority | CA | STATE | State | CALIFORNIA ST | 87 |
| California Enterprise Development Authority | CA | STATE | State | CALIFORNIA ST | 87 |
| California Health Facilities Financing Authority | CA | STATE | State | CALIFORNIA ST | 87 |
| California Housing Finance Agency | CA | STATE | State | CALIFORNIA HOUSING FINANCE AGENCY (CALHFA) - AFFORDABLE HOUS | 100 |
| California Infrastructure & Economic Development Bank | CA | STATE | State | CALIFORNIA INFRASTRUCTURE & ECONOMIC DEV BK LEASE REV | 91 |
| California Pollution Control Financing Authority | CA | STATE | State | CALIFORNIA ST | 87 |
| California School Finance Authority | CA | STATE | State | CALIFORNIA ST | 87 |
| California State Public Works Board | CA | STATE | State | CALIFORNIA ST | 90 |
| State of California | CA | STATE | State | CALIFORNIA STATE TREASURER'S OFFICE | 91 |
| State of California Department of Water Resources | CA | STATE | State | CALIFORNIA ST | 87 |
| Board of Governors of Colorado State University System | CO | STATE | State | COLORADO ST | 90 |
| Connecticut Green Bank | CT | STATE | State | CONNECTICUT ST | 88 |
| Connecticut State Health & Educational Facilities Authority | CT | STATE | State | STATE OF CONNECTICUT | 92 |
| State of Connecticut | CT | STATE | State | STATE OF CONNECTICUT | 100 |
| State of Connecticut Clean Water Fund - State Revolving Fund | CT | STATE | State | STATE OF CONNECTICUT | 100 |
| Florida Department of Environmental Protection | FL | STATE | State | FLORIDA GAS UTIL REV | 86 |
| Florida Development Finance Corp | FL | STATE | State | FLORIDA DEVELOPMENT FINANCE CORPORATION | 92 |
| Guam Department of Education | GU | STATE | State | GUAM GOVT DEPT ED CTFS PARTN | 86 |
| State of Hawaii | HI | STATE | State | HAWAII ST | 86 |
| State of Hawaii Department of Business Economic Development & Tourism | HI | STATE | State | HAWAII ST | 86 |
| Iowa Finance Authority | IA | STATE | State | IOWA FINANCE AUTHORITY | 100 |
| Kansas Development Finance Authority | KS | STATE | State | KANSAS DEVELOPMENT FINANCE AUTHORITY | 100 |
| Louisiana Local Government Environmental Facilities & Community Development Auth | LA | STATE | State | LOUISIANA ST CTFS PARTN | 86 |
| Louisiana Public Facilities Authority | LA | STATE | State | LOUISIANA PUBLIC FACILITIES AUTHORITY | 100 |
| Commonwealth of Massachusetts | MA | STATE | State | THE COMMONWEALTH OF MASSACHUSETTS | 100 |
| Massachusetts Clean Energy Cooperative Corp | MA | STATE | State | MASSACHUSETTS CLEAN ENERGY COOP CORP REV | 93 |
| Massachusetts Clean Water Trust/The | MA | STATE | State | MASSACHUSETTS CLEAN WATER TRUST | 100 |
| Massachusetts Development Finance Agency | MA | STATE | State | MASSACHUSETTS ST | 90 |
| Massachusetts Port Authority | MA | STATE | State | MASSACHUSETTS BAY TRANSPORTATION AUTHORITY | 90 |
| Maryland Economic Development Corp | MD | STATE | State | MARYLAND ST ECONOMIC DEV CORP ECONOMIC DEV REV | 86 |
| Maryland Stadium Authority | MD | STATE | State | MARYLAND ST CTFS PARTN | 90 |
| Maryland Water Infrastructure Financing Administration Bay Restoration Fund | MD | STATE | State | MARYLAND DOT | 86 |
| State of Maryland | MD | STATE | State | STATE OF MARYLAND | 100 |
| Finance Authority of Maine | ME | STATE | State | MAINE LEASE REV | 100 |
| Maine Governmental Facilities Authority | ME | STATE | State | MAINE LEASE REV | 100 |
| Maine State Housing Authority | ME | STATE | State | MAINE LEASE REV | 100 |
| Michigan Finance Authority | MI | STATE | State | MICHIGAN FINANCE AUTHORITY | 100 |
| Michigan Strategic Fund | MI | STATE | State | MICHIGAN ST CTFS PARTN | 90 |
| State of Michigan | MI | STATE | State | STATE OF MICHIGAN | 100 |
| Minnesota Agricultural & Economic Development Board | MN | STATE | State | MINNESOTA ST | 86 |
| Minnesota Higher Education Facilities Authority | MN | STATE | State | MINNESOTA ST | 86 |
| Minnesota Public Facilities Authority State Revolving Fund | MN | STATE | State | MINNESOTA ST | 86 |
| Missouri Clean Energy District | MO | STATE | State | MISSOURI CLEAN ENERGY DIST CTFS PARTN | 93 |
| Missouri State Environmental Improvement & Energy Resources Authority | MO | STATE | State | MISSOURI ST | 90 |
| Mississippi Business Finance Corp | MS | STATE | State | MISSISSIPPI ST | 88 |
| Mississippi Development Bank | MS | STATE | State | MISSISSIPPI ST | 88 |
| University of North Dakota | ND | STATE | State | NORTH DAKOTA ST | 89 |
| Nebraska Utilities Corp | NE | STATE | State | NEBRASKA UTIL CORP REV | 88 |
| New Jersey Economic Development Authority | NJ | STATE | State | NEW JERSEY ST | 87 |
| New Jersey Educational Facilities Authority | NJ | STATE | State | NEW JERSEY ST | 87 |
| New Mexico Institute of Mining & Technology | NM | STATE | State | NEW MEXICO ST | 87 |
| State of Nevada | NV | STATE | State | NEVADA ST | 86 |
| State of Nevada Department of Business & Industry | NV | STATE | State | NEVADA ST | 86 |
| Long Island Power Authority | NY | STATE | State | LONG ISLAND POWER AUTHORITY | 100 |
| New York Liberty Development Corp | NY | STATE | State | NEW YORK LIBERTY DEV CORP LIBERTY REV | 91 |
| New York Power Authority | NY | STATE | State | NEW YORK POWER AUTHORITY | 100 |
| New York State Dormitory Authority | NY | STATE | State | DORMITORY AUTHORITY - STATE OF NEW YORK | 100 |
| New York State Environmental Facilities Corp | NY | STATE | State | STATE OF NEW YORK | 90 |
| New York State Housing Finance Agency | NY | STATE | State | NEW YORK STATE HOUSING FINANCE AGENCY-  SERVICE CONTRACT REV | 100 |
| New York State Thruway Authority | NY | STATE | State | STATE OF NEW YORK | 90 |
| New York Transportation Development Corp | NY | STATE | State | NEW YORK ST | 86 |
| State of Ohio | OH | STATE | State | STATE OF OHIO | 100 |
| Oklahoma Capitol Improvement Authority | OK | STATE | State | OKLAHOMA CAPITOL IMPROVEMENT AUTHORITY | 100 |
| Oklahoma Water Resources Board | OK | STATE | State | OKLAHOMA WATER RESOURCES BOARD | 100 |
| Oregon Health & Science University | OR | STATE | State | UNIVERSITY OF OREGON | 92 |
| State of Oregon | OR | STATE | State | STATE OF OREGON | 100 |
| Pennsylvania Economic Development Financing Authority | PA | STATE | State | PENNSYLVANIA ECONOMIC DEVELOPMENT FINANCING AUTHORITY | 100 |
| Pennsylvania Infrastructure Investment Authority | PA | STATE | State | PENNSYLVANIA ST CTFS PARTN | 89 |
| Rhode Island Infrastructure Bank | RI | STATE | State | RHODE ISLAND INFRASTRUCTURE BANK | 100 |
| Rhode Island Infrastructure Bank State Revolving Fund | RI | STATE | State | RHODE ISLAND INFRASTRUCTURE BANK | 100 |
| Rhode Island Infrastructure Bank Water Pollution Control Revolving Fund | RI | STATE | State | RHODE ISLAND INFRASTRUCTURE BANK | 100 |
| State of Rhode Island | RI | STATE | State | STATE OF RHODE ISLAND | 100 |
| South Carolina Jobs-Economic Development Authority | SC | STATE | State | SOUTH CAROLINA JOBS-ECONOMIC DEVELOPMENT AUTHORITY | 100 |
| South Carolina State Housing Finance & Development Authority | SC | STATE | State | SOUTH CAROLINA ST | 90 |
| South Dakota Conservancy District | SD | STATE | State | SOUTH DAKOTA CONSERVANCY DIST REV | 94 |
| State of Texas | TX | STATE | State | STATE OF TEXAS | 100 |
| Texas Department of Housing & Community Affairs | TX | STATE | State | TEXAS DEPARTMENT OF HOUSING AND COMMUNITY AFFAIRS | 100 |
| Virginia College Building Authority | VA | STATE | State | VIRGINIA COLLEGE BUILDING AUTHORITY | 100 |
| State of Vermont | VT | STATE | State | VERMONT HOUSING FINANCE AGENCY | 86 |
| Vermont Economic Development Authority | VT | STATE | State | VERMONT ST | 86 |
| Vermont Educational & Health Buildings Financing Agency | VT | STATE | State | VERMONT EDL & HEALTH BLDGS FING AGY REV | 86 |
| Vermont Municipal Bond Bank | VT | STATE | State | VERMONT BOND BANK | 100 |
| State of Washington | WA | STATE | State | STATE OF WASHINGTON CERTIFICATES OF PARTICIPATION | 100 |
| State of Wisconsin Clean Water Fund Leveraged Loan Portfolio | WI | STATE | State | STATE OF WISCONSIN | 100 |
| State of Wisconsin Environmental Improvement Fund Revenue | WI | STATE | State | STATE OF WISCONSIN | 100 |
| University of Wisconsin Hospitals & Clinics | WI | STATE | State | STATE OF WISCONSIN | 86 |
| West Virginia Economic Development Authority | WV | STATE | State | WEST VIRGINIA ST | 90 |

## Unable to compare (285 issuers)

Match quality was too low (score < 70 or no specific word overlap) to reliably compare classifications. These issuers may use significantly different naming conventions than MSRB, or may not be in the MSRB database.

| Issuer | State | Your Type | Best MSRB Candidate | Score | Quality |
|---|---|---|---|---|---|
| City of Foley AL | AL | CITY | ARAB CITY BOARD OF EDUCATION | 86 | LOW |
| City of Tallassee AL Water Gas & Sewer Revenue | AL | CITY | CITY OF CENTER POINT | 86 | LOW |
| City of Yuma AZ Water & Sewer Revenue | AZ | CITY | CITY OF MESA | 86 | LOW |
| Brea Public Financing Authority | CA | CITY | CITY OF SAN DIEGO - PUBLIC FACILITIES FINANCING AUTHORITY LE | 91 | LOW |
| Chowchilla Public Financing Authority | CA | CITY | CITY OF SAN DIEGO - PUBLIC FACILITIES FINANCING AUTHORITY LE | 86 | LOW |
| City of Berkeley CA | CA | CITY | CALIFORNIA DEPARTMENT OF VETERANS AFFAIRS (CALVET) | 86 | LOW |
| City of Firebaugh CA | CA | CITY | CALIFORNIA DEPARTMENT OF VETERANS AFFAIRS (CALVET) | 86 | LOW |
| City of Lemoore CA Water Revenue | CA | CITY | CALIFORNIA DEPARTMENT OF VETERANS AFFAIRS (CALVET) | 86 | LOW |
| City of Marina CA | CA | CITY | CALIFORNIA DEPARTMENT OF VETERANS AFFAIRS (CALVET) | 86 | LOW |
| City of Palo Alto CA | CA | CITY | CALIFORNIA DEPARTMENT OF VETERANS AFFAIRS (CALVET) | 86 | LOW |
| City of Santa Cruz CA Water Revenue | CA | CITY | CALIFORNIA DEPARTMENT OF VETERANS AFFAIRS (CALVET) | 86 | LOW |
| City of Santa Monica CA Water Revenue | CA | CITY | CALIFORNIA DEPARTMENT OF VETERANS AFFAIRS (CALVET) | 86 | LOW |
| City of St Helena CA | CA | CITY | CALIFORNIA DEPARTMENT OF VETERANS AFFAIRS (CALVET) | 86 | LOW |
| City of Vallejo CA Water Revenue | CA | CITY | CALIFORNIA DEPARTMENT OF VETERANS AFFAIRS (CALVET) | 86 | LOW |
| Coalinga Public Financing Authority | CA | CITY | CITY OF SAN DIEGO - PUBLIC FACILITIES FINANCING AUTHORITY LE | 86 | LOW |
| Dublin Financing Authority | CA | CITY | CITY OF SAN DIEGO - CONVENTION CENTER EXPANSION FINANCING AU | 86 | LOW |
| Imperial Public Financing Authority | CA | CITY | CITY OF SAN DIEGO - PUBLIC FACILITIES FINANCING AUTHORITY LE | 86 | LOW |
| Lancaster Power Authority | CA | CITY | CITY OF SAN DIEGO - CONVENTION CENTER EXPANSION FINANCING AU | 86 | LOW |
| Lynwood Utility Authority | CA | CITY | CITY OF SAN DIEGO - CONVENTION CENTER EXPANSION FINANCING AU | 86 | LOW |
| Monterey Park Financing Authority | CA | CITY | CITY OF SAN DIEGO - CONVENTION CENTER EXPANSION FINANCING AU | 86 | LOW |
| Mount Shasta Public Financing Authority | CA | CITY | CITY OF SAN DIEGO - PUBLIC FACILITIES FINANCING AUTHORITY LE | 86 | LOW |
| Mountain House Public Financing Authority | CA | CITY | CITY OF SAN DIEGO - PUBLIC FACILITIES FINANCING AUTHORITY LE | 86 | LOW |
| Oxnard Financing Authority | CA | CITY | CITY OF SAN DIEGO - CONVENTION CENTER EXPANSION FINANCING AU | 86 | LOW |
| Poway Public Financing Authority | CA | CITY | CITY OF SAN DIEGO - PUBLIC FACILITIES FINANCING AUTHORITY LE | 90 | LOW |
| Santa Monica Public Financing Authority | CA | CITY | CITY OF SAN DIEGO - PUBLIC FACILITIES FINANCING AUTHORITY LE | 86 | LOW |
| St Helena Financing Authority | CA | CITY | CITY OF SAN DIEGO - CONVENTION CENTER EXPANSION FINANCING AU | 86 | LOW |
| Stockton Public Financing Authority | CA | CITY | CITY OF SAN DIEGO - PUBLIC FACILITIES FINANCING AUTHORITY LE | 86 | LOW |
| Sunnyvale Financing Authority | CA | CITY | CITY OF SAN DIEGO - CONVENTION CENTER EXPANSION FINANCING AU | 86 | LOW |
| Yuba City Public Financing Authority | CA | CITY | CITY OF SAN DIEGO - PUBLIC FACILITIES FINANCING AUTHORITY LE | 93 | LOW |
| City of Westminster CO Water & Wastewater Utility Revenue | CO | CITY | CITY OF GOLDEN | 86 | LOW |
| City of Gainesville FL Utilities System Revenue | FL | CITY | CITY OF BOCA RATON | 86 | LOW |
| City of Orlando FL Reclamation System Revenue | FL | CITY | CITY OF BOCA RATON | 86 | LOW |
| City of Tamarac FL Water & Sewer Utility Revenue | FL | CITY | CITY OF BOCA RATON | 86 | LOW |
| City of Tampa FL | FL | CITY | CHARLOTTE COUNTY BOARD OF COUNTY COMMISSIONERS | 86 | LOW |
| City of Tampa FL Water & Wastewater System Revenue | FL | CITY | CITY OF BOCA RATON | 86 | LOW |
| City of Venice FL Utility Revenue | FL | CITY | CHARLOTTE COUNTY BOARD OF COUNTY COMMISSIONERS | 86 | LOW |
| City of Boone IA Sewer System Revenue | IA | CITY | CITY OF IOWA CITY | 86 | LOW |
| City of Le Mars IA Sewer Revenue | IA | CITY | STATE OF IOWA | 86 | LOW |
| City of Le Mars IA Water Revenue | IA | CITY | STATE OF IOWA | 86 | LOW |
| City of Story City IA Sewer Revenue | IA | CITY | CITY OF IOWA CITY | 86 | LOW |
| City of Winterset IA Water Revenue | IA | CITY | CITY OF IOWA CITY | 86 | LOW |
| City of Joliet IL Waterworks & Sewerage Revenue | IL | CITY | CITY OF CHICAGO | 86 | LOW |
| City of Kankakee IL Waterworks & Sewerage System | IL | CITY | CITY OF CHICAGO | 86 | LOW |
| City of LeRoy IL | IL | CITY | BOARD OF EDUCATION OF THE CITY OF CHICAGO | 86 | LOW |
| City of Olathe KS Water & Sewer System Revenue | KS | CITY | CITY OF LENEXA | 86 | LOW |
| City of Topeka KS Combined Utility Revenue | KS | CITY | CITY OF LENEXA | 86 | LOW |
| Town of Wellfleet MA | MA | CITY | THE COMMONWEALTH OF MASSACHUSETTS | 86 | LOW |
| City of Battle Creek MI Water & Wastewater System Revenue | MI | CITY | CITY OF TAYLOR | 86 | LOW |
| City of Holland MI | MI | CITY | ALCONA CNTY MICH BRD OF CNTY RD COMMRS | 86 | LOW |
| City of Holland MI Water Supply System Revenue | MI | CITY | CITY OF ALLEN PARK | 86 | LOW |
| City of Kalamazoo MI Wastewater System Revenue | MI | CITY | CITY OF TAYLOR | 86 | LOW |
| City of Kalamazoo MI Water Supply System Revenue | MI | CITY | CITY OF TAYLOR | 86 | LOW |
| City of Minneapolis MN | MN | CITY | REGENTS OF THE UNIVERSITY OF MINNESOTA | 86 | LOW |
| City of St Louis Park MN | MN | CITY | CITY OF PLYMOUTH | 86 | LOW |
| City of St Paul MN Sewer Revenue | MN | CITY | CITY OF PLYMOUTH | 86 | LOW |
| City of Asheville NC Water System Revenue | NC | CITY | CITY OF DUNN | 86 | LOW |
| City of Greensboro NC Combined Water & Sewer System Revenue | NC | CITY | CITY OF DUNN | 86 | LOW |
| City of Cincinnati OH | OH | CITY | CITY OF MASON | 86 | LOW |
| City of Cleveland OH Water Pollution Control | OH | CITY | CITY OF MASON | 86 | LOW |
| City of Lebanon OH Waterworks System Revenue | OH | CITY | CITY OF MASON | 86 | LOW |
| City of Lima OH Sanitary Sewer System Revenue | OH | CITY | CITY OF MASON | 86 | LOW |
| City of Marysville OH Water System Revenue | OH | CITY | CITY OF MASON | 86 | LOW |
| City of Strongsville OH | OH | CITY | CITY OF MASON | 86 | LOW |
| City of Vandalia OH | OH | CITY | BOWLING GREEN CITY SCHOOL DISTRICT | 86 | LOW |
| City of Vermilion OH | OH | CITY | CITY OF MASON | 86 | LOW |
| Village of Hebron OH Sewer System Revenue | OH | CITY | CITY OF AKRON, OHIO | 86 | LOW |
| Village of Hebron OH Water System Revenue | OH | CITY | CITY OF AKRON, OHIO | 86 | LOW |
| City of Portland OR Water System Revenue | OR | CITY | CITY OF BEND | 86 | LOW |
| City of Tigard OR Water Revenue | OR | CITY | CITY OF BEND | 86 | LOW |
| City of Lebanon Authority | PA | CITY | CITY OF YORK | 86 | LOW |
| East Lampeter Sewer Authority | PA | CITY | PENNSYLVANIA ECONOMIC DEVELOPMENT FINANCING AUTHORITY | 86 | LOW |
| Paradise Township Sewer Authority | PA | CITY | PENNSYLVANIA ECONOMIC DEVELOPMENT FINANCING AUTHORITY | 86 | LOW |
| Philadelphia Authority for Industrial Development | PA | CITY | AUTHORITY IMPT MUNICIPALITIES PA LEASE REV | 86 | LOW |
| Towanda Municipal Authority Sewer Revenue | PA | CITY | PENNSYLVANIA ECONOMIC DEVELOPMENT FINANCING AUTHORITY | 86 | LOW |
| City of Lebanon TN | TN | CITY | THE CONVENTION CENTER AUTHORITY OF THE METROPOLITAN GOVERNME | 86 | LOW |
| City of Paris TN | TN | CITY | CITY OF FRANKLIN, TENNESSEE | 86 | LOW |
| City of Aubrey TX | TX | CITY | BOARD OF REGENTS OF THE TEXAS TECH UNIVERSITY SYSTEM | 86 | LOW |
| City of Friendswood TX | TX | CITY | BOARD OF REGENTS OF THE TEXAS TECH UNIVERSITY SYSTEM | 86 | LOW |
| City of Hearne TX | TX | CITY | BOARD OF REGENTS OF THE TEXAS TECH UNIVERSITY SYSTEM | 86 | LOW |
| City of Midvale UT Water Sewer & Storm Water Revenue | UT | CITY | SALT LAKE CITY CORP | 86 | LOW |
| City of Midway UT | UT | CITY | UTAH BOARD OF HIGHER EDUCATION (FORMERLY THE BOARD OF REGENT | 86 | LOW |
| City of Park City UT Water Revenue | UT | CITY | STATE OF UTAH | 86 | LOW |
| City of Vineyard UT Water & Sewer Revenue | UT | CITY | SALT LAKE CITY CORP | 86 | LOW |
| City of Renton WA | WA | CITY | CITY OF RICHLAND, WASHINGTON | 86 | LOW |
| City of Tacoma WA Water Revenue | WA | CITY | CITY OF BOTHELL | 86 | LOW |
| City of Lake Mills WI Combined Utility System Revenue | WI | CITY | CITY OF MADISON  | 86 | LOW |
| City of Oshkosh WI Storm Water Utility Revenue | WI | CITY | CITY OF MADISON  | 86 | LOW |
| County of Clarke AL | AL | COUNTY | NORTHEAST MORGAN COUNTY WATER & SEWER AUTHORITY | 86 | LOW |
| County of Mobile AL | AL | COUNTY | NORTHEAST MORGAN COUNTY WATER & SEWER AUTHORITY | 86 | LOW |
| Houston County Water Authority | AL | COUNTY | NORTHEAST MORGAN COUNTY WATER & SEWER AUTHORITY | 86 | LOW |
| Maricopa County Industrial Development Authority | AZ | COUNTY | ARIZONA INDUSTRIAL DEVELOPMENT AUTHORITY | 89 | LOW |
| Pinal County Industrial Development Authority | AZ | COUNTY | ARIZONA INDUSTRIAL DEVELOPMENT AUTHORITY | 89 | LOW |
| Alameda County Water District Financing Authority | CA | COUNTY | CITY OF SAN DIEGO - PUBLIC FACILITIES FINANCING AUTHORITY WA | 86 | LOW |
| Contra Costa County Public Financing Authority | CA | COUNTY | CITY OF SAN DIEGO - PUBLIC FACILITIES FINANCING AUTHORITY LE | 86 | LOW |
| County of Los Angeles CA | CA | COUNTY | ALAMEDA COUNTY TRANSPORTATION COMMISSION | 86 | LOW |
| County of Solano CA | CA | COUNTY | ALAMEDA COUNTY TRANSPORTATION COMMISSION | 86 | LOW |
| County of Sonoma CA | CA | COUNTY | ALAMEDA COUNTY TRANSPORTATION COMMISSION | 86 | LOW |
| County of Yuba CA | CA | COUNTY | CITY & COUNTY OF SAN FRANCISCO - CERTIFICATES OF PARTICIPATI | 86 | LOW |
| Placer County Public Financing Authority | CA | COUNTY | CITY OF SAN DIEGO - PUBLIC FACILITIES FINANCING AUTHORITY LE | 86 | LOW |
| Santa Cruz County Capital Financing Authority | CA | COUNTY | CITY & COUNTY OF SAN FRANCISCO BAYSHORE HESTER AD NO. 95-1 - | 86 | LOW |
| Development Authority of Burke County/The | GA | COUNTY | CITY OF STATHAM | 86 | LOW |
| County of Cook IL Sales Tax Revenue | IL | COUNTY | BOARD OF EDUCATION OF THE CITY OF CHICAGO | 86 | LOW |
| County of Du Page IL | IL | COUNTY | BOARD OF EDUCATION OF THE CITY OF CHICAGO | 86 | LOW |
| County of Will IL | IL | COUNTY | BOARD OF EDUCATION OF THE CITY OF CHICAGO | 86 | LOW |
| Lake County Forest Preserve District | IL | COUNTY | CHICAGO PARK DISTRICT | 86 | LOW |
| County of Meade KY | KY | COUNTY | COMMONWEALTH OF KENTUCKY - KENTUCKY ASSET/LIABILITY COMMISSI | 86 | LOW |
| County of Warren KY | KY | COUNTY | COMMONWEALTH OF KENTUCKY - KENTUCKY ASSET/LIABILITY COMMISSI | 86 | LOW |
| Madison County Water District | KY | COUNTY | LOUISVILLE/JEFFERSON COUNTY METROPOLITAN SEWER DISTRICT | 86 | LOW |
| County of Monroe MI | MI | COUNTY | ALCONA CNTY MICH BRD OF CNTY RD COMMRS | 86 | LOW |
| County of Ramsey MN | MN | COUNTY | REGENTS OF THE UNIVERSITY OF MINNESOTA | 86 | LOW |
| Columbus County Industrial Facilities & Pollution Control Financing Authority | NC | COUNTY | BUNCOMBE COUNTY | 86 | LOW |
| County of Ocean NJ | NJ | COUNTY | LACEY TOWNSHIP BOARD OF EDUCATION | 86 | LOW |
| Franklin County Solid Waste Management Authority/NY | NY | COUNTY | BATTERY PARK CITY AUTHORITY | 86 | LOW |
| Onondaga County Resource Recovery Agency | NY | COUNTY | COUNTY OF SUFFOLK, NEW YORK | 86 | LOW |
| Wayne County Water & Sewer Authority | NY | COUNTY | NEW YORK CITY MUNICIPAL WATER FINANCE AUTHORITY (NYW) | 86 | LOW |
| Delaware County Port Authority | OH | COUNTY | BUTLER COUNTY TRANSPORTATION IMPROVEMENT DISTRICT | 86 | LOW |
| Summit County Development Finance Authority | OH | COUNTY | CUYAHOGA COUNTY, OHIO | 86 | LOW |
| Hospital Facilities Authority of Multnomah County Oregon | OR | COUNTY | CITY OF BEND | 86 | LOW |
| County of Moore TN Water Revenue | TN | COUNTY | THE METROPOLITAN GOVERNMENT OF NASHVILLE AND DAVIDSON COUNTY | 86 | LOW |
| Knox County Industrial Development Board | TN | COUNTY | SUMNER COUNTY, TENNESSEE | 86 | LOW |
| Unicoi County Water Utility District | TN | COUNTY | SUMNER COUNTY, TENNESSEE | 86 | LOW |
| Brazoria County Industrial Development Corp | TX | COUNTY | ABIA DEV CORP TEX ARPT FACS REV | 86 | LOW |
| Harris County Flood Control District | TX | COUNTY | NORTH TEXAS MUNICIPAL WATER DISTRICT - REGIONAL SOLID WASTE  | 86 | LOW |
| County of Mason WA | WA | COUNTY | PUBLIC UTILITY DISTRICT NO 1 OF SKAGIT COUNTY | 86 | LOW |
| County of Pierce WA Sewer Revenue | WA | COUNTY | CITY OF BOTHELL | 86 | LOW |
| Tri-County Regional Water Distribution District | AR | MULTI_JURISDICTIONAL | COUNTY LINE ARK SCH DIST NO 1 | 86 | LOW |
| Bay Area Toll Authority | CA | MULTI_JURISDICTIONAL | CITY OF SAN DIEGO - CONVENTION CENTER EXPANSION FINANCING AU | 86 | LOW |
| East County Advanced Water Purification Joint Powers Authority | CA | MULTI_JURISDICTIONAL | ORANGE COUNTY | 86 | LOW |
| Silicon Valley Clean Water | CA | MULTI_JURISDICTIONAL | CITY OF SAN DIEGO - PUBLIC FACILITIES FINANCING AUTHORITY WA | 86 | LOW |
| Western Placer Waste Management Authority | CA | MULTI_JURISDICTIONAL | CITY OF SAN DIEGO - CONVENTION CENTER EXPANSION FINANCING AU | 86 | LOW |
| Western Riverside Council of Governments | CA | MULTI_JURISDICTIONAL | CITY & COUNTY OF SAN FRANCISCO - CERTIFICATES OF PARTICIPATI | 86 | LOW |
| Summerfield Lebanon Mascoutah Water Commission St Clair County | IL | MULTI_JURISDICTIONAL | CHICAGO WATER | 86 | LOW |
| Great Lakes Water Authority Sewage Disposal System Revenue | MI | MULTI_JURISDICTIONAL | MICHIGAN FINANCE AUTHORITY | 86 | LOW |
| Great Lakes Water Authority Water Supply System Revenue | MI | MULTI_JURISDICTIONAL | MICHIGAN FINANCE AUTHORITY | 86 | LOW |
| Oxford Area Sewer Authority | PA | MULTI_JURISDICTIONAL | PENNSYLVANIA ECONOMIC DEVELOPMENT FINANCING AUTHORITY | 86 | LOW |
| Schertz/Seguin Local Government Corp | TX | MULTI_JURISDICTIONAL | ANGELINA & NECHES RIV AUTH TEX INDL DEV CORP ENVIRONMENTAL | 86 | LOW |
| Three Rivers Regional Wastewater Authority | WA | MULTI_JURISDICTIONAL | THREE RIVS WASH REGL WASTEWATER AUTH WASTEWATERREV | 70 | LOW |
| Deutsche Bank Spears/Lifers Trust | N/A - Financial Vehicle | OTHER | N/A | 0 | NO_STATE |
| Eclipse Funding Trust | N/A - Financial Vehicle | OTHER | N/A | 0 | NO_STATE |
| FYI Properties | N/A - Financial Vehicle | OTHER | N/A | 0 | NO_STATE |
| ISDLP Custodial Account LLC | N/A - Financial Vehicle | OTHER | N/A | 0 | NO_STATE |
| JPMorgan Chase Putters/Drivers Trust | N/A - Financial Vehicle | OTHER | N/A | 0 | NO_STATE |
| Mizuho Floater/Residual Trust | N/A - Financial Vehicle | OTHER | N/A | 0 | NO_STATE |
| RBC Municipal Products Inc Trust | N/A - Financial Vehicle | OTHER | N/A | 0 | NO_STATE |
| Tender Option Bond Trust Receipts/Certificates | N/A - Financial Vehicle | OTHER | N/A | 0 | NO_STATE |
| Prospect CharterCARE RWMC LLC | RI | OTHER | WARREN R I | 54 | LOW |
| Prospect CharterCARE SJHSRI LLC | RI | OTHER | WARREN R I | 54 | LOW |
| Warren School District No 1 | AR | SCHOOL_DISTRICT | ARCH STR PIKE ARK WTR IMPT & FIRE PROTN DIST NO 116 | 86 | LOW |
| Alisal Union School District | CA | SCHOOL_DISTRICT | CITY OF SAN DIEGO - ASSESSMENT DISTRICT NO. 4096 (PIPER RANC | 86 | LOW |
| Fremont Union High School District | CA | SCHOOL_DISTRICT | CITY OF SAN DIEGO - ASSESSMENT DISTRICT NO. 4096 (PIPER RANC | 86 | LOW |
| Harmony Union School District | CA | SCHOOL_DISTRICT | CITY OF SAN DIEGO - ASSESSMENT DISTRICT NO. 4096 (PIPER RANC | 86 | LOW |
| Will County Community Consolidated School District No 30 Troy | IL | SCHOOL_DISTRICT | CHICAGO PARK DISTRICT | 86 | LOW |
| Plymouth Community School Corp | IN | SCHOOL_DISTRICT | ALLEN CNTY IND JUVENILE JUSTICE CTR BLDG CORP | 86 | LOW |
| Randolph Independent Central School Corp | IN | SCHOOL_DISTRICT | ALBION IND MUN BLDG CORP | 86 | LOW |
| Bourbon County Unified School District No 234-Fort Scott | KS | SCHOOL_DISTRICT | CONSOLIDATED RURAL WATER DISTRICT #4 | 86 | LOW |
| Boyd County School District Finance Corp | KY | SCHOOL_DISTRICT | SHELBY COUNTY FISCAL COURT | 86 | LOW |
| Breckinridge County School District Finance Corp | KY | SCHOOL_DISTRICT | SHELBY COUNTY FISCAL COURT | 86 | LOW |
| Bullitt County School District Finance Corp | KY | SCHOOL_DISTRICT | SHELBY COUNTY FISCAL COURT | 86 | LOW |
| Calloway County School District Finance Corp | KY | SCHOOL_DISTRICT | SHELBY COUNTY FISCAL COURT | 86 | LOW |
| Carlisle County School District Finance Corp | KY | SCHOOL_DISTRICT | SHELBY COUNTY FISCAL COURT | 86 | LOW |
| Carroll County School District Finance Corp | KY | SCHOOL_DISTRICT | SHELBY COUNTY FISCAL COURT | 86 | LOW |
| Clinton County School District Finance Corp | KY | SCHOOL_DISTRICT | SHELBY COUNTY FISCAL COURT | 86 | LOW |
| Danville Independent School District Finance Corp | KY | SCHOOL_DISTRICT | ADAIR CNTY KY PUB HOSP DIST CORP REV | 86 | LOW |
| Edmonson County School District Finance Corp | KY | SCHOOL_DISTRICT | SHELBY COUNTY FISCAL COURT | 86 | LOW |
| Floyd County School District Finance Corp | KY | SCHOOL_DISTRICT | SHELBY COUNTY FISCAL COURT | 86 | LOW |
| Fulton Independent School District Finance Corp | KY | SCHOOL_DISTRICT | ADAIR CNTY KY PUB PPTYS CORP REV | 86 | LOW |
| Gallatin County School District Finance Corp | KY | SCHOOL_DISTRICT | SHELBY COUNTY FISCAL COURT | 86 | LOW |
| Grant County School District Finance Corp | KY | SCHOOL_DISTRICT | SHELBY COUNTY FISCAL COURT | 86 | LOW |
| Hardin County School District Finance Corp | KY | SCHOOL_DISTRICT | SHELBY COUNTY FISCAL COURT | 86 | LOW |
| Hart County School District Finance Corp | KY | SCHOOL_DISTRICT | SHELBY COUNTY FISCAL COURT | 86 | LOW |
| Leslie County School District Finance Corp | KY | SCHOOL_DISTRICT | SHELBY COUNTY FISCAL COURT | 86 | LOW |
| Livingston County School District Finance Corp | KY | SCHOOL_DISTRICT | SHELBY COUNTY FISCAL COURT | 86 | LOW |
| Lyon County School District Finance Corp | KY | SCHOOL_DISTRICT | SHELBY COUNTY FISCAL COURT | 86 | LOW |
| McCracken County School District Finance Corp | KY | SCHOOL_DISTRICT | SHELBY COUNTY FISCAL COURT | 86 | LOW |
| Montgomery County School District Finance Corp | KY | SCHOOL_DISTRICT | SHELBY COUNTY FISCAL COURT | 86 | LOW |
| Morgan County School District Finance Corp | KY | SCHOOL_DISTRICT | SHELBY COUNTY FISCAL COURT | 86 | LOW |
| Murray Independent School District Finance Corp | KY | SCHOOL_DISTRICT | ADAIR CNTY KY PUB PPTYS CORP REV | 86 | LOW |
| Nicholas County School District Finance Corp | KY | SCHOOL_DISTRICT | SHELBY COUNTY FISCAL COURT | 86 | LOW |
| Paducah Independent School District Finance Corp | KY | SCHOOL_DISTRICT | ADAIR CNTY KY PUB HOSP DIST CORP REV | 86 | LOW |
| Perry County School District Finance Corp | KY | SCHOOL_DISTRICT | SHELBY COUNTY FISCAL COURT | 86 | LOW |
| Pulaski County School District Finance Corp | KY | SCHOOL_DISTRICT | SHELBY COUNTY FISCAL COURT | 86 | LOW |
| Scott County School District Finance Corp | KY | SCHOOL_DISTRICT | SHELBY COUNTY FISCAL COURT | 86 | LOW |
| Greenway Independent School District No 316 | MN | SCHOOL_DISTRICT | ACGC JT PWRS BRD NO 6062 MINN | 86 | LOW |
| Shakopee Independent School District No 720 | MN | SCHOOL_DISTRICT | ACGC JT PWRS BRD NO 6062 MINN | 86 | LOW |
| Winona Independent School District No 861 | MN | SCHOOL_DISTRICT | ACGC JT PWRS BRD NO 6062 MINN | 86 | LOW |
| DeKalb County Reorganized School District No R-1 | MO | SCHOOL_DISTRICT | RAYMORE-PECULIAR SCHOOL DISTRICT | 86 | LOW |
| Dunklin County Reorganized School District No R-3 Holcomb | MO | SCHOOL_DISTRICT | PULASKI COUNTY SEWER DISTRICT NUMBER 1 | 86 | LOW |
| Wheaton School District No R-III | MO | SCHOOL_DISTRICT | ADAIR CNTY MO PUB WTR SUPPLY DIST NO 001 WTRWKSREV | 86 | LOW |
| Jersey City Board of Education | NJ | SCHOOL_DISTRICT | BORDENTOWN CITY N J | 86 | LOW |
| Oswego City School District | NY | SCHOOL_DISTRICT | NEW YORK CITY HOUSING DEVELOPMENT CORPORATION | 86 | LOW |
| Fairborn City School District | OH | SCHOOL_DISTRICT | DAYTON CITY SCHOOL DISTRICT | 86 | LOW |
| Madison Local School District/Lake County | OH | SCHOOL_DISTRICT | DAYTON CITY SCHOOL DISTRICT | 86 | LOW |
| Willoughby-Eastlake City School District | OH | SCHOOL_DISTRICT | BELLEFONTAINE CITY SCHOOLS | 86 | LOW |
| Yellow Springs Exempt Village School District | OH | SCHOOL_DISTRICT | DAYTON CITY SCHOOL DISTRICT | 86 | LOW |
| Ridley School District | PA | SCHOOL_DISTRICT | LAMPETER-STRASBURG SCHOOL DISTRICT | 86 | LOW |
| Spartanburg County School District No 7 | SC | SCHOOL_DISTRICT | COUNTY OF PICKENS | 86 | LOW |
| Bakerhill Water Authority | AL | SPECIAL_DISTRICT | NORTHEAST MORGAN COUNTY WATER & SEWER AUTHORITY | 86 | LOW |
| Calleguas Municipal Water District | CA | SPECIAL_DISTRICT | EASTERN MUNICIPAL WATER DISTRICT - COMMUNITY FACILITIES DIST | 86 | LOW |
| East Bay Regional Park District | CA | SPECIAL_DISTRICT | EASTERN MUNICIPAL WATER DISTRICT - GENERAL DISTRICT DEBT | 86 | LOW |
| Fallbrook Public Utility District/San Diego County CA Wastewater Revenue | CA | SPECIAL_DISTRICT | ALAMEDA COUNTY TRANSPORTATION COMMISSION | 86 | LOW |
| Midpeninsula Regional Open Space District Field Employees Corp | CA | SPECIAL_DISTRICT | COACHELLA VALLEY WATER DISTRICT | 86 | LOW |
| Palmdale Water District Public Financing Authority | CA | SPECIAL_DISTRICT | CITY OF SAN DIEGO - PUBLIC FACILITIES FINANCING AUTHORITY WA | 86 | LOW |
| Rosedale-Rio Bravo Water Storage District Kern County | CA | SPECIAL_DISTRICT | ORANGE COUNTY | 86 | LOW |
| Rowland Water District | CA | SPECIAL_DISTRICT | EASTERN MUNICIPAL WATER DISTRICT - ARCHIVE | 86 | LOW |
| South Tahoe Public Utility District Wastewater Revenue | CA | SPECIAL_DISTRICT | SCOTTS VALLEY WATER DISTRICT | 86 | LOW |
| Vallecitos Water District | CA | SPECIAL_DISTRICT | EASTERN MUNICIPAL WATER DISTRICT - ARCHIVE | 86 | LOW |
| Donala Water & Sanitation District | CO | SPECIAL_DISTRICT | DENVER WATER | 86 | LOW |
| Snake River Water District | CO | SPECIAL_DISTRICT | DENVER WATER | 86 | LOW |
| Greene County Rural Water District | IL | SPECIAL_DISTRICT | METROPOLITAN WATER RECLAMATION DISTRICT OF GREATER CHICAGO | 86 | LOW |
| Sangamon Valley Public Water District | IL | SPECIAL_DISTRICT | CHICAGO PARK DISTRICT | 86 | LOW |
| Trego County Rural Water District No 2 | KS | SPECIAL_DISTRICT | SEDGWICK COUNTY, KANSAS | 86 | LOW |
| Tangipahoa Sewerage District No 1 | LA | SPECIAL_DISTRICT | ACADIA PARISH LA CONS SCH DIST NO 8 IOTA EGAN OIL FIELD | 86 | LOW |
| Reading Area Water Authority | PA | SPECIAL_DISTRICT | PENNSYLVANIA ECONOMIC DEVELOPMENT FINANCING AUTHORITY | 86 | LOW |
| Ocoee Utility District/The | TN | SPECIAL_DISTRICT | THE CONVENTION CENTER AUTHORITY OF THE METROPOLITAN GOVERNME | 86 | LOW |
| Acton Municipal Utility District | TX | SPECIAL_DISTRICT | NORTH TEXAS MUNICIPAL WATER DISTRICT - REGIONAL SOLID WASTE  | 86 | LOW |
| Bauer Landing Water Control & Improvement District | TX | SPECIAL_DISTRICT | SHALLOW WATER TEX | 86 | LOW |
| Bissonnet Municipal Utility District | TX | SPECIAL_DISTRICT | NORTH TEXAS MUNICIPAL WATER DISTRICT - REGIONAL SOLID WASTE  | 86 | LOW |
| Brazoria County Municipal Utility District No 55 | TX | SPECIAL_DISTRICT | ADAMS GARDENS TEX IRR DIST NO 19 | 86 | LOW |
| Charterwood Municipal Utility District | TX | SPECIAL_DISTRICT | NORTH TEXAS MUNICIPAL WATER DISTRICT - REGIONAL SOLID WASTE  | 86 | LOW |
| Collin County Water Control & Improvement District No 3 | TX | SPECIAL_DISTRICT | AUSTIN INDEPENDENT SCHOOL DISTRICT | 86 | LOW |
| Cottonwood Creek Municipal Utility District No 1 | TX | SPECIAL_DISTRICT | ADAMS GARDENS TEX IRR DIST NO 19 | 86 | LOW |
| East Montgomery Municipal Utility District No 3 | TX | SPECIAL_DISTRICT | ARANSAS CNTY TEX NAV DIST NO 1 | 86 | LOW |
| Fort Bend County Municipal Utility District No 134C | TX | SPECIAL_DISTRICT | AUSTIN INDEPENDENT SCHOOL DISTRICT | 86 | LOW |
| Harris County Municipal Utility District No 096 | TX | SPECIAL_DISTRICT | ARANSAS CNTY TEX NAV DIST NO 1 | 86 | LOW |
| Harris County Municipal Utility District No 105 | TX | SPECIAL_DISTRICT | ARANSAS CNTY TEX NAV DIST NO 1 | 86 | LOW |
| Harris County Municipal Utility District No 11 | TX | SPECIAL_DISTRICT | ARANSAS CNTY TEX NAV DIST NO 1 | 86 | LOW |
| Harris County Municipal Utility District No 150 | TX | SPECIAL_DISTRICT | ARANSAS CNTY TEX NAV DIST NO 1 | 86 | LOW |
| Harris County Municipal Utility District No 153 | TX | SPECIAL_DISTRICT | ARANSAS CNTY TEX NAV DIST NO 1 | 86 | LOW |
| Harris County Municipal Utility District No 276 | TX | SPECIAL_DISTRICT | ARANSAS CNTY TEX NAV DIST NO 1 | 86 | LOW |
| Harris County Municipal Utility District No 278 | TX | SPECIAL_DISTRICT | ARANSAS CNTY TEX NAV DIST NO 1 | 86 | LOW |
| Harris County Municipal Utility District No 281 | TX | SPECIAL_DISTRICT | ARANSAS CNTY TEX NAV DIST NO 1 | 86 | LOW |
| Harris County Municipal Utility District No 33 | TX | SPECIAL_DISTRICT | ARANSAS CNTY TEX NAV DIST NO 1 | 86 | LOW |
| Harris County Municipal Utility District No 368 | TX | SPECIAL_DISTRICT | ARANSAS CNTY TEX NAV DIST NO 1 | 86 | LOW |
| Harris County Municipal Utility District No 396 | TX | SPECIAL_DISTRICT | ARANSAS CNTY TEX NAV DIST NO 1 | 86 | LOW |
| Harris County Municipal Utility District No 397 | TX | SPECIAL_DISTRICT | ARANSAS CNTY TEX NAV DIST NO 1 | 86 | LOW |
| Harris County Municipal Utility District No 416 | TX | SPECIAL_DISTRICT | ARANSAS CNTY TEX NAV DIST NO 1 | 86 | LOW |
| Harris County Municipal Utility District No 419 | TX | SPECIAL_DISTRICT | ARANSAS CNTY TEX NAV DIST NO 1 | 86 | LOW |
| Harris County Municipal Utility District No 433 | TX | SPECIAL_DISTRICT | ARANSAS CNTY TEX NAV DIST NO 1 | 86 | LOW |
| Harris County Municipal Utility District No 489 | TX | SPECIAL_DISTRICT | ARANSAS CNTY TEX NAV DIST NO 1 | 86 | LOW |
| Harris County Municipal Utility District No 65 | TX | SPECIAL_DISTRICT | ARANSAS CNTY TEX NAV DIST NO 1 | 86 | LOW |
| Hays County Water Control & Improvement District No 2 | TX | SPECIAL_DISTRICT | AUSTIN INDEPENDENT SCHOOL DISTRICT | 86 | LOW |
| Hunters Glen Municipal Utility District | TX | SPECIAL_DISTRICT | NORTH TEXAS MUNICIPAL WATER DISTRICT - REGIONAL SOLID WASTE  | 86 | LOW |
| Kaufman County Municipal Utility District No 4 | TX | SPECIAL_DISTRICT | ARANSAS CNTY TEX NAV DIST NO 1 | 86 | LOW |
| Lakeside Municipal Utility District No 3 | TX | SPECIAL_DISTRICT | NORTH TEXAS MUNICIPAL WATER DISTRICT - REGIONAL SOLID WASTE  | 86 | LOW |
| Mission Bend Municipal Utility District No 2 | TX | SPECIAL_DISTRICT | ARCOLA TEX MUN MGMT DIST NO 1 | 86 | LOW |
| Montgomery County Municipal Utility District No 112 | TX | SPECIAL_DISTRICT | AUSTIN INDEPENDENT SCHOOL DISTRICT | 86 | LOW |
| Montgomery County Municipal Utility District No 119 | TX | SPECIAL_DISTRICT | AUSTIN INDEPENDENT SCHOOL DISTRICT | 86 | LOW |
| Montgomery County Municipal Utility District No 128A | TX | SPECIAL_DISTRICT | AUSTIN INDEPENDENT SCHOOL DISTRICT | 86 | LOW |
| Montgomery County Municipal Utility District No 15 | TX | SPECIAL_DISTRICT | ADAMS GARDENS TEX IRR DIST NO 19 | 86 | LOW |
| Montgomery County Municipal Utility District No 94 | TX | SPECIAL_DISTRICT | ADAMS GARDENS TEX IRR DIST NO 19 | 86 | LOW |
| Montgomery County Municipal Utility District No 96 | TX | SPECIAL_DISTRICT | ADAMS GARDENS TEX IRR DIST NO 19 | 86 | LOW |
| Montgomery County Utility District No 3 | TX | SPECIAL_DISTRICT | NORTH TEXAS MUNICIPAL WATER DISTRICT - REGIONAL SOLID WASTE  | 86 | LOW |
| Morningstar Ranch Municipal Utility District No 1 of Parker County | TX | SPECIAL_DISTRICT | AUSTIN INDEPENDENT SCHOOL DISTRICT | 86 | LOW |
| Northampton Municipal Utility District | TX | SPECIAL_DISTRICT | NORTH TEXAS MUNICIPAL WATER DISTRICT - REGIONAL WATER SYSTEM | 86 | LOW |
| Northtown Municipal Utility District | TX | SPECIAL_DISTRICT | NORTH TEXAS MUNICIPAL WATER DISTRICT - REGIONAL SOLID WASTE  | 86 | LOW |
| Northwest Harris County Municipal Utility District No 10/TX | TX | SPECIAL_DISTRICT | AUSTIN INDEPENDENT SCHOOL DISTRICT | 86 | LOW |
| Orange County Water Control & Improvement District No 1 | TX | SPECIAL_DISTRICT | AUSTIN INDEPENDENT SCHOOL DISTRICT | 86 | LOW |
| Point Aquarius Municipal Utility District | TX | SPECIAL_DISTRICT | NORTH TEXAS MUNICIPAL WATER DISTRICT - REGIONAL SOLID WASTE  | 86 | LOW |
| Port of Arthur Navigation District Industrial Development Corp | TX | SPECIAL_DISTRICT | AUSTIN INDEPENDENT SCHOOL DISTRICT | 86 | LOW |
| Port of Port Arthur Navigation District | TX | SPECIAL_DISTRICT | CITY OF ARLINGTON | 86 | LOW |
| Porter Special Utility District | TX | SPECIAL_DISTRICT | NORTH TEXAS MUNICIPAL WATER DISTRICT - REGIONAL SOLID WASTE  | 86 | LOW |
| Rockwall County Municipal Utility District No 6 | TX | SPECIAL_DISTRICT | ARANSAS CNTY TEX NAV DIST NO 1 | 86 | LOW |
| Rockwall County Municipal Utility District No 8 | TX | SPECIAL_DISTRICT | ARANSAS CNTY TEX NAV DIST NO 1 | 86 | LOW |
| Rockwall County Municipal Utility District No 9 | TX | SPECIAL_DISTRICT | ARANSAS CNTY TEX NAV DIST NO 1 | 86 | LOW |
| Rolling Creek Utility District | TX | SPECIAL_DISTRICT | NORTH TEXAS MUNICIPAL WATER DISTRICT - REGIONAL SOLID WASTE  | 86 | LOW |
| Sagemeadow Utility District | TX | SPECIAL_DISTRICT | NORTH TEXAS MUNICIPAL WATER DISTRICT - REGIONAL SOLID WASTE  | 86 | LOW |
| Sienna Parks & Levee Improvement District of Fort Bend County | TX | SPECIAL_DISTRICT | AUSTIN INDEPENDENT SCHOOL DISTRICT | 86 | LOW |
| Southeast Williamson County Municipal Utility District No 1 | TX | SPECIAL_DISTRICT | AUSTIN INDEPENDENT SCHOOL DISTRICT | 86 | LOW |
| Stonewall Ranch Municipal Utility District | TX | SPECIAL_DISTRICT | NORTH TEXAS MUNICIPAL WATER DISTRICT - REGIONAL SOLID WASTE  | 86 | LOW |
| Sunbelt Fresh Water Supply District | TX | SPECIAL_DISTRICT | NORTH TEXAS MUNICIPAL WATER DISTRICT - REGIONAL SOLID WASTE  | 86 | LOW |
| Timber Lane Utility District | TX | SPECIAL_DISTRICT | NORTH TEXAS MUNICIPAL WATER DISTRICT - REGIONAL SOLID WASTE  | 86 | LOW |
| Travis County Municipal Utility District No 14 | TX | SPECIAL_DISTRICT | ARANSAS CNTY TEX NAV DIST NO 1 | 86 | LOW |
| Travis County Municipal Utility District No 17 | TX | SPECIAL_DISTRICT | ARANSAS CNTY TEX NAV DIST NO 1 | 86 | LOW |
| Travis County Water Control & Improvement District No 17 | TX | SPECIAL_DISTRICT | AUSTIN INDEPENDENT SCHOOL DISTRICT | 86 | LOW |
| West Harris County Municipal Utility District No 5 | TX | SPECIAL_DISTRICT | ADAMS GARDENS TEX IRR DIST NO 19 | 86 | LOW |
| West Williamson County Municipal Utility District No 1 | TX | SPECIAL_DISTRICT | AUSTIN INDEPENDENT SCHOOL DISTRICT | 86 | LOW |
| West Williamson County Municipal Utility District No 2 | TX | SPECIAL_DISTRICT | AUSTIN INDEPENDENT SCHOOL DISTRICT | 86 | LOW |
| Williamson County Municipal Utility District No 22 | TX | SPECIAL_DISTRICT | ADAMS GARDENS TEX IRR DIST NO 19 | 86 | LOW |
| Wood Trace Municipal Utility District No 1 | TX | SPECIAL_DISTRICT | NORTH TEXAS MUNICIPAL WATER DISTRICT - REGIONAL SOLID WASTE  | 86 | LOW |
| University of Colorado | CO | STATE | CITY OF GOLDEN | 86 | LOW |
| University of Nebraska Facilities Corp/The | NE | STATE | CITY OF MINDEN | 86 | LOW |
| Empire State Development Corp | NY | STATE | NEW YORK STATE ENERGY RESEARCH AND DEVELOPMENT AUTHORITY (NY | 86 | LOW |
| Triborough Bridge & Tunnel Authority | NY | STATE | NEW YORK CITY MUNICIPAL WATER FINANCE AUTHORITY (NYW) | 86 | LOW |
| Commonwealth Financing Authority | PA | STATE | PENNSYLVANIA ECONOMIC DEVELOPMENT FINANCING AUTHORITY | 86 | LOW |
| Public Finance Authority | WI | STATE | HOUSING AUTHORITY OF THE CITY OF MILWAUKEE | 86 | LOW |
