from .base import build_result, formula

DOMAIN_KEY = "D03_valuation"
DOMAIN_TITLE = "Valuation Metrics & Models"
FORMULA_IDS = [
    "pe_ratio",
    "forward_pe",
    "peg_ratio",
    "pb_ratio",
    "ps_ratio",
    "pcf_ratio",
    "p_fcf_ratio",
    "ev",
    "ev_ebitda",
    "ev_ebit",
    "ev_sales",
    "ev_fcf",
    "dividend_yield",
    "dividend_payout_ratio",
    "retention_ratio",
    "book_value_per_share",
    "tangible_book_value",
    "tangible_book_per_share",
    "market_cap",
    "earnings_yield",
    "fcf_yield",
    "dcf_value",
    "dcf_two_stage",
    "terminal_value_gordon",
    "terminal_value_exit",
    "gordon_growth_model",
    "ddm_multistage",
    "fcff",
    "fcfe",
    "fcf_simple",
    "wacc",
    "cost_of_equity_capm",
    "cost_of_equity_ddm",
    "cost_of_debt",
    "capm",
    "fama_french_3",
    "fama_french_5",
    "residual_income",
    "eva",
    "mva",
    "justified_pe",
    "justified_pb",
    "graham_number",
    "sum_of_parts",
    "net_asset_value",
    "liquidation_value",
    "replacement_value",
    "price_to_tangible_book",
    "ev_to_invested_capital",
    "dividend_per_share",
    "dividend_coverage",
    "total_shareholder_return",
    "implied_growth_rate",
    "ev_per_share",
    "price_to_nav",
    "cape_ratio",
    "rule_of_40",
    "magic_formula_yield",
    "owners_earnings",
    "intrinsic_value_growth",
]

@formula("pe_ratio", "Price-to-Earnings (P/E)", "Price / EPS", DOMAIN_KEY, unit="")
def pe_ratio(price: float | None = None, eps: float | None = None, **kwargs):
    return build_result(
        fid="pe_ratio",
        name="Price-to-Earnings (P/E)",
        expression="Price / EPS",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "price": kwargs.get("price", price),
            "eps": kwargs.get("eps", eps),
        },
    )

@formula("forward_pe", "Forward P/E", "Price / Forward_EPS", DOMAIN_KEY, unit="")
def forward_pe(price: float | None = None, forward_eps: float | None = None, **kwargs):
    return build_result(
        fid="forward_pe",
        name="Forward P/E",
        expression="Price / Forward_EPS",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "price": kwargs.get("price", price),
            "forward_eps": kwargs.get("forward_eps", forward_eps),
        },
    )

@formula("peg_ratio", "PEG Ratio", "PE_Ratio / Earnings_Growth_Rate", DOMAIN_KEY, unit="")
def peg_ratio(pe_ratio: float | None = None, earnings_growth_rate: float | None = None, **kwargs):
    return build_result(
        fid="peg_ratio",
        name="PEG Ratio",
        expression="PE_Ratio / Earnings_Growth_Rate",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "pe_ratio": kwargs.get("pe_ratio", pe_ratio),
            "earnings_growth_rate": kwargs.get("earnings_growth_rate", earnings_growth_rate),
        },
    )

@formula("pb_ratio", "Price-to-Book (P/B)", "Price / Book_Value_Per_Share", DOMAIN_KEY, unit="")
def pb_ratio(price: float | None = None, book_value_per_share: float | None = None, **kwargs):
    return build_result(
        fid="pb_ratio",
        name="Price-to-Book (P/B)",
        expression="Price / Book_Value_Per_Share",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "price": kwargs.get("price", price),
            "book_value_per_share": kwargs.get("book_value_per_share", book_value_per_share),
        },
    )

@formula("ps_ratio", "Price-to-Sales (P/S)", "Market_Cap / Revenue", DOMAIN_KEY, unit="")
def ps_ratio(market_cap: float | None = None, revenue: float | None = None, **kwargs):
    return build_result(
        fid="ps_ratio",
        name="Price-to-Sales (P/S)",
        expression="Market_Cap / Revenue",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "market_cap": kwargs.get("market_cap", market_cap),
            "revenue": kwargs.get("revenue", revenue),
        },
    )

