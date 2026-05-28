from .base import build_result, formula

DOMAIN_KEY = "D01_profitability"
DOMAIN_TITLE = "Profitability & Margin Ratios"
FORMULA_IDS = [
    "gross_margin",
    "gross_profit",
    "operating_margin",
    "net_margin",
    "ebitda_margin",
    "ebit_margin",
    "pretax_margin",
    "contribution_margin",
    "contribution_margin_ratio",
    "fcf_margin",
    "ocf_margin",
    "return_on_equity",
    "return_on_assets",
    "return_on_invested_capital",
    "return_on_capital_employed",
    "return_on_sales",
    "return_on_tangible_equity",
    "return_on_net_assets",
    "nopat",
    "ebitda",
    "ebit",
    "effective_tax_rate",
    "operating_leverage",
    "financial_leverage",
    "combined_leverage",
    "dupont_roe_3step",
    "dupont_roe_5step",
    "tax_burden",
    "interest_burden",
    "equity_multiplier",
    "operating_ratio",
    "cost_of_revenue_ratio",
    "overhead_ratio",
    "sga_ratio",
    "rnd_ratio",
    "rnd_intensity",
    "net_income_growth",
    "revenue_growth",
    "operating_income_growth",
    "eps_basic",
    "eps_diluted",
    "eps_growth",
    "cash_return_on_assets",
    "cash_roe",
    "gross_profit_growth",
    "ebitda_growth",
    "incremental_margin",
    "breakeven_point_units",
    "breakeven_point_revenue",
    "margin_of_safety",
]

@formula("gross_margin", "Gross Margin %", "(Revenue - COGS) / Revenue * 100", DOMAIN_KEY, unit="")
def gross_margin(revenue: float | None = None, cogs: float | None = None, **kwargs):
    return build_result(
        fid="gross_margin",
        name="Gross Margin %",
        expression="(Revenue - COGS) / Revenue * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "revenue": kwargs.get("revenue", revenue),
            "cogs": kwargs.get("cogs", cogs),
        },
    )

@formula("gross_profit", "Gross Profit", "Revenue - COGS", DOMAIN_KEY, unit="")
def gross_profit(revenue: float | None = None, cogs: float | None = None, **kwargs):
    return build_result(
        fid="gross_profit",
        name="Gross Profit",
        expression="Revenue - COGS",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "revenue": kwargs.get("revenue", revenue),
            "cogs": kwargs.get("cogs", cogs),
        },
    )

@formula("operating_margin", "Operating Margin %", "Operating_Income / Revenue * 100", DOMAIN_KEY, unit="")
def operating_margin(operating_income: float | None = None, revenue: float | None = None, **kwargs):
    return build_result(
        fid="operating_margin",
        name="Operating Margin %",
        expression="Operating_Income / Revenue * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "operating_income": kwargs.get("operating_income", operating_income),
            "revenue": kwargs.get("revenue", revenue),
        },
    )

@formula("net_margin", "Net Profit Margin %", "Net_Income / Revenue * 100", DOMAIN_KEY, unit="")
def net_margin(net_income: float | None = None, revenue: float | None = None, **kwargs):
    return build_result(
        fid="net_margin",
        name="Net Profit Margin %",
        expression="Net_Income / Revenue * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_income": kwargs.get("net_income", net_income),
            "revenue": kwargs.get("revenue", revenue),
        },
    )

@formula("ebitda_margin", "EBITDA Margin %", "EBITDA / Revenue * 100", DOMAIN_KEY, unit="")
def ebitda_margin(ebitda: float | None = None, revenue: float | None = None, **kwargs):
    return build_result(
        fid="ebitda_margin",
        name="EBITDA Margin %",
        expression="EBITDA / Revenue * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ebitda": kwargs.get("ebitda", ebitda),
            "revenue": kwargs.get("revenue", revenue),
        },
    )

@formula("ebit_margin", "EBIT Margin %", "EBIT / Revenue * 100", DOMAIN_KEY, unit="")
def ebit_margin(ebit: float | None = None, revenue: float | None = None, **kwargs):
    return build_result(
        fid="ebit_margin",
        name="EBIT Margin %",
        expression="EBIT / Revenue * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ebit": kwargs.get("ebit", ebit),
            "revenue": kwargs.get("revenue", revenue),
        },
    )

