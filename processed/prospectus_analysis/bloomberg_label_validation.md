# Bloomberg Green-Flag Validation

Cross-tabulation of Bloomberg `Self-reported Green` against prospectus-detected green designation (N = 3140 CUSIPs covered by a prospectus).

## Text-green criterion

A CUSIP is 'text-green' if its primary prospectus has ANY of:
- a detected Second-Party Opinion verifier (Kestrel / Sustainalytics / BAM / Moody's ESG)
- a green-bond designation section longer than 500 characters
- at least one cited green-bond framework (ICMA GBP, Climate Bonds Standard, SDGs)


## Confusion matrix (CUSIP-level)

| | text-green = 1 | text-green = 0 | row total |
|---|---:|---:|---:|
| Bloomberg green = Yes | **2134** TP | 298 FN | 2432 |
| Bloomberg green ≠ Yes | 143 FP | **565** TN | 708 |
| **column total** | **2277** | **863** | **3140** |

## Classifier metrics (Bloomberg as predictor of text-green)

- sensitivity (recall)  = TP / (TP+FN) = **0.877**
- specificity           = TN / (TN+FP) = **0.798**
- precision             = TP / (TP+FP) = **0.937**

## Rate of text-green by Bloomberg flag value

| Bloomberg flag | CUSIPs | text-green | rate |
|---|---:|---:|---:|
| -- | 632 | 90 | 14.2% |
| No | 76 | 53 | 69.7% |
| Yes | 2432 | 2134 | 87.7% |

## Intensity stratification by Bloomberg flag

Even a binary 'Self-reported Green' flag hides a continuous labelling intensity. The table below summarizes the prospectus-level intensity measures, stratified by Bloomberg's 'Self-reported Green' value:

| Bloomberg flag | N | green-section median chars | n_green_keywords median | has_SPO rate |
|---|---:|---:|---:|---:|
| Yes | 2432 | 5961 | 158 | 48.0% |
| No | 76 | 4183 | 140 | 42.1% |
| -- | 632 | 0 | 65 | 1.4% |

## Interpretation

If sensitivity is high (>0.9) the Bloomberg flag rarely misses bonds whose prospectuses actually label them green. If specificity is high, the flag rarely inflates — bonds with no green language aren't flagged. Low values on either side indicate noise in the outcome variable the main panel regression uses.

The intensity stratification above reveals the **labelling-margin** story directly: Bloomberg's binary Yes/No distinction carries little information about prospectus content — both groups have similar green-section length, keyword counts, and SPO rates. The real dividing line is 'labelled/not-labelled' (Yes or No) vs 'unknown/missing' (-- or blank). This is consistent with a story where issuer-level green disclosure is a discretionary labelling decision applied to bonds that look the same ex-ante.
