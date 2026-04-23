# Discretionary-Bond Validity Check (H4)

Among the **2449 CUSIPs** currently classified as 'discretionary' (no consent-decree / EPA-enforcement language in the prospectus), how many actually disclose **state-level regulatory compulsion**?

## Headline

**Definitions:**
- *Substantive green mandate*: state green building code (CALGreen, Title 24, LEED requirement, ASHRAE), state GHG/climate statute (AB 32, SB 32, cap-and-trade, state GHG target), or Renewable Portfolio Standard.
- *State legal mandate (broader)*: prospectus uses phrases like 'required by state law', 'statutory mandate'.
- *Voter-approved*: prospectus describes the bond as authorized by ballot measure/proposition. **Not external regulatory compulsion**, but political commitment constrained by voter mandate.

- 770 / 2449 (31.4%) disclose a **substantive state green mandate**.
- 531 / 2449 (21.7%) invoke a **general state legal mandate** ('required by state law').
- 1187 / 2449 (48.5%) have **either** type of state compulsion.
- 2120 / 2449 (86.6%) were **voter-approved** (procedural, not regulatory).

- **1262 / 2449 (51.5%) appear truly discretionary** with neither substantive nor broad legal state compulsion disclosed.


## Breakdown by Bloomberg industry (substantive state mandate rate)

| Industry | N discretionary | substantive state mandate | voter-approved |
|---|---:|---:|---:|
| Water/Sewer | 1333 | 186 (14%) | 1167 (88%) |
| General Obligation | 305 | 116 (38%) | 280 (92%) |
| (blank) | 183 | 126 (69%) | 135 (74%) |
| Airport | 155 | 135 (87%) | 135 (87%) |
| Appropriation | 148 | 27 (18%) | 124 (84%) |
| Mello-Roos | 83 | 83 (100%) | 83 (100%) |
| Special Assessment | 66 | 0 (0%) | 65 (98%) |
| Bond Bank | 43 | 0 (0%) | 0 (0%) |
| Public Power | 34 | 34 (100%) | 34 (100%) |
| Solid Waste | 32 | 11 (34%) | 32 (100%) |
| Municipal Utility | 25 | 25 (100%) | 25 (100%) |
| Payment in Lieu of Taxes | 22 | 22 (100%) | 22 (100%) |
| Ports/Marina | 10 | 0 (0%) | 10 (100%) |
| Limited Multi-Family Housing | 3 | 1 (33%) | 2 (67%) |
| Public Transportation | 3 | 3 (100%) | 3 (100%) |
| School District | 1 | 0 (0%) | 1 (100%) |
| Development | 1 | 0 (0%) | 0 (0%) |
| Not-for-Profit – Cultural | 1 | 1 (100%) | 1 (100%) |
| Texas Municipal Utility District | 1 | 0 (0%) | 1 (100%) |

## Most-common state-compulsion keyword hits

| Keyword | # discretionary CUSIPs with ≥1 hit |
|---|---:|
| `measure_prop` | 2119 (86.5%) |
| `rate_covenant` | 1771 (72.3%) |
| `voter_approved` | 1316 (53.7%) |
| `state_statute` | 694 (28.3%) |
| `state_law_required` | 499 (20.4%) |
| `required_by_law` | 466 (19.0%) |
| `leed_required` | 412 (16.8%) |
| `executive_order` | 370 (15.1%) |
| `cap_and_trade` | 260 (10.6%) |
| `ab_32` | 249 (10.2%) |
| `title_24` | 144 (5.9%) |
| `sb_32` | 141 (5.8%) |
| `ashrae` | 126 (5.1%) |
| `calgreen` | 85 (3.5%) |
| `rps` | 80 (3.3%) |
| `state_ghg_target` | 48 (2.0%) |
| `statutory_mandate` | 47 (1.9%) |
| `energy_star` | 44 (1.8%) |
| `energy_code` | 40 (1.6%) |
| `renewable_mandate` | 37 (1.5%) |
| `clean_energy_mandate` | 31 (1.3%) |

## Interpretation for H4

- If the 'truly discretionary' fraction is high (>70%), H4's compelled-vs-discretionary distinction is clean and the main panel result on discretionary green bonds genuinely identifies voluntary environmental commitment.
- If the 'state-compelled' fraction is high (>30%), the `compelled_by_text` flag undercounts compulsion — many bonds the panel treats as 'voluntary green' are actually issued to comply with state-level regulation. The paper should either (a) expand the compelled flag to include state compulsion, or (b) acknowledge in the paper that 'discretionary' in the federal-enforcement sense includes state-mandated projects.

- **Current result: 51.5% of 'discretionary' bonds show no state compulsion** (1262 CUSIPs). Qualifies the H4 interpretation of a meaningful discretionary channel.