@formula("pretax_margin", "Pretax Margin %", "Pretax_Income / Revenue * 100", DOMAIN_KEY, unit="")
def pretax_margin(pretax_income: float | None = None, revenue: float | None = None, **kwargs):
    return build_result(
        fid="pretax_margin",
        name="Pretax Margin %",
        expression="Pretax_Income / Revenue * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "pretax_income": kwargs.get("pretax_income", pretax_income),
            "revenue": kwargs.get("revenue", revenue),
        },
    )

@formula("contribution_margin", "Contribution Margin", "Revenue - Variable_Costs", DOMAIN_KEY, unit="")
def contribution_margin(revenue: float | None = None, variable_costs: float | None = None, **kwargs):
    return build_result(
        fid="contribution_margin",
        name="Contribution Margin",
        expression="Revenue - Variable_Costs",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "revenue": kwargs.get("revenue", revenue),
            "variable_costs": kwargs.get("variable_costs", variable_costs),
        },
    )

@formula("contribution_margin_ratio", "Contribution Margin Ratio %", "(Revenue - Variable_Costs) / Revenue * 100", DOMAIN_KEY, unit="")
def contribution_margin_ratio(revenue: float | None = None, variable_costs: float | None = None, **kwargs):
    return build_result(
        fid="contribution_margin_ratio",
        name="Contribution Margin Ratio %",
        expression="(Revenue - Variable_Costs) / Revenue * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "revenue": kwargs.get("revenue", revenue),
            "variable_costs": kwargs.get("variable_costs", variable_costs),
        },
    )

@formula("fcf_margin", "Free Cash Flow Margin %", "FCF / Revenue * 100", DOMAIN_KEY, unit="")
def fcf_margin(fcf: float | None = None, revenue: float | None = None, **kwargs):
    return build_result(
        fid="fcf_margin",
        name="Free Cash Flow Margin %",
        expression="FCF / Revenue * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "fcf": kwargs.get("fcf", fcf),
            "revenue": kwargs.get("revenue", revenue),
        },
    )

@formula("ocf_margin", "Operating Cash Flow Margin %", "OCF / Revenue * 100", DOMAIN_KEY, unit="")
def ocf_margin(ocf: float | None = None, revenue: float | None = None, **kwargs):
    return build_result(
        fid="ocf_margin",
        name="Operating Cash Flow Margin %",
        expression="OCF / Revenue * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ocf": kwargs.get("ocf", ocf),
            "revenue": kwargs.get("revenue", revenue),
        },
    )

@formula("return_on_equity", "Return on Equity (ROE) %", "Net_Income / Shareholders_Equity * 100", DOMAIN_KEY, unit="")
def return_on_equity(net_income: float | None = None, shareholders_equity: float | None = None, **kwargs):
    return build_result(
        fid="return_on_equity",
        name="Return on Equity (ROE) %",
        expression="Net_Income / Shareholders_Equity * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_income": kwargs.get("net_income", net_income),
            "shareholders_equity": kwargs.get("shareholders_equity", shareholders_equity),
        },
    )

@formula("return_on_assets", "Return on Assets (ROA) %", "Net_Income / Total_Assets * 100", DOMAIN_KEY, unit="")
def return_on_assets(net_income: float | None = None, total_assets: float | None = None, **kwargs):
    return build_result(
        fid="return_on_assets",
        name="Return on Assets (ROA) %",
        expression="Net_Income / Total_Assets * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_income": kwargs.get("net_income", net_income),
            "total_assets": kwargs.get("total_assets", total_assets),
        },
    )

@formula("return_on_invested_capital", "Return on Invested Capital (ROIC) %", "NOPAT / Invested_Capital * 100", DOMAIN_KEY, unit="")
def return_on_invested_capital(nopat: float | None = None, invested_capital: float | None = None, **kwargs):
    return build_result(
        fid="return_on_invested_capital",
        name="Return on Invested Capital (ROIC) %",
        expression="NOPAT / Invested_Capital * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "nopat": kwargs.get("nopat", nopat),
            "invested_capital": kwargs.get("invested_capital", invested_capital),
        },
    )

