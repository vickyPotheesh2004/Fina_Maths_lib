import pytest

import maths_lib as ml

FORMULA_IDS = ['black_scholes_call', 'black_scholes_put', 'bs_d1', 'bs_d2', 'bsm_call_dividend', 'bsm_put_dividend', 'delta_call', 'delta_put', 'gamma', 'vega', 'theta_call', 'theta_put', 'rho_call', 'rho_put', 'vanna', 'charm', 'vomma', 'speed', 'binomial_call', 'binomial_put', 'trinomial_option', 'monte_carlo_option', 'implied_volatility', 'put_call_parity', 'intrinsic_value_call', 'intrinsic_value_put', 'time_value_option', 'forward_price', 'futures_price', 'forward_rate_agreement', 'swap_fixed_rate', 'swap_value', 'call_payoff', 'put_payoff', 'straddle_payoff', 'strangle_payoff', 'covered_call_return', 'collar_value', 'butterfly_payoff', 'delta_hedge_shares', 'option_leverage', 'breakeven_call', 'breakeven_put', 'max_pain', 'historical_var_option']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_options_count_matches_registry():
    m = __import__(f"maths_lib.options", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 45


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_options_all_formulas_execute_deterministically(fid):
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
