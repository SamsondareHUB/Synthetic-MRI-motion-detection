# Study Protocol

## Working Title

Evaluating Synthetic Motion Simulation Strategies for Transfer Learning-Based
Quality Control in Brain MRI

## Research Question

How do image-space and 3D MRI-aware synthetic motion simulation strategies
affect the performance and generalization of transfer-learning models for
detecting motion artifacts in T1-weighted brain MRI?

## Hypotheses

1. Transfer-learning models will outperform a CNN trained from scratch.
2. Training with 3D MRI-aware motion simulation will generalize better than
   image-space synthetic corruption.
3. Subject-level patient quality-control predictions will be more robust than
   individual slice-level predictions.

## Dataset Plan

- Internal dataset: IXI T1-weighted MRI
- Target size: 50–100 subjects
- External dataset: a separate public T1-weighted brain MRI dataset
- Split rule: no subject appears in more than one partition

## Experiments

1. Image-space synthetic corruption + CNN from scratch
2. Image-space synthetic corruption + ResNet-18
3. Image-space synthetic corruption + DenseNet-121
4. 3D motion simulation + CNN from scratch
5. 3D motion simulation + ResNet-18
6. 3D motion simulation + DenseNet-121

## Evaluation

- Slice-level and subject-level performance
- Accuracy, balanced accuracy, precision, recall, specificity, F1, AUROC, AUPRC
- 95% bootstrap confidence intervals
- Three random seeds per experiment
- Internal held-out testing and external testing
- Confusion matrices, ROC curves, Grad-CAM, and failure analysis

## Limitations to State Up Front

- Synthetic artifacts are approximations of real patient motion.
- Public datasets may not represent clinical populations and scanner diversity.
- External testing does not replace expert-labelled real-motion evaluation.
