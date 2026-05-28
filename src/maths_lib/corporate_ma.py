from .base import build_result, formula

DOMAIN_KEY = "D09_corporate_ma"
DOMAIN_TITLE = "Corporate Finance & M&A"
FORMULA_IDS = [
    "sustainable_growth_rate",
    "internal_growth_rate",
    "plowback_ratio",
    "roic",
    "invested_capital",
    "economic_profit",
    "hamada_equation",
    "unlever_beta",
    "relever_beta",
    "mm_proposition1_no_tax",
    "mm_proposition1_tax",
    "mm_proposition2",
    "tax_shield",
    "interest_tax_shield_annual",
    "degree_total_leverage",
    "free_cash_flow_firm",
    "free_cash_flow_equity",
    "cash_flow_available_debt",
    "accretion_dilution",
    "exchange_ratio",
    "acquisition_premium",
    "synergy_value",
    "goodwill",
    "purchase_price_allocation",
    "pro_forma_eps",
    "breakeven_synergies",
    "lbo_equity_return",
    "lbo_irr",
    "debt_paydown",
    "entry_multiple",
    "exit_multiple",
    "sources_uses_balance",
    "net_borrowing",
    "dividend_discount_value",
    "clientele_effect",
    "share_buyback_eps_impact",
    "treasury_stock_method",
    "weighted_avg_shares",
    "capital_structure_weight_equity",
    "capital_structure_weight_debt",
    "operating_working_capital",
    "invested_capital_turnover",
    "reinvestment_rate",
    "expected_growth_fundamentals",
    "terminal_growth_implied",
    "equity_value_from_ev",
    "net_debt_to_equity_value",
    "dilution_percentage",
    "control_premium",
    "minority_interest_value",
]

@formula("sustainable_growth_rate", "Sustainable Growth Rate", "ROE * Retention_Ratio", DOMAIN_KEY, unit="")
def sustainable_growth_rate(roe: float | None = None, retention_ratio: float | None = None, **kwargs):
    return build_result(
        fid="sustainable_growth_rate",
        name="Sustainable Growth Rate",
        expression="ROE * Retention_Ratio",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "roe": kwargs.get("roe", roe),
            "retention_ratio": kwargs.get("retention_ratio", retention_ratio),
        },
    )

@formula("internal_growth_rate", "Internal Growth Rate", "(ROA*b)/(1-ROA*b)", DOMAIN_KEY, unit="")
def internal_growth_rate(roa: float | None = None, retention_ratio: float | None = None, **kwargs):
    return build_result(
        fid="internal_growth_rate",
        name="Internal Growth Rate",
        expression="(ROA*b)/(1-ROA*b)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "roa": kwargs.get("roa", roa),
            "retention_ratio": kwargs.get("retention_ratio", retention_ratio),
        },
    )

@formula("plowback_ratio", "Plowback Ratio", "1 - Dividend_Payout", DOMAIN_KEY, unit="")
def plowback_ratio(dividend_payout: float | None = None, **kwargs):
    return build_result(
        fid="plowback_ratio",
        name="Plowback Ratio",
        expression="1 - Dividend_Payout",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "dividend_payout": kwargs.get("dividend_payout", dividend_payout),
        },
    )

@formula("roic", "Return on Invested Capital", "NOPAT / Invested_Capital", DOMAIN_KEY, unit="")
def roic(nopat: float | None = None, invested_capital: float | None = None, **kwargs):
    return build_result(
        fid="roic",
        name="Return on Invested Capital",
        expression="NOPAT / Invested_Capital",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "nopat": kwargs.get("nopat", nopat),
            "invested_capital": kwargs.get("invested_capital", invested_capital),
        },
    )

@formula("invested_capital", "Invested Capital", "Total_Debt + Equity - Cash", DOMAIN_KEY, unit="")
def invested_capital(total_debt: float | None = None, equity: float | None = None, cash: float | None = None, **kwargs):
    return build_result(
        fid="invested_capital",
        name="Invested Capital",
        expression="Total_Debt + Equity - Cash",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "total_debt": kwargs.get("total_debt", total_debt),
            "equity": kwargs.get("equity", equity),
            "cash": kwargs.get("cash", cash),
        },
    )

