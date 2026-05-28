import pytest

import maths_lib as ml

FORMULA_IDS = ['conversion_rate', 'retention_rate', 'churn_rate', 'customer_lifetime_value', 'cac', 'cac_payback_period', 'net_promoter_score', 'market_share', 'wallet_share', 'funnel_conversion', 'active_user_ratio', 'engagement_rate', 'bounce_rate', 'cohort_retention', 'linear_forecast', 'seasonal_index', 'weighted_moving_forecast', 'forecast_bias', 'tracking_signal', 'mean_absolute_deviation', 'exponential_smoothing_forecast', 'expected_monetary_value', 'value_of_information', 'decision_tree_value', 'regret_value', 'sensitivity_elasticity', 'breakeven_units_ba', 'roi_business', 'tam_sam_som', 'price_elasticity_demand', 'cross_price_elasticity', 'income_elasticity', 'economic_order_quantity', 'reorder_point', 'safety_stock', 'capacity_utilization', 'learning_curve', 'gmv', 'take_rate', 'average_order_value', 'repeat_purchase_rate', 'attribution_linear', 'roi_marketing', 'roas', 'ltv_cac_payback', 'cash_runway_months', 'weighted_pipeline', 'win_rate', 'market_growth_rate']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_business_analyst_count_matches_registry():
    m = __import__(f"maths_lib.business_analyst", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 49


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_business_analyst_all_formulas_execute_deterministically(fid):
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
