import pytest

import maths_lib as ml

FORMULA_IDS = ['delta_approx', 'gamma_approx', 'vega_approx', 'theta_approx', 'rho_approx', 'vol_surface_metric_1', 'vol_surface_metric_2', 'vol_surface_metric_3', 'vol_surface_metric_4', 'vol_surface_metric_5', 'vol_surface_metric_6', 'vol_surface_metric_7', 'vol_surface_metric_8', 'vol_surface_metric_9', 'vol_surface_metric_10', 'vol_surface_metric_11', 'vol_surface_metric_12', 'vol_surface_metric_13', 'vol_surface_metric_14', 'vol_surface_metric_15', 'vol_surface_metric_16', 'vol_surface_metric_17', 'vol_surface_metric_18', 'vol_surface_metric_19', 'vol_surface_metric_20', 'vol_surface_metric_21', 'vol_surface_metric_22', 'vol_surface_metric_23', 'vol_surface_metric_24', 'vol_surface_metric_25', 'vol_surface_metric_26', 'vol_surface_metric_27', 'vol_surface_metric_28', 'vol_surface_metric_29', 'vol_surface_metric_30', 'vol_surface_metric_31', 'vol_surface_metric_32', 'vol_surface_metric_33', 'vol_surface_metric_34', 'vol_surface_metric_35', 'vol_surface_metric_36', 'vol_surface_metric_37', 'vol_surface_metric_38', 'vol_surface_metric_39', 'vol_surface_metric_40', 'vol_surface_metric_41', 'vol_surface_metric_42', 'vol_surface_metric_43', 'vol_surface_metric_44', 'vol_surface_metric_45', 'vol_surface_metric_46', 'vol_surface_metric_47', 'vol_surface_metric_48', 'vol_surface_metric_49', 'vol_surface_metric_50', 'vol_surface_metric_51', 'vol_surface_metric_52', 'vol_surface_metric_53', 'vol_surface_metric_54', 'vol_surface_metric_55']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_derivatives_greeks_count_matches_registry():
    m = __import__(f"maths_lib.derivatives_greeks", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 60


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_derivatives_greeks_all_formulas_execute_deterministically(fid):
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
