from .base import build_result, formula

DOMAIN_KEY = "D02_liquidity_solvency"
DOMAIN_TITLE = "Liquidity, Solvency & Efficiency Ratios"
FORMULA_IDS = [
    "current_ratio",
    "quick_ratio",
    "cash_ratio",
    "operating_cash_flow_ratio",
    "working_capital",
    "working_capital_ratio",
    "net_working_capital_to_sales",
    "defensive_interval_ratio",
    "debt_to_equity",
    "debt_to_assets",
    "debt_to_capital",
    "debt_to_ebitda",
    "net_debt",
    "net_debt_to_ebitda",
    "equity_ratio",
    "financial_leverage_ratio",
    "interest_coverage",
    "ebitda_coverage",
    "fixed_charge_coverage",
    "times_interest_earned",
    "debt_service_coverage",
    "cash_flow_to_debt",
    "capitalization_ratio",
    "asset_turnover",
    "fixed_asset_turnover",
    "inventory_turnover",
    "receivables_turnover",
    "payables_turnover",
    "working_capital_turnover",
    "equity_turnover",
    "total_capital_turnover",
    "days_sales_outstanding",
    "days_inventory_outstanding",
    "days_payable_outstanding",
    "cash_conversion_cycle",
    "operating_cycle",
    "dso_direct",
    "dio_direct",
    "dpo_direct",
    "capital_intensity",
    "capital_intensity_assets",
    "fixed_assets_to_equity",
    "long_term_debt_to_equity",
    "short_term_debt_ratio",
    "current_liabilities_ratio",
    "solvency_ratio",
    "financial_autonomy_ratio",
    "net_gearing",
    "altman_z_score",
    "piotroski_f_score",
]

@formula("current_ratio", "Current Ratio", "Current_Assets / Current_Liabilities", DOMAIN_KEY, unit="")
def current_ratio(current_assets: float | None = None, current_liabilities: float | None = None, **kwargs):
    return build_result(
        fid="current_ratio",
        name="Current Ratio",
        expression="Current_Assets / Current_Liabilities",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "current_assets": kwargs.get("current_assets", current_assets),
            "current_liabilities": kwargs.get("current_liabilities", current_liabilities),
        },
    )

@formula("quick_ratio", "Quick Ratio (Acid Test)", "(Current_Assets - Inventory) / Current_Liabilities", DOMAIN_KEY, unit="")
def quick_ratio(current_assets: float | None = None, inventory: float | None = None, current_liabilities: float | None = None, **kwargs):
    return build_result(
        fid="quick_ratio",
        name="Quick Ratio (Acid Test)",
        expression="(Current_Assets - Inventory) / Current_Liabilities",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "current_assets": kwargs.get("current_assets", current_assets),
            "inventory": kwargs.get("inventory", inventory),
            "current_liabilities": kwargs.get("current_liabilities", current_liabilities),
        },
    )

@formula("cash_ratio", "Cash Ratio", "(Cash + Marketable_Securities) / Current_Liabilities", DOMAIN_KEY, unit="")
def cash_ratio(cash: float | None = None, marketable_securities: float | None = None, current_liabilities: float | None = None, **kwargs):
    return build_result(
        fid="cash_ratio",
        name="Cash Ratio",
        expression="(Cash + Marketable_Securities) / Current_Liabilities",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cash": kwargs.get("cash", cash),
            "marketable_securities": kwargs.get("marketable_securities", marketable_securities),
            "current_liabilities": kwargs.get("current_liabilities", current_liabilities),
        },
    )

@formula("operating_cash_flow_ratio", "Operating Cash Flow Ratio", "OCF / Current_Liabilities", DOMAIN_KEY, unit="")
def operating_cash_flow_ratio(ocf: float | None = None, current_liabilities: float | None = None, **kwargs):
    return build_result(
        fid="operating_cash_flow_ratio",
        name="Operating Cash Flow Ratio",
        expression="OCF / Current_Liabilities",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ocf": kwargs.get("ocf", ocf),
            "current_liabilities": kwargs.get("current_liabilities", current_liabilities),
        },
    )

