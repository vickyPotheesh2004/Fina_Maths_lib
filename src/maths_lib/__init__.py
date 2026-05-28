from .registry import DOMAINS, all_formulas, count_summary
from .base import FormulaResult, RUNTIME_FORMULA_REGISTRY
from . import profitability
from . import liquidity_solvency
from . import valuation
from . import technical
from . import options
from . import fixed_income
from . import risk
from . import tvm
from . import corporate_ma
from . import accounting
from . import statistics_econ
from . import math_core
from . import growth_segment_forensic
from . import ai_ml
from . import probability
from . import statistics_advanced
from . import business_analyst
from . import crypto_onchain
from . import credit_risk
from . import interest_rate_models
from . import factor_risk
from . import derivatives_greeks
from . import forecasting_ts
from . import optimization_ops
from . import macro_econ
from . import treasury_cash
from . import insurance_actuarial

DOMAIN_MODULES = [
    profitability,
    liquidity_solvency,
    valuation,
    technical,
    options,
    fixed_income,
    risk,
    tvm,
    corporate_ma,
    accounting,
    statistics_econ,
    math_core,
    growth_segment_forensic,
    ai_ml,
    probability,
    statistics_advanced,
    business_analyst,
    crypto_onchain,
    credit_risk,
    interest_rate_models,
    factor_risk,
    derivatives_greeks,
    forecasting_ts,
    optimization_ops,
    macro_econ,
    treasury_cash,
    insurance_actuarial,
]

FORMULA_REGISTRY = {}
for _m in DOMAIN_MODULES:
    for _fid in _m.FORMULA_IDS:
        FORMULA_REGISTRY[_fid] = getattr(_m, _fid)

FORMULA_METADATA_REGISTRY = RUNTIME_FORMULA_REGISTRY

__all__ = [
    "DOMAINS", "all_formulas", "count_summary", "FormulaResult",
    "FORMULA_REGISTRY", "FORMULA_METADATA_REGISTRY",
] + list(FORMULA_REGISTRY.keys())
