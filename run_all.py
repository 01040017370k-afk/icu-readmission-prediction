#!/usr/bin/env python
"""
run_all.py
Execute complete analysis pipeline.
Usage: python run_all.py
"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    print("=" * 70)
    print("ICU Readmission Prediction - Complete Analysis Pipeline")
    print("=" * 70)
    
    steps = [
        ("Data Preprocessing", "src.01_data_preprocessing"),
        ("Feature Selection", "src.02_feature_selection"),
        ("Model Training", "src.03_model_training"),
        ("Model Evaluation", "src.04_model_evaluation"),
        ("SHAP Analysis", "src.05_shap_analysis"),
        ("Visualization", "src.06_visualization"),
    ]
    
    for i, (name, module) in enumerate(steps, 1):
        print(f"\n{'=' * 70}")
        print(f"Step {i}/{len(steps)}: {name}")
        print(f"{'=' * 70}")
        try:
            mod = __import__(module, fromlist=['main'])
            mod.main()
            print(f"[OK] {name} completed successfully")
        except Exception as e:
            print(f"[ERROR] {name} failed: {e}")
            # Continue with next step
    
    print("\n" + "=" * 70)
    print("Pipeline Complete!")
    print("=" * 70)
    print("\nResults saved to:")
    print("  - results/figures/     (All manuscript figures)")
    print("  - results/tables/      (Performance tables)")
    print("  - results/models/      (Saved model objects)")

if __name__ == "__main__":
    main()
