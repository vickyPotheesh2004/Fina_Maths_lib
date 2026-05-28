from .base import build_result, formula

DOMAIN_KEY = "D10_accounting"
DOMAIN_TITLE = "Accounting & Depreciation"
FORMULA_IDS = [
    "straight_line_depreciation",
    "declining_balance",
    "double_declining_balance",
    "units_of_production",
    "sum_of_years_digits",
    "macrs_depreciation",
    "accumulated_depreciation",
    "book_value_asset",
    "depreciation_rate",
    "amortization_intangible",
    "depletion",
    "fifo_cogs",
    "lifo_cogs",
    "weighted_average_cost",
    "lifo_reserve",
    "inventory_write_down",
    "ending_inventory",
    "cogs_calculation",
    "gross_profit_method",
    "bad_debt_percentage_sales",
    "bad_debt_aging",
    "allowance_doubtful_accounts",
    "net_realizable_value",
    "deferred_tax_liability",
    "deferred_tax_asset",
    "effective_tax_rate_acct",
    "stock_compensation_expense",
    "pension_pbo",
    "pension_funded_status",
    "pension_expense",
    "operating_lease_expense",
    "finance_lease_liability",
    "right_of_use_asset",
    "capitalized_interest",
    "revenue_recognition_percentage",
    "deferred_revenue",
    "comprehensive_income",
    "retained_earnings_ending",
    "goodwill_impairment",
    "asset_impairment",
]

@formula("straight_line_depreciation", "Straight-Line Depreciation", "(Cost - Salvage) / Useful_Life", DOMAIN_KEY, unit="")
def straight_line_depreciation(cost: float | None = None, salvage: float | None = None, useful_life: float | None = None, **kwargs):
    return build_result(
        fid="straight_line_depreciation",
        name="Straight-Line Depreciation",
        expression="(Cost - Salvage) / Useful_Life",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cost": kwargs.get("cost", cost),
            "salvage": kwargs.get("salvage", salvage),
            "useful_life": kwargs.get("useful_life", useful_life),
        },
    )

@formula("declining_balance", "Declining Balance Depreciation", "Book_Value * Rate", DOMAIN_KEY, unit="")
def declining_balance(book_value: float | None = None, rate: float | None = None, **kwargs):
    return build_result(
        fid="declining_balance",
        name="Declining Balance Depreciation",
        expression="Book_Value * Rate",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "book_value": kwargs.get("book_value", book_value),
            "rate": kwargs.get("rate", rate),
        },
    )

@formula("double_declining_balance", "Double Declining Balance", "Book_Value * (2/Useful_Life)", DOMAIN_KEY, unit="")
def double_declining_balance(book_value: float | None = None, useful_life: float | None = None, **kwargs):
    return build_result(
        fid="double_declining_balance",
        name="Double Declining Balance",
        expression="Book_Value * (2/Useful_Life)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "book_value": kwargs.get("book_value", book_value),
            "useful_life": kwargs.get("useful_life", useful_life),
        },
    )

@formula("units_of_production", "Units of Production Depreciation", "(Cost-Salvage)/Total_Units * Units_Used", DOMAIN_KEY, unit="")
def units_of_production(cost: float | None = None, salvage: float | None = None, total_units: float | None = None, units_used: float | None = None, **kwargs):
    return build_result(
        fid="units_of_production",
        name="Units of Production Depreciation",
        expression="(Cost-Salvage)/Total_Units * Units_Used",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cost": kwargs.get("cost", cost),
            "salvage": kwargs.get("salvage", salvage),
            "total_units": kwargs.get("total_units", total_units),
            "units_used": kwargs.get("units_used", units_used),
        },
    )

@formula("sum_of_years_digits", "Sum-of-Years-Digits", "(Cost-Salvage)*RemainingLife/SYD", DOMAIN_KEY, unit="")
def sum_of_years_digits(cost: float | None = None, salvage: float | None = None, useful_life: float | None = None, current_year: float | None = None, **kwargs):
    return build_result(
        fid="sum_of_years_digits",
        name="Sum-of-Years-Digits",
        expression="(Cost-Salvage)*RemainingLife/SYD",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cost": kwargs.get("cost", cost),
            "salvage": kwargs.get("salvage", salvage),
            "useful_life": kwargs.get("useful_life", useful_life),
            "current_year": kwargs.get("current_year", current_year),
        },
    )

@formula("macrs_depreciation", "MACRS Depreciation", "Cost * MACRS_Rate", DOMAIN_KEY, unit="")
def macrs_depreciation(cost: float | None = None, macrs_rate: float | None = None, **kwargs):
    return build_result(
        fid="macrs_depreciation",
        name="MACRS Depreciation",
        expression="Cost * MACRS_Rate",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cost": kwargs.get("cost", cost),
            "macrs_rate": kwargs.get("macrs_rate", macrs_rate),
        },
    )

