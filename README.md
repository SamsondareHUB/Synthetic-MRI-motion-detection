## Baseline Results

A pretrained ResNet-18 model was fine-tuned to classify clean and synthetically
motion-corrupted axial T1-weighted brain-MRI slices.

| Metric | Result |
|---|---:|
| Best validation accuracy | 98.23% |
| Test accuracy | 97.00% |
| Test AUROC | 0.9904 |
| Clean-slice recall | 100% |
| Synthetic-artifact recall | 94% |
| Test samples | 566 |

### Experimental setup

- Dataset: 10 IXI T1-weighted brain MRI volumes
- Central axial slices: 1,455
- Split: subject-wise, with 7 training subjects, 1 validation subject, and 2 test subjects
- Model: ImageNet-pretrained ResNet-18
- Classes: clean vs. synthetically motion-corrupted MRI slices

### Important limitation

The synthetic artifact in this baseline was produced with a 2D transformed-image
blending procedure. Therefore, these results demonstrate performance on the
specific synthetic corruption used in this experiment and should not be treated
as clinical performance on real patient-motion artifacts. Future work will use
3D k-space-based motion simulation and evaluate against real motion-corrupted
brain MRI data.
