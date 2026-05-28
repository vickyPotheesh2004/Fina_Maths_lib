import pytest

import maths_lib as ml

FORMULA_IDS = ['objective_value_lp', 'slack_value', 'utilization_ratio_ops', 'throughput_rate', 'queue_wait_estimate', 'ops_score_1', 'ops_score_2', 'ops_score_3', 'ops_score_4', 'ops_score_5', 'ops_score_6', 'ops_score_7', 'ops_score_8', 'ops_score_9', 'ops_score_10', 'ops_score_11', 'ops_score_12', 'ops_score_13', 'ops_score_14', 'ops_score_15', 'ops_score_16', 'ops_score_17', 'ops_score_18', 'ops_score_19', 'ops_score_20', 'ops_score_21', 'ops_score_22', 'ops_score_23', 'ops_score_24', 'ops_score_25', 'ops_score_26', 'ops_score_27', 'ops_score_28', 'ops_score_29', 'ops_score_30', 'ops_score_31', 'ops_score_32', 'ops_score_33', 'ops_score_34', 'ops_score_35', 'ops_score_36', 'ops_score_37', 'ops_score_38', 'ops_score_39', 'ops_score_40', 'ops_score_41', 'ops_score_42', 'ops_score_43', 'ops_score_44', 'ops_score_45', 'ops_score_46', 'ops_score_47', 'ops_score_48', 'ops_score_49', 'ops_score_50', 'ops_score_51', 'ops_score_52', 'ops_score_53', 'ops_score_54', 'ops_score_55']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_optimization_ops_count_matches_registry():
    m = __import__(f"maths_lib.optimization_ops", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 60


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_optimization_ops_all_formulas_execute_deterministically(fid):
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
