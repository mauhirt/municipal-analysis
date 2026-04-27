# Severity Variants Merge Log

**Before merge:** 7514 city-years, 578 cities
**After merge:** 7514 city-years (no change — left join)
**Severity columns added:** 86
**Unmatched cities:** 48 (filled with 0 — no NPDES-permitted facilities)

## Unmatched cities

- APPLE VALLEY_MN
- BALDWIN PARK_CA
- BLAINE_MN
- BLOOMINGTON_MN
- BURNSVILLE_MN
- CATHEDRAL CITY_CA
- CHULA VISTA_CA
- CICERO_IL
- CLEVELAND_OH
- COON RAPIDS_MN
- COSTA MESA_CA
- EAGAN_MN
- EDINA_MN
- EDISON_NJ
- EL CAJON_CA
- EL MONTE_CA
- FAIRFIELD_CA
- FONTANA_CA
- FREMONT_CA
- GARDEN GROVE_CA
- GILROY_CA
- KETTERING_OH
- LANCASTER_CA
- MAPLE GROVE_MN
- MIDDLETOWN_OH
- MILPITAS_CA
- MINNETONKA_MN
- OAK PARK_IL
- ORANGE_CA
- PALMDALE_CA
- PETALUMA_CA
- PICO RIVERA_CA
- PLEASANTON_CA
- PLYMOUTH_MN
- PONTIAC_MI
- RANCHO CUCAMONGA_CA
- RICHMOND_CA
- ROYAL OAK_MI
- SAN RAMON_CA
- ST. CLOUD_MN
- STOCKTON_CA
- TAYLOR_MI
- TINLEY PARK_IL
- UNION CITY_CA
- UPLAND_CA
- WESTMINSTER_CA
- WOODBURY_MN
- WYOMING_MI

## Coverage (nonzero city-years in analysis panel)