@formula("working_capital", "Working Capital", "Current_Assets - Current_Liabilities", DOMAIN_KEY, unit="")
def working_capital(current_assets: float | None = None, current_liabilities: float | None = None, **kwargs):
    return build_result(
        fid="working_capital",
        name="Working Capital",
        expression="Current_Assets - Current_Liabilities",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "current_assets": kwargs.get("current_assets", current_assets),
            "current_liabilities": kwargs.get("current_liabilities", current_liabilities),
        },
    )

@formula("working_capital_ratio", "Working Capital Ratio", "Current_Assets / Current_Liabilities", DOMAIN_KEY, unit="")
def working_capital_ratio(current_assets: float | None = None, current_liabilities: float | None = None, **kwargs):
    return build_result(
        fid="working_capital_ratio",
        name="Working Capital Ratio",
        expression="Current_Assets / Current_Liabilities",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "current_assets": kwargs.get("current_assets", current_assets),
            "current_liabilities": kwargs.get("current_liabilities", current_liabilities),
        },
    )

@formula("net_working_capital_to_sales", "NWC to Sales %", "Working_Capital / Sales * 100", DOMAIN_KEY, unit="")
def net_working_capital_to_sales(working_capital: float | None = None, sales: float | None = None, **kwargs):
    return build_result(
        fid="net_working_capital_to_sales",
        name="NWC to Sales %",
        expression="Working_Capital / Sales * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "working_capital": kwargs.get("working_capital", working_capital),
            "sales": kwargs.get("sales", sales),
        },
    )

@formula("defensive_interval_ratio", "Defensive Interval Ratio (days)", "Liquid_Assets / Daily_Operating_Expenses", DOMAIN_KEY, unit="")
def defensive_interval_ratio(liquid_assets: float | None = None, daily_operating_expenses: float | None = None, **kwargs):
    return build_result(
        fid="defensive_interval_ratio",
        name="Defensive Interval Ratio (days)",
        expression="Liquid_Assets / Daily_Operating_Expenses",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "liquid_assets": kwargs.get("liquid_assets", liquid_assets),
            "daily_operating_expenses": kwargs.get("daily_operating_expenses", daily_operating_expenses),
        },
    )

@formula("debt_to_equity", "Debt-to-Equity", "Total_Debt / Shareholders_Equity", DOMAIN_KEY, unit="")
def debt_to_equity(total_debt: float | None = None, shareholders_equity: float | None = None, **kwargs):
    return build_result(
        fid="debt_to_equity",
        name="Debt-to-Equity",
        expression="Total_Debt / Shareholders_Equity",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "total_debt": kwargs.get("total_debt", total_debt),
            "shareholders_equity": kwargs.get("shareholders_equity", shareholders_equity),
        },
    )

@formula("debt_to_assets", "Debt-to-Assets", "Total_Debt / Total_Assets", DOMAIN_KEY, unit="")
def debt_to_assets(total_debt: float | None = None, total_assets: float | None = None, **kwargs):
    return build_result(
        fid="debt_to_assets",
        name="Debt-to-Assets",
        expression="Total_Debt / Total_Assets",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "total_debt": kwargs.get("total_debt", total_debt),
            "total_assets": kwargs.get("total_assets", total_assets),
        },
    )

@formula("debt_to_capital", "Debt-to-Capital", "Total_Debt / (Total_Debt + Shareholders_Equity)", DOMAIN_KEY, unit="")
def debt_to_capital(total_debt: float | None = None, shareholders_equity: float | None = None, **kwargs):
    return build_result(
        fid="debt_to_capital",
        name="Debt-to-Capital",
        expression="Total_Debt / (Total_Debt + Shareholders_Equity)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "total_debt": kwargs.get("total_debt", total_debt),
            "shareholders_equity": kwargs.get("shareholders_equity", shareholders_equity),
        },
    )

@formula("debt_to_ebitda", "Debt-to-EBITDA", "Total_Debt / EBITDA", DOMAIN_KEY, unit="")
def debt_to_ebitda(total_debt: float | None = None, ebitda: float | None = None, **kwargs):
    return build_result(
        fid="debt_to_ebitda",
        name="Debt-to-EBITDA",
        expression="Total_Debt / EBITDA",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "total_debt": kwargs.get("total_debt", total_debt),
            "ebitda": kwargs.get("ebitda", ebitda),
        },
    )

