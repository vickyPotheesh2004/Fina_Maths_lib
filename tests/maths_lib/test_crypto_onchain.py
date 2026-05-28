import pytest

import maths_lib as ml

FORMULA_IDS = ['realized_cap', 'mvrv_ratio', 'nvt_ratio', 'sopr', 'hash_price', 'crypto_signal_1', 'crypto_signal_2', 'crypto_signal_3', 'crypto_signal_4', 'crypto_signal_5', 'crypto_signal_6', 'crypto_signal_7', 'crypto_signal_8', 'crypto_signal_9', 'crypto_signal_10', 'crypto_signal_11', 'crypto_signal_12', 'crypto_signal_13', 'crypto_signal_14', 'crypto_signal_15', 'crypto_signal_16', 'crypto_signal_17', 'crypto_signal_18', 'crypto_signal_19', 'crypto_signal_20', 'crypto_signal_21', 'crypto_signal_22', 'crypto_signal_23', 'crypto_signal_24', 'crypto_signal_25', 'crypto_signal_26', 'crypto_signal_27', 'crypto_signal_28', 'crypto_signal_29', 'crypto_signal_30', 'crypto_signal_31', 'crypto_signal_32', 'crypto_signal_33', 'crypto_signal_34', 'crypto_signal_35', 'crypto_signal_36', 'crypto_signal_37', 'crypto_signal_38', 'crypto_signal_39', 'crypto_signal_40', 'crypto_signal_41', 'crypto_signal_42', 'crypto_signal_43', 'crypto_signal_44', 'crypto_signal_45', 'crypto_signal_46', 'crypto_signal_47', 'crypto_signal_48', 'crypto_signal_49', 'crypto_signal_50', 'crypto_signal_51', 'crypto_signal_52', 'crypto_signal_53', 'crypto_signal_54', 'crypto_signal_55']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_crypto_onchain_count_matches_registry():
    m = __import__(f"maths_lib.crypto_onchain", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 60


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_crypto_onchain_all_formulas_execute_deterministically(fid):
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
