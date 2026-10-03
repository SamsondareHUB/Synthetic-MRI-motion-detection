# Synthetic-MRI-motion-detection
Detecting synthetic motion artifacts in brain MRI using transfer learning.
Add project overview and research plan

# Synthetic Motion-Artifact Detection in Brain MRI Using Transfer Learning

This project investigates whether transfer learning can improve detection of
motion artifacts in brain MRI using synthetically generated training data.

## Objective

Train and evaluate CNN-based classifiers that distinguish clean brain-MRI slices
from synthetically motion-corrupted slices.

## Dataset

- IXI T1-weighted brain MRI dataset
- Source: https://brain-development.org/ixi-dataset/
- License: CC BY-SA 3.0

## Method

1. Download and preprocess T1-weighted brain MRI volumes.
2. Extract axial slices.
3. Generate synthetic motion artifacts using image-space and k-space simulations.
4. Train a baseline CNN from scratch.
5. Fine-tune a pretrained ResNet-18 using transfer learning.
6. Evaluate both models using subject-wise train/validation/test splits.

## Metrics

- Accuracy
- Balanced accuracy
- Precision
- Recall
- Specificity
- F1 score
- AUROC
- AUPRC

## Repository structure

```text
notebooks/       Colab notebooks for exploration, simulation, and analysis
src/             Reusable Python modules
outputs/         Figures, metrics, and model artifacts excluded from Git
data/            MRI data excluded from Git; stored in Google Drive
```

## Status

- [x] Project initialization
- [ ] Data download and inspection
- [ ] Preprocessing pipeline
- [ ] Synthetic motion-artifact generation
- [ ] Baseline CNN training
- [ ] Transfer-learning experiments
- [ ] Final evaluation and report