@formula("return_on_capital_employed", "Return on Capital Employed (ROCE) %", "EBIT / Capital_Employed * 100", DOMAIN_KEY, unit="")
def return_on_capital_employed(ebit: float | None = None, capital_employed: float | None = None, **kwargs):
    return build_result(
        fid="return_on_capital_employed",
        name="Return on Capital Employed (ROCE) %",
        expression="EBIT / Capital_Employed * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ebit": kwargs.get("ebit", ebit),
            "capital_employed": kwargs.get("capital_employed", capital_employed),
        },
    )

@formula("return_on_sales", "Return on Sales (ROS) %", "Operating_Income / Sales * 100", DOMAIN_KEY, unit="")
def return_on_sales(operating_income: float | None = None, sales: float | None = None, **kwargs):
    return build_result(
        fid="return_on_sales",
        name="Return on Sales (ROS) %",
        expression="Operating_Income / Sales * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "operating_income": kwargs.get("operating_income", operating_income),
            "sales": kwargs.get("sales", sales),
        },
    )

@formula("return_on_tangible_equity", "Return on Tangible Equity %", "Net_Income / (Equity - Intangibles) * 100", DOMAIN_KEY, unit="")
def return_on_tangible_equity(net_income: float | None = None, equity: float | None = None, intangibles: float | None = None, **kwargs):
    return build_result(
        fid="return_on_tangible_equity",
        name="Return on Tangible Equity %",
        expression="Net_Income / (Equity - Intangibles) * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_income": kwargs.get("net_income", net_income),
            "equity": kwargs.get("equity", equity),
            "intangibles": kwargs.get("intangibles", intangibles),
        },
    )

@formula("return_on_net_assets", "Return on Net Assets (RONA) %", "Net_Income / (Fixed_Assets + Working_Capital) * 100", DOMAIN_KEY, unit="")
def return_on_net_assets(net_income: float | None = None, fixed_assets: float | None = None, working_capital: float | None = None, **kwargs):
    return build_result(
        fid="return_on_net_assets",
        name="Return on Net Assets (RONA) %",
        expression="Net_Income / (Fixed_Assets + Working_Capital) * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_income": kwargs.get("net_income", net_income),
            "fixed_assets": kwargs.get("fixed_assets", fixed_assets),
            "working_capital": kwargs.get("working_capital", working_capital),
        },
    )

@formula("nopat", "Net Operating Profit After Tax", "EBIT * (1 - Tax_Rate)", DOMAIN_KEY, unit="")
def nopat(ebit: float | None = None, tax_rate: float | None = None, **kwargs):
    return build_result(
        fid="nopat",
        name="Net Operating Profit After Tax",
        expression="EBIT * (1 - Tax_Rate)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ebit": kwargs.get("ebit", ebit),
            "tax_rate": kwargs.get("tax_rate", tax_rate),
        },
    )

@formula("ebitda", "EBITDA", "Net_Income + Interest + Taxes + Depreciation + Amortization", DOMAIN_KEY, unit="")
def ebitda(net_income: float | None = None, interest: float | None = None, taxes: float | None = None, depreciation: float | None = None, amortization: float | None = None, **kwargs):
    return build_result(
        fid="ebitda",
        name="EBITDA",
        expression="Net_Income + Interest + Taxes + Depreciation + Amortization",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_income": kwargs.get("net_income", net_income),
            "interest": kwargs.get("interest", interest),
            "taxes": kwargs.get("taxes", taxes),
            "depreciation": kwargs.get("depreciation", depreciation),
            "amortization": kwargs.get("amortization", amortization),
        },
    )

@formula("ebit", "EBIT", "Net_Income + Interest + Taxes", DOMAIN_KEY, unit="")
def ebit(net_income: float | None = None, interest: float | None = None, taxes: float | None = None, **kwargs):
    return build_result(
        fid="ebit",
        name="EBIT",
        expression="Net_Income + Interest + Taxes",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_income": kwargs.get("net_income", net_income),
            "interest": kwargs.get("interest", interest),
            "taxes": kwargs.get("taxes", taxes),
        },
    )

