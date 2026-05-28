import pytest

import maths_lib as ml

FORMULA_IDS = ['expected_credit_loss', 'unexpected_loss', 'hazard_rate_credit', 'recovery_rate', 'credit_spread_simple', 'credit_metric_1', 'credit_metric_2', 'credit_metric_3', 'credit_metric_4', 'credit_metric_5', 'credit_metric_6', 'credit_metric_7', 'credit_metric_8', 'credit_metric_9', 'credit_metric_10', 'credit_metric_11', 'credit_metric_12', 'credit_metric_13', 'credit_metric_14', 'credit_metric_15', 'credit_metric_16', 'credit_metric_17', 'credit_metric_18', 'credit_metric_19', 'credit_metric_20', 'credit_metric_21', 'credit_metric_22', 'credit_metric_23', 'credit_metric_24', 'credit_metric_25', 'credit_metric_26', 'credit_metric_27', 'credit_metric_28', 'credit_metric_29', 'credit_metric_30', 'credit_metric_31', 'credit_metric_32', 'credit_metric_33', 'credit_metric_34', 'credit_metric_35', 'credit_metric_36', 'credit_metric_37', 'credit_metric_38', 'credit_metric_39', 'credit_metric_40', 'credit_metric_41', 'credit_metric_42', 'credit_metric_43', 'credit_metric_44', 'credit_metric_45', 'credit_metric_46', 'credit_metric_47', 'credit_metric_48', 'credit_metric_49', 'credit_metric_50', 'credit_metric_51', 'credit_metric_52', 'credit_metric_53', 'credit_metric_54', 'credit_metric_55']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_credit_risk_count_matches_registry():
    m = __import__(f"maths_lib.credit_risk", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 60


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_credit_risk_all_formulas_execute_deterministically(fid):
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
