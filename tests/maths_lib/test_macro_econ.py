import pytest

import maths_lib as ml

FORMULA_IDS = ['real_gdp_growth', 'output_gap', 'fiscal_deficit_ratio', 'debt_to_gdp_macro', 'real_policy_rate', 'macro_signal_1', 'macro_signal_2', 'macro_signal_3', 'macro_signal_4', 'macro_signal_5', 'macro_signal_6', 'macro_signal_7', 'macro_signal_8', 'macro_signal_9', 'macro_signal_10', 'macro_signal_11', 'macro_signal_12', 'macro_signal_13', 'macro_signal_14', 'macro_signal_15', 'macro_signal_16', 'macro_signal_17', 'macro_signal_18', 'macro_signal_19', 'macro_signal_20', 'macro_signal_21', 'macro_signal_22', 'macro_signal_23', 'macro_signal_24', 'macro_signal_25', 'macro_signal_26', 'macro_signal_27', 'macro_signal_28', 'macro_signal_29', 'macro_signal_30', 'macro_signal_31', 'macro_signal_32', 'macro_signal_33', 'macro_signal_34', 'macro_signal_35', 'macro_signal_36', 'macro_signal_37', 'macro_signal_38', 'macro_signal_39', 'macro_signal_40', 'macro_signal_41', 'macro_signal_42', 'macro_signal_43', 'macro_signal_44', 'macro_signal_45', 'macro_signal_46', 'macro_signal_47', 'macro_signal_48', 'macro_signal_49', 'macro_signal_50', 'macro_signal_51', 'macro_signal_52', 'macro_signal_53', 'macro_signal_54', 'macro_signal_55']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_macro_econ_count_matches_registry():
    m = __import__(f"maths_lib.macro_econ", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 60


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_macro_econ_all_formulas_execute_deterministically(fid):
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
