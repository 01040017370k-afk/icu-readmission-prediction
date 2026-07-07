"""
Configuration file for ICU readmission prediction analysis.
All parameters are centralized here for reproducibility.
"""

import os

# Random seed for reproducibility
RANDOM_STATE = 42

# Data paths
DATA_DIR = "data"
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")
RESULTS_DIR = "results"
FIGURES_DIR = os.path.join(RESULTS_DIR, "figures")
TABLES_DIR = os.path.join(RESULTS_DIR, "tables")
MODELS_DIR = os.path.join(RESULTS_DIR, "models")

# Create directories if they don't exist
for dir_path in [RAW_DATA_DIR, PROCESSED_DATA_DIR, FIGURES_DIR, TABLES_DIR, MODELS_DIR]:
    os.makedirs(dir_path, exist_ok=True)

# Cohort parameters
TRAINING_N = 2890
VALIDATION_N = 1351
READMISSION_RATE_TRAIN = 0.171
READMISSION_RATE_VAL = 0.183

# Feature selection parameters
MISSINGNESS_THRESHOLD = 0.20  # Exclude features with >20% missing
MICE_DATASETS = 5  # Number of imputed datasets
LASSO_LAMBDA = 0.0037  # Optimal lambda from analysis
BORUTA_ITERATIONS = 250  # Boruta algorithm iterations
BORUTA_MAX_DEPTH = 5  # Boruta max tree depth
RFE_ESTIMATOR = "RandomForestClassifier"  # Base estimator for RFE
RFE_STEP = 1  # Number of features to remove at each iteration

# Cross-validation parameters
CV_FOLDS = 10
CV_STRATIFIED = True

# Model names
MODEL_NAMES = [
    "Logistic",
    "SVM", 
    "GBM",
    "NeuralNetwork",
    "Xgboost",
    "Adaboost",
    "LightGBM",
    "CatBoost"
]

# Primary model (best performing)
PRIMARY_MODEL = "GBM"
SECONDARY_MODEL = "LightGBM"

# Evaluation parameters
N_BOOTSTRAP = 2000  # Number of bootstrap samples for CI
CALIBRATION_BINS = 10  # Number of bins for calibration curves
CALIBRATION_STRATEGY = "quantile"  # Binning strategy
DCA_THRESHOLDS = 100  # Number of threshold points for DCA

# Threshold optimization
THRESHOLD_METHOD = "youden"  # Method for optimal threshold

# Feature domains (for reporting)
FEATURE_DOMAINS = {
    "demographics": ["age", "sex", "weight", "smoking_status"],
    "comorbidities": ["hypertension", "diabetes", "heart_failure", "aki"],
    "vitals": ["heart_rate", "respiratory_rate", "temperature", "spo2", 
               "nbps", "nbpd", "nbpm", "gcs"],
    "severity_scores": ["sofa", "apsiii", "sapsii"],
    "laboratory": ["wbc", "rbc", "hemoglobin", "hematocrit", "platelet", "rdw",
                   "anion_gap", "glucose", "creatinine", "bun", "bicarbonate",
                   "sodium", "potassium", "chloride", "calcium", "magnesium",
                   "phosphate", "inr", "pt", "aptt"],
    "interventions": ["sedatives", "vasopressors", "crrt"]
}

# Final 10 selected features (from consensus selection)
FINAL_FEATURES = [
    "platelet",
    "nbps", 
    "phosphate",
    "rdw",
    "rbc",
    "chloride",
    "hemoglobin",
    "hematocrit",
    "wbc",
    "calcium"
]

# ICD codes for case identification
ICD9_CODES = ["430", "431"]
ICD10_CODES = ["I60", "I61"]

# Outcome definition
READMISSION_WINDOW_HOURS = 72

# PostgreSQL connection (for data extraction)
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "mimiciv",
    "user": "your_username",
    "password": "your_password"
}

# Figure parameters
FIGURE_DPI = 300
FIGURE_FORMAT = "png"
COLOR_PALETTE = "viridis"
STYLE = "seaborn-v0_8-whitegrid"

# Table formatting
TABLE_DECIMALS = 3
