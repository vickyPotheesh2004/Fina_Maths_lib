import pytest

import maths_lib as ml

FORMULA_IDS = ['sustainable_growth_rate', 'internal_growth_rate', 'plowback_ratio', 'roic', 'invested_capital', 'economic_profit', 'hamada_equation', 'unlever_beta', 'relever_beta', 'mm_proposition1_no_tax', 'mm_proposition1_tax', 'mm_proposition2', 'tax_shield', 'interest_tax_shield_annual', 'degree_total_leverage', 'free_cash_flow_firm', 'free_cash_flow_equity', 'cash_flow_available_debt', 'accretion_dilution', 'exchange_ratio', 'acquisition_premium', 'synergy_value', 'goodwill', 'purchase_price_allocation', 'pro_forma_eps', 'breakeven_synergies', 'lbo_equity_return', 'lbo_irr', 'debt_paydown', 'entry_multiple', 'exit_multiple', 'sources_uses_balance', 'net_borrowing', 'dividend_discount_value', 'clientele_effect', 'share_buyback_eps_impact', 'treasury_stock_method', 'weighted_avg_shares', 'capital_structure_weight_equity', 'capital_structure_weight_debt', 'operating_working_capital', 'invested_capital_turnover', 'reinvestment_rate', 'expected_growth_fundamentals', 'terminal_growth_implied', 'equity_value_from_ev', 'net_debt_to_equity_value', 'dilution_percentage', 'control_premium', 'minority_interest_value']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_corporate_ma_count_matches_registry():
    m = __import__(f"maths_lib.corporate_ma", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 50


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_corporate_ma_all_formulas_execute_deterministically(fid):
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