@formula("net_debt", "Net Debt", "Total_Debt - Cash", DOMAIN_KEY, unit="")
def net_debt(total_debt: float | None = None, cash: float | None = None, **kwargs):
    return build_result(
        fid="net_debt",
        name="Net Debt",
        expression="Total_Debt - Cash",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "total_debt": kwargs.get("total_debt", total_debt),
            "cash": kwargs.get("cash", cash),
        },
    )

@formula("net_debt_to_ebitda", "Net Debt-to-EBITDA", "(Total_Debt - Cash) / EBITDA", DOMAIN_KEY, unit="")
def net_debt_to_ebitda(total_debt: float | None = None, cash: float | None = None, ebitda: float | None = None, **kwargs):
    return build_result(
        fid="net_debt_to_ebitda",
        name="Net Debt-to-EBITDA",
        expression="(Total_Debt - Cash) / EBITDA",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "total_debt": kwargs.get("total_debt", total_debt),
            "cash": kwargs.get("cash", cash),
            "ebitda": kwargs.get("ebitda", ebitda),
        },
    )

@formula("equity_ratio", "Equity Ratio", "Shareholders_Equity / Total_Assets", DOMAIN_KEY, unit="")
def equity_ratio(shareholders_equity: float | None = None, total_assets: float | None = None, **kwargs):
    return build_result(
        fid="equity_ratio",
        name="Equity Ratio",
        expression="Shareholders_Equity / Total_Assets",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "shareholders_equity": kwargs.get("shareholders_equity", shareholders_equity),
            "total_assets": kwargs.get("total_assets", total_assets),
        },
    )

@formula("financial_leverage_ratio", "Financial Leverage Ratio", "Total_Assets / Shareholders_Equity", DOMAIN_KEY, unit="")
def financial_leverage_ratio(total_assets: float | None = None, shareholders_equity: float | None = None, **kwargs):
    return build_result(
        fid="financial_leverage_ratio",
        name="Financial Leverage Ratio",
        expression="Total_Assets / Shareholders_Equity",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "total_assets": kwargs.get("total_assets", total_assets),
            "shareholders_equity": kwargs.get("shareholders_equity", shareholders_equity),
        },
    )

@formula("interest_coverage", "Interest Coverage Ratio", "EBIT / Interest_Expense", DOMAIN_KEY, unit="")
def interest_coverage(ebit: float | None = None, interest_expense: float | None = None, **kwargs):
    return build_result(
        fid="interest_coverage",
        name="Interest Coverage Ratio",
        expression="EBIT / Interest_Expense",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ebit": kwargs.get("ebit", ebit),
            "interest_expense": kwargs.get("interest_expense", interest_expense),
        },
    )

@formula("ebitda_coverage", "EBITDA Coverage Ratio", "EBITDA / Interest_Expense", DOMAIN_KEY, unit="")
def ebitda_coverage(ebitda: float | None = None, interest_expense: float | None = None, **kwargs):
    return build_result(
        fid="ebitda_coverage",
        name="EBITDA Coverage Ratio",
        expression="EBITDA / Interest_Expense",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ebitda": kwargs.get("ebitda", ebitda),
            "interest_expense": kwargs.get("interest_expense", interest_expense),
        },
    )

@formula("fixed_charge_coverage", "Fixed Charge Coverage", "(EBIT + Lease_Payments) / (Interest_Expense + Lease_Payments)", DOMAIN_KEY, unit="")
def fixed_charge_coverage(ebit: float | None = None, lease_payments: float | None = None, interest_expense: float | None = None, **kwargs):
    return build_result(
        fid="fixed_charge_coverage",
        name="Fixed Charge Coverage",
        expression="(EBIT + Lease_Payments) / (Interest_Expense + Lease_Payments)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ebit": kwargs.get("ebit", ebit),
            "lease_payments": kwargs.get("lease_payments", lease_payments),
            "interest_expense": kwargs.get("interest_expense", interest_expense),
        },
    )

