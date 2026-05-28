import pytest

import maths_lib as ml

FORMULA_IDS = ['yoy_change_absolute', 'yoy_change_pct', 'sequential_growth', 'ttm', 'ttm_rolling', 'quarter_annualized', 'monthly_annualized', 'percentage_point_change', 'compound_quarterly', 'constant_currency_growth', 'organic_growth', 'inorganic_growth', 'two_year_stack', 'multi_year_cagr', 'multi_year_average', 'dividend_growth_rate', 'revenue_run_rate', 'segment_growth', 'segment_margin', 'segment_revenue_share', 'segment_contribution', 'mix_shift', 'geographic_concentration', 'customer_concentration', 'herfindahl_index', 'weighted_segment_growth', 'beneish_m_score', 'sloan_ratio', 'accruals_ratio_bs', 'accruals_ratio_cf', 'cash_conversion', 'fcf_conversion', 'earnings_quality_ratio', 'adjusted_ebitda', 'normalized_earnings', 'days_cash_on_hand', 'net_working_capital_change', 'capex_to_depreciation', 'maintenance_capex_estimate', 'growth_capex', 'incremental_roic', 'cfroi', 'buyback_yield', 'total_payout_ratio', 'total_yield', 'effective_interest_rate', 'weighted_avg_cost_debt', 'arpu', 'net_revenue_retention', 'ltv_cac_ratio']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_growth_segment_forensic_count_matches_registry():
    m = __import__(f"maths_lib.growth_segment_forensic", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 50


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_growth_segment_forensic_all_formulas_execute_deterministically(fid):
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
