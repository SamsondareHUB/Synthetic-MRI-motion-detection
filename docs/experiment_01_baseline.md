# Experiment 01: 2D Synthetic Motion Baseline

## Purpose

Establish a reproducible baseline for distinguishing clean T1-weighted brain MRI
slices from synthetically motion-corrupted slices using transfer learning.

## Dataset

- Source: IXI T1-weighted brain MRI
- Volumes used: 10
- Total valid axial slices after preprocessing: 2,429
- Central slices retained for modelling: 1,455
- Image size: 224 x 224 pixels

## Preprocessing

1. Load NIfTI volumes.
2. Reorient volumes to canonical anatomical orientation.
3. Extract axial slices.
4. Remove mostly empty slices.
5. Retain the central 60% of valid slices per subject.
6. Clip image intensities at the 1st and 99th percentiles.
7. Normalize each slice to the range [0, 1].
8. Resize slices to 224 x 224 pixels.

## Labels

- Clean: original normalized axial MRI slice.
- Synthetic artifact: a blended combination of the original slice and a
  randomly rotated and translated version of that slice.

Artifact parameters:

- Rotation: uniformly sampled from -6 to +6 degrees.
- Translation: uniformly sampled from -6 to +6 pixels in both image axes.
- Blending: 0.65 original image + 0.35 transformed image.

## Data Split

A subject-wise split was used to avoid leakage between slices from the same MRI
volume.

| Partition | Subjects | Role |
|---|---:|---|
| Training | 7 | Model fitting |
| Validation | 1 | Model selection |
| Test | 2 | Final held-out evaluation |

## Model

- Architecture: ResNet-18
- Initialization: ImageNet pretrained weights
- Input: grayscale MRI copied to three channels
- Classifier: two output classes
- Frozen backbone; only final classification layer trained
- Optimizer: Adam
- Learning rate: 0.001
- Loss: cross-entropy
- Epochs: 5
- Batch size: 32
- Random seed: 42

## Results

| Metric | Value |
|---|---:|
| Best validation accuracy | 98.23% |
| Test accuracy | 97.00% |
| Test AUROC | 0.9904 |
| Clean precision | 0.95 |
| Clean recall | 1.00 |
| Clean F1 score | 0.97 |
| Synthetic-artifact precision | 1.00 |
| Synthetic-artifact recall | 0.94 |
| Synthetic-artifact F1 score | 0.97 |
| Test samples | 566 |

## Interpretation

The model effectively distinguished clean images from the specific 2D synthetic
corruption used in this experiment. The result demonstrates pipeline feasibility,
but it does not establish performance on real clinical motion artifacts.

## Limitations

- Small sample: 10 MRI volumes.
- Evaluation used only synthetic labels.
- The synthetic corruption is image-space blending, not MRI-acquisition
  or k-space-level motion simulation.
- Results may reflect detection of the particular simulation pattern rather
  than generalizable MRI motion artifacts.
- A single train/validation/test split was used.
