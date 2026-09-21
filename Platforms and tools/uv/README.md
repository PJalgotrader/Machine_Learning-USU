# uv: student quick start

This folder is the same in all of Pedram's course repositories (Machine Learning, Deep Learning, Deep Forecasting, and `platforms-and-tools`). Learn it once, use it everywhere.

**What uv is.** One small program that downloads the right Python, creates an isolated environment (a `.venv` folder inside the project) and installs the exact package versions listed in the project's `uv.lock`. You never `activate` anything: `uv sync` builds the environment, `uv run <command>` uses it.

## 1. Install uv (once per computer)

macOS / Linux (Terminal):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Close and reopen the terminal, then check:

```bash
uv --version
```

Full instructions: <https://docs.astral.sh/uv/getting-started/installation/>

## 2. The ten-second test

From this folder:

```bash
cd simple_test
uv sync
uv run python main.py
```

You should see three lines: your Python version (3.13.x), your pandas version, and **uv is working!**. That is the whole uv workflow: `uv sync` built a tiny environment (Python 3.13 + pandas), `uv run` ran a script inside it.

## 3. The real course environment

The course environment lives at the **root of the repository** (`pyproject.toml` + `uv.lock`). From the top folder of the repo:

```bash
uv sync
```

```bash
uv run python scripts/check_environment.py
```

The check must end with **Your course environment is ready.** Then:

```bash
uv run jupyter lab
```

Details, VS Code kernel setup and troubleshooting are in the repository's main `README.md`.

## Cheat sheet

Coming from conda? [`conda_to_uv_student_cheatsheet.pdf`](conda_to_uv_student_cheatsheet.pdf) (also as [HTML](conda_to_uv_student_cheatsheet.html)) translates every conda command you know into its uv equivalent.

## The five uv commands you will ever need

| Command | What it does |
|---|---|
| `uv sync` | build (or update) the environment from `pyproject.toml` / `uv.lock` |
| `uv run <cmd>` | run anything inside the environment (`uv run python x.py`, `uv run jupyter lab`) |
| `uv init <folder>` | start a new project of your own |
| `uv add <package>` | add a package to your own project (updates `pyproject.toml` and `uv.lock`) |
| `uv remove <package>` | remove one |

Never edit `uv.lock` by hand, and never run `uv sync` inside a Google Drive or OneDrive folder (they upload every file of the environment). Clone the repository into a plain local folder such as `C:\courses` or `~/Documents/GitHub`.
