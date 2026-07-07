# Machine Learning Model for 72-Hour Unplanned ICU Readmission Prediction in Hemorrhagic Stroke

[![DOI](https://zenodo.org/badge/PLACEHOLDER.svg)](https://doi.org/10.5281/zenodo.PLACEHOLDER)

This repository contains the complete analysis code for the study:

> **"Development and external validation of a machine learning model for 72-hour unplanned ICU readmission prediction in hemorrhagic stroke"**

## Overview

This study develops and externally validates a gradient boosting machine (GBM) model to predict 72-hour unplanned ICU readmission in patients with hemorrhagic stroke using 10 routine pre-discharge clinical variables.

### Key Features
- **Training cohort**: MIMIC-IV (N = 2,890, MetaVision system)
- **Validation cohort**: MIMIC-III (N = 1,351, CareVue system)
- **Primary outcome**: Unplanned ICU readmission within 72 hours
- **Feature selection**: Three-stage consensus (LASSO + Boruta + RFE)
- **Top model**: Gradient Boosting Machine (GBM)
- **Validation AUROC**: 0.816 (95% CI: 0.795-0.838)

## Repository Structure

```
icu-readmission-prediction/
|├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── config.py                          # Configuration parameters
├── data/                              # Data directory
│   ├── raw/                           # Raw data (user-provided)
│   └── processed/                     # Processed data
├── src/                               # Source code
│   ├── 01_data_preprocessing.py       # Data loading and preprocessing
│   ├── 02_feature_selection.py        # LASSO + Boruta + RFE
│   ├── 03_model_training.py           # 8 classifier training
│   ├── 04_model_evaluation.py         # AUROC, PR-AUC, Calibration, DCA
│   ├── 05_shap_analysis.py            # SHAP interpretability
│   └── 06_visualization.py            # Figure generation
├── notebooks/                         # Jupyter notebooks
│   └── reproducibility_demo.ipynb     # Interactive demo
└── results/                           # Output directory
    ├── figures/                       # Generated figures
    ├── tables/                        # Generated tables
    └── models/                        # Saved model objects
```

## Data Requirements

The analysis requires data from MIMIC-IV and MIMIC-III databases. Due to data use agreements, the raw clinical data cannot be shared publicly. However, this repository includes:

- **Model predictions** (probabilities) for training and validation cohorts
- **Evaluation metrics** for all 8 classifiers
- **Complete analysis code** to reproduce all figures and tables

### Provided Data Files

| File | Description | N |
|:---|:---|:---:|
| `iv_imputed.csv` | Training cohort with 43 candidate predictors | 2,890 |
| `Train_PRplot.csv` | Training predictions (all models) | 3,407 |
| `Test_PRplot.csv` | Validation predictions (all models) | 1,459 |
| `Train_Evaluation_metrics.csv` | Training threshold/metrics | - |
| `Test_Evaluation_metrics.csv` | Validation threshold/metrics | - |
| `LightGBM_important.csv` | Feature importance rankings | - |

### MIMIC Database Access

To obtain the raw data:
1. Complete CITI training (https://www.citiprogram.org/)
2. Apply for access via PhysioNet (https://physionet.org/)
3. Download MIMIC-III v1.4 and MIMIC-IV v3.1
4. Follow our SQL extraction scripts in `src/01_data_preprocessing.py`

## Installation

### Requirements
- Python >= 3.8
- PostgreSQL >= 12 (for data extraction)

### Setup

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/icu-readmission-prediction.git
cd icu-readmission-prediction

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

## Reproducibility

All analyses were performed with a fixed random seed (`random_state = 42`) for reproducibility.

### Quick Start

```bash
# Run complete pipeline
python src/01_data_preprocessing.py
python src/02_feature_selection.py
python src/03_model_training.py
python src/04_model_evaluation.py
python src/05_shap_analysis.py
python src/06_visualization.py
```

Or use the Jupyter notebook:
```bash
jupyter notebook notebooks/reproducibility_demo.ipynb
```

## Key Results

### Model Performance

| Metric | Training (MIMIC-IV) | Validation (MIMIC-III) |
|:---|:---:|:---:|
| AUROC | 0.933 (0.925-0.941) | 0.816 (0.795-0.838) |
| PR-AUC | 0.928 | 0.793 |
| Brier Score | 0.135 | 0.181 |
| Calibration Slope | 3.023 | 1.580 |
| Calibration Intercept | -0.094 | -0.081 |

### Final 10 Predictors

1. Platelet count
2. Non-invasive systolic blood pressure (NBPs)
3. Serum phosphate
4. Red cell distribution width (RDW)
5. Red blood cell count
6. Serum chloride
7. Hemoglobin
8. Hematocrit
9. White blood cell count
10. Serum calcium

## Figures

| Figure | Description |
|:---|:---|
| Figure 1 | Study flow diagram |
| Figure 2 | Feature selection results (LASSO/Boruta/RFE) |
| Figure 3 | AUROC and PR-AUC curves |
| Figure 4 | Calibration curves (GBM & LightGBM) |
| Figure 5 | Decision curve analysis |
| Figure 6 | SHAP summary and dependency plots |

## Citation

If you use this code or data, please cite:

```bibtex
@article{YOUR_PAPER_2025,
  title={Development and external validation of a machine learning model for 72-hour unplanned ICU readmission prediction in hemorrhagic stroke},
  author={YOUR_NAME and CO_AUTHORS},
  journal={Neurocritical Care},
  year={2025},
  publisher={Springer}
}
```

## License

This project is licensed under the MIT License. The MIMIC databases are available under the PhysioNet Credentialed Health Data License.

## Contact

For questions about the code or methodology, please open an issue or contact the corresponding author.

## Acknowledgments

- MIMIC-IV and MIMIC-III databases from PhysioNet
- Beth Israel Deaconess Medical Center

---

**Last updated**: 2025-07-05
