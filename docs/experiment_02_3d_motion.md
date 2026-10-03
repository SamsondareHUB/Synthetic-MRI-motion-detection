# Experiment 02: 3D TorchIO Motion-Simulation Baseline

## Purpose

Evaluate whether a ResNet-18 model can distinguish clean T1-weighted brain MRI
slices from matching slices extracted from 3D motion-simulated MRI volumes.

## Dataset

- Source: IXI T1-weighted brain MRI
- Volumes used: 10
- Central axial slices retained for modelling: 1,455
- Image size: 224 x 224 pixels
- Clean and artifact slices were extracted at matching axial indices.

## Artifact Generation

Synthetic motion was generated on each full 3D MRI volume before slice
extraction using TorchIO `RandomMotion`.

| Parameter | Setting |
|---|---|
| Rotation magnitude | 2 to 4 degrees |
| Translation magnitude | 2 to 4 mm |
| Motion events | 4 |
| Interpolation | Linear |
| Artifact level | Moderate synthetic motion |

## Data Split

The same fixed subject-wise split as Experiment 01 was used.

| Partition | Subjects | Role |
|---|---:|---|
| Training | 7 | Model fitting |
| Validation | 1 | Model selection |
| Test | 2 | Final held-out evaluation |

## Model

- Architecture: ResNet-18
- Initialization: ImageNet pretrained weights
- Input: grayscale MRI repeated across three channels
- Frozen backbone; final classification layer trained
- Optimizer: Adam
- Learning rate: 0.001
- Loss: cross-entropy
- Batch size: 32
- Epochs: 5
- Random seed: 42

## Results

| Metric | Value |
|---|---:|
| Best validation accuracy | 99.29% |
| Test accuracy | 99.29% |
| Test balanced accuracy | 99.29% |
| Test AUROC | 0.9999 |
| Test AUPRC | 0.9999 |

## Comparison with Experiment 01

| Metric | Experiment 01: 2D baseline | Experiment 02: 3D TorchIO |
|---|---:|---:|
| Test accuracy | 97.00% | 99.29% |
| Test AUROC | 0.9904 | 0.9999 |

## Interpretation

On this 10-subject pilot subset, the 3D TorchIO motion-simulation setup
produced higher held-out-subject classification performance than the simple
2D image-space blending baseline.

This result does not establish improved clinical validity or generalization,
because the same synthetic motion-generation method was used to construct both
training and testing data. The experiment should be repeated with more subjects,
multiple random seeds, cross-simulation testing, and external-dataset testing.

## Limitations

- Only 10 MRI volumes were used.
- A single random subject split and training seed were used.
- All labels are synthetic.
- The test data use the same TorchIO simulation family as training.
- Performance may reflect simulator-specific features rather than realistic
  patient-motion artifacts.
