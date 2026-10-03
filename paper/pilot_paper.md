# Mixed Synthetic Motion Simulation Improves Cross-Simulation Robustness for Transfer Learning-Based Brain MRI Quality Control

## Abstract

Motion artifacts can reduce the diagnostic quality of magnetic resonance imaging
(MRI), while manually labelled motion-corrupted data are limited. Synthetic
artifact generation can provide labels for supervised quality-control models, but
models may overfit to the visual characteristics of a specific simulator. This
pilot study evaluated whether training with multiple synthetic motion simulation
strategies improves robustness across synthetic artifact domains in T1-weighted
brain MRI. Ten IXI T1-weighted brain MRI volumes were canonically reoriented,
preprocessed, and converted to central axial slices. We trained
ImageNet-pretrained ResNet-18 classifiers using: (1) 2D image-space
rotation/translation and blending, (2) 3D TorchIO rigid-motion simulation, and
(3) a mixture of both methods. Subject-wise splitting used seven training, one
validation, and two held-out test subjects. Single-simulator models exhibited
cross-simulation performance decreases: the 2D-trained model obtained 91.17%
accuracy on 3D artifacts, while the 3D-trained model obtained 76.86% accuracy
on 2D artifacts. In contrast, mixed-simulation training achieved mean accuracy
of 95.76% ± 0.50% on 2D artifacts and 98.63% ± 0.26% on 3D artifacts across
four training seeds. Matched-domain threshold calibration did not remove the
cross-simulation performance loss. These preliminary results suggest that
diversity of synthetic motion generators can reduce simulator-specific domain
shift in low-resource brain-MRI quality-control pipelines. Validation on larger
datasets and real patient-motion artifacts is required.

## 1. Introduction

Motion during MRI acquisition can degrade anatomical detail, interfere with
clinical interpretation, and reduce the reliability of downstream automated
image analysis. Manual image quality control is time-consuming, and real
motion-artifact labels are often limited, subjective, or unavailable. Synthetic
motion generation provides a practical mechanism for constructing labelled
training data.

However, synthetic motion artifacts depend on the simulation method. A
classifier trained and evaluated using the same simulation process may learn
simulator-specific features rather than generalizable properties of motion
corruption. This issue is particularly relevant for low-resource research
settings, where access to large clinical datasets with expert quality labels is
limited.

This pilot study investigates synthetic-domain robustness in T1-weighted brain
MRI. We compare a simple 2D image-space artifact generator, a 3D MRI-aware
TorchIO motion simulator, and mixed-simulation training. We hypothesize that
models trained with a mixture of synthetic artifact generators will show higher
performance across both synthetic test domains than models trained with a
single generator.

## 2. Materials and Methods

### 2.1 Dataset

We used ten T1-weighted brain MRI volumes from the IXI dataset. MRI volumes
were de-identified and handled locally in Google Drive; no raw MRI data were
included in the public source-code repository.

### 2.2 Preprocessing

Volumes were reoriented to canonical anatomical orientation. Axial slices were
extracted, and mostly empty slices were removed. The central 60% of valid slices
for each volume were retained. Slice intensities were clipped between the 1st
and 99th percentiles, normalized to [0, 1], and resized to 224 × 224 pixels.
This produced 1,455 central slices from ten subjects.

### 2.3 Synthetic Motion Simulations

The 2D image-space generator applied random rotation from -6° to +6° and random
translation from -6 to +6 pixels in each image direction. The transformed slice
was blended with the original slice using weights of 0.65 and 0.35.

The 3D MRI-aware generator applied TorchIO `RandomMotion` to each full MRI
volume before slice extraction. Motion parameters used rotation magnitudes of
2–4°, translation magnitudes of 2–4 mm, four motion events, and linear
interpolation.

The mixed-simulation dataset selected the 2D or 3D generator with equal
probability for each artifact example.

### 2.4 Model and Training

An ImageNet-pretrained ResNet-18 model was used for binary classification of
clean versus synthetic-motion artifact slices. Grayscale slices were duplicated
to three channels and normalized using ImageNet channel means and standard
deviations. The ResNet-18 backbone was frozen and the final two-class
classification layer was trained using Adam optimization, a learning rate of
0.001, cross-entropy loss, a batch size of 32, and five epochs.

Subjects were partitioned into seven training, one validation, and two held-out
test subjects. Model selection was based on validation performance. The mixed
model was evaluated over four independent training seeds: 42, 7, 21, and 123.

### 2.5 Evaluation

We report slice-level accuracy, balanced accuracy, area under the receiver
operating characteristic curve (AUROC), and area under the precision-recall
curve (AUPRC). Matched-simulation and cross-simulation testing were performed.
For calibration analysis, decision thresholds were chosen using Youden’s J
statistic on matched-domain validation data and applied unchanged to
cross-simulation test data.

## 3. Results

### 3.1 Matched- and Cross-Simulation Results

| Training simulation | Test simulation | Accuracy | AUROC | AUPRC |
|---|---|---:|---:|---:|
| 2D only | 2D | 97.00% | 0.9904 | Not recorded |
| 2D only | 3D | 91.17% | 0.9939 | 0.9942 |
| 3D only | 3D | 99.29% | 0.9999 | 0.9999 |
| 3D only | 2D | 76.86% | 0.9751 | 0.9778 |