@formula("economic_profit", "Economic Profit", "NOPAT - Invested_Capital*WACC", DOMAIN_KEY, unit="")
def economic_profit(nopat: float | None = None, invested_capital: float | None = None, wacc: float | None = None, **kwargs):
    return build_result(
        fid="economic_profit",
        name="Economic Profit",
        expression="NOPAT - Invested_Capital*WACC",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "nopat": kwargs.get("nopat", nopat),
            "invested_capital": kwargs.get("invested_capital", invested_capital),
            "wacc": kwargs.get("wacc", wacc),
        },
    )

@formula("hamada_equation", "Hamada Equation", "Bu*(1 + (1-T)*D/E)", DOMAIN_KEY, unit="")
def hamada_equation(unlevered_beta: float | None = None, tax_rate: float | None = None, debt: float | None = None, equity: float | None = None, **kwargs):
    return build_result(
        fid="hamada_equation",
        name="Hamada Equation",
        expression="Bu*(1 + (1-T)*D/E)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "unlevered_beta": kwargs.get("unlevered_beta", unlevered_beta),
            "tax_rate": kwargs.get("tax_rate", tax_rate),
            "debt": kwargs.get("debt", debt),
            "equity": kwargs.get("equity", equity),
        },
    )

@formula("unlever_beta", "Unlevered Beta", "Be / (1 + (1-T)*D/E)", DOMAIN_KEY, unit="")
def unlever_beta(levered_beta: float | None = None, tax_rate: float | None = None, debt: float | None = None, equity: float | None = None, **kwargs):
    return build_result(
        fid="unlever_beta",
        name="Unlevered Beta",
        expression="Be / (1 + (1-T)*D/E)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "levered_beta": kwargs.get("levered_beta", levered_beta),
            "tax_rate": kwargs.get("tax_rate", tax_rate),
            "debt": kwargs.get("debt", debt),
            "equity": kwargs.get("equity", equity),
        },
    )

@formula("relever_beta", "Relevered Beta", "Ba*(1 + (1-T)*D/E)", DOMAIN_KEY, unit="")
def relever_beta(asset_beta: float | None = None, tax_rate: float | None = None, debt: float | None = None, equity: float | None = None, **kwargs):
    return build_result(
        fid="relever_beta",
        name="Relevered Beta",
        expression="Ba*(1 + (1-T)*D/E)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "asset_beta": kwargs.get("asset_beta", asset_beta),
            "tax_rate": kwargs.get("tax_rate", tax_rate),
            "debt": kwargs.get("debt", debt),
            "equity": kwargs.get("equity", equity),
        },
    )

@formula("mm_proposition1_no_tax", "M&M Proposition I (No Tax)", "VL = VU", DOMAIN_KEY, unit="")
def mm_proposition1_no_tax(unlevered_value: float | None = None, **kwargs):
    return build_result(
        fid="mm_proposition1_no_tax",
        name="M&M Proposition I (No Tax)",
        expression="VL = VU",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "unlevered_value": kwargs.get("unlevered_value", unlevered_value),
        },
    )

@formula("mm_proposition1_tax", "M&M Proposition I (Tax)", "VU + Tax_Rate*Debt", DOMAIN_KEY, unit="")
def mm_proposition1_tax(unlevered_value: float | None = None, tax_rate: float | None = None, debt: float | None = None, **kwargs):
    return build_result(
        fid="mm_proposition1_tax",
        name="M&M Proposition I (Tax)",
        expression="VU + Tax_Rate*Debt",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "unlevered_value": kwargs.get("unlevered_value", unlevered_value),
            "tax_rate": kwargs.get("tax_rate", tax_rate),
            "debt": kwargs.get("debt", debt),
        },
    )

@formula("mm_proposition2", "M&M Proposition II", "Ru + (Ru-Rd)*(D/E)*(1-T)", DOMAIN_KEY, unit="")
def mm_proposition2(unlevered_cost: float | None = None, cost_debt: float | None = None, debt: float | None = None, equity: float | None = None, tax_rate: float | None = None, **kwargs):
    return build_result(
        fid="mm_proposition2",
        name="M&M Proposition II",
        expression="Ru + (Ru-Rd)*(D/E)*(1-T)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "unlevered_cost": kwargs.get("unlevered_cost", unlevered_cost),
            "cost_debt": kwargs.get("cost_debt", cost_debt),
            "debt": kwargs.get("debt", debt),
            "equity": kwargs.get("equity", equity),
            "tax_rate": kwargs.get("tax_rate", tax_rate),
        },
    )

