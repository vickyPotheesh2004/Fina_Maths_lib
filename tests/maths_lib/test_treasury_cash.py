import pytest

import maths_lib as ml

FORMULA_IDS = ['cash_conversion_efficiency', 'liquidity_buffer_ratio', 'cash_yield_treasury', 'funding_gap', 'revolver_utilization', 'treasury_metric_1', 'treasury_metric_2', 'treasury_metric_3', 'treasury_metric_4', 'treasury_metric_5', 'treasury_metric_6', 'treasury_metric_7', 'treasury_metric_8', 'treasury_metric_9', 'treasury_metric_10', 'treasury_metric_11', 'treasury_metric_12', 'treasury_metric_13', 'treasury_metric_14', 'treasury_metric_15', 'treasury_metric_16', 'treasury_metric_17', 'treasury_metric_18', 'treasury_metric_19', 'treasury_metric_20', 'treasury_metric_21', 'treasury_metric_22', 'treasury_metric_23', 'treasury_metric_24', 'treasury_metric_25', 'treasury_metric_26', 'treasury_metric_27', 'treasury_metric_28', 'treasury_metric_29', 'treasury_metric_30', 'treasury_metric_31', 'treasury_metric_32', 'treasury_metric_33', 'treasury_metric_34', 'treasury_metric_35', 'treasury_metric_36', 'treasury_metric_37', 'treasury_metric_38', 'treasury_metric_39', 'treasury_metric_40', 'treasury_metric_41', 'treasury_metric_42', 'treasury_metric_43', 'treasury_metric_44', 'treasury_metric_45', 'treasury_metric_46', 'treasury_metric_47', 'treasury_metric_48', 'treasury_metric_49', 'treasury_metric_50']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_treasury_cash_count_matches_registry():
    m = __import__(f"maths_lib.treasury_cash", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 55


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_treasury_cash_all_formulas_execute_deterministically(fid):
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
