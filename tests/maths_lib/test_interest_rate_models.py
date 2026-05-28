import pytest

import maths_lib as ml

FORMULA_IDS = ['forward_rate_from_spot', 'par_swap_rate', 'ir_zero_coupon_price', 'duration_approx', 'convexity_approx', 'ir_curve_factor_1', 'ir_curve_factor_2', 'ir_curve_factor_3', 'ir_curve_factor_4', 'ir_curve_factor_5', 'ir_curve_factor_6', 'ir_curve_factor_7', 'ir_curve_factor_8', 'ir_curve_factor_9', 'ir_curve_factor_10', 'ir_curve_factor_11', 'ir_curve_factor_12', 'ir_curve_factor_13', 'ir_curve_factor_14', 'ir_curve_factor_15', 'ir_curve_factor_16', 'ir_curve_factor_17', 'ir_curve_factor_18', 'ir_curve_factor_19', 'ir_curve_factor_20', 'ir_curve_factor_21', 'ir_curve_factor_22', 'ir_curve_factor_23', 'ir_curve_factor_24', 'ir_curve_factor_25', 'ir_curve_factor_26', 'ir_curve_factor_27', 'ir_curve_factor_28', 'ir_curve_factor_29', 'ir_curve_factor_30', 'ir_curve_factor_31', 'ir_curve_factor_32', 'ir_curve_factor_33', 'ir_curve_factor_34', 'ir_curve_factor_35', 'ir_curve_factor_36', 'ir_curve_factor_37', 'ir_curve_factor_38', 'ir_curve_factor_39', 'ir_curve_factor_40', 'ir_curve_factor_41', 'ir_curve_factor_42', 'ir_curve_factor_43', 'ir_curve_factor_44', 'ir_curve_factor_45', 'ir_curve_factor_46', 'ir_curve_factor_47', 'ir_curve_factor_48', 'ir_curve_factor_49', 'ir_curve_factor_50', 'ir_curve_factor_51', 'ir_curve_factor_52', 'ir_curve_factor_53', 'ir_curve_factor_54', 'ir_curve_factor_55']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_interest_rate_models_count_matches_registry():
    m = __import__(f"maths_lib.interest_rate_models", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 60


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_interest_rate_models_all_formulas_execute_deterministically(fid):
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