@formula("tax_shield", "Tax Shield Value", "Tax_Rate * Debt", DOMAIN_KEY, unit="")
def tax_shield(tax_rate: float | None = None, debt: float | None = None, **kwargs):
    return build_result(
        fid="tax_shield",
        name="Tax Shield Value",
        expression="Tax_Rate * Debt",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "tax_rate": kwargs.get("tax_rate", tax_rate),
            "debt": kwargs.get("debt", debt),
        },
    )

@formula("interest_tax_shield_annual", "Annual Interest Tax Shield", "Interest * Tax_Rate", DOMAIN_KEY, unit="")
def interest_tax_shield_annual(interest: float | None = None, tax_rate: float | None = None, **kwargs):
    return build_result(
        fid="interest_tax_shield_annual",
        name="Annual Interest Tax Shield",
        expression="Interest * Tax_Rate",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "interest": kwargs.get("interest", interest),
            "tax_rate": kwargs.get("tax_rate", tax_rate),
        },
    )

@formula("degree_total_leverage", "Degree of Total Leverage", "DOL * DFL", DOMAIN_KEY, unit="")
def degree_total_leverage(dol: float | None = None, dfl: float | None = None, **kwargs):
    return build_result(
        fid="degree_total_leverage",
        name="Degree of Total Leverage",
        expression="DOL * DFL",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "dol": kwargs.get("dol", dol),
            "dfl": kwargs.get("dfl", dfl),
        },
    )

@formula("free_cash_flow_firm", "FCFF (Detailed)", "NI + NCC + Int*(1-T) - FCInv - WCInv", DOMAIN_KEY, unit="")
def free_cash_flow_firm(net_income: float | None = None, ncc: float | None = None, interest: float | None = None, tax_rate: float | None = None, fcinv: float | None = None, wcinv: float | None = None, **kwargs):
    return build_result(
        fid="free_cash_flow_firm",
        name="FCFF (Detailed)",
        expression="NI + NCC + Int*(1-T) - FCInv - WCInv",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_income": kwargs.get("net_income", net_income),
            "ncc": kwargs.get("ncc", ncc),
            "interest": kwargs.get("interest", interest),
            "tax_rate": kwargs.get("tax_rate", tax_rate),
            "fcinv": kwargs.get("fcinv", fcinv),
            "wcinv": kwargs.get("wcinv", wcinv),
        },
    )

@formula("free_cash_flow_equity", "FCFE (Detailed)", "NI + NCC - FCInv - WCInv + Net_Borrowing", DOMAIN_KEY, unit="")
def free_cash_flow_equity(net_income: float | None = None, ncc: float | None = None, fcinv: float | None = None, wcinv: float | None = None, net_borrowing: float | None = None, **kwargs):
    return build_result(
        fid="free_cash_flow_equity",
        name="FCFE (Detailed)",
        expression="NI + NCC - FCInv - WCInv + Net_Borrowing",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_income": kwargs.get("net_income", net_income),
            "ncc": kwargs.get("ncc", ncc),
            "fcinv": kwargs.get("fcinv", fcinv),
            "wcinv": kwargs.get("wcinv", wcinv),
            "net_borrowing": kwargs.get("net_borrowing", net_borrowing),
        },
    )

@formula("cash_flow_available_debt", "CFADS", "EBITDA - Tax - WC - CapEx", DOMAIN_KEY, unit="")
def cash_flow_available_debt(ebitda: float | None = None, tax: float | None = None, working_capital_change: float | None = None, capex: float | None = None, **kwargs):
    return build_result(
        fid="cash_flow_available_debt",
        name="CFADS",
        expression="EBITDA - Tax - WC - CapEx",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ebitda": kwargs.get("ebitda", ebitda),
            "tax": kwargs.get("tax", tax),
            "working_capital_change": kwargs.get("working_capital_change", working_capital_change),
            "capex": kwargs.get("capex", capex),
        },
    )

