# Fina Maths Lib

Deterministic financial mathematics library for FinBench, built to move formula execution away from LLM memory and into auditable, deterministic Python functions.

## Package Identity

- Package name (PyPI): `fina-maths-lib`
- Import name (Python): `maths_lib`
- Current release: `0.1.1`
- PyPI: https://pypi.org/project/fina-maths-lib/

## FinBench Context

This library is prepared as a core computation component for:

- https://github.com/vickyPotheesh2004/finbench_agent-Multi_Agent_Business_Analyst_System

## Author

- Potheesh Vignesh K
- Contact: `kpotheeshvignesh@gmail.com`

## Why This Library Exists

LLMs are good orchestrators but not always reliable calculators for multi-step finance arithmetic. `fina-maths-lib` provides deterministic formula execution so FinBench agents can call tested functions instead of estimating formulas in prompt space.

## Highlights

- Total formulas: **1500**
- Explicit function-per-formula implementation
- Domain-wise modular architecture
- Registry-backed function and metadata lookup
- Deterministic test execution and uniqueness checks

## Project Structure

- `src/maths_lib/` - source package
- `tests/maths_lib/` - exhaustive tests
- `PDR_maths_lib.md` - product requirement/design reference
- `formula_registry.py` - source formula catalog reference

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -U pip
.\.venv\Scripts\python -m pip install -r requirements.txt
```

## Run Tests

```powershell
.\.venv\Scripts\python -m pytest tests\ -v
```

## Build and Publish

Build package artifacts:

```powershell
python -m build
```

Upload to PyPI:

```powershell
python -m twine upload dist/*
```

Install from PyPI:

```powershell
pip install fina-maths-lib
```

## Quick Usage

```python
import maths_lib as ml

print(len(ml.FORMULA_REGISTRY))  # expected: 1500
result = ml.FORMULA_REGISTRY["gross_margin"](revenue=1000, cogs=600)
print(result.value, result.valid)
```

## Notes

- Formula IDs are enforced unique across all domains.
- Expressions are evaluated through a deterministic engine in `base.py`.
- Tests cover per-formula execution determinism and registry integrity.
