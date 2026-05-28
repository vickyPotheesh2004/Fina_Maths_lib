import pytest

import maths_lib as ml

FORMULA_IDS = ['bond_price', 'bond_price_clean', 'bond_price_dirty', 'accrued_interest', 'ytm', 'ytc', 'ytw', 'current_yield', 'coupon_rate', 'macaulay_duration', 'modified_duration', 'effective_duration', 'dollar_duration', 'convexity', 'effective_convexity', 'dv01', 'price_change_duration', 'price_change_convexity', 'spot_rate', 'forward_rate', 'par_yield', 'zero_coupon_price', 'discount_factor', 'bond_equivalent_yield', 'effective_annual_yield', 'holding_period_return', 'realized_compound_yield', 'z_spread', 'oas', 'nominal_spread', 'g_spread', 'i_spread', 'asset_swap_spread', 'credit_spread', 'yield_curve_slope', 'yield_curve_butterfly', 'key_rate_duration', 'portfolio_duration', 'portfolio_convexity', 'reinvestment_income', 'interest_on_interest', 'clean_to_invoice', 'bond_floor', 'conversion_value', 'conversion_premium', 'tips_principal', 'real_yield', 'breakeven_inflation', 'rolling_yield', 'expected_loss']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_fixed_income_count_matches_registry():
    m = __import__(f"maths_lib.fixed_income", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 50


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_fixed_income_all_formulas_execute_deterministically(fid):
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