Within-domain performance was high for both single-simulation models. However,
performance declined under cross-simulation evaluation, particularly when the
3D-trained model was evaluated on 2D image-space artifacts.

### 3.2 Threshold Calibration

Thresholds selected from matched-domain validation sets were 0.5338 for the
2D-trained model and 0.6024 for the 3D-trained model. Applying these thresholds
to the alternate artifact domain did not remove cross-domain performance loss.
The 2D-trained model achieved 89.58% accuracy on 3D artifacts, while the
3D-trained model achieved 71.55% accuracy on 2D artifacts. Both models showed
100% specificity but reduced artifact sensitivity, indicating persistent
synthetic-domain shift.

### 3.3 Mixed-Simulation Training

Mixed-simulation training produced stable performance across four training
seeds.

| Test artifact domain | Accuracy, mean ± SD | AUROC, mean ± SD | AUPRC, mean ± SD |
|---|---:|---:|---:|
| 2D image-space artifacts | 95.76% ± 0.50% | 0.9943 ± 0.0011 | 0.9954 ± 0.0006 |
| 3D TorchIO artifacts | 98.63% ± 0.26% | 0.9997 ± 0.0002 | 0.9997 ± 0.0002 |

Mixed training maintained high performance across both domains. Compared with
cross-simulation single-generator models, it improved accuracy from 76.86% to
95.76% on 2D artifacts and from 91.17% to 98.63% on 3D artifacts.

## 4. Discussion

This pilot study found that high performance on synthetic motion-artifact
detection can be simulator-dependent. Although 2D-only and 3D-only models
performed well when evaluated on artifacts generated by their training
simulator, performance declined on artifacts generated by the alternate
simulator. Threshold calibration on matched-domain validation data did not
resolve this decrease, suggesting that the effect was not solely a
decision-threshold shift.

Training with a mixture of 2D image-space and 3D MRI-aware synthetic artifacts
substantially reduced cross-simulation performance loss. The mixed model
retained high accuracy across both artifact domains and showed low variation
over four training seeds. This suggests that simulator diversity may serve as a
practical form of domain diversification for synthetic-data-driven MRI quality
control.

The study has important limitations. It used only ten MRI volumes and two
held-out test subjects. All artifacts were synthetic, and therefore the results
cannot be interpreted as clinical validation for real patient motion. A single
subject partition was used, and evaluation was performed at the slice level.
Future work should evaluate larger multi-site cohorts, use scan-level
aggregation, compare additional architectures, incorporate real expert-rated
motion artifacts, and conduct external testing on independently acquired MRI
data.

## 5. Conclusion

In this pilot study, mixed synthetic motion simulation improved the robustness
of transfer-learning-based motion-artifact detection across two synthetic brain
MRI artifact domains. The results highlight the risk of simulator-specific
overestimation and support the use of diverse synthetic generators when
developing low-resource MRI quality-control models.

## Data Availability

The IXI brain MRI dataset used in this study is publicly available from the
IXI project subject to its data-access and licensing terms. Raw MRI volumes,
derived slice arrays, and trained model checkpoints are not redistributed in
this repository. The code, preprocessing workflow, experimental configuration,
and aggregate results are available at: [https://github.com/SamsondareHUB/Synthetic-MRI-motion-detection].

## Code Availability

All code required to reproduce the reported preprocessing, synthetic-artifact
generation, training, and evaluation workflows is available at:
[https://github.com/SamsondareHUB/Synthetic-MRI-motion-detection]. The repository excludes raw MRI data and
derived image arrays.

## Ethics Statement

This study used de-identified, publicly available brain MRI data. No new human
participants were recruited, no interventions were performed, and no private
patient information was accessed. The study followed the applicable terms of
use for the source dataset. Institutional ethics approval was not sought for
this secondary analysis of publicly available de-identified data; authors should
confirm this statement against their institution's requirements before public
submission.

## Funding

No external funding was received for this work.

## Competing Interests

The author declares no competing interests.

## Author Contributions

[Samson Oluwadare]: Conceptualization, methodology, software, formal analysis,
visualization, writing—original draft, and writing—review and editing.

 ## Disclosure

The author reviewed, verified, and takes full responsibility for all methods,
code, analyses, results, interpretations, and manuscript content.

## References

1. Pérez-García F, Sparks R, Ourselin S. TorchIO: A Python library for
   efficient loading, preprocessing, augmentation and patch-based sampling of
   medical images in deep learning. Computer Methods and Programs in
   Biomedicine. 2021;208:106236. doi:10.1016/j.cmpb.2021.106236.

2. Loizillon S, Bottani S, Mabille S, et al. Automatic motion artefact
   detection in brain T1-weighted magnetic resonance images from a clinical
   data warehouse using synthetic data. Medical Image Analysis. 2024;93:103073.
   doi:10.1016/j.media.2023.103073.

3. Tejani AS, Klontzas ME, et al. Checklist for Artificial Intelligence in
   Medical Imaging (CLAIM): 2024 Update. Radiology: Artificial Intelligence.
   2024;6(4):e240300. doi:10.1148/ryai.240300.
