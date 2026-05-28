import pytest

import maths_lib as ml

FORMULA_IDS = ['present_value', 'future_value', 'npv', 'irr', 'mirr', 'xirr', 'pv_annuity', 'fv_annuity', 'pv_annuity_due', 'fv_annuity_due', 'perpetuity', 'growing_perpetuity', 'growing_annuity_pv', 'annuity_payment', 'loan_payment', 'loan_balance', 'amortization_interest', 'amortization_principal', 'effective_annual_rate', 'nominal_rate', 'continuous_compounding', 'continuous_pv', 'rule_of_72', 'rule_of_69', 'payback_period', 'discounted_payback', 'profitability_index', 'equivalent_annual_cost', 'equivalent_annual_annuity', 'crossover_rate', 'real_rate', 'fisher_equation', 'annuity_factor', 'future_value_factor', 'present_value_factor', 'sinking_fund', 'capital_recovery_factor', 'deferred_annuity_pv', 'net_future_value', 'modified_payback', 'accounting_rate_of_return', 'bcr', 'annualized_return', 'holding_period_yield', 'breakeven_interest_rate']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_tvm_count_matches_registry():
    m = __import__(f"maths_lib.tvm", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 45


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_tvm_all_formulas_execute_deterministically(fid):
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
