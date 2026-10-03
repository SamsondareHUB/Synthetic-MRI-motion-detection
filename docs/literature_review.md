# Literature Review: Motion-Artifact Detection in Brain MRI

## Purpose

This review identifies the research gap for a low-resource, reproducible study
of transfer learning for synthetic motion-artifact detection in T1-weighted
brain MRI.

## Key Studies

| Study | Data and Labels | Method | Evaluation | Key Result | Relevance to This Project |
|---|---|---|---|---|---|
| Loizillon et al., 2024 | Research MRI with synthetic motion; 4,045 manually labelled clinical T1 MRI scans | Synthetic-motion pretraining followed by transfer learning to clinical data | Severe and mild motion detection on clinical data | Severe-motion balanced accuracy exceeded 80%; mild motion was substantially harder | Strongest prior reference. Our project must not claim clinical validation without real labelled artifacts |
| Beljaards et al., 2024 | 4,387 synthetic training images; 1,304 synthetic validation images; 28 in-vivo motion scans | CNN estimates motion severity in undersampled MRI | Synthetic and real in-vivo testing; quality grading | Synthetic-trained model detected motion-free versus motion scans with 91% accuracy on real data | Supports the value of synthetic training but shows real-motion testing is required |
| Manso Jimeno et al., 2025 | Motion-synthesized T1 brain MRI, retrospective public data, and prospective data | 2D CNN for three-class motion classification with Grad-CAM | Multiple retrospective datasets and prospective radiologist-labelled data | Average precision 85%, recall 80%; 93% agreement with radiologist labels prospectively | Supports adding Grad-CAM and testing beyond one internal data source |
| Roecher et al., 2024 | 420 T1-weighted whole-brain MRI volumes with expert motion ratings | CNN for binary and three-class motion classification | Human-labelled artifact prominence | 95% accuracy for pronounced motion; 76% for three classes | Shows subtle/intermediate artifact grading is difficult and binary severe-artifact detection is easier |
| Bouchard et al., 2025 | HCPEP, AMP SCZ, and synthetic motion-corrupted T1 MRI | Synthetic-motion regression pretraining, then transfer learning for QC classification | Site-based split and five random seeds | Transfer learning outperformed training from scratch on imbalanced QC labels | Supports comparisons against a from-scratch baseline and repeated random seeds |

## What Is Already Known

1. Synthetic motion can support training for MRI quality control.
2. Transfer learning can improve performance compared with training from scratch.
3. Detecting severe motion is easier than detecting mild or intermediate motion.
4. High synthetic-test accuracy does not establish clinical validity.
5. Patient- or subject-level splitting is required to prevent leakage.
6. Real-motion or external-data evaluation is essential for generalization claims.
7. Grad-CAM and failure analysis improve transparency.

## Gap for This Study

Most published studies use large clinical datasets, specialist computational
resources, expert-labelled data, or proprietary clinical repositories. This
project will evaluate whether a compact, reproducible pipeline can provide
meaningful cross-dataset performance under low-resource conditions.

The study will compare:

1. A CNN trained from scratch versus ImageNet-pretrained transfer-learning models.
2. The preliminary 2D image-space motion-like augmentation versus 3D TorchIO
   motion simulation.
3. Internal IXI testing versus zero-shot external testing on a separate public
   T1-weighted brain MRI dataset.
4. Slice-level versus subject-level prediction aggregation.

## Planned Contribution

A reproducible, Colab-compatible benchmark for synthetic motion-artifact
detection in T1-weighted brain MRI that reports subject-wise and cross-dataset
performance, documents resource requirements, and clearly distinguishes
synthetic performance from clinical validity.

## References

1. Loizillon S, Bottani S, Maire A, et al. Automatic motion artefact detection
   in brain T1-weighted magnetic resonance images from a clinical data warehouse
   using synthetic data. Medical Image Analysis. 2024;93:103073.
   doi:10.1016/j.media.2023.103073

2. Beljaards L, Pezzotti N, Rao C, et al. AI-based motion artifact severity
   estimation in undersampled MRI allowing for selection of appropriate
   reconstruction models. Medical Physics. 2024;51(5):3555-3565.
   doi:10.1002/mp.16918

3. Manso Jimeno M, Ravi KS, Fung M, et al. Automated detection of motion
   artifacts in brain MR images using deep learning. NMR in Biomedicine.
   2025;38(1):e5276. doi:10.1002/nbm.5276

4. Roecher E, Mösch L, Zweerings J, et al. Motion Artifact Detection for
   T1-Weighted Brain MR Images Using Convolutional Neural Networks.
   International Journal of Neural Systems. 2024;34(10):2450052.
   doi:10.1142/S0129065724500527

5. Bouchard S, et al. Improving Quality Control of MRI Images Using Synthetic
   Motion Data. arXiv:2502.00160. 2025.
