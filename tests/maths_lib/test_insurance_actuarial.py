import pytest

import maths_lib as ml

FORMULA_IDS = ['loss_ratio', 'expense_ratio_ins', 'combined_ratio_ins', 'claim_frequency', 'claim_severity', 'actuarial_metric_1', 'actuarial_metric_2', 'actuarial_metric_3', 'actuarial_metric_4', 'actuarial_metric_5', 'actuarial_metric_6', 'actuarial_metric_7', 'actuarial_metric_8', 'actuarial_metric_9', 'actuarial_metric_10', 'actuarial_metric_11', 'actuarial_metric_12', 'actuarial_metric_13', 'actuarial_metric_14', 'actuarial_metric_15', 'actuarial_metric_16', 'actuarial_metric_17', 'actuarial_metric_18', 'actuarial_metric_19', 'actuarial_metric_20', 'actuarial_metric_21', 'actuarial_metric_22', 'actuarial_metric_23', 'actuarial_metric_24', 'actuarial_metric_25', 'actuarial_metric_26', 'actuarial_metric_27', 'actuarial_metric_28', 'actuarial_metric_29', 'actuarial_metric_30', 'actuarial_metric_31', 'actuarial_metric_32', 'actuarial_metric_33', 'actuarial_metric_34', 'actuarial_metric_35', 'actuarial_metric_36', 'actuarial_metric_37', 'actuarial_metric_38', 'actuarial_metric_39', 'actuarial_metric_40', 'actuarial_metric_41', 'actuarial_metric_42', 'actuarial_metric_43', 'actuarial_metric_44', 'actuarial_metric_45', 'actuarial_metric_46', 'actuarial_metric_47', 'actuarial_metric_48', 'actuarial_metric_49', 'actuarial_metric_50']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_insurance_actuarial_count_matches_registry():
    m = __import__(f"maths_lib.insurance_actuarial", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 55


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_insurance_actuarial_all_formulas_execute_deterministically(fid):
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
