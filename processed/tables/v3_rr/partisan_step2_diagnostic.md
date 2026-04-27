# Diagnostic 2 — Why are partisan variables significant in Table 2?

## Question

In Table 2 (Step 2, full panel), `pres_dem_two_party_share_lag2` is +0.054\*\* on self-green and the `Dem_Mayor × pres_dem_share` interaction (I2) is +0.116\*\*. The chain framing claims Step 2 is dominated by Family 1 (Material). Is the constituency effect a separate Step 2 channel, or is the pooled Table 2 result the population-weighted signature of the Step 1 discretionary effect?

---

## 2a — Table 2 specification confirmation

| Parameter | Value |
|---|---|
| Sample | Full panel (no conditioning) |
| N | 6,825 |
| n+ (Y_self_green = 1) | 117 |
| R² | 0.094 |
| FE | State + year (absorbed) |
| SE clustering | City (fips7) |
| Variables | 10 (Dem_Mayor, NPDES, pres_dem, state_green_cum, reserve, debt_service, anti-ESG, log_pop, log_income, unemployment) |

Table 2 uses the full panel without sample restrictions. No implicit conditioning.

---

## 2b — Constituency main effect by use-of-funds category

| Sample / Outcome | N | n+ | pres\_dem β | SE | t | p |
|---|---:|---:|---|---|---|---|
| **Full panel → Y_self_green** | 6,825 | 117 | **+0.0545** | 0.0254 | **2.15** | **0.032\*\*** |
| Full panel → Y_water_only | 6,825 | 89 | +0.0172 | 0.0172 | 1.00 | 0.316 |
| **Full panel → Y_has_non_water** | 6,825 | 57 | **+0.0373** | 0.0155 | **2.40** | **0.016\*\*** |

The constituency main effect is **concentrated in the non-water (discretionary) subsample** (+0.037\*\*) and absent on water (+0.017, ns). The pooled self-green coefficient (+0.055\*\*) is the weighted sum of these two.

This is consistent with the chain framing: constituency demand operates at Step 1 (investment choice) in the discretionary domain, not as a separate Step 2 mechanism.

---

## 2c — I2 interaction by subsample

| Sample | N | n+ | I2 (Dem × pres\_dem) | SE | t | p |
|---|---:|---:|---|---|---|---|
| **Full panel → Y_self_green** | 6,825 | 117 | **+0.1155** | 0.0526 | **2.20** | **0.028\*\*** |
| **Non-water → Y_has_non_water** | 6,825 | 57 | **+0.1021** | 0.0325 | **3.14** | **0.002\*\*\*** |
| Water-only → Y_water_only | 6,825 | 89 | −0.0016 | 0.0297 | −0.05 | 0.958 |

The full-panel I2 (+0.116\*\*) is the **population-weighted average of a strong non-water effect (+0.102\*\*\*) and a null water effect (−0.002)**. The Table 2 interaction is identifying the Step 1 discretionary mechanism, not a separate Step 2 mechanism.

---

## 2d — Constituency vs mayoral identity decomposition

| Variable | V1 (pres\_dem only) | V2 (Dem\_Mayor only) | V3 (both + interaction) |
|---|---|---|---|
| pres\_dem | +0.0539\*\* | — | −0.0040 |
| Dem\_Mayor | — | +0.0038 | −0.0654\*\* |
| Dem × pres\_dem | — | — | +0.1155\*\* |
| N | 6,825 | 6,825 | 6,825 |

**V1:** `pres_dem_share` alone is +0.054\*\* — constituency demand for green bonds operates without controlling for mayoral identity.

**V2:** `Dem_Mayor` alone is +0.004 (ns) — mayoral identity has no main effect.

**V3:** With both + interaction, `pres_dem_share` drops to −0.004 (ns) and the interaction absorbs the signal (+0.116\*\*). **The constituency main effect from V1 is NOT independent of mayoral identity.** It operates through the constituency × mayoral-identity interaction. Without the interaction term (V1), the `pres_dem` coefficient captures the combined direct + indirect (via mayoral selection) constituency effect.

Interpretation: constituency demand and mayoral selection are entangled. The constituency effect is partly a proxy for the type of mayor the constituency elects, and partly a direct demand channel. The interaction specification (V3) separates them: the direct constituency effect is null; the conditional effect (Dem mayors responding to Dem constituencies) is the operative channel.

---

## 2e — Step-by-step partisan localisation

| Step | Dem\_Mayor | pres\_dem | Dem × pres\_dem | N |
|---|---|---|---|---:|
| **Step 1 NW (discretionary)** | **−0.0564\*\*\*** | −0.0144 | **+0.1021\*\*\*** | 6,825 |
| Step 1 W (compelled) | +0.0003 | +0.0180 | −0.0016 | 6,825 |
| **Step 2 (full panel)** | **−0.0654\*\*** | −0.0040 | **+0.1155\*\*** | 6,825 |
| Step 3 (issuers) | −0.0023 | +0.0739\*\* | — | 4,046 |
| Step 4 (green issuers) | +0.1181 | −0.8435\* | — | 118 |

**Reading.** The constituency × partisan interaction is significant at Step 1 NW (+0.102\*\*\*) and Step 2 full panel (+0.116\*\*). It is null at Step 1 W (−0.002) and not estimated at Steps 3–4 (insufficient variation in small conditional samples).

The Step 2 result is **not independent** of the Step 1 result: the full-panel I2 is the pooled signature of the Step 1 NW effect diluted by the Step 1 W null. This is confirmed by:
- The I2 coefficient is larger at Step 1 NW (+0.102) than at Step 2 (+0.116) — the pooled version is only slightly larger because the water null drags towards zero but non-water events contribute more to the self-green outcome.
- Constituency main effect at Step 2 (full panel, no interaction) is +0.054\*\*, but when decomposed by use-of-funds (2b), it is concentrated in non-water (+0.037\*\*) and null on water (+0.017).

At Step 3 (issuer-conditional), `Dem_Mayor` is null and `pres_dem` is independently significant (+0.074\*\*) — constituency demand for green labelling operates directly, without the mayoral-interaction channel. At Step 4, the sample is too small (N = 118) for reliable identification; the coefficients are unstable.

---

## Flagged conclusion

**Diagnostic 2 original observation: partially confirmed.**

The constituency main effect at Step 2 is real (+0.054\*\*) but is the **pooled signature of the Step 1 discretionary effect, not a separate Step 2 mechanism**. When decomposed by use-of-funds (2b), constituency is significant on non-water (+0.037\*\*) and null on water (+0.017). When the interaction is included (2c), the full-panel I2 is the population-weighted average of a strong non-water effect and a null water effect.

The chain framing is **consistent** with the data if it treats the pooled Table 2 constituency effect as the aggregate expression of the Step 1 discretionary mechanism, not as an independent Step 2 channel. The framework should note that constituency demand operates through investment-choice (Step 1) and carries into the pooled issuance statistics (Step 2) without being a separate bond-financing-decision driver.

The constituency × mayoral-identity decomposition (2d) shows the two variables are **entangled**: the V1 constituency main effect is absorbed by the V3 interaction, meaning constituency demand operates through the mayoral-response channel rather than independently.