@formula("pcf_ratio", "Price-to-Cash-Flow", "Price / Cash_Flow_Per_Share", DOMAIN_KEY, unit="")
def pcf_ratio(price: float | None = None, cash_flow_per_share: float | None = None, **kwargs):
    return build_result(
        fid="pcf_ratio",
        name="Price-to-Cash-Flow",
        expression="Price / Cash_Flow_Per_Share",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "price": kwargs.get("price", price),
            "cash_flow_per_share": kwargs.get("cash_flow_per_share", cash_flow_per_share),
        },
    )

@formula("p_fcf_ratio", "Price-to-Free-Cash-Flow", "Market_Cap / FCF", DOMAIN_KEY, unit="")
def p_fcf_ratio(market_cap: float | None = None, fcf: float | None = None, **kwargs):
    return build_result(
        fid="p_fcf_ratio",
        name="Price-to-Free-Cash-Flow",
        expression="Market_Cap / FCF",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "market_cap": kwargs.get("market_cap", market_cap),
            "fcf": kwargs.get("fcf", fcf),
        },
    )

@formula("ev", "Enterprise Value", "Market_Cap + Total_Debt - Cash", DOMAIN_KEY, unit="")
def ev(market_cap: float | None = None, total_debt: float | None = None, cash: float | None = None, **kwargs):
    return build_result(
        fid="ev",
        name="Enterprise Value",
        expression="Market_Cap + Total_Debt - Cash",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "market_cap": kwargs.get("market_cap", market_cap),
            "total_debt": kwargs.get("total_debt", total_debt),
            "cash": kwargs.get("cash", cash),
        },
    )

@formula("ev_ebitda", "EV/EBITDA", "EV / EBITDA", DOMAIN_KEY, unit="")
def ev_ebitda(ev: float | None = None, ebitda: float | None = None, **kwargs):
    return build_result(
        fid="ev_ebitda",
        name="EV/EBITDA",
        expression="EV / EBITDA",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ev": kwargs.get("ev", ev),
            "ebitda": kwargs.get("ebitda", ebitda),
        },
    )

@formula("ev_ebit", "EV/EBIT", "EV / EBIT", DOMAIN_KEY, unit="")
def ev_ebit(ev: float | None = None, ebit: float | None = None, **kwargs):
    return build_result(
        fid="ev_ebit",
        name="EV/EBIT",
        expression="EV / EBIT",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ev": kwargs.get("ev", ev),
            "ebit": kwargs.get("ebit", ebit),
        },
    )

@formula("ev_sales", "EV/Sales", "EV / Revenue", DOMAIN_KEY, unit="")
def ev_sales(ev: float | None = None, revenue: float | None = None, **kwargs):
    return build_result(
        fid="ev_sales",
        name="EV/Sales",
        expression="EV / Revenue",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ev": kwargs.get("ev", ev),
            "revenue": kwargs.get("revenue", revenue),
        },
    )

@formula("ev_fcf", "EV/FCF", "EV / FCF", DOMAIN_KEY, unit="")
def ev_fcf(ev: float | None = None, fcf: float | None = None, **kwargs):
    return build_result(
        fid="ev_fcf",
        name="EV/FCF",
        expression="EV / FCF",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ev": kwargs.get("ev", ev),
            "fcf": kwargs.get("fcf", fcf),
        },
    )

@formula("dividend_yield", "Dividend Yield %", "Annual_Dividend / Price * 100", DOMAIN_KEY, unit="")
def dividend_yield(annual_dividend: float | None = None, price: float | None = None, **kwargs):
    return build_result(
        fid="dividend_yield",
        name="Dividend Yield %",
        expression="Annual_Dividend / Price * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "annual_dividend": kwargs.get("annual_dividend", annual_dividend),
            "price": kwargs.get("price", price),
        },
    )

@formula("dividend_payout_ratio", "Dividend Payout Ratio %", "Dividends / Net_Income * 100", DOMAIN_KEY, unit="")
def dividend_payout_ratio(dividends: float | None = None, net_income: float | None = None, **kwargs):
    return build_result(
        fid="dividend_payout_ratio",
        name="Dividend Payout Ratio %",
        expression="Dividends / Net_Income * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "dividends": kwargs.get("dividends", dividends),
            "net_income": kwargs.get("net_income", net_income),
        },
    )

@formula("retention_ratio", "Retention Ratio %", "(1 - Payout_Ratio) * 100", DOMAIN_KEY, unit="")
def retention_ratio(payout_ratio: float | None = None, **kwargs):
    return build_result(
        fid="retention_ratio",
        name="Retention Ratio %",
        expression="(1 - Payout_Ratio) * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "payout_ratio": kwargs.get("payout_ratio", payout_ratio),
        },
    )