@formula("accumulated_depreciation", "Accumulated Depreciation", "Sum(Annual_Depreciation)", DOMAIN_KEY, unit="")
def accumulated_depreciation(annual_depreciations: float | None = None, **kwargs):
    return build_result(
        fid="accumulated_depreciation",
        name="Accumulated Depreciation",
        expression="Sum(Annual_Depreciation)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "annual_depreciations": kwargs.get("annual_depreciations", annual_depreciations),
        },
    )

@formula("book_value_asset", "Net Book Value", "Cost - Accumulated_Depreciation", DOMAIN_KEY, unit="")
def book_value_asset(cost: float | None = None, accumulated_depreciation: float | None = None, **kwargs):
    return build_result(
        fid="book_value_asset",
        name="Net Book Value",
        expression="Cost - Accumulated_Depreciation",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cost": kwargs.get("cost", cost),
            "accumulated_depreciation": kwargs.get("accumulated_depreciation", accumulated_depreciation),
        },
    )

@formula("depreciation_rate", "Depreciation Rate %", "Annual_Depreciation / Cost * 100", DOMAIN_KEY, unit="")
def depreciation_rate(annual_depreciation: float | None = None, cost: float | None = None, **kwargs):
    return build_result(
        fid="depreciation_rate",
        name="Depreciation Rate %",
        expression="Annual_Depreciation / Cost * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "annual_depreciation": kwargs.get("annual_depreciation", annual_depreciation),
            "cost": kwargs.get("cost", cost),
        },
    )

@formula("amortization_intangible", "Intangible Amortization", "Cost / Useful_Life", DOMAIN_KEY, unit="")
def amortization_intangible(cost: float | None = None, useful_life: float | None = None, **kwargs):
    return build_result(
        fid="amortization_intangible",
        name="Intangible Amortization",
        expression="Cost / Useful_Life",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cost": kwargs.get("cost", cost),
            "useful_life": kwargs.get("useful_life", useful_life),
        },
    )

@formula("depletion", "Depletion Expense", "(Cost-Salvage)/Total_Units * Extracted", DOMAIN_KEY, unit="")
def depletion(cost: float | None = None, salvage: float | None = None, total_units: float | None = None, units_extracted: float | None = None, **kwargs):
    return build_result(
        fid="depletion",
        name="Depletion Expense",
        expression="(Cost-Salvage)/Total_Units * Extracted",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cost": kwargs.get("cost", cost),
            "salvage": kwargs.get("salvage", salvage),
            "total_units": kwargs.get("total_units", total_units),
            "units_extracted": kwargs.get("units_extracted", units_extracted),
        },
    )

@formula("fifo_cogs", "FIFO COGS", "Oldest inventory costs", DOMAIN_KEY, unit="")
def fifo_cogs(inventory_layers: float | None = None, units_sold: float | None = None, **kwargs):
    return build_result(
        fid="fifo_cogs",
        name="FIFO COGS",
        expression="Oldest inventory costs",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "inventory_layers": kwargs.get("inventory_layers", inventory_layers),
            "units_sold": kwargs.get("units_sold", units_sold),
        },
    )

@formula("lifo_cogs", "LIFO COGS", "Newest inventory costs", DOMAIN_KEY, unit="")
def lifo_cogs(inventory_layers: float | None = None, units_sold: float | None = None, **kwargs):
    return build_result(
        fid="lifo_cogs",
        name="LIFO COGS",
        expression="Newest inventory costs",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "inventory_layers": kwargs.get("inventory_layers", inventory_layers),
            "units_sold": kwargs.get("units_sold", units_sold),
        },
    )

@formula("weighted_average_cost", "Weighted Average Cost", "Total_Cost / Total_Units", DOMAIN_KEY, unit="")
def weighted_average_cost(total_cost: float | None = None, total_units: float | None = None, **kwargs):
    return build_result(
        fid="weighted_average_cost",
        name="Weighted Average Cost",
        expression="Total_Cost / Total_Units",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "total_cost": kwargs.get("total_cost", total_cost),
            "total_units": kwargs.get("total_units", total_units),
        },
    )

