# Synthetic Motion-Artifact Detection in Brain MRI Using Transfer Learning

A proof-of-concept deep-learning pipeline for detecting synthetically
motion-corrupted T1-weighted brain MRI slices using transfer learning.

## Overview

Motion during MRI acquisition can reduce image quality and affect downstream
clinical interpretation and automated analysis. This project investigates whether
an ImageNet-pretrained ResNet-18 model can distinguish clean brain MRI slices
from synthetically motion-corrupted slices.

> Important: This is a research/portfolio baseline. It does not claim clinical
> performance because artifacts are synthetic and the dataset is small.

## Dataset

- Source: IXI Brain MRI Dataset
- Modality: T1-weighted structural brain MRI
- Volumes used: 10
- Total extracted axial slices: 2,429
- Central brain slices used for modelling: 1,455
- Data are excluded from this repository.

## Method

1. Load IXI T1-weighted NIfTI MRI volumes.
2. Reorient volumes into canonical anatomical orientation.
3. Extract and normalize axial brain slices.
4. Retain the central 60% of valid slices per subject.
5. Create synthetic motion-like artifacts using random rotation, translation,
   and blended transformed images.
6. Fine-tune an ImageNet-pretrained ResNet-18 classifier.
7. Evaluate with a subject-wise split to avoid slice-level leakage.

## Experimental Setup

| Item | Configuration |
|---|---|
| Task | Binary classification: clean vs. synthetic artifact |
| Model | ImageNet-pretrained ResNet-18 |
| Training split | 7 subjects |
| Validation split | 1 subject |
| Test split | 2 subjects |
| Training image size | 224 × 224 |
| Training epochs | 5 |
| Optimizer | Adam |
| Loss function | Cross-entropy loss |

## Results

| Metric | Result |
|---|---:|
| Best validation accuracy | 98.23% |
| Test accuracy | 97.00% |
| Test AUROC | 0.9904 |
| Clean-slice recall | 100% |
| Synthetic-artifact recall | 94% |
| Test samples | 566 |

The model correctly classified 97% of held-out test slices. These results apply
to the specific synthetic corruption procedure used in this baseline experiment.

## Example Synthetic Artifact

![Clean versus synthetic motion-like MRI](outputs/figures/clean_vs_moderate_motion.png)

## Evaluation

![Confusion matrix and ROC curve](outputs/figures/resnet18_test_confusion_matrix_roc.png)

## Repository Structure

```text
notebooks/
├── 01_data_exploration.ipynb
├── 02_motion_simulation.ipynb
└── 03_train_resnet18.ipynb

src/
├── config.py
├── data_utils.py
├── motion_simulation.py
├── dataset.py
├── model.py
├── train.py
└── evaluate.py

outputs/
└── figures/
    ├── clean_vs_moderate_motion.png
    └── resnet18_test_confusion_matrix_roc.png
```

## Limitations

- The experiment uses a small subset of 10 MRI volumes.
- Artifacts are synthetic rather than clinically labelled patient-motion artifacts.
- The baseline corruption procedure is 2D image-space blending, not full
  acquisition-level k-space simulation.
- Results may not generalize across scanners, acquisition protocols, populations,
  or real clinical artifact patterns.

## Future Work

- Generate artifacts using 3D k-space-based motion simulation.
- Increase the number and diversity of MRI volumes.
- Compare ResNet-18 with DenseNet-121 and EfficientNet.
- Train a 3D CNN or a 2.5D slice-stack classifier.
- Evaluate on real motion-corrupted brain MRI with expert quality labels.
- Use Grad-CAM to examine whether predictions focus on plausible motion-artifact regions.

## Tools

- Python
- Google Colab
- PyTorch and Torchvision
- NiBabel
- TorchIO
- OpenCV
- scikit-learn
- Google Drive