@formula("book_value_per_share", "Book Value Per Share", "Shareholders_Equity / Shares_Outstanding", DOMAIN_KEY, unit="")
def book_value_per_share(shareholders_equity: float | None = None, shares_outstanding: float | None = None, **kwargs):
    return build_result(
        fid="book_value_per_share",
        name="Book Value Per Share",
        expression="Shareholders_Equity / Shares_Outstanding",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "shareholders_equity": kwargs.get("shareholders_equity", shareholders_equity),
            "shares_outstanding": kwargs.get("shares_outstanding", shares_outstanding),
        },
    )

@formula("tangible_book_value", "Tangible Book Value", "Shareholders_Equity - Intangibles - Goodwill", DOMAIN_KEY, unit="")
def tangible_book_value(shareholders_equity: float | None = None, intangibles: float | None = None, goodwill: float | None = None, **kwargs):
    return build_result(
        fid="tangible_book_value",
        name="Tangible Book Value",
        expression="Shareholders_Equity - Intangibles - Goodwill",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "shareholders_equity": kwargs.get("shareholders_equity", shareholders_equity),
            "intangibles": kwargs.get("intangibles", intangibles),
            "goodwill": kwargs.get("goodwill", goodwill),
        },
    )

@formula("tangible_book_per_share", "Tangible Book Value Per Share", "Tangible_Book_Value / Shares_Outstanding", DOMAIN_KEY, unit="")
def tangible_book_per_share(tangible_book_value: float | None = None, shares_outstanding: float | None = None, **kwargs):
    return build_result(
        fid="tangible_book_per_share",
        name="Tangible Book Value Per Share",
        expression="Tangible_Book_Value / Shares_Outstanding",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "tangible_book_value": kwargs.get("tangible_book_value", tangible_book_value),
            "shares_outstanding": kwargs.get("shares_outstanding", shares_outstanding),
        },
    )

@formula("market_cap", "Market Capitalization", "Price * Shares_Outstanding", DOMAIN_KEY, unit="")
def market_cap(price: float | None = None, shares_outstanding: float | None = None, **kwargs):
    return build_result(
        fid="market_cap",
        name="Market Capitalization",
        expression="Price * Shares_Outstanding",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "price": kwargs.get("price", price),
            "shares_outstanding": kwargs.get("shares_outstanding", shares_outstanding),
        },
    )

@formula("earnings_yield", "Earnings Yield %", "EPS / Price * 100", DOMAIN_KEY, unit="")
def earnings_yield(eps: float | None = None, price: float | None = None, **kwargs):
    return build_result(
        fid="earnings_yield",
        name="Earnings Yield %",
        expression="EPS / Price * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "eps": kwargs.get("eps", eps),
            "price": kwargs.get("price", price),
        },
    )

@formula("fcf_yield", "Free Cash Flow Yield %", "FCF_Per_Share / Price * 100", DOMAIN_KEY, unit="")
def fcf_yield(fcf_per_share: float | None = None, price: float | None = None, **kwargs):
    return build_result(
        fid="fcf_yield",
        name="Free Cash Flow Yield %",
        expression="FCF_Per_Share / Price * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "fcf_per_share": kwargs.get("fcf_per_share", fcf_per_share),
            "price": kwargs.get("price", price),
        },
    )

@formula("dcf_value", "DCF Present Value", "Sum(CF_t / (1+r)^t)", DOMAIN_KEY, unit="")
def dcf_value(cash_flows: float | None = None, discount_rate: float | None = None, **kwargs):
    return build_result(
        fid="dcf_value",
        name="DCF Present Value",
        expression="Sum(CF_t / (1+r)^t)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cash_flows": kwargs.get("cash_flows", cash_flows),
            "discount_rate": kwargs.get("discount_rate", discount_rate),
        },
    )

@formula("dcf_two_stage", "Two-Stage DCF", "Sum(CF_t/(1+r)^t) + TV/(1+r)^n", DOMAIN_KEY, unit="")
def dcf_two_stage(cash_flows: float | None = None, discount_rate: float | None = None, terminal_value: float | None = None, **kwargs):
    return build_result(
        fid="dcf_two_stage",
        name="Two-Stage DCF",
        expression="Sum(CF_t/(1+r)^t) + TV/(1+r)^n",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cash_flows": kwargs.get("cash_flows", cash_flows),
            "discount_rate": kwargs.get("discount_rate", discount_rate),
            "terminal_value": kwargs.get("terminal_value", terminal_value),
        },
    )