@formula("lifo_reserve", "LIFO Reserve", "FIFO_Inventory - LIFO_Inventory", DOMAIN_KEY, unit="")
def lifo_reserve(fifo_inventory: float | None = None, lifo_inventory: float | None = None, **kwargs):
    return build_result(
        fid="lifo_reserve",
        name="LIFO Reserve",
        expression="FIFO_Inventory - LIFO_Inventory",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "fifo_inventory": kwargs.get("fifo_inventory", fifo_inventory),
            "lifo_inventory": kwargs.get("lifo_inventory", lifo_inventory),
        },
    )

@formula("inventory_write_down", "Inventory Write-Down", "max(0, Cost - Market)", DOMAIN_KEY, unit="")
def inventory_write_down(cost: float | None = None, market_value: float | None = None, **kwargs):
    return build_result(
        fid="inventory_write_down",
        name="Inventory Write-Down",
        expression="max(0, Cost - Market)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cost": kwargs.get("cost", cost),
            "market_value": kwargs.get("market_value", market_value),
        },
    )

@formula("ending_inventory", "Ending Inventory", "Beginning + Purchases - COGS", DOMAIN_KEY, unit="")
def ending_inventory(beginning: float | None = None, purchases: float | None = None, cogs: float | None = None, **kwargs):
    return build_result(
        fid="ending_inventory",
        name="Ending Inventory",
        expression="Beginning + Purchases - COGS",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "beginning": kwargs.get("beginning", beginning),
            "purchases": kwargs.get("purchases", purchases),
            "cogs": kwargs.get("cogs", cogs),
        },
    )

@formula("cogs_calculation", "COGS Calculation", "Beginning + Purchases - Ending", DOMAIN_KEY, unit="")
def cogs_calculation(beginning_inventory: float | None = None, purchases: float | None = None, ending_inventory: float | None = None, **kwargs):
    return build_result(
        fid="cogs_calculation",
        name="COGS Calculation",
        expression="Beginning + Purchases - Ending",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "beginning_inventory": kwargs.get("beginning_inventory", beginning_inventory),
            "purchases": kwargs.get("purchases", purchases),
            "ending_inventory": kwargs.get("ending_inventory", ending_inventory),
        },
    )

@formula("gross_profit_method", "Gross Profit Method", "Sales - (Sales*Gross_Margin)", DOMAIN_KEY, unit="")
def gross_profit_method(sales: float | None = None, gross_margin: float | None = None, **kwargs):
    return build_result(
        fid="gross_profit_method",
        name="Gross Profit Method",
        expression="Sales - (Sales*Gross_Margin)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "sales": kwargs.get("sales", sales),
            "gross_margin": kwargs.get("gross_margin", gross_margin),
        },
    )

@formula("bad_debt_percentage_sales", "Bad Debt (% of Sales)", "Credit_Sales * Bad_Debt_Rate", DOMAIN_KEY, unit="")
def bad_debt_percentage_sales(credit_sales: float | None = None, bad_debt_rate: float | None = None, **kwargs):
    return build_result(
        fid="bad_debt_percentage_sales",
        name="Bad Debt (% of Sales)",
        expression="Credit_Sales * Bad_Debt_Rate",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "credit_sales": kwargs.get("credit_sales", credit_sales),
            "bad_debt_rate": kwargs.get("bad_debt_rate", bad_debt_rate),
        },
    )

@formula("bad_debt_aging", "Bad Debt (Aging)", "Sum(Receivable_Bucket * Rate)", DOMAIN_KEY, unit="")
def bad_debt_aging(receivable_buckets: float | None = None, rates: float | None = None, **kwargs):
    return build_result(
        fid="bad_debt_aging",
        name="Bad Debt (Aging)",
        expression="Sum(Receivable_Bucket * Rate)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "receivable_buckets": kwargs.get("receivable_buckets", receivable_buckets),
            "rates": kwargs.get("rates", rates),
        },
    )

@formula("allowance_doubtful_accounts", "Allowance for Doubtful Accounts", "Receivables * Uncollectible_Rate", DOMAIN_KEY, unit="")
def allowance_doubtful_accounts(receivables: float | None = None, uncollectible_rate: float | None = None, **kwargs):
    return build_result(
        fid="allowance_doubtful_accounts",
        name="Allowance for Doubtful Accounts",
        expression="Receivables * Uncollectible_Rate",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "receivables": kwargs.get("receivables", receivables),
            "uncollectible_rate": kwargs.get("uncollectible_rate", uncollectible_rate),
        },
    )

@formula("net_realizable_value", "Net Realizable Value", "Receivables - Allowance", DOMAIN_KEY, unit="")
def net_realizable_value(receivables: float | None = None, allowance: float | None = None, **kwargs):
    return build_result(
        fid="net_realizable_value",
        name="Net Realizable Value",
        expression="Receivables - Allowance",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "receivables": kwargs.get("receivables", receivables),
            "allowance": kwargs.get("allowance", allowance),
        },
    )