@formula("effective_tax_rate", "Effective Tax Rate %", "Tax_Expense / Pretax_Income * 100", DOMAIN_KEY, unit="")
def effective_tax_rate(tax_expense: float | None = None, pretax_income: float | None = None, **kwargs):
    return build_result(
        fid="effective_tax_rate",
        name="Effective Tax Rate %",
        expression="Tax_Expense / Pretax_Income * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "tax_expense": kwargs.get("tax_expense", tax_expense),
            "pretax_income": kwargs.get("pretax_income", pretax_income),
        },
    )

@formula("operating_leverage", "Degree of Operating Leverage", "Pct_Change_EBIT / Pct_Change_Sales", DOMAIN_KEY, unit="")
def operating_leverage(pct_change_ebit: float | None = None, pct_change_sales: float | None = None, **kwargs):
    return build_result(
        fid="operating_leverage",
        name="Degree of Operating Leverage",
        expression="Pct_Change_EBIT / Pct_Change_Sales",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "pct_change_ebit": kwargs.get("pct_change_ebit", pct_change_ebit),
            "pct_change_sales": kwargs.get("pct_change_sales", pct_change_sales),
        },
    )

@formula("financial_leverage", "Degree of Financial Leverage", "Pct_Change_EPS / Pct_Change_EBIT", DOMAIN_KEY, unit="")
def financial_leverage(pct_change_eps: float | None = None, pct_change_ebit: float | None = None, **kwargs):
    return build_result(
        fid="financial_leverage",
        name="Degree of Financial Leverage",
        expression="Pct_Change_EPS / Pct_Change_EBIT",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "pct_change_eps": kwargs.get("pct_change_eps", pct_change_eps),
            "pct_change_ebit": kwargs.get("pct_change_ebit", pct_change_ebit),
        },
    )

@formula("combined_leverage", "Degree of Combined Leverage", "DOL * DFL", DOMAIN_KEY, unit="")
def combined_leverage(dol: float | None = None, dfl: float | None = None, **kwargs):
    return build_result(
        fid="combined_leverage",
        name="Degree of Combined Leverage",
        expression="DOL * DFL",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "dol": kwargs.get("dol", dol),
            "dfl": kwargs.get("dfl", dfl),
        },
    )

@formula("dupont_roe_3step", "DuPont ROE (3-Step)", "Net_Margin * Asset_Turnover * Equity_Multiplier", DOMAIN_KEY, unit="")
def dupont_roe_3step(net_margin: float | None = None, asset_turnover: float | None = None, equity_multiplier: float | None = None, **kwargs):
    return build_result(
        fid="dupont_roe_3step",
        name="DuPont ROE (3-Step)",
        expression="Net_Margin * Asset_Turnover * Equity_Multiplier",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_margin": kwargs.get("net_margin", net_margin),
            "asset_turnover": kwargs.get("asset_turnover", asset_turnover),
            "equity_multiplier": kwargs.get("equity_multiplier", equity_multiplier),
        },
    )

@formula("dupont_roe_5step", "DuPont ROE (5-Step)", "Tax_Burden * Interest_Burden * Operating_Margin * Asset_Turnover * Equity_Multiplier", DOMAIN_KEY, unit="")
def dupont_roe_5step(tax_burden: float | None = None, interest_burden: float | None = None, operating_margin: float | None = None, asset_turnover: float | None = None, equity_multiplier: float | None = None, **kwargs):
    return build_result(
        fid="dupont_roe_5step",
        name="DuPont ROE (5-Step)",
        expression="Tax_Burden * Interest_Burden * Operating_Margin * Asset_Turnover * Equity_Multiplier",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "tax_burden": kwargs.get("tax_burden", tax_burden),
            "interest_burden": kwargs.get("interest_burden", interest_burden),
            "operating_margin": kwargs.get("operating_margin", operating_margin),
            "asset_turnover": kwargs.get("asset_turnover", asset_turnover),
            "equity_multiplier": kwargs.get("equity_multiplier", equity_multiplier),
        },
    )

@formula("tax_burden", "Tax Burden Ratio", "Net_Income / Pretax_Income", DOMAIN_KEY, unit="")
def tax_burden(net_income: float | None = None, pretax_income: float | None = None, **kwargs):
    return build_result(
        fid="tax_burden",
        name="Tax Burden Ratio",
        expression="Net_Income / Pretax_Income",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_income": kwargs.get("net_income", net_income),
            "pretax_income": kwargs.get("pretax_income", pretax_income),
        },
    )