@formula("terminal_value_gordon", "Terminal Value (Gordon)", "FCF * (1 + g) / (r - g)", DOMAIN_KEY, unit="")
def terminal_value_gordon(fcf: float | None = None, growth_rate: float | None = None, discount_rate: float | None = None, **kwargs):
    return build_result(
        fid="terminal_value_gordon",
        name="Terminal Value (Gordon)",
        expression="FCF * (1 + g) / (r - g)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "fcf": kwargs.get("fcf", fcf),
            "growth_rate": kwargs.get("growth_rate", growth_rate),
            "discount_rate": kwargs.get("discount_rate", discount_rate),
        },
    )

@formula("terminal_value_exit", "Terminal Value (Exit Multiple)", "Final_EBITDA * Exit_Multiple", DOMAIN_KEY, unit="")
def terminal_value_exit(final_ebitda: float | None = None, exit_multiple: float | None = None, **kwargs):
    return build_result(
        fid="terminal_value_exit",
        name="Terminal Value (Exit Multiple)",
        expression="Final_EBITDA * Exit_Multiple",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "final_ebitda": kwargs.get("final_ebitda", final_ebitda),
            "exit_multiple": kwargs.get("exit_multiple", exit_multiple),
        },
    )

@formula("gordon_growth_model", "Gordon Growth Model (DDM)", "D1 / (Required_Return - Growth_Rate)", DOMAIN_KEY, unit="")
def gordon_growth_model(d1: float | None = None, required_return: float | None = None, growth_rate: float | None = None, **kwargs):
    return build_result(
        fid="gordon_growth_model",
        name="Gordon Growth Model (DDM)",
        expression="D1 / (Required_Return - Growth_Rate)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "d1": kwargs.get("d1", d1),
            "required_return": kwargs.get("required_return", required_return),
            "growth_rate": kwargs.get("growth_rate", growth_rate),
        },
    )

@formula("ddm_multistage", "Multi-Stage DDM", "Sum(D_t/(1+r)^t) + TV", DOMAIN_KEY, unit="")
def ddm_multistage(dividends: float | None = None, discount_rate: float | None = None, terminal_value: float | None = None, **kwargs):
    return build_result(
        fid="ddm_multistage",
        name="Multi-Stage DDM",
        expression="Sum(D_t/(1+r)^t) + TV",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "dividends": kwargs.get("dividends", dividends),
            "discount_rate": kwargs.get("discount_rate", discount_rate),
            "terminal_value": kwargs.get("terminal_value", terminal_value),
        },
    )

@formula("fcff", "Free Cash Flow to Firm", "EBIT*(1-Tax) + DA - CapEx - Delta_WC", DOMAIN_KEY, unit="")
def fcff(ebit: float | None = None, tax_rate: float | None = None, da: float | None = None, capex: float | None = None, delta_wc: float | None = None, **kwargs):
    return build_result(
        fid="fcff",
        name="Free Cash Flow to Firm",
        expression="EBIT*(1-Tax) + DA - CapEx - Delta_WC",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ebit": kwargs.get("ebit", ebit),
            "tax_rate": kwargs.get("tax_rate", tax_rate),
            "da": kwargs.get("da", da),
            "capex": kwargs.get("capex", capex),
            "delta_wc": kwargs.get("delta_wc", delta_wc),
        },
    )

@formula("fcfe", "Free Cash Flow to Equity", "FCFF - Interest*(1-Tax) + Net_Borrowing", DOMAIN_KEY, unit="")
def fcfe(fcff: float | None = None, interest: float | None = None, tax_rate: float | None = None, net_borrowing: float | None = None, **kwargs):
    return build_result(
        fid="fcfe",
        name="Free Cash Flow to Equity",
        expression="FCFF - Interest*(1-Tax) + Net_Borrowing",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "fcff": kwargs.get("fcff", fcff),
            "interest": kwargs.get("interest", interest),
            "tax_rate": kwargs.get("tax_rate", tax_rate),
            "net_borrowing": kwargs.get("net_borrowing", net_borrowing),
        },
    )

