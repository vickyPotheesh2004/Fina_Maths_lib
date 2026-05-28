import pytest

import maths_lib as ml

FORMULA_IDS = ['current_ratio', 'quick_ratio', 'cash_ratio', 'operating_cash_flow_ratio', 'working_capital', 'working_capital_ratio', 'net_working_capital_to_sales', 'defensive_interval_ratio', 'debt_to_equity', 'debt_to_assets', 'debt_to_capital', 'debt_to_ebitda', 'net_debt', 'net_debt_to_ebitda', 'equity_ratio', 'financial_leverage_ratio', 'interest_coverage', 'ebitda_coverage', 'fixed_charge_coverage', 'times_interest_earned', 'debt_service_coverage', 'cash_flow_to_debt', 'capitalization_ratio', 'asset_turnover', 'fixed_asset_turnover', 'inventory_turnover', 'receivables_turnover', 'payables_turnover', 'working_capital_turnover', 'equity_turnover', 'total_capital_turnover', 'days_sales_outstanding', 'days_inventory_outstanding', 'days_payable_outstanding', 'cash_conversion_cycle', 'operating_cycle', 'dso_direct', 'dio_direct', 'dpo_direct', 'capital_intensity', 'capital_intensity_assets', 'fixed_assets_to_equity', 'long_term_debt_to_equity', 'short_term_debt_ratio', 'current_liabilities_ratio', 'solvency_ratio', 'financial_autonomy_ratio', 'net_gearing', 'altman_z_score', 'piotroski_f_score']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_liquidity_solvency_count_matches_registry():
    m = __import__(f"maths_lib.liquidity_solvency", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 50


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_liquidity_solvency_all_formulas_execute_deterministically(fid):
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
