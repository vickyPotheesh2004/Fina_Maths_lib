import pytest

import maths_lib as ml

FORMULA_IDS = ['var_historical', 'var_parametric', 'var_monte_carlo', 'cvar', 'expected_shortfall', 'sharpe_ratio', 'sortino_ratio', 'treynor_ratio', 'information_ratio', 'jensens_alpha', 'calmar_ratio', 'sterling_ratio', 'max_drawdown', 'drawdown_duration', 'beta', 'alpha', 'tracking_error', 'downside_deviation', 'semi_variance', 'covariance', 'correlation', 'portfolio_return', 'portfolio_variance', 'portfolio_std', 'portfolio_beta', 'minimum_variance_weight', 'efficient_frontier_return', 'capital_allocation_line', 'capital_market_line', 'security_market_line', 'diversification_ratio', 'risk_parity_weight', 'marginal_var', 'component_var', 'incremental_var', 'ulcer_index', 'gain_to_pain', 'omega_ratio', 'kappa_ratio', 'upside_potential_ratio', 'value_at_risk_normal', 'conditional_drawdown', 'pain_index', 'burke_ratio', 'm2_measure', 'active_premium', 'hurst_exponent', 'kelly_criterion', 'risk_of_ruin', 'expected_value']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_risk_count_matches_registry():
    m = __import__(f"maths_lib.risk", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 50


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_risk_all_formulas_execute_deterministically(fid):
    fn = ml.FORMULA_REGISTRY[fid]
    kwargs = _inputs_for(fid)
    r1 = fn(**kwargs)
    r2 = fn(**kwargs)
    assert r1.formula_id == fid
    assert r1.formula_name
    assert r1.expression
    assert r1.domain
    assert r1.inputs_used == kwargs
    assert r1.value == r2.value
    assert r1.valid == r2.valid