@formula("fcf_simple", "Free Cash Flow (Simple)", "OCF - CapEx", DOMAIN_KEY, unit="")
def fcf_simple(ocf: float | None = None, capex: float | None = None, **kwargs):
    return build_result(
        fid="fcf_simple",
        name="Free Cash Flow (Simple)",
        expression="OCF - CapEx",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ocf": kwargs.get("ocf", ocf),
            "capex": kwargs.get("capex", capex),
        },
    )

@formula("wacc", "Weighted Average Cost of Capital", "We*Re + Wd*Rd*(1-Tax)", DOMAIN_KEY, unit="")
def wacc(weight_equity: float | None = None, cost_equity: float | None = None, weight_debt: float | None = None, cost_debt: float | None = None, tax_rate: float | None = None, **kwargs):
    return build_result(
        fid="wacc",
        name="Weighted Average Cost of Capital",
        expression="We*Re + Wd*Rd*(1-Tax)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "weight_equity": kwargs.get("weight_equity", weight_equity),
            "cost_equity": kwargs.get("cost_equity", cost_equity),
            "weight_debt": kwargs.get("weight_debt", weight_debt),
            "cost_debt": kwargs.get("cost_debt", cost_debt),
            "tax_rate": kwargs.get("tax_rate", tax_rate),
        },
    )

@formula("cost_of_equity_capm", "Cost of Equity (CAPM)", "Rf + Beta * (Rm - Rf)", DOMAIN_KEY, unit="")
def cost_of_equity_capm(risk_free: float | None = None, beta: float | None = None, market_return: float | None = None, **kwargs):
    return build_result(
        fid="cost_of_equity_capm",
        name="Cost of Equity (CAPM)",
        expression="Rf + Beta * (Rm - Rf)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "risk_free": kwargs.get("risk_free", risk_free),
            "beta": kwargs.get("beta", beta),
            "market_return": kwargs.get("market_return", market_return),
        },
    )

@formula("cost_of_equity_ddm", "Cost of Equity (DDM)", "D1 / Price + Growth_Rate", DOMAIN_KEY, unit="")
def cost_of_equity_ddm(d1: float | None = None, price: float | None = None, growth_rate: float | None = None, **kwargs):
    return build_result(
        fid="cost_of_equity_ddm",
        name="Cost of Equity (DDM)",
        expression="D1 / Price + Growth_Rate",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "d1": kwargs.get("d1", d1),
            "price": kwargs.get("price", price),
            "growth_rate": kwargs.get("growth_rate", growth_rate),
        },
    )

@formula("cost_of_debt", "Cost of Debt (After-Tax)", "Interest_Rate * (1 - Tax_Rate)", DOMAIN_KEY, unit="")
def cost_of_debt(interest_rate: float | None = None, tax_rate: float | None = None, **kwargs):
    return build_result(
        fid="cost_of_debt",
        name="Cost of Debt (After-Tax)",
        expression="Interest_Rate * (1 - Tax_Rate)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "interest_rate": kwargs.get("interest_rate", interest_rate),
            "tax_rate": kwargs.get("tax_rate", tax_rate),
        },
    )

@formula("capm", "CAPM Expected Return", "Rf + Beta * (Rm - Rf)", DOMAIN_KEY, unit="")
def capm(risk_free: float | None = None, beta: float | None = None, market_return: float | None = None, **kwargs):
    return build_result(
        fid="capm",
        name="CAPM Expected Return",
        expression="Rf + Beta * (Rm - Rf)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "risk_free": kwargs.get("risk_free", risk_free),
            "beta": kwargs.get("beta", beta),
            "market_return": kwargs.get("market_return", market_return),
        },
    )

@formula("fama_french_3", "Fama-French 3-Factor", "Rf + b1*MKT + b2*SMB + b3*HML", DOMAIN_KEY, unit="")
def fama_french_3(risk_free: float | None = None, b1: float | None = None, mkt: float | None = None, b2: float | None = None, smb: float | None = None, b3: float | None = None, hml: float | None = None, **kwargs):
    return build_result(
        fid="fama_french_3",
        name="Fama-French 3-Factor",
        expression="Rf + b1*MKT + b2*SMB + b3*HML",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "risk_free": kwargs.get("risk_free", risk_free),
            "b1": kwargs.get("b1", b1),
            "mkt": kwargs.get("mkt", mkt),
            "b2": kwargs.get("b2", b2),
            "smb": kwargs.get("smb", smb),
            "b3": kwargs.get("b3", b3),
            "hml": kwargs.get("hml", hml),
        },
    )

