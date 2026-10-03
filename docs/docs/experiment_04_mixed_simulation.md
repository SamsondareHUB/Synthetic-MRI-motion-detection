# Experiment 04: Mixed-Simulation Training

## Purpose

Test whether training with both 2D image-space and 3D MRI-aware synthetic motion
artifacts improves robustness across distinct synthetic artifact generators.

## Training Data

Each clean axial MRI slice was paired with one artifact version. During training,
artifact slices were generated using one of two methods selected with equal
probability:

1. **2D image-space blending:** random rotation and translation followed by
   transformed-image blending.
2. **3D TorchIO motion simulation:** motion introduced in the full MRI volume
   before axial-slice extraction.

Clean and artifact classes were balanced because each clean slice produced one
clean and one artifact training example.

## Dataset and Split

- Dataset: IXI T1-weighted brain MRI.
- Subjects: 10.
- Central axial slices: 1,455.
- Subject-wise split: 7 training subjects, 1 validation subject, and 2 held-out
  test subjects.
- Image size: 224 × 224 pixels.

## Model and Training

- Model: ImageNet-pretrained ResNet-18.
- Backbone: frozen.
- Trainable layer: final two-class fully connected classifier.
- Optimizer: Adam.
- Learning rate: 0.001.
- Loss: cross-entropy.
- Batch size: 32.
- Epochs: 5.
- Random seed: 42.

## Results

| Evaluation artifacts | Accuracy | Balanced accuracy | AUROC | AUPRC |
|---|---:|---:|---:|---:|
| 2D image-space artifacts | 96.11% | 96.11% | 0.9936 | 0.9951 |
| 3D TorchIO artifacts | 98.76% | 98.76% | 0.9998 | 0.9998 |

Best mixed-domain validation accuracy: **98.23%**.

## Comparison With Single-Simulation Training

| Model | Test on 2D artifacts | Test on 3D artifacts |
|---|---:|---:|
| 2D-only training | 97.00% | 91.17% |
| 3D-only training | 76.86% | 99.29% |
| Mixed 2D + 3D training | **96.11%** | **98.76%** |

## Interpretation

Mixed-simulation training achieved high performance on both synthetic artifact
domains. It substantially improved performance relative to a mismatched
single-simulator model:

- On 2D artifacts, mixed training improved accuracy from 76.86% for the
  3D-only model to 96.11%.
- On 3D artifacts, mixed training improved accuracy from 91.17% for the
  2D-only model to 98.76%.

The mixed model remained close to each matched-domain specialist model,
suggesting that simulator diversity can reduce synthetic-domain shift without a
large loss of within-domain performance.

## Limitations

- All artifacts were synthetic.
- Only 10 MRI volumes and two held-out test subjects were used.
- The model was evaluated at the slice level.
- One subject split and one training seed were used.
- Results do not establish performance on real clinical motion artifacts.
