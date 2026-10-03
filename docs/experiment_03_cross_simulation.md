## Threshold Calibration Analysis

Decision thresholds were selected on each model's matched-simulation validation
data by maximizing Youden's J statistic:

\[
J = \text{sensitivity} + \text{specificity} - 1
\]

| Model | Matched validation simulation | Selected threshold | Validation sensitivity | Validation specificity |
|---|---|---:|---:|---:|
| 2D image-space model | 2D image-space artifacts | 0.5338 | 96.45% | 100.00% |
| 3D TorchIO model | 3D TorchIO artifacts | 0.6024 | 98.58% | 100.00% |

The validation-derived thresholds were then applied without modification to the
alternate-simulation test data.

| Training simulation | Testing simulation | Default-threshold accuracy | Calibrated accuracy | Sensitivity | Specificity | False negatives |
|---|---|---:|---:|---:|---:|---:|
| 2D image-space blending | 3D TorchIO motion | 91.17% | 89.58% | 79.15% | 100.00% | 59 / 283 |
| 3D TorchIO motion | 2D image-space blending | 76.86% | 71.55% | 43.11% | 100.00% | 161 / 283 |

## Calibration Interpretation

Threshold calibration on the matched simulation domain did not restore
cross-simulation performance. Both models remained highly specific for clean
slices but showed reduced sensitivity for artifacts generated with the alternate
simulator.

This supports the interpretation that cross-simulation degradation reflects
synthetic-domain shift rather than only a fixed-threshold calibration problem.
The result should be interpreted cautiously because it is based on a 10-subject
pilot dataset and two held-out test subjects.