@formula("fama_french_5", "Fama-French 5-Factor", "Rf + b1*MKT + b2*SMB + b3*HML + b4*RMW + b5*CMA", DOMAIN_KEY, unit="")
def fama_french_5(risk_free: float | None = None, betas: float | None = None, factors: float | None = None, **kwargs):
    return build_result(
        fid="fama_french_5",
        name="Fama-French 5-Factor",
        expression="Rf + b1*MKT + b2*SMB + b3*HML + b4*RMW + b5*CMA",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "risk_free": kwargs.get("risk_free", risk_free),
            "betas": kwargs.get("betas", betas),
            "factors": kwargs.get("factors", factors),
        },
    )

@formula("residual_income", "Residual Income", "Net_Income - (Equity * Cost_of_Equity)", DOMAIN_KEY, unit="")
def residual_income(net_income: float | None = None, equity: float | None = None, cost_of_equity: float | None = None, **kwargs):
    return build_result(
        fid="residual_income",
        name="Residual Income",
        expression="Net_Income - (Equity * Cost_of_Equity)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_income": kwargs.get("net_income", net_income),
            "equity": kwargs.get("equity", equity),
            "cost_of_equity": kwargs.get("cost_of_equity", cost_of_equity),
        },
    )

@formula("eva", "Economic Value Added", "NOPAT - (Invested_Capital * WACC)", DOMAIN_KEY, unit="")
def eva(nopat: float | None = None, invested_capital: float | None = None, wacc: float | None = None, **kwargs):
    return build_result(
        fid="eva",
        name="Economic Value Added",
        expression="NOPAT - (Invested_Capital * WACC)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "nopat": kwargs.get("nopat", nopat),
            "invested_capital": kwargs.get("invested_capital", invested_capital),
            "wacc": kwargs.get("wacc", wacc),
        },
    )

@formula("mva", "Market Value Added", "Market_Value - Invested_Capital", DOMAIN_KEY, unit="")
def mva(market_value: float | None = None, invested_capital: float | None = None, **kwargs):
    return build_result(
        fid="mva",
        name="Market Value Added",
        expression="Market_Value - Invested_Capital",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "market_value": kwargs.get("market_value", market_value),
            "invested_capital": kwargs.get("invested_capital", invested_capital),
        },
    )

@formula("justified_pe", "Justified P/E", "Payout * (1+g) / (r-g)", DOMAIN_KEY, unit="")
def justified_pe(payout: float | None = None, growth_rate: float | None = None, required_return: float | None = None, **kwargs):
    return build_result(
        fid="justified_pe",
        name="Justified P/E",
        expression="Payout * (1+g) / (r-g)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "payout": kwargs.get("payout", payout),
            "growth_rate": kwargs.get("growth_rate", growth_rate),
            "required_return": kwargs.get("required_return", required_return),
        },
    )

@formula("justified_pb", "Justified P/B", "(ROE - g) / (r - g)", DOMAIN_KEY, unit="")
def justified_pb(roe: float | None = None, growth_rate: float | None = None, required_return: float | None = None, **kwargs):
    return build_result(
        fid="justified_pb",
        name="Justified P/B",
        expression="(ROE - g) / (r - g)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "roe": kwargs.get("roe", roe),
            "growth_rate": kwargs.get("growth_rate", growth_rate),
            "required_return": kwargs.get("required_return", required_return),
        },
    )

@formula("graham_number", "Graham Number", "sqrt(22.5 * EPS * BVPS)", DOMAIN_KEY, unit="")
def graham_number(eps: float | None = None, bvps: float | None = None, **kwargs):
    return build_result(
        fid="graham_number",
        name="Graham Number",
        expression="sqrt(22.5 * EPS * BVPS)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "eps": kwargs.get("eps", eps),
            "bvps": kwargs.get("bvps", bvps),
        },
    )

@formula("sum_of_parts", "Sum-of-the-Parts Value", "Sum(Segment_Value_i)", DOMAIN_KEY, unit="")
def sum_of_parts(segment_values: float | None = None, **kwargs):
    return build_result(
        fid="sum_of_parts",
        name="Sum-of-the-Parts Value",
        expression="Sum(Segment_Value_i)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "segment_values": kwargs.get("segment_values", segment_values),
        },
    )

