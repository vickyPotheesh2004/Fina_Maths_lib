import pytest

import maths_lib as ml

FORMULA_IDS = ['tracking_error_ex_ante', 'information_ratio_ex_ante', 'factor_marginal_var', 'factor_component_var', 'factor_contribution_risk', 'factor_signal_1', 'factor_signal_2', 'factor_signal_3', 'factor_signal_4', 'factor_signal_5', 'factor_signal_6', 'factor_signal_7', 'factor_signal_8', 'factor_signal_9', 'factor_signal_10', 'factor_signal_11', 'factor_signal_12', 'factor_signal_13', 'factor_signal_14', 'factor_signal_15', 'factor_signal_16', 'factor_signal_17', 'factor_signal_18', 'factor_signal_19', 'factor_signal_20', 'factor_signal_21', 'factor_signal_22', 'factor_signal_23', 'factor_signal_24', 'factor_signal_25', 'factor_signal_26', 'factor_signal_27', 'factor_signal_28', 'factor_signal_29', 'factor_signal_30', 'factor_signal_31', 'factor_signal_32', 'factor_signal_33', 'factor_signal_34', 'factor_signal_35', 'factor_signal_36', 'factor_signal_37', 'factor_signal_38', 'factor_signal_39', 'factor_signal_40', 'factor_signal_41', 'factor_signal_42', 'factor_signal_43', 'factor_signal_44', 'factor_signal_45', 'factor_signal_46', 'factor_signal_47', 'factor_signal_48', 'factor_signal_49', 'factor_signal_50', 'factor_signal_51', 'factor_signal_52', 'factor_signal_53', 'factor_signal_54', 'factor_signal_55']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_factor_risk_count_matches_registry():
    m = __import__(f"maths_lib.factor_risk", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 60


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_factor_risk_all_formulas_execute_deterministically(fid):
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
