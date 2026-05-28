# Fina Maths Lib

Deterministic financial mathematics library for FinBench with explicit formula functions and registry-backed lookup.

## Library Name

- **PyPI/Package name:** `fina-maths-lib`
- **Python import name:** `maths_lib`

## Parent Repository

This library is prepared as a sub-module/component for:

- [vickyPotheesh2004/finbench_agent-Multi_Agent_Business_Analyst_System](https://github.com/vickyPotheesh2004/finbench_agent-Multi_Agent_Business_Analyst_System.git)

## Author

- **Potheesh Vignesh K**

## Contact

- **Email:** `kpotheeshvignesh@gmail.com`

## Highlights

- Total formulas: **1500**
- Explicit formula functions (no hidden dynamic-only API)
- Domain-wise module organization
- Central registry for formula metadata and callable access
- Deterministic test suite with uniqueness/overlap checks

## Project Structure

- `src/maths_lib/` - source package
- `tests/maths_lib/` - exhaustive tests
- `PDR_maths_lib.md` - requirement document
- `formula_registry.py` - source registry reference

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -U pip
.\.venv\Scripts\python -m pip install -r requirements.txt
```

## Build Package

```powershell
.\.venv\Scripts\python -m build
```

Note: run only `python -m build` (do not append extra words like `success`).

## Run Tests

```powershell
.\.venv\Scripts\python -m pytest tests\ -v
```

## Registry Usage

```python
import maths_lib as ml

print(len(ml.FORMULA_REGISTRY))
result = ml.FORMULA_REGISTRY["gross_margin"](revenue=1000, cogs=600)
print(result.value, result.valid)
```

## Notes

- Formula IDs are unique across all domains.
- Expressions are evaluated via deterministic expression engine in `base.py`.
- Tests include per-formula deterministic execution and registry integrity checks.