@formula("net_asset_value", "Net Asset Value (NAV)", "Total_Assets - Total_Liabilities", DOMAIN_KEY, unit="")
def net_asset_value(total_assets: float | None = None, total_liabilities: float | None = None, **kwargs):
    return build_result(
        fid="net_asset_value",
        name="Net Asset Value (NAV)",
        expression="Total_Assets - Total_Liabilities",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "total_assets": kwargs.get("total_assets", total_assets),
            "total_liabilities": kwargs.get("total_liabilities", total_liabilities),
        },
    )

@formula("liquidation_value", "Liquidation Value", "Asset_Recovery_Value - Total_Liabilities", DOMAIN_KEY, unit="")
def liquidation_value(asset_recovery_value: float | None = None, total_liabilities: float | None = None, **kwargs):
    return build_result(
        fid="liquidation_value",
        name="Liquidation Value",
        expression="Asset_Recovery_Value - Total_Liabilities",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "asset_recovery_value": kwargs.get("asset_recovery_value", asset_recovery_value),
            "total_liabilities": kwargs.get("total_liabilities", total_liabilities),
        },
    )

@formula("replacement_value", "Replacement Value", "Replacement_Cost_Assets - Liabilities", DOMAIN_KEY, unit="")
def replacement_value(replacement_cost_assets: float | None = None, liabilities: float | None = None, **kwargs):
    return build_result(
        fid="replacement_value",
        name="Replacement Value",
        expression="Replacement_Cost_Assets - Liabilities",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "replacement_cost_assets": kwargs.get("replacement_cost_assets", replacement_cost_assets),
            "liabilities": kwargs.get("liabilities", liabilities),
        },
    )

@formula("price_to_tangible_book", "Price-to-Tangible-Book", "Price / Tangible_BVPS", DOMAIN_KEY, unit="")
def price_to_tangible_book(price: float | None = None, tangible_bvps: float | None = None, **kwargs):
    return build_result(
        fid="price_to_tangible_book",
        name="Price-to-Tangible-Book",
        expression="Price / Tangible_BVPS",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "price": kwargs.get("price", price),
            "tangible_bvps": kwargs.get("tangible_bvps", tangible_bvps),
        },
    )

@formula("ev_to_invested_capital", "EV/Invested Capital", "EV / Invested_Capital", DOMAIN_KEY, unit="")
def ev_to_invested_capital(ev: float | None = None, invested_capital: float | None = None, **kwargs):
    return build_result(
        fid="ev_to_invested_capital",
        name="EV/Invested Capital",
        expression="EV / Invested_Capital",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ev": kwargs.get("ev", ev),
            "invested_capital": kwargs.get("invested_capital", invested_capital),
        },
    )

@formula("dividend_per_share", "Dividend Per Share", "Total_Dividends / Shares_Outstanding", DOMAIN_KEY, unit="")
def dividend_per_share(total_dividends: float | None = None, shares_outstanding: float | None = None, **kwargs):
    return build_result(
        fid="dividend_per_share",
        name="Dividend Per Share",
        expression="Total_Dividends / Shares_Outstanding",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "total_dividends": kwargs.get("total_dividends", total_dividends),
            "shares_outstanding": kwargs.get("shares_outstanding", shares_outstanding),
        },
    )

@formula("dividend_coverage", "Dividend Coverage Ratio", "EPS / Dividend_Per_Share", DOMAIN_KEY, unit="")
def dividend_coverage(eps: float | None = None, dividend_per_share: float | None = None, **kwargs):
    return build_result(
        fid="dividend_coverage",
        name="Dividend Coverage Ratio",
        expression="EPS / Dividend_Per_Share",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "eps": kwargs.get("eps", eps),
            "dividend_per_share": kwargs.get("dividend_per_share", dividend_per_share),
        },
    )

@formula("total_shareholder_return", "Total Shareholder Return %", "(Price_End - Price_Start + Dividends) / Price_Start * 100", DOMAIN_KEY, unit="")
def total_shareholder_return(price_end: float | None = None, price_start: float | None = None, dividends: float | None = None, **kwargs):
    return build_result(
        fid="total_shareholder_return",
        name="Total Shareholder Return %",
        expression="(Price_End - Price_Start + Dividends) / Price_Start * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "price_end": kwargs.get("price_end", price_end),
            "price_start": kwargs.get("price_start", price_start),
            "dividends": kwargs.get("dividends", dividends),
        },
    )