@formula("times_interest_earned", "Times Interest Earned", "EBIT / Interest_Expense", DOMAIN_KEY, unit="")
def times_interest_earned(ebit: float | None = None, interest_expense: float | None = None, **kwargs):
    return build_result(
        fid="times_interest_earned",
        name="Times Interest Earned",
        expression="EBIT / Interest_Expense",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ebit": kwargs.get("ebit", ebit),
            "interest_expense": kwargs.get("interest_expense", interest_expense),
        },
    )

@formula("debt_service_coverage", "Debt Service Coverage Ratio (DSCR)", "Net_Operating_Income / Total_Debt_Service", DOMAIN_KEY, unit="")
def debt_service_coverage(net_operating_income: float | None = None, total_debt_service: float | None = None, **kwargs):
    return build_result(
        fid="debt_service_coverage",
        name="Debt Service Coverage Ratio (DSCR)",
        expression="Net_Operating_Income / Total_Debt_Service",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_operating_income": kwargs.get("net_operating_income", net_operating_income),
            "total_debt_service": kwargs.get("total_debt_service", total_debt_service),
        },
    )

@formula("cash_flow_to_debt", "Cash Flow to Debt", "OCF / Total_Debt", DOMAIN_KEY, unit="")
def cash_flow_to_debt(ocf: float | None = None, total_debt: float | None = None, **kwargs):
    return build_result(
        fid="cash_flow_to_debt",
        name="Cash Flow to Debt",
        expression="OCF / Total_Debt",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ocf": kwargs.get("ocf", ocf),
            "total_debt": kwargs.get("total_debt", total_debt),
        },
    )

@formula("capitalization_ratio", "Capitalization Ratio", "Long_Term_Debt / (Long_Term_Debt + Shareholders_Equity)", DOMAIN_KEY, unit="")
def capitalization_ratio(long_term_debt: float | None = None, shareholders_equity: float | None = None, **kwargs):
    return build_result(
        fid="capitalization_ratio",
        name="Capitalization Ratio",
        expression="Long_Term_Debt / (Long_Term_Debt + Shareholders_Equity)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "long_term_debt": kwargs.get("long_term_debt", long_term_debt),
            "shareholders_equity": kwargs.get("shareholders_equity", shareholders_equity),
        },
    )

@formula("asset_turnover", "Asset Turnover", "Revenue / Total_Assets", DOMAIN_KEY, unit="")
def asset_turnover(revenue: float | None = None, total_assets: float | None = None, **kwargs):
    return build_result(
        fid="asset_turnover",
        name="Asset Turnover",
        expression="Revenue / Total_Assets",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "revenue": kwargs.get("revenue", revenue),
            "total_assets": kwargs.get("total_assets", total_assets),
        },
    )

@formula("fixed_asset_turnover", "Fixed Asset Turnover", "Revenue / Net_PPE", DOMAIN_KEY, unit="")
def fixed_asset_turnover(revenue: float | None = None, net_ppe: float | None = None, **kwargs):
    return build_result(
        fid="fixed_asset_turnover",
        name="Fixed Asset Turnover",
        expression="Revenue / Net_PPE",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "revenue": kwargs.get("revenue", revenue),
            "net_ppe": kwargs.get("net_ppe", net_ppe),
        },
    )

@formula("inventory_turnover", "Inventory Turnover", "COGS / Average_Inventory", DOMAIN_KEY, unit="")
def inventory_turnover(cogs: float | None = None, average_inventory: float | None = None, **kwargs):
    return build_result(
        fid="inventory_turnover",
        name="Inventory Turnover",
        expression="COGS / Average_Inventory",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cogs": kwargs.get("cogs", cogs),
            "average_inventory": kwargs.get("average_inventory", average_inventory),
        },
    )

@formula("receivables_turnover", "Receivables Turnover", "Revenue / Average_Receivables", DOMAIN_KEY, unit="")
def receivables_turnover(revenue: float | None = None, average_receivables: float | None = None, **kwargs):
    return build_result(
        fid="receivables_turnover",
        name="Receivables Turnover",
        expression="Revenue / Average_Receivables",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "revenue": kwargs.get("revenue", revenue),
            "average_receivables": kwargs.get("average_receivables", average_receivables),
        },
    )