@formula("interest_burden", "Interest Burden Ratio", "Pretax_Income / EBIT", DOMAIN_KEY, unit="")
def interest_burden(pretax_income: float | None = None, ebit: float | None = None, **kwargs):
    return build_result(
        fid="interest_burden",
        name="Interest Burden Ratio",
        expression="Pretax_Income / EBIT",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "pretax_income": kwargs.get("pretax_income", pretax_income),
            "ebit": kwargs.get("ebit", ebit),
        },
    )

@formula("equity_multiplier", "Equity Multiplier", "Total_Assets / Shareholders_Equity", DOMAIN_KEY, unit="")
def equity_multiplier(total_assets: float | None = None, shareholders_equity: float | None = None, **kwargs):
    return build_result(
        fid="equity_multiplier",
        name="Equity Multiplier",
        expression="Total_Assets / Shareholders_Equity",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "total_assets": kwargs.get("total_assets", total_assets),
            "shareholders_equity": kwargs.get("shareholders_equity", shareholders_equity),
        },
    )

@formula("operating_ratio", "Operating Ratio %", "Operating_Costs / Revenue * 100", DOMAIN_KEY, unit="")
def operating_ratio(operating_costs: float | None = None, revenue: float | None = None, **kwargs):
    return build_result(
        fid="operating_ratio",
        name="Operating Ratio %",
        expression="Operating_Costs / Revenue * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "operating_costs": kwargs.get("operating_costs", operating_costs),
            "revenue": kwargs.get("revenue", revenue),
        },
    )

@formula("cost_of_revenue_ratio", "Cost of Revenue Ratio %", "COGS / Revenue * 100", DOMAIN_KEY, unit="")
def cost_of_revenue_ratio(cogs: float | None = None, revenue: float | None = None, **kwargs):
    return build_result(
        fid="cost_of_revenue_ratio",
        name="Cost of Revenue Ratio %",
        expression="COGS / Revenue * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cogs": kwargs.get("cogs", cogs),
            "revenue": kwargs.get("revenue", revenue),
        },
    )

@formula("overhead_ratio", "Overhead Ratio %", "Operating_Expenses / (Net_Interest + Operating_Income) * 100", DOMAIN_KEY, unit="")
def overhead_ratio(operating_expenses: float | None = None, net_interest: float | None = None, operating_income: float | None = None, **kwargs):
    return build_result(
        fid="overhead_ratio",
        name="Overhead Ratio %",
        expression="Operating_Expenses / (Net_Interest + Operating_Income) * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "operating_expenses": kwargs.get("operating_expenses", operating_expenses),
            "net_interest": kwargs.get("net_interest", net_interest),
            "operating_income": kwargs.get("operating_income", operating_income),
        },
    )

@formula("sga_ratio", "SG&A to Revenue %", "SGA / Revenue * 100", DOMAIN_KEY, unit="")
def sga_ratio(sga: float | None = None, revenue: float | None = None, **kwargs):
    return build_result(
        fid="sga_ratio",
        name="SG&A to Revenue %",
        expression="SGA / Revenue * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "sga": kwargs.get("sga", sga),
            "revenue": kwargs.get("revenue", revenue),
        },
    )

@formula("rnd_ratio", "R&D to Revenue %", "RnD / Revenue * 100", DOMAIN_KEY, unit="")
def rnd_ratio(rnd: float | None = None, revenue: float | None = None, **kwargs):
    return build_result(
        fid="rnd_ratio",
        name="R&D to Revenue %",
        expression="RnD / Revenue * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "rnd": kwargs.get("rnd", rnd),
            "revenue": kwargs.get("revenue", revenue),
        },
    )

@formula("rnd_intensity", "R&D Intensity %", "RnD_Expense / Revenue * 100", DOMAIN_KEY, unit="")
def rnd_intensity(rnd_expense: float | None = None, revenue: float | None = None, **kwargs):
    return build_result(
        fid="rnd_intensity",
        name="R&D Intensity %",
        expression="RnD_Expense / Revenue * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "rnd_expense": kwargs.get("rnd_expense", rnd_expense),
            "revenue": kwargs.get("revenue", revenue),
        },
    )