@formula("deferred_tax_liability", "Deferred Tax Liability", "Temp_Difference * Tax_Rate", DOMAIN_KEY, unit="")
def deferred_tax_liability(temporary_difference: float | None = None, tax_rate: float | None = None, **kwargs):
    return build_result(
        fid="deferred_tax_liability",
        name="Deferred Tax Liability",
        expression="Temp_Difference * Tax_Rate",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "temporary_difference": kwargs.get("temporary_difference", temporary_difference),
            "tax_rate": kwargs.get("tax_rate", tax_rate),
        },
    )

@formula("deferred_tax_asset", "Deferred Tax Asset", "Deductible_Difference * Tax_Rate", DOMAIN_KEY, unit="")
def deferred_tax_asset(deductible_difference: float | None = None, tax_rate: float | None = None, **kwargs):
    return build_result(
        fid="deferred_tax_asset",
        name="Deferred Tax Asset",
        expression="Deductible_Difference * Tax_Rate",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "deductible_difference": kwargs.get("deductible_difference", deductible_difference),
            "tax_rate": kwargs.get("tax_rate", tax_rate),
        },
    )

@formula("effective_tax_rate_acct", "Effective Tax Rate", "Tax_Expense / Pretax_Income * 100", DOMAIN_KEY, unit="")
def effective_tax_rate_acct(tax_expense: float | None = None, pretax_income: float | None = None, **kwargs):
    return build_result(
        fid="effective_tax_rate_acct",
        name="Effective Tax Rate",
        expression="Tax_Expense / Pretax_Income * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "tax_expense": kwargs.get("tax_expense", tax_expense),
            "pretax_income": kwargs.get("pretax_income", pretax_income),
        },
    )

@formula("stock_compensation_expense", "Stock Comp Expense", "Fair_Value / Vesting_Period", DOMAIN_KEY, unit="")
def stock_compensation_expense(fair_value: float | None = None, vesting_period: float | None = None, **kwargs):
    return build_result(
        fid="stock_compensation_expense",
        name="Stock Comp Expense",
        expression="Fair_Value / Vesting_Period",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "fair_value": kwargs.get("fair_value", fair_value),
            "vesting_period": kwargs.get("vesting_period", vesting_period),
        },
    )

@formula("pension_pbo", "Projected Benefit Obligation", "PV of future benefits", DOMAIN_KEY, unit="")
def pension_pbo(benefits: float | None = None, discount_rate: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="pension_pbo",
        name="Projected Benefit Obligation",
        expression="PV of future benefits",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "benefits": kwargs.get("benefits", benefits),
            "discount_rate": kwargs.get("discount_rate", discount_rate),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("pension_funded_status", "Pension Funded Status", "Plan_Assets - PBO", DOMAIN_KEY, unit="")
def pension_funded_status(plan_assets: float | None = None, pbo: float | None = None, **kwargs):
    return build_result(
        fid="pension_funded_status",
        name="Pension Funded Status",
        expression="Plan_Assets - PBO",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "plan_assets": kwargs.get("plan_assets", plan_assets),
            "pbo": kwargs.get("pbo", pbo),
        },
    )

@formula("pension_expense", "Net Periodic Pension Cost", "Service + Interest - ExpReturn + Amort", DOMAIN_KEY, unit="")
def pension_expense(service_cost: float | None = None, interest_cost: float | None = None, expected_return: float | None = None, amortization: float | None = None, **kwargs):
    return build_result(
        fid="pension_expense",
        name="Net Periodic Pension Cost",
        expression="Service + Interest - ExpReturn + Amort",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "service_cost": kwargs.get("service_cost", service_cost),
            "interest_cost": kwargs.get("interest_cost", interest_cost),
            "expected_return": kwargs.get("expected_return", expected_return),
            "amortization": kwargs.get("amortization", amortization),
        },
    )

@formula("operating_lease_expense", "Operating Lease Expense", "Total_Lease / Lease_Term", DOMAIN_KEY, unit="")
def operating_lease_expense(total_lease_payments: float | None = None, lease_term: float | None = None, **kwargs):
    return build_result(
        fid="operating_lease_expense",
        name="Operating Lease Expense",
        expression="Total_Lease / Lease_Term",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "total_lease_payments": kwargs.get("total_lease_payments", total_lease_payments),
            "lease_term": kwargs.get("lease_term", lease_term),
        },
    )

