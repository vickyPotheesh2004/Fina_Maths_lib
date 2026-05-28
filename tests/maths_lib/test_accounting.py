import pytest

import maths_lib as ml

FORMULA_IDS = ['straight_line_depreciation', 'declining_balance', 'double_declining_balance', 'units_of_production', 'sum_of_years_digits', 'macrs_depreciation', 'accumulated_depreciation', 'book_value_asset', 'depreciation_rate', 'amortization_intangible', 'depletion', 'fifo_cogs', 'lifo_cogs', 'weighted_average_cost', 'lifo_reserve', 'inventory_write_down', 'ending_inventory', 'cogs_calculation', 'gross_profit_method', 'bad_debt_percentage_sales', 'bad_debt_aging', 'allowance_doubtful_accounts', 'net_realizable_value', 'deferred_tax_liability', 'deferred_tax_asset', 'effective_tax_rate_acct', 'stock_compensation_expense', 'pension_pbo', 'pension_funded_status', 'pension_expense', 'operating_lease_expense', 'finance_lease_liability', 'right_of_use_asset', 'capitalized_interest', 'revenue_recognition_percentage', 'deferred_revenue', 'comprehensive_income', 'retained_earnings_ending', 'goodwill_impairment', 'asset_impairment']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_accounting_count_matches_registry():
    m = __import__(f"maths_lib.accounting", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 40


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_accounting_all_formulas_execute_deterministically(fid):
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