@formula("payables_turnover", "Payables Turnover", "COGS / Average_Payables", DOMAIN_KEY, unit="")
def payables_turnover(cogs: float | None = None, average_payables: float | None = None, **kwargs):
    return build_result(
        fid="payables_turnover",
        name="Payables Turnover",
        expression="COGS / Average_Payables",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cogs": kwargs.get("cogs", cogs),
            "average_payables": kwargs.get("average_payables", average_payables),
        },
    )

@formula("working_capital_turnover", "Working Capital Turnover", "Revenue / Working_Capital", DOMAIN_KEY, unit="")
def working_capital_turnover(revenue: float | None = None, working_capital: float | None = None, **kwargs):
    return build_result(
        fid="working_capital_turnover",
        name="Working Capital Turnover",
        expression="Revenue / Working_Capital",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "revenue": kwargs.get("revenue", revenue),
            "working_capital": kwargs.get("working_capital", working_capital),
        },
    )

@formula("equity_turnover", "Equity Turnover", "Revenue / Shareholders_Equity", DOMAIN_KEY, unit="")
def equity_turnover(revenue: float | None = None, shareholders_equity: float | None = None, **kwargs):
    return build_result(
        fid="equity_turnover",
        name="Equity Turnover",
        expression="Revenue / Shareholders_Equity",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "revenue": kwargs.get("revenue", revenue),
            "shareholders_equity": kwargs.get("shareholders_equity", shareholders_equity),
        },
    )

@formula("total_capital_turnover", "Total Capital Turnover", "Revenue / Total_Capital", DOMAIN_KEY, unit="")
def total_capital_turnover(revenue: float | None = None, total_capital: float | None = None, **kwargs):
    return build_result(
        fid="total_capital_turnover",
        name="Total Capital Turnover",
        expression="Revenue / Total_Capital",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "revenue": kwargs.get("revenue", revenue),
            "total_capital": kwargs.get("total_capital", total_capital),
        },
    )

@formula("days_sales_outstanding", "Days Sales Outstanding (DSO)", "365 / Receivables_Turnover", DOMAIN_KEY, unit="")
def days_sales_outstanding(receivables_turnover: float | None = None, **kwargs):
    return build_result(
        fid="days_sales_outstanding",
        name="Days Sales Outstanding (DSO)",
        expression="365 / Receivables_Turnover",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "receivables_turnover": kwargs.get("receivables_turnover", receivables_turnover),
        },
    )

@formula("days_inventory_outstanding", "Days Inventory Outstanding (DIO)", "365 / Inventory_Turnover", DOMAIN_KEY, unit="")
def days_inventory_outstanding(inventory_turnover: float | None = None, **kwargs):
    return build_result(
        fid="days_inventory_outstanding",
        name="Days Inventory Outstanding (DIO)",
        expression="365 / Inventory_Turnover",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "inventory_turnover": kwargs.get("inventory_turnover", inventory_turnover),
        },
    )

@formula("days_payable_outstanding", "Days Payable Outstanding (DPO)", "365 / Payables_Turnover", DOMAIN_KEY, unit="")
def days_payable_outstanding(payables_turnover: float | None = None, **kwargs):
    return build_result(
        fid="days_payable_outstanding",
        name="Days Payable Outstanding (DPO)",
        expression="365 / Payables_Turnover",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "payables_turnover": kwargs.get("payables_turnover", payables_turnover),
        },
    )

@formula("cash_conversion_cycle", "Cash Conversion Cycle (days)", "DSO + DIO - DPO", DOMAIN_KEY, unit="")
def cash_conversion_cycle(dso: float | None = None, dio: float | None = None, dpo: float | None = None, **kwargs):
    return build_result(
        fid="cash_conversion_cycle",
        name="Cash Conversion Cycle (days)",
        expression="DSO + DIO - DPO",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "dso": kwargs.get("dso", dso),
            "dio": kwargs.get("dio", dio),
            "dpo": kwargs.get("dpo", dpo),
        },
    )