@formula("accretion_dilution", "Accretion/Dilution %", "(ProForma_EPS - Standalone_EPS)/Standalone*100", DOMAIN_KEY, unit="")
def accretion_dilution(proforma_eps: float | None = None, standalone_eps: float | None = None, **kwargs):
    return build_result(
        fid="accretion_dilution",
        name="Accretion/Dilution %",
        expression="(ProForma_EPS - Standalone_EPS)/Standalone*100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "proforma_eps": kwargs.get("proforma_eps", proforma_eps),
            "standalone_eps": kwargs.get("standalone_eps", standalone_eps),
        },
    )

@formula("exchange_ratio", "Exchange Ratio", "Offer_Price / Acquirer_Price", DOMAIN_KEY, unit="")
def exchange_ratio(offer_price: float | None = None, acquirer_price: float | None = None, **kwargs):
    return build_result(
        fid="exchange_ratio",
        name="Exchange Ratio",
        expression="Offer_Price / Acquirer_Price",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "offer_price": kwargs.get("offer_price", offer_price),
            "acquirer_price": kwargs.get("acquirer_price", acquirer_price),
        },
    )

@formula("acquisition_premium", "Acquisition Premium %", "(Offer - Market)/Market * 100", DOMAIN_KEY, unit="")
def acquisition_premium(offer_price: float | None = None, market_price: float | None = None, **kwargs):
    return build_result(
        fid="acquisition_premium",
        name="Acquisition Premium %",
        expression="(Offer - Market)/Market * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "offer_price": kwargs.get("offer_price", offer_price),
            "market_price": kwargs.get("market_price", market_price),
        },
    )

@formula("synergy_value", "Synergy Value", "V_Combined - (V_A + V_B)", DOMAIN_KEY, unit="")
def synergy_value(combined_value: float | None = None, value_a: float | None = None, value_b: float | None = None, **kwargs):
    return build_result(
        fid="synergy_value",
        name="Synergy Value",
        expression="V_Combined - (V_A + V_B)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "combined_value": kwargs.get("combined_value", combined_value),
            "value_a": kwargs.get("value_a", value_a),
            "value_b": kwargs.get("value_b", value_b),
        },
    )

@formula("goodwill", "Goodwill", "Purchase_Price - Fair_Value_Net_Assets", DOMAIN_KEY, unit="")
def goodwill(purchase_price: float | None = None, fair_value_net_assets: float | None = None, **kwargs):
    return build_result(
        fid="goodwill",
        name="Goodwill",
        expression="Purchase_Price - Fair_Value_Net_Assets",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "purchase_price": kwargs.get("purchase_price", purchase_price),
            "fair_value_net_assets": kwargs.get("fair_value_net_assets", fair_value_net_assets),
        },
    )

@formula("purchase_price_allocation", "Net Identifiable Assets", "FV_Assets - FV_Liabilities", DOMAIN_KEY, unit="")
def purchase_price_allocation(fv_assets: float | None = None, fv_liabilities: float | None = None, **kwargs):
    return build_result(
        fid="purchase_price_allocation",
        name="Net Identifiable Assets",
        expression="FV_Assets - FV_Liabilities",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "fv_assets": kwargs.get("fv_assets", fv_assets),
            "fv_liabilities": kwargs.get("fv_liabilities", fv_liabilities),
        },
    )

@formula("pro_forma_eps", "Pro Forma EPS", "Combined_NI / Combined_Shares", DOMAIN_KEY, unit="")
def pro_forma_eps(combined_net_income: float | None = None, combined_shares: float | None = None, **kwargs):
    return build_result(
        fid="pro_forma_eps",
        name="Pro Forma EPS",
        expression="Combined_NI / Combined_Shares",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "combined_net_income": kwargs.get("combined_net_income", combined_net_income),
            "combined_shares": kwargs.get("combined_shares", combined_shares),
        },
    )

@formula("breakeven_synergies", "Breakeven Synergies", "Premium_Paid value", DOMAIN_KEY, unit="")
def breakeven_synergies(premium: float | None = None, target_shares: float | None = None, **kwargs):
    return build_result(
        fid="breakeven_synergies",
        name="Breakeven Synergies",
        expression="Premium_Paid value",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "premium": kwargs.get("premium", premium),
            "target_shares": kwargs.get("target_shares", target_shares),
        },
    )

