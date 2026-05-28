import pytest

import maths_lib as ml

FORMULA_IDS = ['mae_forecast', 'mse_forecast', 'rmse_forecast', 'mape_forecast', 'wape_forecast', 'ts_component_1', 'ts_component_2', 'ts_component_3', 'ts_component_4', 'ts_component_5', 'ts_component_6', 'ts_component_7', 'ts_component_8', 'ts_component_9', 'ts_component_10', 'ts_component_11', 'ts_component_12', 'ts_component_13', 'ts_component_14', 'ts_component_15', 'ts_component_16', 'ts_component_17', 'ts_component_18', 'ts_component_19', 'ts_component_20', 'ts_component_21', 'ts_component_22', 'ts_component_23', 'ts_component_24', 'ts_component_25', 'ts_component_26', 'ts_component_27', 'ts_component_28', 'ts_component_29', 'ts_component_30', 'ts_component_31', 'ts_component_32', 'ts_component_33', 'ts_component_34', 'ts_component_35', 'ts_component_36', 'ts_component_37', 'ts_component_38', 'ts_component_39', 'ts_component_40', 'ts_component_41', 'ts_component_42', 'ts_component_43', 'ts_component_44', 'ts_component_45', 'ts_component_46', 'ts_component_47', 'ts_component_48', 'ts_component_49', 'ts_component_50', 'ts_component_51', 'ts_component_52', 'ts_component_53', 'ts_component_54', 'ts_component_55']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_forecasting_ts_count_matches_registry():
    m = __import__(f"maths_lib.forecasting_ts", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 60


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_forecasting_ts_all_formulas_execute_deterministically(fid):
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