@formula("operating_cycle", "Operating Cycle (days)", "DSO + DIO", DOMAIN_KEY, unit="")
def operating_cycle(dso: float | None = None, dio: float | None = None, **kwargs):
    return build_result(
        fid="operating_cycle",
        name="Operating Cycle (days)",
        expression="DSO + DIO",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "dso": kwargs.get("dso", dso),
            "dio": kwargs.get("dio", dio),
        },
    )

@formula("dso_direct", "DSO Direct", "Receivables / Revenue * 365", DOMAIN_KEY, unit="")
def dso_direct(receivables: float | None = None, revenue: float | None = None, **kwargs):
    return build_result(
        fid="dso_direct",
        name="DSO Direct",
        expression="Receivables / Revenue * 365",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "receivables": kwargs.get("receivables", receivables),
            "revenue": kwargs.get("revenue", revenue),
        },
    )

@formula("dio_direct", "DIO Direct", "Inventory / COGS * 365", DOMAIN_KEY, unit="")
def dio_direct(inventory: float | None = None, cogs: float | None = None, **kwargs):
    return build_result(
        fid="dio_direct",
        name="DIO Direct",
        expression="Inventory / COGS * 365",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "inventory": kwargs.get("inventory", inventory),
            "cogs": kwargs.get("cogs", cogs),
        },
    )

@formula("dpo_direct", "DPO Direct", "Payables / COGS * 365", DOMAIN_KEY, unit="")
def dpo_direct(payables: float | None = None, cogs: float | None = None, **kwargs):
    return build_result(
        fid="dpo_direct",
        name="DPO Direct",
        expression="Payables / COGS * 365",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "payables": kwargs.get("payables", payables),
            "cogs": kwargs.get("cogs", cogs),
        },
    )

@formula("capital_intensity", "Capital Intensity %", "CapEx / Revenue * 100", DOMAIN_KEY, unit="")
def capital_intensity(capex: float | None = None, revenue: float | None = None, **kwargs):
    return build_result(
        fid="capital_intensity",
        name="Capital Intensity %",
        expression="CapEx / Revenue * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "capex": kwargs.get("capex", capex),
            "revenue": kwargs.get("revenue", revenue),
        },
    )

@formula("capital_intensity_assets", "Capital Intensity (Assets)", "Total_Assets / Revenue", DOMAIN_KEY, unit="")
def capital_intensity_assets(total_assets: float | None = None, revenue: float | None = None, **kwargs):
    return build_result(
        fid="capital_intensity_assets",
        name="Capital Intensity (Assets)",
        expression="Total_Assets / Revenue",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "total_assets": kwargs.get("total_assets", total_assets),
            "revenue": kwargs.get("revenue", revenue),
        },
    )

@formula("fixed_assets_to_equity", "Fixed Assets to Equity", "Net_PPE / Shareholders_Equity", DOMAIN_KEY, unit="")
def fixed_assets_to_equity(net_ppe: float | None = None, shareholders_equity: float | None = None, **kwargs):
    return build_result(
        fid="fixed_assets_to_equity",
        name="Fixed Assets to Equity",
        expression="Net_PPE / Shareholders_Equity",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_ppe": kwargs.get("net_ppe", net_ppe),
            "shareholders_equity": kwargs.get("shareholders_equity", shareholders_equity),
        },
    )

@formula("long_term_debt_to_equity", "LT Debt to Equity", "Long_Term_Debt / Shareholders_Equity", DOMAIN_KEY, unit="")
def long_term_debt_to_equity(long_term_debt: float | None = None, shareholders_equity: float | None = None, **kwargs):
    return build_result(
        fid="long_term_debt_to_equity",
        name="LT Debt to Equity",
        expression="Long_Term_Debt / Shareholders_Equity",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "long_term_debt": kwargs.get("long_term_debt", long_term_debt),
            "shareholders_equity": kwargs.get("shareholders_equity", shareholders_equity),
        },
    )