@formula("implied_growth_rate", "Implied Growth Rate", "Required_Return - D1/Price", DOMAIN_KEY, unit="")
def implied_growth_rate(required_return: float | None = None, d1: float | None = None, price: float | None = None, **kwargs):
    return build_result(
        fid="implied_growth_rate",
        name="Implied Growth Rate",
        expression="Required_Return - D1/Price",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "required_return": kwargs.get("required_return", required_return),
            "d1": kwargs.get("d1", d1),
            "price": kwargs.get("price", price),
        },
    )

@formula("ev_per_share", "EV Per Share", "EV / Shares_Outstanding", DOMAIN_KEY, unit="")
def ev_per_share(ev: float | None = None, shares_outstanding: float | None = None, **kwargs):
    return build_result(
        fid="ev_per_share",
        name="EV Per Share",
        expression="EV / Shares_Outstanding",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ev": kwargs.get("ev", ev),
            "shares_outstanding": kwargs.get("shares_outstanding", shares_outstanding),
        },
    )

@formula("price_to_nav", "Price-to-NAV", "Price / NAV_Per_Share", DOMAIN_KEY, unit="")
def price_to_nav(price: float | None = None, nav_per_share: float | None = None, **kwargs):
    return build_result(
        fid="price_to_nav",
        name="Price-to-NAV",
        expression="Price / NAV_Per_Share",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "price": kwargs.get("price", price),
            "nav_per_share": kwargs.get("nav_per_share", nav_per_share),
        },
    )

@formula("cape_ratio", "CAPE (Shiller P/E)", "Price / Avg_10yr_Real_EPS", DOMAIN_KEY, unit="")
def cape_ratio(price: float | None = None, avg_10yr_real_eps: float | None = None, **kwargs):
    return build_result(
        fid="cape_ratio",
        name="CAPE (Shiller P/E)",
        expression="Price / Avg_10yr_Real_EPS",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "price": kwargs.get("price", price),
            "avg_10yr_real_eps": kwargs.get("avg_10yr_real_eps", avg_10yr_real_eps),
        },
    )

@formula("rule_of_40", "Rule of 40 %", "Revenue_Growth_Pct + Profit_Margin_Pct", DOMAIN_KEY, unit="")
def rule_of_40(revenue_growth_pct: float | None = None, profit_margin_pct: float | None = None, **kwargs):
    return build_result(
        fid="rule_of_40",
        name="Rule of 40 %",
        expression="Revenue_Growth_Pct + Profit_Margin_Pct",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "revenue_growth_pct": kwargs.get("revenue_growth_pct", revenue_growth_pct),
            "profit_margin_pct": kwargs.get("profit_margin_pct", profit_margin_pct),
        },
    )

@formula("magic_formula_yield", "Magic Formula Earnings Yield", "EBIT / EV", DOMAIN_KEY, unit="")
def magic_formula_yield(ebit: float | None = None, ev: float | None = None, **kwargs):
    return build_result(
        fid="magic_formula_yield",
        name="Magic Formula Earnings Yield",
        expression="EBIT / EV",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ebit": kwargs.get("ebit", ebit),
            "ev": kwargs.get("ev", ev),
        },
    )

@formula("owners_earnings", "Owner's Earnings (Buffett)", "Net_Income + DA - Maintenance_CapEx", DOMAIN_KEY, unit="")
def owners_earnings(net_income: float | None = None, da: float | None = None, maintenance_capex: float | None = None, **kwargs):
    return build_result(
        fid="owners_earnings",
        name="Owner's Earnings (Buffett)",
        expression="Net_Income + DA - Maintenance_CapEx",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_income": kwargs.get("net_income", net_income),
            "da": kwargs.get("da", da),
            "maintenance_capex": kwargs.get("maintenance_capex", maintenance_capex),
        },
    )

@formula("intrinsic_value_growth", "Intrinsic Value (Growth)", "EPS * (8.5 + 2 * Growth_Rate)", DOMAIN_KEY, unit="")
def intrinsic_value_growth(eps: float | None = None, growth_rate: float | None = None, **kwargs):
    return build_result(
        fid="intrinsic_value_growth",
        name="Intrinsic Value (Growth)",
        expression="EPS * (8.5 + 2 * Growth_Rate)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "eps": kwargs.get("eps", eps),
            "growth_rate": kwargs.get("growth_rate", growth_rate),
        },
    )
