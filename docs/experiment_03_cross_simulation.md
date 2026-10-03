# Experiment 03: Cross-Simulation Generalization

## Purpose

Evaluate whether motion-artifact classifiers trained using one synthetic artifact
simulation method generalize to images generated with a different synthetic
motion simulation method.

## Models

Two previously trained ImageNet-pretrained ResNet-18 classifiers were evaluated:

1. **2D model:** trained using image-space rotation, translation, and transformed-image blending.
2. **3D model:** trained using full-volume TorchIO `RandomMotion` simulation.

No model was retrained or fine-tuned for the cross-simulation evaluation.

## Test Data

- Dataset: the two held-out IXI test subjects used in Experiments 01 and 02.
- Clean images: original central axial MRI slices.
- Artifact images: paired synthetic slices from the alternate simulation method.
- Evaluation level: slice-level binary classification.

## Results

| Training simulation | Testing simulation | Accuracy | Balanced accuracy | AUROC | AUPRC |
|---|---|---:|---:|---:|---:|
| 2D image-space blending | 3D TorchIO motion | 91.17% | 91.17% | 0.9939 | 0.9942 |
| 3D TorchIO motion | 2D image-space blending | 76.86% | 76.86% | 0.9751 | 0.9778 |

## Comparison to Matched-Simulation Testing

| Model | Matched-simulation accuracy | Cross-simulation accuracy | Accuracy decrease |
|---|---:|---:|---:|
| 2D image-space model | 97.00% | 91.17% | 5.83 percentage points |
| 3D TorchIO model | 99.29% | 76.86% | 22.43 percentage points |

## Interpretation

Both models preserved high ranking discrimination across artifact simulations,
as reflected by AUROC values above 0.97. However, accuracy decreased when each
model was evaluated on a different artifact-generation mechanism.

The 3D TorchIO-trained model showed a larger decrease in threshold-based
accuracy when evaluated on 2D image-space artifacts. This suggests that
high performance obtained from training and testing with the same synthetic
simulator may not fully transfer to a distinct synthetic artifact domain.

The results indicate simulator-dependent domain shift. They do not establish
performance on real clinical patient motion.

## Limitations

- The study used 10 MRI volumes and only two held-out test subjects.
- Both artifact domains were synthetic.
- The same source MRI distribution was used for both simulation domains.
- Only one random training seed and one subject split were evaluated.
- A fixed default decision threshold was used; threshold calibration was not
  performed on the alternative simulation domain.
