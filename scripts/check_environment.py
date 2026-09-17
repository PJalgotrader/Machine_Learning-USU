"""Checks that your local Python environment can run the course notebooks.

uv:     uv run python scripts/check_environment.py
conda:  conda activate ml_pycaret, then: python scripts/check_environment.py
"""
import importlib
import sys
import warnings

warnings.filterwarnings("ignore")
problems = []

print(f"Python {sys.version.split()[0]}  ({sys.executable})")
if sys.version_info[:2] != (3, 13):
    problems.append("Python 3.13 expected. Rebuild the environment by following the README.")

for name in ["pycaret", "sklearn", "numpy", "pandas", "scipy", "statsmodels", "matplotlib", "seaborn",
             "lightgbm", "xgboost", "catboost", "shap", "kmodes", "pca", "yfinance"]:
    try:
        module = importlib.import_module(name)
        print(f"  {name:<12} {getattr(module, '__version__', 'ok')}")
    except Exception as err:
        problems.append(f"cannot import {name}: {err}")

if not problems:
    from pycaret.classification import ClassificationExperiment
    from pycaret.clustering import ClusteringExperiment
    from pycaret.datasets import get_data
    from pycaret.regression import RegressionExperiment

    print("Running a tiny PyCaret experiment of each kind ...")
    try:
        data = get_data("juice", verbose=False)
        clf = ClassificationExperiment()
        clf.setup(data, target="Purchase", session_id=1, verbose=False)
        available = set(clf.models().index)
        for booster in ["lightgbm", "xgboost", "catboost"]:
            if booster not in available:
                problems.append(f"{booster} is missing from the PyCaret model list")
        clf.create_model("lr", verbose=False)

        reg = RegressionExperiment()
        reg.setup(get_data("insurance", verbose=False), target="charges", session_id=1, verbose=False)
        reg.create_model("dt", verbose=False)

        clu = ClusteringExperiment()
        clu.setup(get_data("jewellery", verbose=False), session_id=1, verbose=False)
        clu.create_model("kmeans", verbose=False)
    except Exception as err:
        problems.append(f"PyCaret experiment failed: {type(err).__name__}: {err}")

print()
if problems:
    print("Something is wrong:")
    for p in problems:
        print("  -", p)
    sys.exit(1)
print("Your course environment is ready.")