| Variable | Nonzero |
|---|---:|
| `npdes_qncr_count` | 4700 |
| `npdes_qncr_snc_count` | 256 |
| `npdes_qncr_severe_eff_count` | 2045 |
| `npdes_qncr_any_eff_count` | 2745 |
| `npdes_qncr_severe_count` | 2186 |
| `unique_facilities` | 4700 |
| `npdes_qncr_count_asinh` | 4700 |
| `npdes_qncr_any` | 4700 |
| `npdes_qncr_snc_count_asinh` | 256 |
| `npdes_qncr_snc_any` | 256 |
| `npdes_qncr_severe_eff_count_asinh` | 2045 |
| `npdes_qncr_severe_eff_any` | 2045 |
| `npdes_qncr_any_eff_count_asinh` | 2745 |
| `npdes_qncr_any_eff_any` | 2745 |
| `npdes_qncr_severe_count_asinh` | 2186 |
| `npdes_qncr_severe_any` | 2186 |
| `npdes_qncr_count_lag1` | 4624 |
| `npdes_qncr_count_lag2` | 4562 |
| `npdes_qncr_count_lag3` | 4497 |
| `npdes_qncr_count_prior2yr` | 4961 |
| `npdes_qncr_count_prior3yr` | 5179 |
| `npdes_qncr_count_prior5yr` | 5415 |
| `npdes_qncr_count_cum` | 5844 |
| `npdes_qncr_snc_count_lag1` | 242 |
| `npdes_qncr_snc_count_lag2` | 239 |
| `npdes_qncr_snc_count_lag3` | 248 |
| `npdes_qncr_snc_count_prior2yr` | 330 |
| `npdes_qncr_snc_count_prior3yr` | 422 |
| `npdes_qncr_snc_count_prior5yr` | 588 |
| `npdes_qncr_snc_count_cum` | 1369 |
| `npdes_qncr_severe_eff_count_lag1` | 2034 |
| `npdes_qncr_severe_eff_count_lag2` | 2036 |
| `npdes_qncr_severe_eff_count_lag3` | 2018 |
| `npdes_qncr_severe_eff_count_prior2yr` | 2461 |
| `npdes_qncr_severe_eff_count_prior3yr` | 2686 |
| `npdes_qncr_severe_eff_count_prior5yr` | 2925 |
| `npdes_qncr_severe_eff_count_cum` | 3361 |
| `npdes_qncr_any_eff_count_lag1` | 2723 |
| `npdes_qncr_any_eff_count_lag2` | 2713 |
| `npdes_qncr_any_eff_count_lag3` | 2697 |
| `npdes_qncr_any_eff_count_prior2yr` | 3148 |
| `npdes_qncr_any_eff_count_prior3yr` | 3360 |
| `npdes_qncr_any_eff_count_prior5yr` | 3562 |
| `npdes_qncr_any_eff_count_cum` | 3830 |
| `npdes_qncr_severe_count_lag1` | 2164 |
| `npdes_qncr_severe_count_lag2` | 2156 |
| `npdes_qncr_severe_count_lag3` | 2136 |
| `npdes_qncr_severe_count_prior2yr` | 2600 |
| `npdes_qncr_severe_count_prior3yr` | 2835 |
| `npdes_qncr_severe_count_prior5yr` | 3085 |
| `npdes_qncr_severe_count_cum` | 3593 |
| `npdes_qncr_count_lag1_asinh` | 4624 |
| `npdes_qncr_count_lag2_asinh` | 4562 |
| `npdes_qncr_count_lag3_asinh` | 4497 |
| `npdes_qncr_count_prior2yr_asinh` | 4961 |
| `npdes_qncr_count_prior3yr_asinh` | 5179 |
| `npdes_qncr_count_prior5yr_asinh` | 5415 |
| `npdes_qncr_count_cum_asinh` | 5844 |
| `npdes_qncr_snc_count_lag1_asinh` | 242 |
| `npdes_qncr_snc_count_lag2_asinh` | 239 |
| `npdes_qncr_snc_count_lag3_asinh` | 248 |
| `npdes_qncr_snc_count_prior2yr_asinh` | 330 |
| `npdes_qncr_snc_count_prior3yr_asinh` | 422 |
| `npdes_qncr_snc_count_prior5yr_asinh` | 588 |
| `npdes_qncr_snc_count_cum_asinh` | 1369 |
| `npdes_qncr_severe_eff_count_lag1_asinh` | 2034 |
| `npdes_qncr_severe_eff_count_lag2_asinh` | 2036 |
| `npdes_qncr_severe_eff_count_lag3_asinh` | 2018 |
| `npdes_qncr_severe_eff_count_prior2yr_asinh` | 2461 |
| `npdes_qncr_severe_eff_count_prior3yr_asinh` | 2686 |
| `npdes_qncr_severe_eff_count_prior5yr_asinh` | 2925 |
| `npdes_qncr_severe_eff_count_cum_asinh` | 3361 |
| `npdes_qncr_any_eff_count_lag1_asinh` | 2723 |
| `npdes_qncr_any_eff_count_lag2_asinh` | 2713 |
| `npdes_qncr_any_eff_count_lag3_asinh` | 2697 |
| `npdes_qncr_any_eff_count_prior2yr_asinh` | 3148 |
| `npdes_qncr_any_eff_count_prior3yr_asinh` | 3360 |
| `npdes_qncr_any_eff_count_prior5yr_asinh` | 3562 |
| `npdes_qncr_any_eff_count_cum_asinh` | 3830 |
| `npdes_qncr_severe_count_lag1_asinh` | 2164 |
| `npdes_qncr_severe_count_lag2_asinh` | 2156 |
| `npdes_qncr_severe_count_lag3_asinh` | 2136 |
| `npdes_qncr_severe_count_prior2yr_asinh` | 2600 |
| `npdes_qncr_severe_count_prior3yr_asinh` | 2835 |
| `npdes_qncr_severe_count_prior5yr_asinh` | 3085 |
| `npdes_qncr_severe_count_cum_asinh` | 3593 |
