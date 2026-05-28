import pytest

import maths_lib as ml

FORMULA_IDS = ['gross_margin', 'gross_profit', 'operating_margin', 'net_margin', 'ebitda_margin', 'ebit_margin', 'pretax_margin', 'contribution_margin', 'contribution_margin_ratio', 'fcf_margin', 'ocf_margin', 'return_on_equity', 'return_on_assets', 'return_on_invested_capital', 'return_on_capital_employed', 'return_on_sales', 'return_on_tangible_equity', 'return_on_net_assets', 'nopat', 'ebitda', 'ebit', 'effective_tax_rate', 'operating_leverage', 'financial_leverage', 'combined_leverage', 'dupont_roe_3step', 'dupont_roe_5step', 'tax_burden', 'interest_burden', 'equity_multiplier', 'operating_ratio', 'cost_of_revenue_ratio', 'overhead_ratio', 'sga_ratio', 'rnd_ratio', 'rnd_intensity', 'net_income_growth', 'revenue_growth', 'operating_income_growth', 'eps_basic', 'eps_diluted', 'eps_growth', 'cash_return_on_assets', 'cash_roe', 'gross_profit_growth', 'ebitda_growth', 'incremental_margin', 'breakeven_point_units', 'breakeven_point_revenue', 'margin_of_safety']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_profitability_count_matches_registry():
    m = __import__(f"maths_lib.profitability", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 50


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_profitability_all_formulas_execute_deterministically(fid):
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