@formula("net_income_growth", "Net Income Growth %", "(NI_Current - NI_Prior) / NI_Prior * 100", DOMAIN_KEY, unit="")
def net_income_growth(ni_current: float | None = None, ni_prior: float | None = None, **kwargs):
    return build_result(
        fid="net_income_growth",
        name="Net Income Growth %",
        expression="(NI_Current - NI_Prior) / NI_Prior * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ni_current": kwargs.get("ni_current", ni_current),
            "ni_prior": kwargs.get("ni_prior", ni_prior),
        },
    )

@formula("revenue_growth", "Revenue Growth %", "(Rev_Current - Rev_Prior) / Rev_Prior * 100", DOMAIN_KEY, unit="")
def revenue_growth(rev_current: float | None = None, rev_prior: float | None = None, **kwargs):
    return build_result(
        fid="revenue_growth",
        name="Revenue Growth %",
        expression="(Rev_Current - Rev_Prior) / Rev_Prior * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "rev_current": kwargs.get("rev_current", rev_current),
            "rev_prior": kwargs.get("rev_prior", rev_prior),
        },
    )

@formula("operating_income_growth", "Operating Income Growth %", "(OI_Current - OI_Prior) / OI_Prior * 100", DOMAIN_KEY, unit="")
def operating_income_growth(oi_current: float | None = None, oi_prior: float | None = None, **kwargs):
    return build_result(
        fid="operating_income_growth",
        name="Operating Income Growth %",
        expression="(OI_Current - OI_Prior) / OI_Prior * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "oi_current": kwargs.get("oi_current", oi_current),
            "oi_prior": kwargs.get("oi_prior", oi_prior),
        },
    )

@formula("eps_basic", "Basic EPS", "(Net_Income - Pref_Dividends) / Basic_Shares", DOMAIN_KEY, unit="")
def eps_basic(net_income: float | None = None, pref_dividends: float | None = None, basic_shares: float | None = None, **kwargs):
    return build_result(
        fid="eps_basic",
        name="Basic EPS",
        expression="(Net_Income - Pref_Dividends) / Basic_Shares",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_income": kwargs.get("net_income", net_income),
            "pref_dividends": kwargs.get("pref_dividends", pref_dividends),
            "basic_shares": kwargs.get("basic_shares", basic_shares),
        },
    )

@formula("eps_diluted", "Diluted EPS", "(Net_Income - Pref_Dividends) / Diluted_Shares", DOMAIN_KEY, unit="")
def eps_diluted(net_income: float | None = None, pref_dividends: float | None = None, diluted_shares: float | None = None, **kwargs):
    return build_result(
        fid="eps_diluted",
        name="Diluted EPS",
        expression="(Net_Income - Pref_Dividends) / Diluted_Shares",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_income": kwargs.get("net_income", net_income),
            "pref_dividends": kwargs.get("pref_dividends", pref_dividends),
            "diluted_shares": kwargs.get("diluted_shares", diluted_shares),
        },
    )

@formula("eps_growth", "EPS Growth %", "(EPS_Current - EPS_Prior) / EPS_Prior * 100", DOMAIN_KEY, unit="")
def eps_growth(eps_current: float | None = None, eps_prior: float | None = None, **kwargs):
    return build_result(
        fid="eps_growth",
        name="EPS Growth %",
        expression="(EPS_Current - EPS_Prior) / EPS_Prior * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "eps_current": kwargs.get("eps_current", eps_current),
            "eps_prior": kwargs.get("eps_prior", eps_prior),
        },
    )

@formula("cash_return_on_assets", "Cash Return on Assets %", "OCF / Total_Assets * 100", DOMAIN_KEY, unit="")
def cash_return_on_assets(ocf: float | None = None, total_assets: float | None = None, **kwargs):
    return build_result(
        fid="cash_return_on_assets",
        name="Cash Return on Assets %",
        expression="OCF / Total_Assets * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ocf": kwargs.get("ocf", ocf),
            "total_assets": kwargs.get("total_assets", total_assets),
        },
    )