@formula("lbo_equity_return", "LBO Equity Return (MOIC)", "Exit_Equity / Entry_Equity", DOMAIN_KEY, unit="")
def lbo_equity_return(exit_equity: float | None = None, entry_equity: float | None = None, **kwargs):
    return build_result(
        fid="lbo_equity_return",
        name="LBO Equity Return (MOIC)",
        expression="Exit_Equity / Entry_Equity",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "exit_equity": kwargs.get("exit_equity", exit_equity),
            "entry_equity": kwargs.get("entry_equity", entry_equity),
        },
    )

@formula("lbo_irr", "LBO IRR", "(Exit/Entry)^(1/years) - 1", DOMAIN_KEY, unit="")
def lbo_irr(entry_equity: float | None = None, exit_equity: float | None = None, years: float | None = None, **kwargs):
    return build_result(
        fid="lbo_irr",
        name="LBO IRR",
        expression="(Exit/Entry)^(1/years) - 1",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "entry_equity": kwargs.get("entry_equity", entry_equity),
            "exit_equity": kwargs.get("exit_equity", exit_equity),
            "years": kwargs.get("years", years),
        },
    )

@formula("debt_paydown", "Debt Paydown", "Entry_Debt - Exit_Debt", DOMAIN_KEY, unit="")
def debt_paydown(entry_debt: float | None = None, exit_debt: float | None = None, **kwargs):
    return build_result(
        fid="debt_paydown",
        name="Debt Paydown",
        expression="Entry_Debt - Exit_Debt",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "entry_debt": kwargs.get("entry_debt", entry_debt),
            "exit_debt": kwargs.get("exit_debt", exit_debt),
        },
    )

@formula("entry_multiple", "Entry Multiple", "Entry_EV / EBITDA", DOMAIN_KEY, unit="")
def entry_multiple(entry_ev: float | None = None, ebitda: float | None = None, **kwargs):
    return build_result(
        fid="entry_multiple",
        name="Entry Multiple",
        expression="Entry_EV / EBITDA",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "entry_ev": kwargs.get("entry_ev", entry_ev),
            "ebitda": kwargs.get("ebitda", ebitda),
        },
    )

@formula("exit_multiple", "Exit Multiple", "Exit_EV / EBITDA", DOMAIN_KEY, unit="")
def exit_multiple(exit_ev: float | None = None, ebitda: float | None = None, **kwargs):
    return build_result(
        fid="exit_multiple",
        name="Exit Multiple",
        expression="Exit_EV / EBITDA",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "exit_ev": kwargs.get("exit_ev", exit_ev),
            "ebitda": kwargs.get("ebitda", ebitda),
        },
    )

@formula("sources_uses_balance", "Sources and Uses Balance", "Sum(Sources) - Sum(Uses)", DOMAIN_KEY, unit="")
def sources_uses_balance(sources: float | None = None, uses: float | None = None, **kwargs):
    return build_result(
        fid="sources_uses_balance",
        name="Sources and Uses Balance",
        expression="Sum(Sources) - Sum(Uses)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "sources": kwargs.get("sources", sources),
            "uses": kwargs.get("uses", uses),
        },
    )

@formula("net_borrowing", "Net Borrowing", "Debt_Issued - Debt_Repaid", DOMAIN_KEY, unit="")
def net_borrowing(debt_issued: float | None = None, debt_repaid: float | None = None, **kwargs):
    return build_result(
        fid="net_borrowing",
        name="Net Borrowing",
        expression="Debt_Issued - Debt_Repaid",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "debt_issued": kwargs.get("debt_issued", debt_issued),
            "debt_repaid": kwargs.get("debt_repaid", debt_repaid),
        },
    )

@formula("dividend_discount_value", "DDM Value", "Sum(D_t/(1+r)^t)", DOMAIN_KEY, unit="")
def dividend_discount_value(dividends: float | None = None, rate: float | None = None, **kwargs):
    return build_result(
        fid="dividend_discount_value",
        name="DDM Value",
        expression="Sum(D_t/(1+r)^t)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "dividends": kwargs.get("dividends", dividends),
            "rate": kwargs.get("rate", rate),
        },
    )