@formula("finance_lease_liability", "Finance Lease Liability", "PV(Lease_Payments, Rate)", DOMAIN_KEY, unit="")
def finance_lease_liability(lease_payments: float | None = None, rate: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="finance_lease_liability",
        name="Finance Lease Liability",
        expression="PV(Lease_Payments, Rate)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "lease_payments": kwargs.get("lease_payments", lease_payments),
            "rate": kwargs.get("rate", rate),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("right_of_use_asset", "Right-of-Use Asset", "Lease_Liability + Initial_Costs", DOMAIN_KEY, unit="")
def right_of_use_asset(lease_liability: float | None = None, initial_costs: float | None = None, **kwargs):
    return build_result(
        fid="right_of_use_asset",
        name="Right-of-Use Asset",
        expression="Lease_Liability + Initial_Costs",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "lease_liability": kwargs.get("lease_liability", lease_liability),
            "initial_costs": kwargs.get("initial_costs", initial_costs),
        },
    )

@formula("capitalized_interest", "Capitalized Interest", "Avg_Expenditure * Rate", DOMAIN_KEY, unit="")
def capitalized_interest(average_expenditure: float | None = None, interest_rate: float | None = None, **kwargs):
    return build_result(
        fid="capitalized_interest",
        name="Capitalized Interest",
        expression="Avg_Expenditure * Rate",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "average_expenditure": kwargs.get("average_expenditure", average_expenditure),
            "interest_rate": kwargs.get("interest_rate", interest_rate),
        },
    )

@formula("revenue_recognition_percentage", "Percentage of Completion", "Total_Revenue * Pct_Complete", DOMAIN_KEY, unit="")
def revenue_recognition_percentage(total_revenue: float | None = None, percent_complete: float | None = None, **kwargs):
    return build_result(
        fid="revenue_recognition_percentage",
        name="Percentage of Completion",
        expression="Total_Revenue * Pct_Complete",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "total_revenue": kwargs.get("total_revenue", total_revenue),
            "percent_complete": kwargs.get("percent_complete", percent_complete),
        },
    )

@formula("deferred_revenue", "Deferred Revenue", "Cash_Received - Revenue_Earned", DOMAIN_KEY, unit="")
def deferred_revenue(cash_received: float | None = None, revenue_earned: float | None = None, **kwargs):
    return build_result(
        fid="deferred_revenue",
        name="Deferred Revenue",
        expression="Cash_Received - Revenue_Earned",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cash_received": kwargs.get("cash_received", cash_received),
            "revenue_earned": kwargs.get("revenue_earned", revenue_earned),
        },
    )

@formula("comprehensive_income", "Comprehensive Income", "Net_Income + Other_Comprehensive_Income", DOMAIN_KEY, unit="")
def comprehensive_income(net_income: float | None = None, oci: float | None = None, **kwargs):
    return build_result(
        fid="comprehensive_income",
        name="Comprehensive Income",
        expression="Net_Income + Other_Comprehensive_Income",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_income": kwargs.get("net_income", net_income),
            "oci": kwargs.get("oci", oci),
        },
    )

@formula("retained_earnings_ending", "Ending Retained Earnings", "Beginning_RE + Net_Income - Dividends", DOMAIN_KEY, unit="")
def retained_earnings_ending(beginning_re: float | None = None, net_income: float | None = None, dividends: float | None = None, **kwargs):
    return build_result(
        fid="retained_earnings_ending",
        name="Ending Retained Earnings",
        expression="Beginning_RE + Net_Income - Dividends",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "beginning_re": kwargs.get("beginning_re", beginning_re),
            "net_income": kwargs.get("net_income", net_income),
            "dividends": kwargs.get("dividends", dividends),
        },
    )

@formula("goodwill_impairment", "Goodwill Impairment", "max(0, Carrying - Fair_Value)", DOMAIN_KEY, unit="")
def goodwill_impairment(carrying_value: float | None = None, fair_value: float | None = None, **kwargs):
    return build_result(
        fid="goodwill_impairment",
        name="Goodwill Impairment",
        expression="max(0, Carrying - Fair_Value)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "carrying_value": kwargs.get("carrying_value", carrying_value),
            "fair_value": kwargs.get("fair_value", fair_value),
        },
    )

@formula("asset_impairment", "Asset Impairment Loss", "max(0, Carrying - Recoverable)", DOMAIN_KEY, unit="")
def asset_impairment(carrying_value: float | None = None, recoverable_amount: float | None = None, **kwargs):
    return build_result(
        fid="asset_impairment",
        name="Asset Impairment Loss",
        expression="max(0, Carrying - Recoverable)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "carrying_value": kwargs.get("carrying_value", carrying_value),
            "recoverable_amount": kwargs.get("recoverable_amount", recoverable_amount),
        },
    )