@formula("short_term_debt_ratio", "Short-Term Debt Ratio", "Short_Term_Debt / Total_Debt", DOMAIN_KEY, unit="")
def short_term_debt_ratio(short_term_debt: float | None = None, total_debt: float | None = None, **kwargs):
    return build_result(
        fid="short_term_debt_ratio",
        name="Short-Term Debt Ratio",
        expression="Short_Term_Debt / Total_Debt",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "short_term_debt": kwargs.get("short_term_debt", short_term_debt),
            "total_debt": kwargs.get("total_debt", total_debt),
        },
    )

@formula("current_liabilities_ratio", "Current Liabilities Ratio", "Current_Liabilities / Total_Liabilities", DOMAIN_KEY, unit="")
def current_liabilities_ratio(current_liabilities: float | None = None, total_liabilities: float | None = None, **kwargs):
    return build_result(
        fid="current_liabilities_ratio",
        name="Current Liabilities Ratio",
        expression="Current_Liabilities / Total_Liabilities",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "current_liabilities": kwargs.get("current_liabilities", current_liabilities),
            "total_liabilities": kwargs.get("total_liabilities", total_liabilities),
        },
    )

@formula("solvency_ratio", "Solvency Ratio", "(Net_Income + Depreciation) / Total_Liabilities", DOMAIN_KEY, unit="")
def solvency_ratio(net_income: float | None = None, depreciation: float | None = None, total_liabilities: float | None = None, **kwargs):
    return build_result(
        fid="solvency_ratio",
        name="Solvency Ratio",
        expression="(Net_Income + Depreciation) / Total_Liabilities",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_income": kwargs.get("net_income", net_income),
            "depreciation": kwargs.get("depreciation", depreciation),
            "total_liabilities": kwargs.get("total_liabilities", total_liabilities),
        },
    )

@formula("financial_autonomy_ratio", "Financial Autonomy Ratio", "Shareholders_Equity / Total_Liabilities", DOMAIN_KEY, unit="")
def financial_autonomy_ratio(shareholders_equity: float | None = None, total_liabilities: float | None = None, **kwargs):
    return build_result(
        fid="financial_autonomy_ratio",
        name="Financial Autonomy Ratio",
        expression="Shareholders_Equity / Total_Liabilities",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "shareholders_equity": kwargs.get("shareholders_equity", shareholders_equity),
            "total_liabilities": kwargs.get("total_liabilities", total_liabilities),
        },
    )

@formula("net_gearing", "Net Gearing %", "(Total_Debt - Cash) / Shareholders_Equity * 100", DOMAIN_KEY, unit="")
def net_gearing(total_debt: float | None = None, cash: float | None = None, shareholders_equity: float | None = None, **kwargs):
    return build_result(
        fid="net_gearing",
        name="Net Gearing %",
        expression="(Total_Debt - Cash) / Shareholders_Equity * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "total_debt": kwargs.get("total_debt", total_debt),
            "cash": kwargs.get("cash", cash),
            "shareholders_equity": kwargs.get("shareholders_equity", shareholders_equity),
        },
    )

@formula("altman_z_score", "Altman Z-Score", "1.2*A + 1.4*B + 3.3*C + 0.6*D + 1.0*E", DOMAIN_KEY, unit="")
def altman_z_score(a: float | None = None, b: float | None = None, c: float | None = None, d: float | None = None, e: float | None = None, **kwargs):
    return build_result(
        fid="altman_z_score",
        name="Altman Z-Score",
        expression="1.2*A + 1.4*B + 3.3*C + 0.6*D + 1.0*E",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "a": kwargs.get("a", a),
            "b": kwargs.get("b", b),
            "c": kwargs.get("c", c),
            "d": kwargs.get("d", d),
            "e": kwargs.get("e", e),
        },
    )

@formula("piotroski_f_score", "Piotroski F-Score", "Sum of 9 binary signals", DOMAIN_KEY, unit="")
def piotroski_f_score(signals_list: float | None = None, **kwargs):
    return build_result(
        fid="piotroski_f_score",
        name="Piotroski F-Score",
        expression="Sum of 9 binary signals",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "signals_list": kwargs.get("signals_list", signals_list),
        },
    )
