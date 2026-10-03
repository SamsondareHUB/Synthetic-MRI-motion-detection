# Experiment 05: Multi-Seed Stability Analysis

## Purpose

Assess the stability of mixed-simulation ResNet-18 training across independent
random seeds.

## Fixed Experimental Design

All runs used the same:

- IXI dataset subset of 10 T1-weighted brain MRI volumes.
- Subject-wise split: 7 training subjects, 1 validation subject, and 2 test
  subjects.
- Central axial-slice selection and preprocessing pipeline.
- ResNet-18 architecture with ImageNet pretrained weights.
- Mixed 2D image-space and 3D TorchIO synthetic motion training.
- Training configuration: frozen backbone, Adam optimizer, learning rate 0.001,
  batch size 32, and 5 epochs.

## Training Seeds

Four independent training seeds were evaluated:

- 42
- 7
- 21
- 123

The subject split remained fixed. Training order, classifier-head initialization,
mixed-simulation selection, and 2D synthetic-artifact parameters varied with
the seed.

## Per-Seed Results

| Seed | Test domain | Accuracy | Balanced accuracy | AUROC | AUPRC |
|---:|---|---:|---:|---:|---:|
| 42 | 2D | 0.9611 | 0.9611 | 0.9936 | 0.9951 |
| 42 | 3D | 0.9876 | 0.9876 | 0.9998 | 0.9998 |
| 7 | 2D | 0.9576 | 0.9576 | 0.9942 | 0.9951 |
| 7 | 3D | 0.9894 | 0.9894 | 0.9999 | 0.9999 |
| 21 | 2D | 0.9611 | 0.9611 | 0.9959 | 0.9962 |
| 21 | 3D | 0.9841 | 0.9841 | 0.9995 | 0.9995 |
| 123 | 2D | 0.9505 | 0.9505 | 0.9935 | 0.9950 |
| 123 | 3D | 0.9841 | 0.9841 | 0.9996 | 0.9996 |

## Mean and Standard Deviation

| Test artifact domain | Accuracy | Balanced accuracy | AUROC | AUPRC |
|---|---:|---:|---:|---:|
| 2D image-space artifacts | 0.9576 ± 0.0050 | 0.9576 ± 0.0050 | 0.9943 ± 0.0011 | 0.9954 ± 0.0006 |
| 3D TorchIO artifacts | 0.9863 ± 0.0026 | 0.9863 ± 0.0026 | 0.9997 ± 0.0002 | 0.9997 ± 0.0002 |

## Interpretation

Mixed-simulation training produced stable performance across the four random
training seeds. The low standard deviations indicate that the observed
performance is not strongly dependent on a particular classifier-head
initialization, batch order, or sampled 2D synthetic-artifact parameters.

This analysis evaluates training-seed stability only. It does not estimate
uncertainty due to dataset selection or subject partitioning because the same
10 subjects and fixed subject-wise split were used for every run.

## Limitations

- The dataset contains only 10 MRI volumes.
- Only two held-out subjects were used for testing.
- The subject split was fixed across all seeds.
- All labels and artifact domains were synthetic.
- Results should not be interpreted as clinical performance.