@formula("clientele_effect", "After-Tax Dividend", "Dividend * (1 - Tax_Rate)", DOMAIN_KEY, unit="")
def clientele_effect(dividend: float | None = None, tax_rate: float | None = None, **kwargs):
    return build_result(
        fid="clientele_effect",
        name="After-Tax Dividend",
        expression="Dividend * (1 - Tax_Rate)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "dividend": kwargs.get("dividend", dividend),
            "tax_rate": kwargs.get("tax_rate", tax_rate),
        },
    )

@formula("share_buyback_eps_impact", "Buyback EPS Impact", "NI / (Shares - Bought)", DOMAIN_KEY, unit="")
def share_buyback_eps_impact(net_income: float | None = None, shares: float | None = None, shares_bought: float | None = None, **kwargs):
    return build_result(
        fid="share_buyback_eps_impact",
        name="Buyback EPS Impact",
        expression="NI / (Shares - Bought)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_income": kwargs.get("net_income", net_income),
            "shares": kwargs.get("shares", shares),
            "shares_bought": kwargs.get("shares_bought", shares_bought),
        },
    )

@formula("treasury_stock_method", "Treasury Stock Method", "Options - (Options*Strike/Price)", DOMAIN_KEY, unit="")
def treasury_stock_method(options: float | None = None, strike: float | None = None, price: float | None = None, **kwargs):
    return build_result(
        fid="treasury_stock_method",
        name="Treasury Stock Method",
        expression="Options - (Options*Strike/Price)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "options": kwargs.get("options", options),
            "strike": kwargs.get("strike", strike),
            "price": kwargs.get("price", price),
        },
    )

@formula("weighted_avg_shares", "Weighted Average Shares", "Sum(Shares_i * Months_i / 12)", DOMAIN_KEY, unit="")
def weighted_avg_shares(share_periods: float | None = None, **kwargs):
    return build_result(
        fid="weighted_avg_shares",
        name="Weighted Average Shares",
        expression="Sum(Shares_i * Months_i / 12)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "share_periods": kwargs.get("share_periods", share_periods),
        },
    )

@formula("capital_structure_weight_equity", "Equity Weight", "Equity / (Equity + Debt)", DOMAIN_KEY, unit="")
def capital_structure_weight_equity(equity: float | None = None, debt: float | None = None, **kwargs):
    return build_result(
        fid="capital_structure_weight_equity",
        name="Equity Weight",
        expression="Equity / (Equity + Debt)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "equity": kwargs.get("equity", equity),
            "debt": kwargs.get("debt", debt),
        },
    )

@formula("capital_structure_weight_debt", "Debt Weight", "Debt / (Equity + Debt)", DOMAIN_KEY, unit="")
def capital_structure_weight_debt(equity: float | None = None, debt: float | None = None, **kwargs):
    return build_result(
        fid="capital_structure_weight_debt",
        name="Debt Weight",
        expression="Debt / (Equity + Debt)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "equity": kwargs.get("equity", equity),
            "debt": kwargs.get("debt", debt),
        },
    )

@formula("operating_working_capital", "Operating Working Capital", "Op_Current_Assets - Op_Current_Liabilities", DOMAIN_KEY, unit="")
def operating_working_capital(op_current_assets: float | None = None, op_current_liabilities: float | None = None, **kwargs):
    return build_result(
        fid="operating_working_capital",
        name="Operating Working Capital",
        expression="Op_Current_Assets - Op_Current_Liabilities",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "op_current_assets": kwargs.get("op_current_assets", op_current_assets),
            "op_current_liabilities": kwargs.get("op_current_liabilities", op_current_liabilities),
        },
    )

@formula("invested_capital_turnover", "Invested Capital Turnover", "Revenue / Invested_Capital", DOMAIN_KEY, unit="")
def invested_capital_turnover(revenue: float | None = None, invested_capital: float | None = None, **kwargs):
    return build_result(
        fid="invested_capital_turnover",
        name="Invested Capital Turnover",
        expression="Revenue / Invested_Capital",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "revenue": kwargs.get("revenue", revenue),
            "invested_capital": kwargs.get("invested_capital", invested_capital),
        },
    )

