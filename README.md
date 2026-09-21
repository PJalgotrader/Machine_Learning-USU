![ML cover](https://user-images.githubusercontent.com/19335954/210504261-55016ce4-6d1e-4f32-9077-6af513d9f924.png)


# Machine Learning

Lecture slides, Python notebooks, data and cheatsheets for the machine learning courses taught by Prof. Pedram Jahangiry at Utah State University.

Every notebook runs in three ways: on **Google Colab** with nothing to install, or on your own computer with **uv** (recommended) or **conda**. See [Setup](#setup).


## 📂 What is in this repository

| Folder | Content |
|---|---|
| [Lectures and codes](Lectures%20and%20codes) | One folder per module: the lecture slides (PDF) and the Python notebooks |
| [Platforms and tools](Platforms%20and%20tools) | Google Colab jumpstart, the PyCaret demos (regression, classification, time series), and the [uv quick start](Platforms%20and%20tools/uv/) (cheat sheet + ten-second test) |
| [data](data) | The datasets used in the notebooks |
| [Cheatsheets](Cheatsheets) | Python, pandas, statistics, probability and machine learning cheatsheets |


## 🎲 Topics covered

| Module | Topic | Notebooks use |
|---|---|---|
| 1 | Introduction to Machine Learning | slides only |
| 2 | Setting up the Machine Learning Environment (Python crash course, EDA) | pandas, NumPy, Matplotlib, seaborn |
| 3 | Linear Regression (Econometrics approach) | statsmodels |
| 4 | Machine Learning Fundamentals | slides only |
| 5 | Linear Regression (Machine Learning approach) | scikit-learn, **PyCaret** |
| 6 | Penalized Regression (Ridge, LASSO, Elastic Net) | scikit-learn, **PyCaret** |
| 7 | Logistic Regression | scikit-learn, **PyCaret** |
| 8 | K-Nearest Neighbors (KNN) | scikit-learn, **PyCaret** |
| 9 | Classification and Regression Trees (CART) | scikit-learn, **PyCaret** |
| 10 | Bagging and Boosting (Random Forest, AdaBoost, XGBoost, LightGBM, CatBoost) | scikit-learn, xgboost, **PyCaret** |
| 11 | Dimensionality Reduction (PCA) | scikit-learn, pca |
| 12 | Clustering (KMeans, Hierarchical, K-modes) | scikit-learn, kmodes, **PyCaret** |
| Extra | Support Vector Machines (in `miscellaneous`) | slides only |


## Setup

### Read this first: PyCaret is now `pycaret-core`

The second half of each module uses [PyCaret](https://github.com/sktime/pycaret), a low-code machine learning library. The original `pycaret` package is no longer maintained and **does not run on current Python versions**, including the one on Google Colab. If you `pip install pycaret` you get one of these:

* `RuntimeError: Pycaret only supports python 3.9, 3.10, 3.11 ... Please DOWNGRADE`
* a long failed build of NumPy

This course uses **`pycaret-core`**, the community-maintained continuation of PyCaret 3 under the sktime organization. You still write `import pycaret`, and every function used in the lectures (`setup`, `compare_models`, `create_model`, `tune_model`, `plot_model`, ...) works the same. Only the install command changed:

```
pip install pycaret-core lightgbm xgboost catboost shap
```

`lightgbm`, `xgboost` and `catboost` are listed so that `compare_models()` shows the same models for everybody. `shap` is needed by `interpret_model`.

### Option 1: Google Colab (nothing to install)

1. Open a notebook on GitHub and click the **Open in Colab** badge at the top.
2. Save a copy to your own Google Drive if you want to keep your changes.
3. Run the cells from top to bottom. The PyCaret notebooks contain an install cell like this one. It installs the PyCaret stack on Colab and does nothing anywhere else:

```python
import sys
if "google.colab" in sys.modules:
    !pip install -q pycaret-core lightgbm xgboost catboost shap
```

Start from a fresh runtime (**Runtime > Disconnect and delete runtime**) if you already installed or imported anything PyCaret-related in that session. No runtime restart is needed after the install.

### Option 2: your own computer with uv (recommended)

[uv](https://docs.astral.sh/uv/) installs Python and all the packages for you, in a folder inside this repository. It does not touch any Python or Anaconda you already have. New to uv? Start with [`Platforms and tools/uv/`](Platforms%20and%20tools/uv/): a quick start, the conda-to-uv cheat sheet, and a ten-second test project. The same folder, and the same commands, are used in the Deep Learning and Deep Forecasting courses.

1. Install uv ([instructions](https://docs.astral.sh/uv/getting-started/installation/)), then reopen the terminal and check `uv --version`.

   Windows (PowerShell):
   ```
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
   macOS / Linux:
   ```
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
2. Get the repository (clone into a normal local folder, not inside Google Drive or OneDrive) and build the environment:
   ```
   git clone https://github.com/PJalgotrader/Machine_Learning-USU.git
   cd Machine_Learning-USU
   uv sync
   ```
   Optional first: the ten-second test in `Platforms and tools/uv/simple_test` (`uv sync`, then `uv run python main.py`) prints your Python and pandas versions and `uv is working!`.
3. Check it:
   ```
   uv run python scripts/check_environment.py
   ```
   The last line should say `Your course environment is ready.`
4. Start Jupyter:
   ```
   uv run jupyter lab
   ```

**VS Code:** register the environment as a Jupyter kernel once, then pick it with **Select Kernel > Jupyter Kernel**:

```
uv run python -m ipykernel install --user --name ml-course --display-name "Python 3.13 (ML course)"
```

### Option 3: your own computer with conda

```
git clone https://github.com/PJalgotrader/Machine_Learning-USU.git
cd Machine_Learning-USU
conda env create -f environment.yml
conda activate ml_pycaret
python scripts/check_environment.py
jupyter lab
```

In VS Code, the `ml_pycaret` environment shows up under **Select Kernel > Python Environments**.

### What the environment contains

Python 3.13 with `pycaret-core`, scikit-learn, pandas, NumPy, statsmodels, Matplotlib, seaborn, LightGBM, XGBoost, CatBoost, shap, kmodes, pca, yfinance and JupyterLab. The exact versions are locked in [uv.lock](uv.lock). The package list lives in [pyproject.toml](pyproject.toml) (uv) and [environment.yml](environment.yml) (conda).

The automated EDA notebook in Module 2 (`pandas-profiling`, `sweetviz`, `dtale`) is not part of this environment. Run that one on Colab.

### Troubleshooting

| Symptom | Fix |
|---|---|
| `Pycaret only supports python 3.9, 3.10, 3.11 ... Please DOWNGRADE` | You installed the old `pycaret` package. Colab: delete the runtime and run the notebook's install cell. Local: `pip uninstall pycaret`, then build the environment as above. |
| pip tries to build NumPy from source and fails | Same cause: the old `pycaret` package on a new Python. Install `pycaret-core` instead. |
| `ValueError: Estimator xgboost Not Available` (or `catboost`, `lightgbm`) on Colab | The library was installed after PyCaret was already imported. **Runtime > Disconnect and delete runtime**, then run the notebook from the top. |
| The checker reports the wrong Python version | The notebook or terminal is not using the course environment. Use `uv run ...`, or `conda activate ml_pycaret`, or pick the right kernel in VS Code. |
| `DLL load failed` on Windows inside a uv environment | The environment was built on top of Anaconda's Python. Delete the `.venv` folder and run `uv sync` again. This repository tells uv to use its own Python. |
| Install errors about paths that are too long (Windows) | Clone the repository into a short path such as `C:\ML`, and not inside OneDrive or Google Drive. |
| `ETSResults.simulate() got an unexpected keyword argument 'random_state'` in the time series demos | statsmodels is too new for the time series module. The time series notebooks and the local environment pin `statsmodels<0.15`. |


## 🚀 About Me

Pedram Jahangiry, CFA, is a Professional Practice Associate Professor of Data Analytics and Information Systems in the [Huntsman School of Business at Utah State University](https://huntsman.usu.edu/directory/jahangiry-pedram). Prior to joining the Huntsman School, Pedram was a research associate within the Financial Modeling Group at BlackRock NYC. His current research is involved in machine learning, deep learning and time series forecasting.
Pedram is one of the project mentors at the [Analytics Solutions Center](https://huntsman.usu.edu/asc/index), where students from across USU’s Logan and Statewide campuses work with corporate partners on analytics projects.


## 🔗 Links

[![linkedin](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pedram-jahangiry-cfa-5778015a)

[![Youtube](https://img.shields.io/badge/youtube_channel-1DA1F2?style=for-the-badge&logo=youtube&logoColor=white&color=FF0000)](https://www.youtube.com/channel/UCNDElcuuyX-2pSatVBDpJJQ)

[![X URL](https://img.shields.io/twitter/url/https/twitter.com/PedramJahangiry.svg?style=social&label=Follow%20%40PedramJahangiry)](https://twitter.com/PedramJahangiry)


<img src="images/Jahangirylogo.png" width=150 align="right">