@formula("cash_roe", "Cash Return on Equity %", "OCF / Shareholders_Equity * 100", DOMAIN_KEY, unit="")
def cash_roe(ocf: float | None = None, shareholders_equity: float | None = None, **kwargs):
    return build_result(
        fid="cash_roe",
        name="Cash Return on Equity %",
        expression="OCF / Shareholders_Equity * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ocf": kwargs.get("ocf", ocf),
            "shareholders_equity": kwargs.get("shareholders_equity", shareholders_equity),
        },
    )

@formula("gross_profit_growth", "Gross Profit Growth %", "(GP_Current - GP_Prior) / GP_Prior * 100", DOMAIN_KEY, unit="")
def gross_profit_growth(gp_current: float | None = None, gp_prior: float | None = None, **kwargs):
    return build_result(
        fid="gross_profit_growth",
        name="Gross Profit Growth %",
        expression="(GP_Current - GP_Prior) / GP_Prior * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "gp_current": kwargs.get("gp_current", gp_current),
            "gp_prior": kwargs.get("gp_prior", gp_prior),
        },
    )

@formula("ebitda_growth", "EBITDA Growth %", "(EBITDA_Current - EBITDA_Prior) / EBITDA_Prior * 100", DOMAIN_KEY, unit="")
def ebitda_growth(ebitda_current: float | None = None, ebitda_prior: float | None = None, **kwargs):
    return build_result(
        fid="ebitda_growth",
        name="EBITDA Growth %",
        expression="(EBITDA_Current - EBITDA_Prior) / EBITDA_Prior * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ebitda_current": kwargs.get("ebitda_current", ebitda_current),
            "ebitda_prior": kwargs.get("ebitda_prior", ebitda_prior),
        },
    )

@formula("incremental_margin", "Incremental Margin %", "Delta_Profit / Delta_Revenue * 100", DOMAIN_KEY, unit="")
def incremental_margin(delta_profit: float | None = None, delta_revenue: float | None = None, **kwargs):
    return build_result(
        fid="incremental_margin",
        name="Incremental Margin %",
        expression="Delta_Profit / Delta_Revenue * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "delta_profit": kwargs.get("delta_profit", delta_profit),
            "delta_revenue": kwargs.get("delta_revenue", delta_revenue),
        },
    )

@formula("breakeven_point_units", "Breakeven Point (Units)", "Fixed_Costs / (Price - Variable_Cost_Per_Unit)", DOMAIN_KEY, unit="")
def breakeven_point_units(fixed_costs: float | None = None, price: float | None = None, variable_cost_per_unit: float | None = None, **kwargs):
    return build_result(
        fid="breakeven_point_units",
        name="Breakeven Point (Units)",
        expression="Fixed_Costs / (Price - Variable_Cost_Per_Unit)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "fixed_costs": kwargs.get("fixed_costs", fixed_costs),
            "price": kwargs.get("price", price),
            "variable_cost_per_unit": kwargs.get("variable_cost_per_unit", variable_cost_per_unit),
        },
    )

@formula("breakeven_point_revenue", "Breakeven Point (Revenue)", "Fixed_Costs / Contribution_Margin_Ratio", DOMAIN_KEY, unit="")
def breakeven_point_revenue(fixed_costs: float | None = None, contribution_margin_ratio: float | None = None, **kwargs):
    return build_result(
        fid="breakeven_point_revenue",
        name="Breakeven Point (Revenue)",
        expression="Fixed_Costs / Contribution_Margin_Ratio",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "fixed_costs": kwargs.get("fixed_costs", fixed_costs),
            "contribution_margin_ratio": kwargs.get("contribution_margin_ratio", contribution_margin_ratio),
        },
    )

@formula("margin_of_safety", "Margin of Safety %", "(Sales - Breakeven_Sales) / Sales * 100", DOMAIN_KEY, unit="")
def margin_of_safety(sales: float | None = None, breakeven_sales: float | None = None, **kwargs):
    return build_result(
        fid="margin_of_safety",
        name="Margin of Safety %",
        expression="(Sales - Breakeven_Sales) / Sales * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "sales": kwargs.get("sales", sales),
            "breakeven_sales": kwargs.get("breakeven_sales", breakeven_sales),
        },
    )
