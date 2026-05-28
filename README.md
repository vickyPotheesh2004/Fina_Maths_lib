# maths_lib_

Deterministic financial mathematics library built from PDR with explicit formula functions and registry-backed lookup.

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

## Run Tests

```powershell
.\.venv\Scripts\python -m pytest tests\ -v
```

## Registry Usage

```python
import maths_lib as ml

# total formulas
print(len(ml.FORMULA_REGISTRY))

# call a formula
result = ml.FORMULA_REGISTRY["gross_margin"](revenue=1000, cogs=600)
print(result.value, result.valid)
```

## Notes

- Formula IDs are unique across all domains.
- Expressions are evaluated via deterministic expression engine in `base.py`.
- Tests include per-formula deterministic execution and registry integrity checks.
