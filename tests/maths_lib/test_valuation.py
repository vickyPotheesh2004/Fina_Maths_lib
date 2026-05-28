import pytest

import maths_lib as ml

FORMULA_IDS = ['pe_ratio', 'forward_pe', 'peg_ratio', 'pb_ratio', 'ps_ratio', 'pcf_ratio', 'p_fcf_ratio', 'ev', 'ev_ebitda', 'ev_ebit', 'ev_sales', 'ev_fcf', 'dividend_yield', 'dividend_payout_ratio', 'retention_ratio', 'book_value_per_share', 'tangible_book_value', 'tangible_book_per_share', 'market_cap', 'earnings_yield', 'fcf_yield', 'dcf_value', 'dcf_two_stage', 'terminal_value_gordon', 'terminal_value_exit', 'gordon_growth_model', 'ddm_multistage', 'fcff', 'fcfe', 'fcf_simple', 'wacc', 'cost_of_equity_capm', 'cost_of_equity_ddm', 'cost_of_debt', 'capm', 'fama_french_3', 'fama_french_5', 'residual_income', 'eva', 'mva', 'justified_pe', 'justified_pb', 'graham_number', 'sum_of_parts', 'net_asset_value', 'liquidation_value', 'replacement_value', 'price_to_tangible_book', 'ev_to_invested_capital', 'dividend_per_share', 'dividend_coverage', 'total_shareholder_return', 'implied_growth_rate', 'ev_per_share', 'price_to_nav', 'cape_ratio', 'rule_of_40', 'magic_formula_yield', 'owners_earnings', 'intrinsic_value_growth']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_valuation_count_matches_registry():
    m = __import__(f"maths_lib.valuation", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 60


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_valuation_all_formulas_execute_deterministically(fid):
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