@formula("reinvestment_rate", "Reinvestment Rate", "(CapEx - Depr + WCInv) / NOPAT", DOMAIN_KEY, unit="")
def reinvestment_rate(capex: float | None = None, depreciation: float | None = None, wc_investment: float | None = None, nopat: float | None = None, **kwargs):
    return build_result(
        fid="reinvestment_rate",
        name="Reinvestment Rate",
        expression="(CapEx - Depr + WCInv) / NOPAT",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "capex": kwargs.get("capex", capex),
            "depreciation": kwargs.get("depreciation", depreciation),
            "wc_investment": kwargs.get("wc_investment", wc_investment),
            "nopat": kwargs.get("nopat", nopat),
        },
    )

@formula("expected_growth_fundamentals", "Expected Growth (Fundamentals)", "Reinvestment_Rate * ROIC", DOMAIN_KEY, unit="")
def expected_growth_fundamentals(reinvestment_rate: float | None = None, roic: float | None = None, **kwargs):
    return build_result(
        fid="expected_growth_fundamentals",
        name="Expected Growth (Fundamentals)",
        expression="Reinvestment_Rate * ROIC",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "reinvestment_rate": kwargs.get("reinvestment_rate", reinvestment_rate),
            "roic": kwargs.get("roic", roic),
        },
    )

@formula("terminal_growth_implied", "Implied Terminal Growth", "r - FCF/TV", DOMAIN_KEY, unit="")
def terminal_growth_implied(rate: float | None = None, fcf: float | None = None, terminal_value: float | None = None, **kwargs):
    return build_result(
        fid="terminal_growth_implied",
        name="Implied Terminal Growth",
        expression="r - FCF/TV",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "rate": kwargs.get("rate", rate),
            "fcf": kwargs.get("fcf", fcf),
            "terminal_value": kwargs.get("terminal_value", terminal_value),
        },
    )

@formula("equity_value_from_ev", "Equity Value from EV", "EV - Net_Debt", DOMAIN_KEY, unit="")
def equity_value_from_ev(ev: float | None = None, net_debt: float | None = None, **kwargs):
    return build_result(
        fid="equity_value_from_ev",
        name="Equity Value from EV",
        expression="EV - Net_Debt",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ev": kwargs.get("ev", ev),
            "net_debt": kwargs.get("net_debt", net_debt),
        },
    )

@formula("net_debt_to_equity_value", "Net Debt to Equity Value", "Net_Debt / Equity_Value", DOMAIN_KEY, unit="")
def net_debt_to_equity_value(net_debt: float | None = None, equity_value: float | None = None, **kwargs):
    return build_result(
        fid="net_debt_to_equity_value",
        name="Net Debt to Equity Value",
        expression="Net_Debt / Equity_Value",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_debt": kwargs.get("net_debt", net_debt),
            "equity_value": kwargs.get("equity_value", equity_value),
        },
    )

@formula("dilution_percentage", "Dilution Percentage", "New_Shares / (Old + New) * 100", DOMAIN_KEY, unit="")
def dilution_percentage(old_shares: float | None = None, new_shares: float | None = None, **kwargs):
    return build_result(
        fid="dilution_percentage",
        name="Dilution Percentage",
        expression="New_Shares / (Old + New) * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "old_shares": kwargs.get("old_shares", old_shares),
            "new_shares": kwargs.get("new_shares", new_shares),
        },
    )

@formula("control_premium", "Control Premium %", "(Control_Price - Minority)/Minority*100", DOMAIN_KEY, unit="")
def control_premium(control_price: float | None = None, minority_price: float | None = None, **kwargs):
    return build_result(
        fid="control_premium",
        name="Control Premium %",
        expression="(Control_Price - Minority)/Minority*100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "control_price": kwargs.get("control_price", control_price),
            "minority_price": kwargs.get("minority_price", minority_price),
        },
    )

@formula("minority_interest_value", "Minority Interest Value", "Subsidiary_Value * Minority_Pct", DOMAIN_KEY, unit="")
def minority_interest_value(subsidiary_value: float | None = None, minority_pct: float | None = None, **kwargs):
    return build_result(
        fid="minority_interest_value",
        name="Minority Interest Value",
        expression="Subsidiary_Value * Minority_Pct",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "subsidiary_value": kwargs.get("subsidiary_value", subsidiary_value),
            "minority_pct": kwargs.get("minority_pct", minority_pct),
        },
    )
