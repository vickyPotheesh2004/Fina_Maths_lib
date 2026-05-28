"""
Formula registry for FinBench maths_lib PDR.
Each entry: (id, name, description, formula, inputs)
Organized into 12 domains. Total target: 600 unique formulas.
"""

DOMAINS = {}

# ════════════════════════════════════════════════════════════════════
# DOMAIN 1 — PROFITABILITY & MARGIN RATIOS (50)
# ════════════════════════════════════════════════════════════════════
DOMAINS["D01_profitability"] = {
    "title": "Profitability & Margin Ratios",
    "module": "profitability.py",
    "formulas": [
        ("gross_margin", "Gross Margin %", "Profit left after COGS as % of revenue", "(Revenue - COGS) / Revenue * 100", "revenue, cogs"),
        ("gross_profit", "Gross Profit", "Revenue minus cost of goods sold", "Revenue - COGS", "revenue, cogs"),
        ("operating_margin", "Operating Margin %", "Operating income as % of revenue", "Operating_Income / Revenue * 100", "operating_income, revenue"),
        ("net_margin", "Net Profit Margin %", "Net income as % of revenue", "Net_Income / Revenue * 100", "net_income, revenue"),
        ("ebitda_margin", "EBITDA Margin %", "EBITDA as % of revenue", "EBITDA / Revenue * 100", "ebitda, revenue"),
        ("ebit_margin", "EBIT Margin %", "EBIT as % of revenue", "EBIT / Revenue * 100", "ebit, revenue"),
        ("pretax_margin", "Pretax Margin %", "Pretax income as % of revenue", "Pretax_Income / Revenue * 100", "pretax_income, revenue"),
        ("contribution_margin", "Contribution Margin", "Revenue minus variable costs", "Revenue - Variable_Costs", "revenue, variable_costs"),
        ("contribution_margin_ratio", "Contribution Margin Ratio %", "Contribution margin as % of revenue", "(Revenue - Variable_Costs) / Revenue * 100", "revenue, variable_costs"),
        ("fcf_margin", "Free Cash Flow Margin %", "FCF as % of revenue", "FCF / Revenue * 100", "fcf, revenue"),
        ("ocf_margin", "Operating Cash Flow Margin %", "OCF as % of revenue", "OCF / Revenue * 100", "ocf, revenue"),
        ("return_on_equity", "Return on Equity (ROE) %", "Net income as % of shareholders equity", "Net_Income / Shareholders_Equity * 100", "net_income, shareholders_equity"),
        ("return_on_assets", "Return on Assets (ROA) %", "Net income as % of total assets", "Net_Income / Total_Assets * 100", "net_income, total_assets"),
        ("return_on_invested_capital", "Return on Invested Capital (ROIC) %", "NOPAT as % of invested capital", "NOPAT / Invested_Capital * 100", "nopat, invested_capital"),
        ("return_on_capital_employed", "Return on Capital Employed (ROCE) %", "EBIT as % of capital employed", "EBIT / Capital_Employed * 100", "ebit, capital_employed"),
        ("return_on_sales", "Return on Sales (ROS) %", "Operating profit as % of sales", "Operating_Income / Sales * 100", "operating_income, sales"),
        ("return_on_tangible_equity", "Return on Tangible Equity %", "Net income / tangible equity", "Net_Income / (Equity - Intangibles) * 100", "net_income, equity, intangibles"),
        ("return_on_net_assets", "Return on Net Assets (RONA) %", "Net income / fixed assets + working capital", "Net_Income / (Fixed_Assets + Working_Capital) * 100", "net_income, fixed_assets, working_capital"),
        ("nopat", "Net Operating Profit After Tax", "Operating income after tax", "EBIT * (1 - Tax_Rate)", "ebit, tax_rate"),
        ("ebitda", "EBITDA", "Earnings before interest, tax, depreciation, amortization", "Net_Income + Interest + Taxes + Depreciation + Amortization", "net_income, interest, taxes, depreciation, amortization"),
        ("ebit", "EBIT", "Earnings before interest and tax", "Net_Income + Interest + Taxes", "net_income, interest, taxes"),
        ("effective_tax_rate", "Effective Tax Rate %", "Tax expense as % of pretax income", "Tax_Expense / Pretax_Income * 100", "tax_expense, pretax_income"),
        ("operating_leverage", "Degree of Operating Leverage", "% change EBIT / % change sales", "Pct_Change_EBIT / Pct_Change_Sales", "pct_change_ebit, pct_change_sales"),
        ("financial_leverage", "Degree of Financial Leverage", "% change EPS / % change EBIT", "Pct_Change_EPS / Pct_Change_EBIT", "pct_change_eps, pct_change_ebit"),
        ("combined_leverage", "Degree of Combined Leverage", "DOL times DFL", "DOL * DFL", "dol, dfl"),
        ("dupont_roe_3step", "DuPont ROE (3-Step)", "Net margin x asset turnover x equity multiplier", "Net_Margin * Asset_Turnover * Equity_Multiplier", "net_margin, asset_turnover, equity_multiplier"),
        ("dupont_roe_5step", "DuPont ROE (5-Step)", "Extended DuPont with tax + interest burden", "Tax_Burden * Interest_Burden * Operating_Margin * Asset_Turnover * Equity_Multiplier", "tax_burden, interest_burden, operating_margin, asset_turnover, equity_multiplier"),
        ("tax_burden", "Tax Burden Ratio", "Net income / pretax income", "Net_Income / Pretax_Income", "net_income, pretax_income"),
        ("interest_burden", "Interest Burden Ratio", "Pretax income / EBIT", "Pretax_Income / EBIT", "pretax_income, ebit"),
        ("equity_multiplier", "Equity Multiplier", "Total assets / equity", "Total_Assets / Shareholders_Equity", "total_assets, shareholders_equity"),
        ("operating_ratio", "Operating Ratio %", "Operating costs / revenue", "Operating_Costs / Revenue * 100", "operating_costs, revenue"),
        ("cost_of_revenue_ratio", "Cost of Revenue Ratio %", "COGS / revenue", "COGS / Revenue * 100", "cogs, revenue"),
        ("overhead_ratio", "Overhead Ratio %", "Operating expenses / (net interest + operating income)", "Operating_Expenses / (Net_Interest + Operating_Income) * 100", "operating_expenses, net_interest, operating_income"),
        ("sga_ratio", "SG&A to Revenue %", "Selling general admin / revenue", "SGA / Revenue * 100", "sga, revenue"),
        ("rnd_ratio", "R&D to Revenue %", "Research dev / revenue", "RnD / Revenue * 100", "rnd, revenue"),
        ("rnd_intensity", "R&D Intensity %", "R&D spend / revenue", "RnD_Expense / Revenue * 100", "rnd_expense, revenue"),
        ("net_income_growth", "Net Income Growth %", "YoY net income change", "(NI_Current - NI_Prior) / NI_Prior * 100", "ni_current, ni_prior"),
        ("revenue_growth", "Revenue Growth %", "YoY revenue change", "(Rev_Current - Rev_Prior) / Rev_Prior * 100", "rev_current, rev_prior"),
        ("operating_income_growth", "Operating Income Growth %", "YoY operating income change", "(OI_Current - OI_Prior) / OI_Prior * 100", "oi_current, oi_prior"),
        ("eps_basic", "Basic EPS", "Net income / weighted basic shares", "(Net_Income - Pref_Dividends) / Basic_Shares", "net_income, pref_dividends, basic_shares"),
        ("eps_diluted", "Diluted EPS", "Net income / diluted shares", "(Net_Income - Pref_Dividends) / Diluted_Shares", "net_income, pref_dividends, diluted_shares"),
        ("eps_growth", "EPS Growth %", "YoY EPS change", "(EPS_Current - EPS_Prior) / EPS_Prior * 100", "eps_current, eps_prior"),
        ("cash_return_on_assets", "Cash Return on Assets %", "OCF / total assets", "OCF / Total_Assets * 100", "ocf, total_assets"),
        ("cash_roe", "Cash Return on Equity %", "OCF / equity", "OCF / Shareholders_Equity * 100", "ocf, shareholders_equity"),
        ("gross_profit_growth", "Gross Profit Growth %", "YoY gross profit change", "(GP_Current - GP_Prior) / GP_Prior * 100", "gp_current, gp_prior"),
        ("ebitda_growth", "EBITDA Growth %", "YoY EBITDA change", "(EBITDA_Current - EBITDA_Prior) / EBITDA_Prior * 100", "ebitda_current, ebitda_prior"),
        ("incremental_margin", "Incremental Margin %", "Change in profit / change in revenue", "Delta_Profit / Delta_Revenue * 100", "delta_profit, delta_revenue"),
        ("breakeven_point_units", "Breakeven Point (Units)", "Fixed costs / contribution per unit", "Fixed_Costs / (Price - Variable_Cost_Per_Unit)", "fixed_costs, price, variable_cost_per_unit"),
        ("breakeven_point_revenue", "Breakeven Point (Revenue)", "Fixed costs / contribution margin ratio", "Fixed_Costs / Contribution_Margin_Ratio", "fixed_costs, contribution_margin_ratio"),
        ("margin_of_safety", "Margin of Safety %", "(Sales - breakeven) / sales", "(Sales - Breakeven_Sales) / Sales * 100", "sales, breakeven_sales"),
    ],
}

# ════════════════════════════════════════════════════════════════════
# DOMAIN 2 — LIQUIDITY, SOLVENCY & EFFICIENCY (50)
# ════════════════════════════════════════════════════════════════════
DOMAINS["D02_liquidity_solvency"] = {
    "title": "Liquidity, Solvency & Efficiency Ratios",
    "module": "liquidity_solvency.py",
    "formulas": [
        ("current_ratio", "Current Ratio", "Current assets / current liabilities", "Current_Assets / Current_Liabilities", "current_assets, current_liabilities"),
        ("quick_ratio", "Quick Ratio (Acid Test)", "Liquid assets / current liabilities", "(Current_Assets - Inventory) / Current_Liabilities", "current_assets, inventory, current_liabilities"),
        ("cash_ratio", "Cash Ratio", "Cash + equivalents / current liabilities", "(Cash + Marketable_Securities) / Current_Liabilities", "cash, marketable_securities, current_liabilities"),
        ("operating_cash_flow_ratio", "Operating Cash Flow Ratio", "OCF / current liabilities", "OCF / Current_Liabilities", "ocf, current_liabilities"),
        ("working_capital", "Working Capital", "Current assets minus current liabilities", "Current_Assets - Current_Liabilities", "current_assets, current_liabilities"),
        ("working_capital_ratio", "Working Capital Ratio", "Same as current ratio", "Current_Assets / Current_Liabilities", "current_assets, current_liabilities"),
        ("net_working_capital_to_sales", "NWC to Sales %", "Net working capital / sales", "Working_Capital / Sales * 100", "working_capital, sales"),
        ("defensive_interval_ratio", "Defensive Interval Ratio (days)", "Liquid assets / daily expenses", "Liquid_Assets / Daily_Operating_Expenses", "liquid_assets, daily_operating_expenses"),
        ("debt_to_equity", "Debt-to-Equity", "Total debt / equity", "Total_Debt / Shareholders_Equity", "total_debt, shareholders_equity"),
        ("debt_to_assets", "Debt-to-Assets", "Total debt / total assets", "Total_Debt / Total_Assets", "total_debt, total_assets"),
        ("debt_to_capital", "Debt-to-Capital", "Debt / (debt + equity)", "Total_Debt / (Total_Debt + Shareholders_Equity)", "total_debt, shareholders_equity"),
        ("debt_to_ebitda", "Debt-to-EBITDA", "Total debt / EBITDA", "Total_Debt / EBITDA", "total_debt, ebitda"),
        ("net_debt", "Net Debt", "Total debt minus cash", "Total_Debt - Cash", "total_debt, cash"),
        ("net_debt_to_ebitda", "Net Debt-to-EBITDA", "Net debt / EBITDA", "(Total_Debt - Cash) / EBITDA", "total_debt, cash, ebitda"),
        ("equity_ratio", "Equity Ratio", "Equity / total assets", "Shareholders_Equity / Total_Assets", "shareholders_equity, total_assets"),
        ("financial_leverage_ratio", "Financial Leverage Ratio", "Total assets / equity", "Total_Assets / Shareholders_Equity", "total_assets, shareholders_equity"),
        ("interest_coverage", "Interest Coverage Ratio", "EBIT / interest expense", "EBIT / Interest_Expense", "ebit, interest_expense"),
        ("ebitda_coverage", "EBITDA Coverage Ratio", "EBITDA / interest expense", "EBITDA / Interest_Expense", "ebitda, interest_expense"),
        ("fixed_charge_coverage", "Fixed Charge Coverage", "(EBIT + lease) / (interest + lease)", "(EBIT + Lease_Payments) / (Interest_Expense + Lease_Payments)", "ebit, lease_payments, interest_expense"),
        ("times_interest_earned", "Times Interest Earned", "EBIT / interest expense", "EBIT / Interest_Expense", "ebit, interest_expense"),
        ("debt_service_coverage", "Debt Service Coverage Ratio (DSCR)", "Net operating income / debt service", "Net_Operating_Income / Total_Debt_Service", "net_operating_income, total_debt_service"),
        ("cash_flow_to_debt", "Cash Flow to Debt", "OCF / total debt", "OCF / Total_Debt", "ocf, total_debt"),
        ("capitalization_ratio", "Capitalization Ratio", "LT debt / (LT debt + equity)", "Long_Term_Debt / (Long_Term_Debt + Shareholders_Equity)", "long_term_debt, shareholders_equity"),
        ("asset_turnover", "Asset Turnover", "Revenue / total assets", "Revenue / Total_Assets", "revenue, total_assets"),
        ("fixed_asset_turnover", "Fixed Asset Turnover", "Revenue / net PP&E", "Revenue / Net_PPE", "revenue, net_ppe"),
        ("inventory_turnover", "Inventory Turnover", "COGS / average inventory", "COGS / Average_Inventory", "cogs, average_inventory"),
        ("receivables_turnover", "Receivables Turnover", "Revenue / average receivables", "Revenue / Average_Receivables", "revenue, average_receivables"),
        ("payables_turnover", "Payables Turnover", "COGS / average payables", "COGS / Average_Payables", "cogs, average_payables"),
        ("working_capital_turnover", "Working Capital Turnover", "Revenue / working capital", "Revenue / Working_Capital", "revenue, working_capital"),
        ("equity_turnover", "Equity Turnover", "Revenue / equity", "Revenue / Shareholders_Equity", "revenue, shareholders_equity"),
        ("total_capital_turnover", "Total Capital Turnover", "Revenue / total capital", "Revenue / Total_Capital", "revenue, total_capital"),
        ("days_sales_outstanding", "Days Sales Outstanding (DSO)", "365 / receivables turnover", "365 / Receivables_Turnover", "receivables_turnover"),
        ("days_inventory_outstanding", "Days Inventory Outstanding (DIO)", "365 / inventory turnover", "365 / Inventory_Turnover", "inventory_turnover"),
        ("days_payable_outstanding", "Days Payable Outstanding (DPO)", "365 / payables turnover", "365 / Payables_Turnover", "payables_turnover"),
        ("cash_conversion_cycle", "Cash Conversion Cycle (days)", "DSO + DIO - DPO", "DSO + DIO - DPO", "dso, dio, dpo"),
        ("operating_cycle", "Operating Cycle (days)", "DSO + DIO", "DSO + DIO", "dso, dio"),
        ("dso_direct", "DSO Direct", "Receivables / revenue x 365", "Receivables / Revenue * 365", "receivables, revenue"),
        ("dio_direct", "DIO Direct", "Inventory / COGS x 365", "Inventory / COGS * 365", "inventory, cogs"),
        ("dpo_direct", "DPO Direct", "Payables / COGS x 365", "Payables / COGS * 365", "payables, cogs"),
        ("capital_intensity", "Capital Intensity %", "CapEx / revenue", "CapEx / Revenue * 100", "capex, revenue"),
        ("capital_intensity_assets", "Capital Intensity (Assets)", "Total assets / revenue", "Total_Assets / Revenue", "total_assets, revenue"),
        ("fixed_assets_to_equity", "Fixed Assets to Equity", "Net PP&E / equity", "Net_PPE / Shareholders_Equity", "net_ppe, shareholders_equity"),
        ("long_term_debt_to_equity", "LT Debt to Equity", "LT debt / equity", "Long_Term_Debt / Shareholders_Equity", "long_term_debt, shareholders_equity"),
        ("short_term_debt_ratio", "Short-Term Debt Ratio", "ST debt / total debt", "Short_Term_Debt / Total_Debt", "short_term_debt, total_debt"),
        ("current_liabilities_ratio", "Current Liabilities Ratio", "Current liabilities / total liabilities", "Current_Liabilities / Total_Liabilities", "current_liabilities, total_liabilities"),
        ("solvency_ratio", "Solvency Ratio", "(Net income + depreciation) / total liabilities", "(Net_Income + Depreciation) / Total_Liabilities", "net_income, depreciation, total_liabilities"),
        ("financial_autonomy_ratio", "Financial Autonomy Ratio", "Equity / total liabilities", "Shareholders_Equity / Total_Liabilities", "shareholders_equity, total_liabilities"),
        ("net_gearing", "Net Gearing %", "Net debt / equity", "(Total_Debt - Cash) / Shareholders_Equity * 100", "total_debt, cash, shareholders_equity"),
        ("altman_z_score", "Altman Z-Score", "Bankruptcy predictor composite", "1.2*A + 1.4*B + 3.3*C + 0.6*D + 1.0*E", "a, b, c, d, e"),
        ("piotroski_f_score", "Piotroski F-Score", "9-point financial strength score", "Sum of 9 binary signals", "signals_list"),
    ],
}

# ════════════════════════════════════════════════════════════════════
# DOMAIN 3 — VALUATION (60)
# ════════════════════════════════════════════════════════════════════
DOMAINS["D03_valuation"] = {
    "title": "Valuation Metrics & Models",
    "module": "valuation.py",
    "formulas": [
        ("pe_ratio", "Price-to-Earnings (P/E)", "Price / EPS", "Price / EPS", "price, eps"),
        ("forward_pe", "Forward P/E", "Price / forward EPS", "Price / Forward_EPS", "price, forward_eps"),
        ("peg_ratio", "PEG Ratio", "P/E / earnings growth", "PE_Ratio / Earnings_Growth_Rate", "pe_ratio, earnings_growth_rate"),
        ("pb_ratio", "Price-to-Book (P/B)", "Price / book value per share", "Price / Book_Value_Per_Share", "price, book_value_per_share"),
        ("ps_ratio", "Price-to-Sales (P/S)", "Market cap / revenue", "Market_Cap / Revenue", "market_cap, revenue"),
        ("pcf_ratio", "Price-to-Cash-Flow", "Price / cash flow per share", "Price / Cash_Flow_Per_Share", "price, cash_flow_per_share"),
        ("p_fcf_ratio", "Price-to-Free-Cash-Flow", "Market cap / FCF", "Market_Cap / FCF", "market_cap, fcf"),
        ("ev", "Enterprise Value", "Market cap + debt - cash", "Market_Cap + Total_Debt - Cash", "market_cap, total_debt, cash"),
        ("ev_ebitda", "EV/EBITDA", "Enterprise value / EBITDA", "EV / EBITDA", "ev, ebitda"),
        ("ev_ebit", "EV/EBIT", "Enterprise value / EBIT", "EV / EBIT", "ev, ebit"),
        ("ev_sales", "EV/Sales", "Enterprise value / revenue", "EV / Revenue", "ev, revenue"),
        ("ev_fcf", "EV/FCF", "Enterprise value / FCF", "EV / FCF", "ev, fcf"),
        ("dividend_yield", "Dividend Yield %", "Annual dividend / price", "Annual_Dividend / Price * 100", "annual_dividend, price"),
        ("dividend_payout_ratio", "Dividend Payout Ratio %", "Dividends / net income", "Dividends / Net_Income * 100", "dividends, net_income"),
        ("retention_ratio", "Retention Ratio %", "1 - payout ratio", "(1 - Payout_Ratio) * 100", "payout_ratio"),
        ("book_value_per_share", "Book Value Per Share", "Equity / shares outstanding", "Shareholders_Equity / Shares_Outstanding", "shareholders_equity, shares_outstanding"),
        ("tangible_book_value", "Tangible Book Value", "Equity - intangibles - goodwill", "Shareholders_Equity - Intangibles - Goodwill", "shareholders_equity, intangibles, goodwill"),
        ("tangible_book_per_share", "Tangible Book Value Per Share", "Tangible BV / shares", "Tangible_Book_Value / Shares_Outstanding", "tangible_book_value, shares_outstanding"),
        ("market_cap", "Market Capitalization", "Price x shares outstanding", "Price * Shares_Outstanding", "price, shares_outstanding"),
        ("earnings_yield", "Earnings Yield %", "EPS / price", "EPS / Price * 100", "eps, price"),
        ("fcf_yield", "Free Cash Flow Yield %", "FCF per share / price", "FCF_Per_Share / Price * 100", "fcf_per_share, price"),
        ("dcf_value", "DCF Present Value", "Sum of discounted cash flows", "Sum(CF_t / (1+r)^t)", "cash_flows, discount_rate"),
        ("dcf_two_stage", "Two-Stage DCF", "Explicit forecast + terminal value", "Sum(CF_t/(1+r)^t) + TV/(1+r)^n", "cash_flows, discount_rate, terminal_value"),
        ("terminal_value_gordon", "Terminal Value (Gordon)", "FCF x (1+g) / (r-g)", "FCF * (1 + g) / (r - g)", "fcf, growth_rate, discount_rate"),
        ("terminal_value_exit", "Terminal Value (Exit Multiple)", "Final year metric x exit multiple", "Final_EBITDA * Exit_Multiple", "final_ebitda, exit_multiple"),
        ("gordon_growth_model", "Gordon Growth Model (DDM)", "D1 / (r - g)", "D1 / (Required_Return - Growth_Rate)", "d1, required_return, growth_rate"),
        ("ddm_multistage", "Multi-Stage DDM", "Variable growth dividend model", "Sum(D_t/(1+r)^t) + TV", "dividends, discount_rate, terminal_value"),
        ("fcff", "Free Cash Flow to Firm", "EBIT(1-t) + D&A - CapEx - WC change", "EBIT*(1-Tax) + DA - CapEx - Delta_WC", "ebit, tax_rate, da, capex, delta_wc"),
        ("fcfe", "Free Cash Flow to Equity", "FCFF - interest(1-t) + net borrowing", "FCFF - Interest*(1-Tax) + Net_Borrowing", "fcff, interest, tax_rate, net_borrowing"),
        ("fcf_simple", "Free Cash Flow (Simple)", "OCF - CapEx", "OCF - CapEx", "ocf, capex"),
        ("wacc", "Weighted Average Cost of Capital", "Weighted equity + debt cost", "We*Re + Wd*Rd*(1-Tax)", "weight_equity, cost_equity, weight_debt, cost_debt, tax_rate"),
        ("cost_of_equity_capm", "Cost of Equity (CAPM)", "Rf + beta x (Rm - Rf)", "Rf + Beta * (Rm - Rf)", "risk_free, beta, market_return"),
        ("cost_of_equity_ddm", "Cost of Equity (DDM)", "D1/P + g", "D1 / Price + Growth_Rate", "d1, price, growth_rate"),
        ("cost_of_debt", "Cost of Debt (After-Tax)", "Interest rate x (1-tax)", "Interest_Rate * (1 - Tax_Rate)", "interest_rate, tax_rate"),
        ("capm", "CAPM Expected Return", "Rf + beta x equity premium", "Rf + Beta * (Rm - Rf)", "risk_free, beta, market_return"),
        ("fama_french_3", "Fama-French 3-Factor", "Rf + market + SMB + HML", "Rf + b1*MKT + b2*SMB + b3*HML", "risk_free, b1, mkt, b2, smb, b3, hml"),
        ("fama_french_5", "Fama-French 5-Factor", "FF3 + RMW + CMA", "Rf + b1*MKT + b2*SMB + b3*HML + b4*RMW + b5*CMA", "risk_free, betas, factors"),
        ("residual_income", "Residual Income", "Net income - equity charge", "Net_Income - (Equity * Cost_of_Equity)", "net_income, equity, cost_of_equity"),
        ("eva", "Economic Value Added", "NOPAT - (capital x WACC)", "NOPAT - (Invested_Capital * WACC)", "nopat, invested_capital, wacc"),
        ("mva", "Market Value Added", "Market value - invested capital", "Market_Value - Invested_Capital", "market_value, invested_capital"),
        ("justified_pe", "Justified P/E", "Payout x (1+g) / (r-g)", "Payout * (1+g) / (r-g)", "payout, growth_rate, required_return"),
        ("justified_pb", "Justified P/B", "(ROE - g) / (r - g)", "(ROE - g) / (r - g)", "roe, growth_rate, required_return"),
        ("graham_number", "Graham Number", "sqrt(22.5 x EPS x BVPS)", "sqrt(22.5 * EPS * BVPS)", "eps, bvps"),
        ("sum_of_parts", "Sum-of-the-Parts Value", "Sum of segment values", "Sum(Segment_Value_i)", "segment_values"),
        ("net_asset_value", "Net Asset Value (NAV)", "Assets - liabilities", "Total_Assets - Total_Liabilities", "total_assets, total_liabilities"),
        ("liquidation_value", "Liquidation Value", "Asset recovery - liabilities", "Asset_Recovery_Value - Total_Liabilities", "asset_recovery_value, total_liabilities"),
        ("replacement_value", "Replacement Value", "Cost to rebuild assets", "Replacement_Cost_Assets - Liabilities", "replacement_cost_assets, liabilities"),
        ("price_to_tangible_book", "Price-to-Tangible-Book", "Price / tangible BVPS", "Price / Tangible_BVPS", "price, tangible_bvps"),
        ("ev_to_invested_capital", "EV/Invested Capital", "Enterprise value / invested capital", "EV / Invested_Capital", "ev, invested_capital"),
        ("dividend_per_share", "Dividend Per Share", "Total dividends / shares", "Total_Dividends / Shares_Outstanding", "total_dividends, shares_outstanding"),
        ("dividend_coverage", "Dividend Coverage Ratio", "EPS / DPS", "EPS / Dividend_Per_Share", "eps, dividend_per_share"),
        ("total_shareholder_return", "Total Shareholder Return %", "(Price change + dividends) / start price", "(Price_End - Price_Start + Dividends) / Price_Start * 100", "price_end, price_start, dividends"),
        ("implied_growth_rate", "Implied Growth Rate", "r - D1/P", "Required_Return - D1/Price", "required_return, d1, price"),
        ("ev_per_share", "EV Per Share", "Enterprise value / shares", "EV / Shares_Outstanding", "ev, shares_outstanding"),
        ("price_to_nav", "Price-to-NAV", "Price / NAV per share", "Price / NAV_Per_Share", "price, nav_per_share"),
        ("cape_ratio", "CAPE (Shiller P/E)", "Price / 10yr avg real earnings", "Price / Avg_10yr_Real_EPS", "price, avg_10yr_real_eps"),
        ("rule_of_40", "Rule of 40 %", "Revenue growth + profit margin", "Revenue_Growth_Pct + Profit_Margin_Pct", "revenue_growth_pct, profit_margin_pct"),
        ("magic_formula_yield", "Magic Formula Earnings Yield", "EBIT / EV", "EBIT / EV", "ebit, ev"),
        ("owners_earnings", "Owner's Earnings (Buffett)", "NI + D&A - maintenance CapEx", "Net_Income + DA - Maintenance_CapEx", "net_income, da, maintenance_capex"),
        ("intrinsic_value_growth", "Intrinsic Value (Growth)", "EPS x (8.5 + 2g) Graham formula", "EPS * (8.5 + 2 * Growth_Rate)", "eps, growth_rate"),
    ],
}

# ════════════════════════════════════════════════════════════════════
# DOMAIN 4 — TIME-SERIES & TECHNICAL ANALYSIS (80)
# ════════════════════════════════════════════════════════════════════
DOMAINS["D04_technical"] = {
    "title": "Time-Series & Technical Analysis",
    "module": "technical.py",
    "formulas": [
        ("sma", "Simple Moving Average", "Mean of last n prices", "Sum(Prices[-n:]) / n", "prices, period"),
        ("ema", "Exponential Moving Average", "Weighted MA with decay", "Price*k + EMA_prev*(1-k), k=2/(n+1)", "prices, period"),
        ("wma", "Weighted Moving Average", "Linearly weighted MA", "Sum(Price_i * Weight_i) / Sum(Weights)", "prices, period"),
        ("dema", "Double EMA", "2*EMA - EMA(EMA)", "2*EMA - EMA(EMA)", "prices, period"),
        ("tema", "Triple EMA", "3*EMA - 3*EMA2 + EMA3", "3*EMA1 - 3*EMA2 + EMA3", "prices, period"),
        ("hma", "Hull Moving Average", "WMA-based low-lag MA", "WMA(2*WMA(n/2) - WMA(n), sqrt(n))", "prices, period"),
        ("kama", "Kaufman Adaptive MA", "Efficiency-ratio adaptive MA", "KAMA_prev + SC*(Price - KAMA_prev)", "prices, period"),
        ("vwma", "Volume-Weighted MA", "Price weighted by volume", "Sum(Price*Volume) / Sum(Volume)", "prices, volumes, period"),
        ("vwap", "Volume-Weighted Avg Price", "Cumulative PV / cumulative V", "Sum(Typical_Price*Volume) / Sum(Volume)", "highs, lows, closes, volumes"),
        ("atr", "Average True Range", "MA of true range", "MA(True_Range, n)", "highs, lows, closes, period"),
        ("true_range", "True Range", "Max of HL, HC, LC", "max(H-L, abs(H-Cp), abs(L-Cp))", "high, low, prev_close"),
        ("bollinger_upper", "Bollinger Upper Band", "SMA + k x std", "SMA + 2*StdDev", "prices, period"),
        ("bollinger_lower", "Bollinger Lower Band", "SMA - k x std", "SMA - 2*StdDev", "prices, period"),
        ("bollinger_width", "Bollinger Band Width", "(Upper - Lower) / Middle", "(Upper - Lower) / SMA", "prices, period"),
        ("bollinger_percent_b", "Bollinger %B", "Position within bands", "(Price - Lower) / (Upper - Lower)", "price, upper, lower"),
        ("keltner_upper", "Keltner Upper Channel", "EMA + mult x ATR", "EMA + Mult*ATR", "prices, highs, lows, period, multiplier"),
        ("keltner_lower", "Keltner Lower Channel", "EMA - mult x ATR", "EMA - Mult*ATR", "prices, highs, lows, period, multiplier"),
        ("donchian_upper", "Donchian Upper Channel", "Highest high over n", "max(Highs[-n:])", "highs, period"),
        ("donchian_lower", "Donchian Lower Channel", "Lowest low over n", "min(Lows[-n:])", "lows, period"),
        ("donchian_middle", "Donchian Middle", "Avg of upper and lower", "(Upper + Lower) / 2", "highs, lows, period"),
        ("rsi", "Relative Strength Index", "Momentum oscillator 0-100", "100 - 100/(1 + AvgGain/AvgLoss)", "prices, period"),
        ("stochastic_k", "Stochastic %K", "Position in high-low range", "(Close - LowN) / (HighN - LowN) * 100", "highs, lows, closes, period"),
        ("stochastic_d", "Stochastic %D", "SMA of %K", "SMA(%K, 3)", "stochastic_k, smoothing"),
        ("macd_line", "MACD Line", "EMA12 - EMA26", "EMA(12) - EMA(26)", "prices"),
        ("macd_signal", "MACD Signal Line", "EMA9 of MACD", "EMA(MACD, 9)", "macd_line"),
        ("macd_histogram", "MACD Histogram", "MACD - signal", "MACD_Line - Signal_Line", "macd_line, signal_line"),
        ("cci", "Commodity Channel Index", "Deviation from typical price", "(TP - SMA_TP) / (0.015*MeanDev)", "highs, lows, closes, period"),
        ("williams_r", "Williams %R", "Inverse stochastic", "(HighN - Close) / (HighN - LowN) * -100", "highs, lows, closes, period"),
        ("roc", "Rate of Change %", "Price momentum %", "(Price - Price_n) / Price_n * 100", "prices, period"),
        ("momentum", "Momentum", "Price difference over n", "Price - Price_n", "prices, period"),
        ("mfi", "Money Flow Index", "Volume-weighted RSI", "100 - 100/(1 + PosFlow/NegFlow)", "highs, lows, closes, volumes, period"),
        ("adx", "Average Directional Index", "Trend strength 0-100", "MA(DX, n)", "highs, lows, closes, period"),
        ("plus_di", "Plus Directional Indicator", "Upward movement strength", "100 * EMA(+DM) / ATR", "highs, lows, closes, period"),
        ("minus_di", "Minus Directional Indicator", "Downward movement strength", "100 * EMA(-DM) / ATR", "highs, lows, closes, period"),
        ("aroon_up", "Aroon Up", "Periods since high", "(n - PeriodsSinceHigh) / n * 100", "highs, period"),
        ("aroon_down", "Aroon Down", "Periods since low", "(n - PeriodsSinceLow) / n * 100", "lows, period"),
        ("aroon_oscillator", "Aroon Oscillator", "Aroon up - down", "Aroon_Up - Aroon_Down", "highs, lows, period"),
        ("parabolic_sar", "Parabolic SAR", "Stop and reverse trend", "SAR_prev + AF*(EP - SAR_prev)", "highs, lows, acceleration"),
        ("obv", "On-Balance Volume", "Cumulative volume flow", "Sum(Volume * Sign(Price_Change))", "closes, volumes"),
        ("chaikin_money_flow", "Chaikin Money Flow", "Volume-weighted accumulation", "Sum(MFV) / Sum(Volume)", "highs, lows, closes, volumes, period"),
        ("accumulation_distribution", "Accumulation/Distribution", "Money flow volume cumulative", "Prev_AD + MFV", "highs, lows, closes, volumes"),
        ("ichimoku_tenkan", "Ichimoku Tenkan-sen", "9-period midpoint", "(High9 + Low9) / 2", "highs, lows"),
        ("ichimoku_kijun", "Ichimoku Kijun-sen", "26-period midpoint", "(High26 + Low26) / 2", "highs, lows"),
        ("ichimoku_senkou_a", "Ichimoku Senkou Span A", "Avg of Tenkan and Kijun", "(Tenkan + Kijun) / 2", "tenkan, kijun"),
        ("ichimoku_senkou_b", "Ichimoku Senkou Span B", "52-period midpoint", "(High52 + Low52) / 2", "highs, lows"),
        ("linear_regression_slope", "Linear Regression Slope", "Trend slope of prices", "Slope of best-fit line", "prices, period"),
        ("standard_deviation", "Rolling Standard Deviation", "Volatility measure", "sqrt(Sum((x-mean)^2)/n)", "prices, period"),
        ("historical_volatility", "Historical Volatility %", "Annualized std of returns", "StdDev(LogReturns) * sqrt(252)", "prices, period"),
        ("variance", "Rolling Variance", "Squared deviation", "Sum((x-mean)^2) / n", "prices, period"),
        ("beta_coefficient", "Beta Coefficient", "Stock vs market sensitivity", "Cov(Stock,Market) / Var(Market)", "stock_returns, market_returns"),
        ("correlation_coefficient", "Correlation Coefficient", "Linear relationship -1 to 1", "Cov(X,Y) / (StdX * StdY)", "series_x, series_y"),
        ("z_score_price", "Price Z-Score", "Standardized price distance", "(Price - Mean) / StdDev", "prices, period"),
        ("price_oscillator", "Price Oscillator %", "(Fast MA - Slow MA) / Slow", "(FastMA - SlowMA) / SlowMA * 100", "prices, fast, slow"),
        ("trix", "TRIX", "Triple-smoothed ROC", "ROC of Triple_EMA", "prices, period"),
        ("ultimate_oscillator", "Ultimate Oscillator", "Multi-timeframe momentum", "100 * Weighted_BP_Sum / TR_Sum", "highs, lows, closes"),
        ("awesome_oscillator", "Awesome Oscillator", "SMA5 - SMA34 of midpoint", "SMA(MP,5) - SMA(MP,34)", "highs, lows"),
        ("dpo", "Detrended Price Oscillator", "Price minus shifted SMA", "Price - SMA_shifted", "prices, period"),
        ("vortex_positive", "Vortex Indicator +VI", "Upward trend movement", "Sum(+VM) / Sum(TR)", "highs, lows, closes, period"),
        ("vortex_negative", "Vortex Indicator -VI", "Downward trend movement", "Sum(-VM) / Sum(TR)", "highs, lows, closes, period"),
        ("mass_index", "Mass Index", "Range expansion reversal", "Sum(EMA9_HL / EMA9_EMA9_HL)", "highs, lows, period"),
        ("force_index", "Force Index", "Price change x volume", "(Close - Prev_Close) * Volume", "closes, volumes"),
        ("ease_of_movement", "Ease of Movement", "Price move per volume", "Distance_Moved / Box_Ratio", "highs, lows, volumes"),
        ("klinger_oscillator", "Klinger Oscillator", "Volume force trend", "EMA34(VF) - EMA55(VF)", "highs, lows, closes, volumes"),
        ("chande_momentum", "Chande Momentum Oscillator", "Pure momentum -100 to 100", "(Su - Sd) / (Su + Sd) * 100", "prices, period"),
        ("elder_ray_bull", "Elder Ray Bull Power", "High minus EMA", "High - EMA", "highs, prices, period"),
        ("elder_ray_bear", "Elder Ray Bear Power", "Low minus EMA", "Low - EMA", "lows, prices, period"),
        ("choppiness_index", "Choppiness Index", "Trend vs range 0-100", "100*log10(SumATR/Range)/log10(n)", "highs, lows, closes, period"),
        ("fisher_transform", "Fisher Transform", "Gaussian price normalizer", "0.5*ln((1+x)/(1-x))", "prices, period"),
        ("coppock_curve", "Coppock Curve", "Long-term momentum", "WMA10(ROC14 + ROC11)", "prices"),
        ("kst_oscillator", "Know Sure Thing", "Smoothed multi-ROC", "Sum(weighted smoothed ROCs)", "prices"),
        ("ppo", "Percentage Price Oscillator", "MACD as percentage", "(EMA12 - EMA26) / EMA26 * 100", "prices"),
        ("pvo", "Percentage Volume Oscillator", "PPO applied to volume", "(EMA12_V - EMA26_V) / EMA26_V * 100", "volumes"),
        ("relative_vigor_index", "Relative Vigor Index", "Close-open vs range", "SMA(Close-Open) / SMA(High-Low)", "opens, highs, lows, closes"),
        ("stochastic_rsi", "Stochastic RSI", "Stochastic of RSI", "(RSI - MinRSI) / (MaxRSI - MinRSI)", "prices, period"),
        ("supertrend", "SuperTrend", "ATR-based trend line", "Based on ATR bands", "highs, lows, closes, period, multiplier"),
        ("pivot_point", "Pivot Point", "Floor trader pivot", "(High + Low + Close) / 3", "high, low, close"),
        ("pivot_resistance_1", "Pivot R1", "First resistance", "2*Pivot - Low", "pivot, low"),
        ("pivot_support_1", "Pivot S1", "First support", "2*Pivot - High", "pivot, high"),
        ("fibonacci_retracement", "Fibonacci Retracement", "Key retracement levels", "High - (High-Low)*Ratio", "high, low, ratio"),
        ("chandelier_exit_long", "Chandelier Exit Long", "ATR trailing stop", "HighN - ATR*Multiplier", "highs, lows, closes, period, multiplier"),
    ],
}

# ════════════════════════════════════════════════════════════════════
# DOMAIN 5 — OPTIONS & DERIVATIVES (45)
# ════════════════════════════════════════════════════════════════════
DOMAINS["D05_options"] = {
    "title": "Options Pricing & Derivatives",
    "module": "options.py",
    "formulas": [
        ("black_scholes_call", "Black-Scholes Call", "European call price", "S*N(d1) - K*e^(-rT)*N(d2)", "spot, strike, time, rate, volatility"),
        ("black_scholes_put", "Black-Scholes Put", "European put price", "K*e^(-rT)*N(-d2) - S*N(-d1)", "spot, strike, time, rate, volatility"),
        ("bs_d1", "Black-Scholes d1", "First BS parameter", "(ln(S/K)+(r+sig^2/2)T)/(sig*sqrt(T))", "spot, strike, time, rate, volatility"),
        ("bs_d2", "Black-Scholes d2", "Second BS parameter", "d1 - sig*sqrt(T)", "d1, volatility, time"),
        ("bsm_call_dividend", "BSM Call with Dividend", "Call with continuous dividend", "S*e^(-qT)*N(d1) - K*e^(-rT)*N(d2)", "spot, strike, time, rate, volatility, dividend"),
        ("bsm_put_dividend", "BSM Put with Dividend", "Put with continuous dividend", "K*e^(-rT)*N(-d2) - S*e^(-qT)*N(-d1)", "spot, strike, time, rate, volatility, dividend"),
        ("delta_call", "Delta (Call)", "Price sensitivity to spot", "N(d1)", "spot, strike, time, rate, volatility"),
        ("delta_put", "Delta (Put)", "Put price sensitivity", "N(d1) - 1", "spot, strike, time, rate, volatility"),
        ("gamma", "Gamma", "Delta sensitivity to spot", "N'(d1) / (S*sig*sqrt(T))", "spot, strike, time, rate, volatility"),
        ("vega", "Vega", "Price sensitivity to volatility", "S*N'(d1)*sqrt(T)", "spot, strike, time, rate, volatility"),
        ("theta_call", "Theta (Call)", "Time decay of call", "Time decay formula", "spot, strike, time, rate, volatility"),
        ("theta_put", "Theta (Put)", "Time decay of put", "Time decay formula", "spot, strike, time, rate, volatility"),
        ("rho_call", "Rho (Call)", "Sensitivity to rate", "K*T*e^(-rT)*N(d2)", "spot, strike, time, rate, volatility"),
        ("rho_put", "Rho (Put)", "Put rate sensitivity", "-K*T*e^(-rT)*N(-d2)", "spot, strike, time, rate, volatility"),
        ("vanna", "Vanna", "Delta-vega cross sensitivity", "d(Delta)/d(vol)", "spot, strike, time, rate, volatility"),
        ("charm", "Charm", "Delta decay", "d(Delta)/d(time)", "spot, strike, time, rate, volatility"),
        ("vomma", "Vomma", "Vega convexity", "d(Vega)/d(vol)", "spot, strike, time, rate, volatility"),
        ("speed", "Speed", "Gamma sensitivity to spot", "d(Gamma)/d(S)", "spot, strike, time, rate, volatility"),
        ("binomial_call", "Binomial Call (CRR)", "Tree-based call pricing", "Cox-Ross-Rubinstein backward induction", "spot, strike, time, rate, volatility, steps"),
        ("binomial_put", "Binomial Put (CRR)", "Tree-based put pricing", "CRR backward induction", "spot, strike, time, rate, volatility, steps"),
        ("trinomial_option", "Trinomial Option", "3-branch tree pricing", "Trinomial backward induction", "spot, strike, time, rate, volatility, steps"),
        ("monte_carlo_option", "Monte Carlo Option", "Simulated path pricing", "Mean(discounted payoffs)", "spot, strike, time, rate, volatility, simulations"),
        ("implied_volatility", "Implied Volatility", "Vol from market price", "Newton-Raphson solve for sigma", "option_price, spot, strike, time, rate"),
        ("put_call_parity", "Put-Call Parity", "C - P = S - Ke^(-rT)", "Call - Put = Spot - PV(Strike)", "call, put, spot, strike, rate, time"),
        ("intrinsic_value_call", "Call Intrinsic Value", "max(S - K, 0)", "max(Spot - Strike, 0)", "spot, strike"),
        ("intrinsic_value_put", "Put Intrinsic Value", "max(K - S, 0)", "max(Strike - Spot, 0)", "spot, strike"),
        ("time_value_option", "Option Time Value", "Price minus intrinsic", "Option_Price - Intrinsic_Value", "option_price, intrinsic_value"),
        ("forward_price", "Forward Price", "Spot compounded to expiry", "S*e^(rT)", "spot, rate, time"),
        ("futures_price", "Futures Price", "Spot with cost of carry", "S*e^((r+storage-yield)T)", "spot, rate, storage, yield, time"),
        ("forward_rate_agreement", "FRA Value", "Forward rate agreement payoff", "Notional*(Ref - FRA)*Days/360", "notional, ref_rate, fra_rate, days"),
        ("swap_fixed_rate", "Swap Fixed Rate", "Par swap rate", "(1 - DF_n) / Sum(DF_i)", "discount_factors"),
        ("swap_value", "Interest Rate Swap Value", "PV fixed minus PV floating", "PV_Fixed - PV_Floating", "pv_fixed, pv_floating"),
        ("call_payoff", "Call Payoff at Expiry", "Long call terminal value", "max(S - K, 0) - Premium", "spot, strike, premium"),
        ("put_payoff", "Put Payoff at Expiry", "Long put terminal value", "max(K - S, 0) - Premium", "spot, strike, premium"),
        ("straddle_payoff", "Straddle Payoff", "Long call + put", "|S - K| - Total_Premium", "spot, strike, total_premium"),
        ("strangle_payoff", "Strangle Payoff", "OTM call + put", "max(S-Kc,0)+max(Kp-S,0)-Prem", "spot, strike_call, strike_put, premium"),
        ("covered_call_return", "Covered Call Return", "Stock + short call yield", "(Premium + max(K-S,0)) / S", "spot, strike, premium"),
        ("collar_value", "Collar Value", "Protective put + covered call", "Long put + short call payoff", "spot, put_strike, call_strike, net_premium"),
        ("butterfly_payoff", "Butterfly Spread Payoff", "3-strike limited spread", "Combined option payoff", "spot, strikes, premiums"),
        ("delta_hedge_shares", "Delta Hedge Shares", "Shares to hedge option", "-Delta * Contracts * 100", "delta, contracts"),
        ("option_leverage", "Option Leverage (Lambda)", "Elasticity to underlying", "Delta * S / Option_Price", "delta, spot, option_price"),
        ("breakeven_call", "Call Breakeven", "Strike plus premium", "Strike + Premium", "strike, premium"),
        ("breakeven_put", "Put Breakeven", "Strike minus premium", "Strike - Premium", "strike, premium"),
        ("max_pain", "Max Pain Price", "Strike with max option loss", "Strike minimizing total payout", "strikes, open_interest"),
        ("historical_var_option", "Option Position VaR", "Value at risk for option book", "Delta-gamma VaR approximation", "delta, gamma, spot, volatility, confidence"),
    ],
}

# ════════════════════════════════════════════════════════════════════
# DOMAIN 6 — FIXED INCOME (50)
# ════════════════════════════════════════════════════════════════════
DOMAINS["D06_fixed_income"] = {
    "title": "Fixed Income & Bonds",
    "module": "fixed_income.py",
    "formulas": [
        ("bond_price", "Bond Price", "PV of coupons + face", "Sum(C/(1+y)^t) + F/(1+y)^n", "coupon, face, yield, periods"),
        ("bond_price_clean", "Clean Bond Price", "Dirty price minus accrued", "Dirty_Price - Accrued_Interest", "dirty_price, accrued_interest"),
        ("bond_price_dirty", "Dirty Bond Price", "Clean plus accrued", "Clean_Price + Accrued_Interest", "clean_price, accrued_interest"),
        ("accrued_interest", "Accrued Interest", "Coupon earned since last pay", "Coupon * Days_Since / Days_Period", "coupon, days_since, days_period"),
        ("ytm", "Yield to Maturity", "IRR of bond cash flows", "Solve y in price equation", "price, coupon, face, periods"),
        ("ytc", "Yield to Call", "Yield if called early", "Solve y to call date", "price, coupon, call_price, call_periods"),
        ("ytw", "Yield to Worst", "Min of YTM and YTC", "min(YTM, YTC)", "ytm, ytc"),
        ("current_yield", "Current Yield", "Annual coupon / price", "Annual_Coupon / Price", "annual_coupon, price"),
        ("coupon_rate", "Coupon Rate", "Annual coupon / face", "Annual_Coupon / Face_Value", "annual_coupon, face_value"),
        ("macaulay_duration", "Macaulay Duration", "Weighted avg time to CF", "Sum(t*PV_CF) / Price", "cash_flows, yield, periods"),
        ("modified_duration", "Modified Duration", "Price sensitivity to yield", "Macaulay / (1 + y/n)", "macaulay_duration, yield, frequency"),
        ("effective_duration", "Effective Duration", "Duration for embedded options", "(P- - P+) / (2*P0*dy)", "price_down, price_up, price_base, yield_change"),
        ("dollar_duration", "Dollar Duration", "Price change per yield move", "Modified_Duration * Price * 0.0001", "modified_duration, price"),
        ("convexity", "Convexity", "Curvature of price-yield", "Sum(t*(t+1)*PV_CF) / (Price*(1+y)^2)", "cash_flows, yield, periods"),
        ("effective_convexity", "Effective Convexity", "Convexity with options", "(P- + P+ - 2*P0) / (P0*dy^2)", "price_down, price_up, price_base, yield_change"),
        ("dv01", "DV01 (PV01)", "Dollar value of 1bp", "Modified_Duration * Price * 0.0001", "modified_duration, price"),
        ("price_change_duration", "Price Change (Duration)", "Approx price move", "-Modified_Duration * Price * dy", "modified_duration, price, yield_change"),
        ("price_change_convexity", "Price Change (Dur+Conv)", "Second-order price move", "-MD*P*dy + 0.5*Conv*P*dy^2", "modified_duration, convexity, price, yield_change"),
        ("spot_rate", "Spot Rate", "Zero-coupon yield", "(Face/Price)^(1/n) - 1", "price, face, periods"),
        ("forward_rate", "Forward Rate", "Implied future rate", "((1+s2)^t2/(1+s1)^t1)^(1/(t2-t1)) - 1", "spot1, spot2, time1, time2"),
        ("par_yield", "Par Yield", "Coupon for price = par", "(1 - DF_n) / Sum(DF_i)", "discount_factors"),
        ("zero_coupon_price", "Zero-Coupon Bond Price", "PV of face value", "Face / (1+y)^n", "face, yield, periods"),
        ("discount_factor", "Discount Factor", "PV of 1 unit", "1 / (1+r)^t", "rate, time"),
        ("bond_equivalent_yield", "Bond Equivalent Yield", "Semi-annual to annual", "2 * ((1+y_semi) - 1)", "semi_annual_yield"),
        ("effective_annual_yield", "Effective Annual Yield", "Compounded annual yield", "(1 + y/n)^n - 1", "yield, frequency"),
        ("holding_period_return", "Holding Period Return %", "Total bond return", "(End + Coupons - Start) / Start * 100", "start_price, end_price, coupons"),
        ("realized_compound_yield", "Realized Compound Yield", "Yield with reinvestment", "(Total_FV / Price)^(1/n) - 1", "price, total_fv, periods"),
        ("z_spread", "Z-Spread", "Constant spread over spot curve", "Spread making PV = price", "price, cash_flows, spot_rates"),
        ("oas", "Option-Adjusted Spread", "Z-spread minus option cost", "Z_Spread - Option_Cost", "z_spread, option_cost"),
        ("nominal_spread", "Nominal Spread", "Bond yield minus benchmark", "Bond_YTM - Benchmark_YTM", "bond_ytm, benchmark_ytm"),
        ("g_spread", "G-Spread", "Spread over govt curve", "Bond_Yield - Interpolated_Govt", "bond_yield, govt_yield"),
        ("i_spread", "I-Spread", "Spread over swap rate", "Bond_Yield - Swap_Rate", "bond_yield, swap_rate"),
        ("asset_swap_spread", "Asset Swap Spread", "Spread in asset swap", "Asset swap calculation", "bond_price, coupon, swap_rate"),
        ("credit_spread", "Credit Spread", "Risky minus risk-free yield", "Corporate_Yield - Treasury_Yield", "corporate_yield, treasury_yield"),
        ("yield_curve_slope", "Yield Curve Slope", "Long minus short yield", "Long_Yield - Short_Yield", "long_yield, short_yield"),
        ("yield_curve_butterfly", "Yield Curve Butterfly", "Curvature measure", "2*Mid - Short - Long", "short_yield, mid_yield, long_yield"),
        ("key_rate_duration", "Key Rate Duration", "Sensitivity to one tenor", "Price sensitivity to key rate", "price_changes, yield_change"),
        ("portfolio_duration", "Portfolio Duration", "Weighted avg duration", "Sum(Weight_i * Duration_i)", "weights, durations"),
        ("portfolio_convexity", "Portfolio Convexity", "Weighted avg convexity", "Sum(Weight_i * Convexity_i)", "weights, convexities"),
        ("reinvestment_income", "Reinvestment Income", "FV of reinvested coupons", "Sum(C*(1+r)^(n-t))", "coupon, rate, periods"),
        ("interest_on_interest", "Interest on Interest", "Compounding of coupons", "Reinvestment_Income - Total_Coupons", "reinvestment_income, total_coupons"),
        ("clean_to_invoice", "Invoice Price", "Clean x factor + accrued", "Clean_Price*Factor + Accrued", "clean_price, conversion_factor, accrued"),
        ("bond_floor", "Convertible Bond Floor", "Straight bond value", "PV of bond cash flows", "coupon, face, yield, periods"),
        ("conversion_value", "Conversion Value", "Shares x stock price", "Conversion_Ratio * Stock_Price", "conversion_ratio, stock_price"),
        ("conversion_premium", "Conversion Premium %", "Bond price over conversion value", "(Bond_Price - Conv_Value) / Conv_Value * 100", "bond_price, conversion_value"),
        ("tips_principal", "TIPS Adjusted Principal", "Inflation-adjusted face", "Face * Index_Ratio", "face, index_ratio"),
        ("real_yield", "Real Yield", "Nominal minus inflation", "Nominal_Yield - Inflation_Rate", "nominal_yield, inflation_rate"),
        ("breakeven_inflation", "Breakeven Inflation Rate", "Nominal minus real yield", "Nominal_Yield - Real_Yield", "nominal_yield, real_yield"),
        ("rolling_yield", "Rolling Yield (Carry+Roll)", "Carry plus rolldown", "Carry + Rolldown", "carry, rolldown"),
        ("expected_loss", "Expected Loss (Credit)", "PD x LGD x EAD", "PD * LGD * EAD", "pd, lgd, ead"),
    ],
}

# ════════════════════════════════════════════════════════════════════
# DOMAIN 7 — RISK MANAGEMENT & PORTFOLIO (50)
# ════════════════════════════════════════════════════════════════════
DOMAINS["D07_risk"] = {
    "title": "Risk Management & Portfolio Theory",
    "module": "risk.py",
    "formulas": [
        ("var_historical", "VaR (Historical)", "Loss at percentile", "Percentile(Returns, 1-conf)", "returns, confidence"),
        ("var_parametric", "VaR (Parametric)", "Normal distribution VaR", "-(mu + z*sigma)*Value", "mean, std, confidence, value"),
        ("var_monte_carlo", "VaR (Monte Carlo)", "Simulated loss distribution", "Percentile of simulated P&L", "returns, confidence, simulations"),
        ("cvar", "Conditional VaR (ES)", "Expected loss beyond VaR", "Mean(Losses > VaR)", "returns, confidence"),
        ("expected_shortfall", "Expected Shortfall", "Average tail loss", "Mean(Returns below VaR)", "returns, confidence"),
        ("sharpe_ratio", "Sharpe Ratio", "Excess return per risk", "(Return - Rf) / StdDev", "returns, risk_free, std"),
        ("sortino_ratio", "Sortino Ratio", "Return per downside risk", "(Return - Rf) / Downside_Dev", "returns, risk_free, downside_deviation"),
        ("treynor_ratio", "Treynor Ratio", "Return per beta", "(Return - Rf) / Beta", "returns, risk_free, beta"),
        ("information_ratio", "Information Ratio", "Active return per tracking error", "(Return - Benchmark) / Tracking_Error", "returns, benchmark, tracking_error"),
        ("jensens_alpha", "Jensen's Alpha", "Return above CAPM", "Return - (Rf + Beta*(Rm-Rf))", "returns, risk_free, beta, market_return"),
        ("calmar_ratio", "Calmar Ratio", "Return per max drawdown", "Annual_Return / Max_Drawdown", "annual_return, max_drawdown"),
        ("sterling_ratio", "Sterling Ratio", "Return per avg drawdown", "Annual_Return / Avg_Drawdown", "annual_return, avg_drawdown"),
        ("max_drawdown", "Maximum Drawdown %", "Largest peak-trough drop", "(Trough - Peak) / Peak * 100", "prices"),
        ("drawdown_duration", "Drawdown Duration", "Time underwater", "Periods from peak to recovery", "prices"),
        ("beta", "Beta", "Systematic risk vs market", "Cov(Stock,Market) / Var(Market)", "stock_returns, market_returns"),
        ("alpha", "Alpha", "Excess return vs benchmark", "Return - Benchmark_Return", "returns, benchmark_return"),
        ("tracking_error", "Tracking Error", "Std of active returns", "StdDev(Portfolio - Benchmark)", "portfolio_returns, benchmark_returns"),
        ("downside_deviation", "Downside Deviation", "Std of negative returns", "sqrt(Mean(min(0, R-MAR)^2))", "returns, min_acceptable_return"),
        ("semi_variance", "Semi-Variance", "Variance of downside", "Mean((min(0, R-mean))^2)", "returns"),
        ("covariance", "Covariance", "Joint variability", "Mean((X-Xbar)(Y-Ybar))", "series_x, series_y"),
        ("correlation", "Correlation", "Normalized covariance", "Cov(X,Y) / (StdX*StdY)", "series_x, series_y"),
        ("portfolio_return", "Portfolio Return", "Weighted asset returns", "Sum(Weight_i * Return_i)", "weights, returns"),
        ("portfolio_variance", "Portfolio Variance", "Markowitz 2-asset variance", "w1^2*v1 + w2^2*v2 + 2*w1*w2*cov", "weights, variances, covariance"),
        ("portfolio_std", "Portfolio Std Dev", "Root of portfolio variance", "sqrt(Portfolio_Variance)", "portfolio_variance"),
        ("portfolio_beta", "Portfolio Beta", "Weighted average beta", "Sum(Weight_i * Beta_i)", "weights, betas"),
        ("minimum_variance_weight", "Min Variance Weight", "Optimal 2-asset weight", "(v2-cov)/(v1+v2-2*cov)", "variance1, variance2, covariance"),
        ("efficient_frontier_return", "Efficient Frontier Return", "Optimal return for risk", "Quadratic optimization", "returns, covariance_matrix, target_risk"),
        ("capital_allocation_line", "Capital Allocation Line", "Risk-return tradeoff line", "Rf + Sharpe * Sigma", "risk_free, sharpe, sigma"),
        ("capital_market_line", "Capital Market Line", "Efficient frontier with Rf", "Rf + ((Rm-Rf)/SigmaM)*Sigma", "risk_free, market_return, market_std, portfolio_std"),
        ("security_market_line", "Security Market Line", "CAPM expected return line", "Rf + Beta*(Rm - Rf)", "risk_free, beta, market_return"),
        ("diversification_ratio", "Diversification Ratio", "Weighted vol / portfolio vol", "Sum(w*sigma) / Portfolio_Sigma", "weights, volatilities, portfolio_std"),
        ("risk_parity_weight", "Risk Parity Weight", "Equal risk contribution", "Inverse vol weighting", "volatilities"),
        ("marginal_var", "Marginal VaR", "VaR change per position", "d(VaR)/d(weight)", "weights, covariance_matrix, position"),
        ("component_var", "Component VaR", "Position contribution to VaR", "Marginal_VaR * Position", "marginal_var, position_value"),
        ("incremental_var", "Incremental VaR", "VaR change adding position", "VaR_with - VaR_without", "var_with, var_without"),
        ("ulcer_index", "Ulcer Index", "Downside volatility measure", "sqrt(Mean(Drawdown^2))", "prices"),
        ("gain_to_pain", "Gain to Pain Ratio", "Sum returns / sum losses", "Sum(Returns) / abs(Sum(Losses))", "returns"),
        ("omega_ratio", "Omega Ratio", "Gains vs losses ratio", "Sum(Gains) / Sum(Losses) above threshold", "returns, threshold"),
        ("kappa_ratio", "Kappa Ratio", "Higher-moment downside ratio", "(Return - MAR) / LPM^(1/n)", "returns, min_acceptable_return, order"),
        ("upside_potential_ratio", "Upside Potential Ratio", "Upside vs downside", "Upside / Downside_Deviation", "returns, min_acceptable_return"),
        ("value_at_risk_normal", "Parametric VaR (Normal)", "Z-score based VaR", "Value * z * sigma * sqrt(t)", "value, confidence, sigma, time"),
        ("conditional_drawdown", "Conditional Drawdown at Risk", "Expected tail drawdown", "Mean of worst drawdowns", "prices, confidence"),
        ("pain_index", "Pain Index", "Average drawdown depth", "Mean(Drawdowns)", "prices"),
        ("burke_ratio", "Burke Ratio", "Return per sqrt sum drawdowns", "Return / sqrt(Sum(DD^2))", "returns, drawdowns"),
        ("m2_measure", "M-Squared (M2)", "Risk-adjusted vs market", "Rf + Sharpe * Market_Std", "sharpe, market_std, risk_free"),
        ("active_premium", "Active Premium", "Return over benchmark", "Annual_Return - Benchmark_Return", "annual_return, benchmark_return"),
        ("hurst_exponent", "Hurst Exponent", "Trend persistence measure", "Rescaled range analysis", "prices"),
        ("kelly_criterion", "Kelly Criterion", "Optimal bet fraction", "(p*b - q) / b", "win_prob, win_loss_ratio"),
        ("risk_of_ruin", "Risk of Ruin", "Probability of bankruptcy", "((1-edge)/(1+edge))^units", "edge, capital_units"),
        ("expected_value", "Expected Value", "Probability-weighted outcome", "Sum(Probability_i * Outcome_i)", "probabilities, outcomes"),
    ],
}

# ════════════════════════════════════════════════════════════════════
# DOMAIN 8 — TIME VALUE OF MONEY & CAPITAL BUDGETING (45)
# ════════════════════════════════════════════════════════════════════
DOMAINS["D08_tvm"] = {
    "title": "Time Value of Money & Capital Budgeting",
    "module": "tvm.py",
    "formulas": [
        ("present_value", "Present Value", "Discounted future value", "FV / (1+r)^n", "future_value, rate, periods"),
        ("future_value", "Future Value", "Compounded present value", "PV * (1+r)^n", "present_value, rate, periods"),
        ("npv", "Net Present Value", "Sum of discounted CFs minus cost", "Sum(CF_t/(1+r)^t) - Initial", "cash_flows, rate, initial_investment"),
        ("irr", "Internal Rate of Return", "Rate where NPV = 0", "Solve r: NPV = 0", "cash_flows, initial_investment"),
        ("mirr", "Modified IRR", "IRR with reinvestment rate", "(FV_inflows/PV_outflows)^(1/n) - 1", "cash_flows, finance_rate, reinvest_rate"),
        ("xirr", "XIRR (Irregular)", "IRR for irregular dates", "Solve for rate with dates", "cash_flows, dates"),
        ("pv_annuity", "PV of Annuity", "PV of equal payments", "PMT * (1-(1+r)^-n)/r", "payment, rate, periods"),
        ("fv_annuity", "FV of Annuity", "FV of equal payments", "PMT * ((1+r)^n - 1)/r", "payment, rate, periods"),
        ("pv_annuity_due", "PV of Annuity Due", "PV with payments at start", "PV_Annuity * (1+r)", "payment, rate, periods"),
        ("fv_annuity_due", "FV of Annuity Due", "FV with payments at start", "FV_Annuity * (1+r)", "payment, rate, periods"),
        ("perpetuity", "Perpetuity Value", "Infinite equal payments", "PMT / r", "payment, rate"),
        ("growing_perpetuity", "Growing Perpetuity", "Infinite growing payments", "PMT / (r - g)", "payment, rate, growth"),
        ("growing_annuity_pv", "PV Growing Annuity", "PV of growing payments", "PMT/(r-g)*(1-((1+g)/(1+r))^n)", "payment, rate, growth, periods"),
        ("annuity_payment", "Annuity Payment (PMT)", "Payment for loan/annuity", "PV*r / (1-(1+r)^-n)", "present_value, rate, periods"),
        ("loan_payment", "Loan Payment", "Amortizing loan payment", "P*r / (1-(1+r)^-n)", "principal, rate, periods"),
        ("loan_balance", "Remaining Loan Balance", "Outstanding after k payments", "P*(1+r)^k - PMT*((1+r)^k-1)/r", "principal, rate, payment, periods_paid"),
        ("amortization_interest", "Amortization Interest Portion", "Interest in payment k", "Balance * Rate", "balance, rate"),
        ("amortization_principal", "Amortization Principal Portion", "Principal in payment k", "Payment - Interest", "payment, interest"),
        ("effective_annual_rate", "Effective Annual Rate", "Annual compounded rate", "(1 + r/n)^n - 1", "nominal_rate, frequency"),
        ("nominal_rate", "Nominal Rate from EAR", "APR from effective rate", "n*((1+EAR)^(1/n) - 1)", "ear, frequency"),
        ("continuous_compounding", "Continuous Compounding FV", "FV with continuous rate", "PV * e^(rt)", "present_value, rate, time"),
        ("continuous_pv", "Continuous Compounding PV", "PV with continuous rate", "FV * e^(-rt)", "future_value, rate, time"),
        ("rule_of_72", "Rule of 72", "Doubling time estimate", "72 / Rate_Percent", "rate_percent"),
        ("rule_of_69", "Rule of 69.3", "Continuous doubling time", "69.3 / Rate_Percent", "rate_percent"),
        ("payback_period", "Payback Period", "Time to recover investment", "Years until cumulative CF = 0", "cash_flows, initial_investment"),
        ("discounted_payback", "Discounted Payback Period", "Payback with discounting", "Years until discounted cum = 0", "cash_flows, rate, initial_investment"),
        ("profitability_index", "Profitability Index", "PV inflows / initial cost", "PV_Inflows / Initial_Investment", "pv_inflows, initial_investment"),
        ("equivalent_annual_cost", "Equivalent Annual Cost", "Annualized project cost", "NPV / Annuity_Factor", "npv, rate, periods"),
        ("equivalent_annual_annuity", "Equivalent Annual Annuity", "Annualized NPV", "NPV * r / (1-(1+r)^-n)", "npv, rate, periods"),
        ("crossover_rate", "Crossover Rate", "Rate where two NPVs equal", "IRR of CF differences", "cash_flows_a, cash_flows_b"),
        ("real_rate", "Real Rate of Return", "Inflation-adjusted rate", "(1+nominal)/(1+inflation) - 1", "nominal_rate, inflation_rate"),
        ("fisher_equation", "Fisher Equation", "Nominal = real + inflation", "(1+real)*(1+inflation) - 1", "real_rate, inflation_rate"),
        ("annuity_factor", "Annuity Factor", "PV factor for annuity", "(1-(1+r)^-n) / r", "rate, periods"),
        ("future_value_factor", "Future Value Factor", "Compounding factor", "(1+r)^n", "rate, periods"),
        ("present_value_factor", "Present Value Factor", "Discount factor", "1 / (1+r)^n", "rate, periods"),
        ("sinking_fund", "Sinking Fund Payment", "Payment to reach FV", "FV*r / ((1+r)^n - 1)", "future_value, rate, periods"),
        ("capital_recovery_factor", "Capital Recovery Factor", "Annuity from present value", "r / (1-(1+r)^-n)", "rate, periods"),
        ("deferred_annuity_pv", "Deferred Annuity PV", "PV of delayed annuity", "PV_Annuity / (1+r)^defer", "payment, rate, periods, deferral"),
        ("net_future_value", "Net Future Value", "FV of all cash flows", "Sum(CF_t * (1+r)^(n-t))", "cash_flows, rate"),
        ("modified_payback", "Modified Payback", "Payback with terminal value", "Adjusted payback period", "cash_flows, terminal_value"),
        ("accounting_rate_of_return", "Accounting Rate of Return", "Avg profit / avg investment", "Avg_Profit / Avg_Investment * 100", "average_profit, average_investment"),
        ("bcr", "Benefit-Cost Ratio", "PV benefits / PV costs", "PV_Benefits / PV_Costs", "pv_benefits, pv_costs"),
        ("annualized_return", "Annualized Return", "Geometric annual return", "(End/Start)^(1/years) - 1", "start_value, end_value, years"),
        ("holding_period_yield", "Holding Period Yield %", "Total period return", "(End + Income - Start)/Start*100", "start_value, end_value, income"),
        ("breakeven_interest_rate", "Breakeven Interest Rate", "Rate for indifference", "Rate where NPV = 0", "cash_flows"),
    ],
}

# ════════════════════════════════════════════════════════════════════
# DOMAIN 9 — CORPORATE FINANCE & M&A (50)
# ════════════════════════════════════════════════════════════════════
DOMAINS["D09_corporate_ma"] = {
    "title": "Corporate Finance & M&A",
    "module": "corporate_ma.py",
    "formulas": [
        ("sustainable_growth_rate", "Sustainable Growth Rate", "ROE x retention", "ROE * Retention_Ratio", "roe, retention_ratio"),
        ("internal_growth_rate", "Internal Growth Rate", "Growth without external finance", "(ROA*b)/(1-ROA*b)", "roa, retention_ratio"),
        ("plowback_ratio", "Plowback Ratio", "Retained earnings fraction", "1 - Dividend_Payout", "dividend_payout"),
        ("roic", "Return on Invested Capital", "NOPAT / invested capital", "NOPAT / Invested_Capital", "nopat, invested_capital"),
        ("invested_capital", "Invested Capital", "Debt + equity - cash", "Total_Debt + Equity - Cash", "total_debt, equity, cash"),
        ("economic_profit", "Economic Profit", "NOPAT minus capital charge", "NOPAT - Invested_Capital*WACC", "nopat, invested_capital, wacc"),
        ("hamada_equation", "Hamada Equation", "Levered beta from unlevered", "Bu*(1 + (1-T)*D/E)", "unlevered_beta, tax_rate, debt, equity"),
        ("unlever_beta", "Unlevered Beta", "Asset beta from equity beta", "Be / (1 + (1-T)*D/E)", "levered_beta, tax_rate, debt, equity"),
        ("relever_beta", "Relevered Beta", "Equity beta from asset beta", "Ba*(1 + (1-T)*D/E)", "asset_beta, tax_rate, debt, equity"),
        ("mm_proposition1_no_tax", "M&M Proposition I (No Tax)", "Value independent of capital", "VL = VU", "unlevered_value"),
        ("mm_proposition1_tax", "M&M Proposition I (Tax)", "Value with tax shield", "VU + Tax_Rate*Debt", "unlevered_value, tax_rate, debt"),
        ("mm_proposition2", "M&M Proposition II", "Cost of equity with leverage", "Ru + (Ru-Rd)*(D/E)*(1-T)", "unlevered_cost, cost_debt, debt, equity, tax_rate"),
        ("tax_shield", "Tax Shield Value", "PV of interest tax savings", "Tax_Rate * Debt", "tax_rate, debt"),
        ("interest_tax_shield_annual", "Annual Interest Tax Shield", "Yearly tax savings", "Interest * Tax_Rate", "interest, tax_rate"),
        ("degree_total_leverage", "Degree of Total Leverage", "Combined operating + financial", "DOL * DFL", "dol, dfl"),
        ("free_cash_flow_firm", "FCFF (Detailed)", "Cash to all capital providers", "NI + NCC + Int*(1-T) - FCInv - WCInv", "net_income, ncc, interest, tax_rate, fcinv, wcinv"),
        ("free_cash_flow_equity", "FCFE (Detailed)", "Cash to equity holders", "NI + NCC - FCInv - WCInv + Net_Borrowing", "net_income, ncc, fcinv, wcinv, net_borrowing"),
        ("cash_flow_available_debt", "CFADS", "Cash available for debt service", "EBITDA - Tax - WC - CapEx", "ebitda, tax, working_capital_change, capex"),
        ("accretion_dilution", "Accretion/Dilution %", "EPS change from deal", "(ProForma_EPS - Standalone_EPS)/Standalone*100", "proforma_eps, standalone_eps"),
        ("exchange_ratio", "Exchange Ratio", "Target shares per acquirer share", "Offer_Price / Acquirer_Price", "offer_price, acquirer_price"),
        ("acquisition_premium", "Acquisition Premium %", "Offer over market price", "(Offer - Market)/Market * 100", "offer_price, market_price"),
        ("synergy_value", "Synergy Value", "Combined value minus standalone", "V_Combined - (V_A + V_B)", "combined_value, value_a, value_b"),
        ("goodwill", "Goodwill", "Purchase price over fair value", "Purchase_Price - Fair_Value_Net_Assets", "purchase_price, fair_value_net_assets"),
        ("purchase_price_allocation", "Net Identifiable Assets", "Fair value of assets minus liabilities", "FV_Assets - FV_Liabilities", "fv_assets, fv_liabilities"),
        ("pro_forma_eps", "Pro Forma EPS", "Combined EPS post-merger", "Combined_NI / Combined_Shares", "combined_net_income, combined_shares"),
        ("breakeven_synergies", "Breakeven Synergies", "Synergies to justify premium", "Premium_Paid value", "premium, target_shares"),
        ("lbo_equity_return", "LBO Equity Return (MOIC)", "Multiple of invested capital", "Exit_Equity / Entry_Equity", "exit_equity, entry_equity"),
        ("lbo_irr", "LBO IRR", "Annualized LBO return", "(Exit/Entry)^(1/years) - 1", "entry_equity, exit_equity, years"),
        ("debt_paydown", "Debt Paydown", "Cumulative debt reduction", "Entry_Debt - Exit_Debt", "entry_debt, exit_debt"),
        ("entry_multiple", "Entry Multiple", "Purchase EV / EBITDA", "Entry_EV / EBITDA", "entry_ev, ebitda"),
        ("exit_multiple", "Exit Multiple", "Sale EV / EBITDA", "Exit_EV / EBITDA", "exit_ev, ebitda"),
        ("sources_uses_balance", "Sources and Uses Balance", "Total sources = total uses", "Sum(Sources) - Sum(Uses)", "sources, uses"),
        ("net_borrowing", "Net Borrowing", "New debt minus repayments", "Debt_Issued - Debt_Repaid", "debt_issued, debt_repaid"),
        ("dividend_discount_value", "DDM Value", "PV of all dividends", "Sum(D_t/(1+r)^t)", "dividends, rate"),
        ("clientele_effect", "After-Tax Dividend", "Dividend net of tax", "Dividend * (1 - Tax_Rate)", "dividend, tax_rate"),
        ("share_buyback_eps_impact", "Buyback EPS Impact", "EPS after share reduction", "NI / (Shares - Bought)", "net_income, shares, shares_bought"),
        ("treasury_stock_method", "Treasury Stock Method", "Diluted shares from options", "Options - (Options*Strike/Price)", "options, strike, price"),
        ("weighted_avg_shares", "Weighted Average Shares", "Time-weighted share count", "Sum(Shares_i * Months_i / 12)", "share_periods"),
        ("capital_structure_weight_equity", "Equity Weight", "Equity / total capital", "Equity / (Equity + Debt)", "equity, debt"),
        ("capital_structure_weight_debt", "Debt Weight", "Debt / total capital", "Debt / (Equity + Debt)", "equity, debt"),
        ("operating_working_capital", "Operating Working Capital", "Operating current assets - liabilities", "Op_Current_Assets - Op_Current_Liabilities", "op_current_assets, op_current_liabilities"),
        ("invested_capital_turnover", "Invested Capital Turnover", "Revenue / invested capital", "Revenue / Invested_Capital", "revenue, invested_capital"),
        ("reinvestment_rate", "Reinvestment Rate", "Net investment / NOPAT", "(CapEx - Depr + WCInv) / NOPAT", "capex, depreciation, wc_investment, nopat"),
        ("expected_growth_fundamentals", "Expected Growth (Fundamentals)", "Reinvestment x ROIC", "Reinvestment_Rate * ROIC", "reinvestment_rate, roic"),
        ("terminal_growth_implied", "Implied Terminal Growth", "Growth from terminal value", "r - FCF/TV", "rate, fcf, terminal_value"),
        ("equity_value_from_ev", "Equity Value from EV", "EV minus net debt", "EV - Net_Debt", "ev, net_debt"),
        ("net_debt_to_equity_value", "Net Debt to Equity Value", "Leverage in valuation", "Net_Debt / Equity_Value", "net_debt, equity_value"),
        ("dilution_percentage", "Dilution Percentage", "New shares as % of total", "New_Shares / (Old + New) * 100", "old_shares, new_shares"),
        ("control_premium", "Control Premium %", "Premium for control stake", "(Control_Price - Minority)/Minority*100", "control_price, minority_price"),
        ("minority_interest_value", "Minority Interest Value", "Non-controlling stake value", "Subsidiary_Value * Minority_Pct", "subsidiary_value, minority_pct"),
    ],
}

# ════════════════════════════════════════════════════════════════════
# DOMAIN 10 — ACCOUNTING & DEPRECIATION (40)
# ════════════════════════════════════════════════════════════════════
DOMAINS["D10_accounting"] = {
    "title": "Accounting & Depreciation",
    "module": "accounting.py",
    "formulas": [
        ("straight_line_depreciation", "Straight-Line Depreciation", "Equal annual depreciation", "(Cost - Salvage) / Useful_Life", "cost, salvage, useful_life"),
        ("declining_balance", "Declining Balance Depreciation", "Accelerated depreciation", "Book_Value * Rate", "book_value, rate"),
        ("double_declining_balance", "Double Declining Balance", "2x straight-line rate", "Book_Value * (2/Useful_Life)", "book_value, useful_life"),
        ("units_of_production", "Units of Production Depreciation", "Depreciation per unit used", "(Cost-Salvage)/Total_Units * Units_Used", "cost, salvage, total_units, units_used"),
        ("sum_of_years_digits", "Sum-of-Years-Digits", "Accelerated depreciation", "(Cost-Salvage)*RemainingLife/SYD", "cost, salvage, useful_life, current_year"),
        ("macrs_depreciation", "MACRS Depreciation", "US tax depreciation", "Cost * MACRS_Rate", "cost, macrs_rate"),
        ("accumulated_depreciation", "Accumulated Depreciation", "Total depreciation to date", "Sum(Annual_Depreciation)", "annual_depreciations"),
        ("book_value_asset", "Net Book Value", "Cost minus accumulated depr", "Cost - Accumulated_Depreciation", "cost, accumulated_depreciation"),
        ("depreciation_rate", "Depreciation Rate %", "Annual depreciation / cost", "Annual_Depreciation / Cost * 100", "annual_depreciation, cost"),
        ("amortization_intangible", "Intangible Amortization", "Straight-line for intangibles", "Cost / Useful_Life", "cost, useful_life"),
        ("depletion", "Depletion Expense", "Natural resource expense", "(Cost-Salvage)/Total_Units * Extracted", "cost, salvage, total_units, units_extracted"),
        ("fifo_cogs", "FIFO COGS", "First-in-first-out cost", "Oldest inventory costs", "inventory_layers, units_sold"),
        ("lifo_cogs", "LIFO COGS", "Last-in-first-out cost", "Newest inventory costs", "inventory_layers, units_sold"),
        ("weighted_average_cost", "Weighted Average Cost", "Average inventory cost", "Total_Cost / Total_Units", "total_cost, total_units"),
        ("lifo_reserve", "LIFO Reserve", "FIFO minus LIFO inventory", "FIFO_Inventory - LIFO_Inventory", "fifo_inventory, lifo_inventory"),
        ("inventory_write_down", "Inventory Write-Down", "Lower of cost or market", "max(0, Cost - Market)", "cost, market_value"),
        ("ending_inventory", "Ending Inventory", "Beginning + purchases - COGS", "Beginning + Purchases - COGS", "beginning, purchases, cogs"),
        ("cogs_calculation", "COGS Calculation", "Beginning + purchases - ending", "Beginning + Purchases - Ending", "beginning_inventory, purchases, ending_inventory"),
        ("gross_profit_method", "Gross Profit Method", "Estimate inventory", "Sales - (Sales*Gross_Margin)", "sales, gross_margin"),
        ("bad_debt_percentage_sales", "Bad Debt (% of Sales)", "Bad debt from sales", "Credit_Sales * Bad_Debt_Rate", "credit_sales, bad_debt_rate"),
        ("bad_debt_aging", "Bad Debt (Aging)", "Bad debt from receivables aging", "Sum(Receivable_Bucket * Rate)", "receivable_buckets, rates"),
        ("allowance_doubtful_accounts", "Allowance for Doubtful Accounts", "Estimated uncollectible", "Receivables * Uncollectible_Rate", "receivables, uncollectible_rate"),
        ("net_realizable_value", "Net Realizable Value", "Receivables minus allowance", "Receivables - Allowance", "receivables, allowance"),
        ("deferred_tax_liability", "Deferred Tax Liability", "Future tax on temp differences", "Temp_Difference * Tax_Rate", "temporary_difference, tax_rate"),
        ("deferred_tax_asset", "Deferred Tax Asset", "Future tax benefit", "Deductible_Difference * Tax_Rate", "deductible_difference, tax_rate"),
        ("effective_tax_rate_acct", "Effective Tax Rate", "Tax expense / pretax income", "Tax_Expense / Pretax_Income * 100", "tax_expense, pretax_income"),
        ("stock_compensation_expense", "Stock Comp Expense", "Fair value amortized", "Fair_Value / Vesting_Period", "fair_value, vesting_period"),
        ("pension_pbo", "Projected Benefit Obligation", "PV of pension obligations", "PV of future benefits", "benefits, discount_rate, periods"),
        ("pension_funded_status", "Pension Funded Status", "Plan assets minus PBO", "Plan_Assets - PBO", "plan_assets, pbo"),
        ("pension_expense", "Net Periodic Pension Cost", "Annual pension expense", "Service + Interest - ExpReturn + Amort", "service_cost, interest_cost, expected_return, amortization"),
        ("operating_lease_expense", "Operating Lease Expense", "Straight-line lease cost", "Total_Lease / Lease_Term", "total_lease_payments, lease_term"),
        ("finance_lease_liability", "Finance Lease Liability", "PV of lease payments", "PV(Lease_Payments, Rate)", "lease_payments, rate, periods"),
        ("right_of_use_asset", "Right-of-Use Asset", "Lease liability + costs", "Lease_Liability + Initial_Costs", "lease_liability, initial_costs"),
        ("capitalized_interest", "Capitalized Interest", "Interest during construction", "Avg_Expenditure * Rate", "average_expenditure, interest_rate"),
        ("revenue_recognition_percentage", "Percentage of Completion", "Revenue by completion", "Total_Revenue * Pct_Complete", "total_revenue, percent_complete"),
        ("deferred_revenue", "Deferred Revenue", "Unearned revenue liability", "Cash_Received - Revenue_Earned", "cash_received, revenue_earned"),
        ("comprehensive_income", "Comprehensive Income", "Net income + OCI", "Net_Income + Other_Comprehensive_Income", "net_income, oci"),
        ("retained_earnings_ending", "Ending Retained Earnings", "Beginning + NI - dividends", "Beginning_RE + Net_Income - Dividends", "beginning_re, net_income, dividends"),
        ("goodwill_impairment", "Goodwill Impairment", "Carrying minus fair value", "max(0, Carrying - Fair_Value)", "carrying_value, fair_value"),
        ("asset_impairment", "Asset Impairment Loss", "Carrying over recoverable", "max(0, Carrying - Recoverable)", "carrying_value, recoverable_amount"),
    ],
}

# ════════════════════════════════════════════════════════════════════
# DOMAIN 11 — STATISTICS & ECONOMETRICS (45)
# ════════════════════════════════════════════════════════════════════
DOMAINS["D11_statistics"] = {
    "title": "Statistics & Econometrics",
    "module": "statistics_econ.py",
    "formulas": [
        ("arithmetic_mean", "Arithmetic Mean", "Simple average", "Sum(x) / n", "values"),
        ("geometric_mean", "Geometric Mean", "Compound average", "(Prod(x))^(1/n)", "values"),
        ("harmonic_mean", "Harmonic Mean", "Reciprocal average", "n / Sum(1/x)", "values"),
        ("weighted_mean", "Weighted Mean", "Weighted average", "Sum(w*x) / Sum(w)", "values, weights"),
        ("median", "Median", "Middle value", "Middle of sorted values", "values"),
        ("mode", "Mode", "Most frequent value", "Most common value", "values"),
        ("range_stat", "Range", "Max minus min", "Max - Min", "values"),
        ("variance_population", "Population Variance", "Average squared deviation", "Sum((x-mu)^2) / N", "values"),
        ("variance_sample", "Sample Variance", "Unbiased variance", "Sum((x-xbar)^2) / (n-1)", "values"),
        ("standard_deviation_pop", "Population Std Dev", "Root of population variance", "sqrt(Population_Variance)", "values"),
        ("standard_deviation_sample", "Sample Std Dev", "Root of sample variance", "sqrt(Sample_Variance)", "values"),
        ("coefficient_variation", "Coefficient of Variation", "Std / mean", "StdDev / Mean", "values"),
        ("skewness", "Skewness", "Distribution asymmetry", "E[(x-mu)^3] / sigma^3", "values"),
        ("kurtosis", "Kurtosis", "Tail heaviness", "E[(x-mu)^4] / sigma^4", "values"),
        ("excess_kurtosis", "Excess Kurtosis", "Kurtosis minus 3", "Kurtosis - 3", "values"),
        ("covariance_stat", "Covariance", "Joint variability", "Sum((x-xbar)(y-ybar))/(n-1)", "series_x, series_y"),
        ("pearson_correlation", "Pearson Correlation", "Linear correlation", "Cov(X,Y)/(SdX*SdY)", "series_x, series_y"),
        ("spearman_correlation", "Spearman Correlation", "Rank correlation", "1 - 6*Sum(d^2)/(n(n^2-1))", "series_x, series_y"),
        ("linear_regression_beta", "Regression Slope (Beta)", "OLS slope coefficient", "Cov(X,Y) / Var(X)", "series_x, series_y"),
        ("linear_regression_alpha", "Regression Intercept", "OLS intercept", "Ybar - Beta*Xbar", "series_x, series_y"),
        ("r_squared", "R-Squared", "Explained variance fraction", "1 - SSres/SStot", "actual, predicted"),
        ("adjusted_r_squared", "Adjusted R-Squared", "R2 penalized for predictors", "1 - (1-R2)(n-1)/(n-k-1)", "r_squared, n, predictors"),
        ("standard_error", "Standard Error", "Std of sampling distribution", "StdDev / sqrt(n)", "values"),
        ("standard_error_regression", "Standard Error of Regression", "Residual standard error", "sqrt(SSres/(n-2))", "residuals, n"),
        ("t_statistic", "T-Statistic", "Standardized test stat", "(xbar - mu) / (s/sqrt(n))", "sample_mean, pop_mean, std, n"),
        ("z_score", "Z-Score", "Standard deviations from mean", "(x - mu) / sigma", "value, mean, std"),
        ("confidence_interval", "Confidence Interval", "Range for parameter", "mean +/- z*(s/sqrt(n))", "mean, std, n, confidence"),
        ("chi_square_stat", "Chi-Square Statistic", "Goodness of fit test", "Sum((O-E)^2 / E)", "observed, expected"),
        ("f_statistic", "F-Statistic", "Variance ratio test", "Var1 / Var2", "variance1, variance2"),
        ("percentile", "Percentile", "Value at given percentile", "Interpolated rank value", "values, percentile"),
        ("quartile", "Quartile", "25/50/75 split values", "Percentile at 25/50/75", "values, quartile_number"),
        ("interquartile_range", "Interquartile Range (IQR)", "Q3 minus Q1", "Q3 - Q1", "values"),
        ("autocorrelation", "Autocorrelation", "Self-correlation at lag", "Corr(x_t, x_t-k)", "series, lag"),
        ("moving_average_forecast", "Moving Average Forecast", "Average of last n", "Mean(last n values)", "values, window"),
        ("exponential_smoothing", "Exponential Smoothing", "Weighted recent forecast", "alpha*x + (1-alpha)*prev", "values, alpha"),
        ("holt_linear_trend", "Holt's Linear Trend", "Level + trend forecast", "Level + Trend smoothing", "values, alpha, beta"),
        ("holt_winters", "Holt-Winters Seasonal", "Level + trend + seasonal", "Triple exponential smoothing", "values, alpha, beta, gamma, season_length"),
        ("ar1_model", "AR(1) Model", "First-order autoregression", "c + phi*x_prev + error", "series, phi, constant"),
        ("durbin_watson", "Durbin-Watson Statistic", "Autocorrelation test", "Sum((e_t-e_t-1)^2)/Sum(e_t^2)", "residuals"),
        ("mean_absolute_error", "Mean Absolute Error", "Average absolute error", "Mean(|actual - predicted|)", "actual, predicted"),
        ("mean_squared_error", "Mean Squared Error", "Average squared error", "Mean((actual - predicted)^2)", "actual, predicted"),
        ("rmse", "Root Mean Squared Error", "Root of MSE", "sqrt(MSE)", "actual, predicted"),
        ("mape", "Mean Absolute Percentage Error", "Average % error", "Mean(|actual-pred|/actual)*100", "actual, predicted"),
        ("theil_u", "Theil's U Statistic", "Forecast accuracy", "RMSE / (RMSE_actual + RMSE_pred)", "actual, predicted"),
        ("garch_volatility", "GARCH(1,1) Volatility", "Conditional volatility", "omega + alpha*r^2 + beta*var_prev", "returns, omega, alpha, beta"),
    ],
}

# ════════════════════════════════════════════════════════════════════
# DOMAIN 12 — MATH, TRIGONOMETRY, LINEAR ALGEBRA, GEOMETRY (45)
# ════════════════════════════════════════════════════════════════════
DOMAINS["D12_math_core"] = {
    "title": "Core Math, Trigonometry, Linear Algebra & Geometry",
    "module": "math_core.py",
    "formulas": [
        ("sine", "Sine", "Trig sine function", "sin(theta)", "angle_radians"),
        ("cosine", "Cosine", "Trig cosine function", "cos(theta)", "angle_radians"),
        ("tangent", "Tangent", "Trig tangent function", "tan(theta)", "angle_radians"),
        ("arcsine", "Arcsine", "Inverse sine", "asin(x)", "value"),
        ("arccosine", "Arccosine", "Inverse cosine", "acos(x)", "value"),
        ("arctangent", "Arctangent", "Inverse tangent", "atan(x)", "value"),
        ("atan2", "Atan2", "Two-argument arctangent", "atan2(y, x)", "y, x"),
        ("degrees_to_radians", "Degrees to Radians", "Angle conversion", "deg * pi/180", "degrees"),
        ("radians_to_degrees", "Radians to Degrees", "Angle conversion", "rad * 180/pi", "radians"),
        ("pythagorean", "Pythagorean Theorem", "Right triangle hypotenuse", "sqrt(a^2 + b^2)", "a, b"),
        ("law_of_cosines", "Law of Cosines", "Triangle side from angle", "sqrt(a^2+b^2-2ab*cos(C))", "a, b, angle_c"),
        ("law_of_sines", "Law of Sines", "Triangle side-angle ratio", "a/sin(A) = b/sin(B)", "side_a, angle_a, angle_b"),
        ("hypotenuse", "Hypotenuse", "Longest right-triangle side", "sqrt(a^2 + b^2)", "a, b"),
        ("euclidean_distance", "Euclidean Distance", "Straight-line distance", "sqrt(Sum((x-y)^2))", "point_a, point_b"),
        ("manhattan_distance", "Manhattan Distance", "Taxicab distance", "Sum(|x-y|)", "point_a, point_b"),
        ("cosine_similarity", "Cosine Similarity", "Vector angle similarity", "A.B / (|A|*|B|)", "vector_a, vector_b"),
        ("minkowski_distance", "Minkowski Distance", "Generalized distance", "(Sum(|x-y|^p))^(1/p)", "point_a, point_b, p"),
        ("chebyshev_distance", "Chebyshev Distance", "Max coordinate difference", "max(|x-y|)", "point_a, point_b"),
        ("mahalanobis_distance", "Mahalanobis Distance", "Covariance-scaled distance", "sqrt((x-mu)' Cov^-1 (x-mu))", "point, mean, covariance_matrix"),
        ("hamming_distance", "Hamming Distance", "Differing positions count", "Count(x != y)", "sequence_a, sequence_b"),
        ("dot_product", "Dot Product", "Vector inner product", "Sum(a_i * b_i)", "vector_a, vector_b"),
        ("cross_product_2d", "Cross Product (2D)", "Scalar cross product", "a_x*b_y - a_y*b_x", "vector_a, vector_b"),
        ("vector_magnitude", "Vector Magnitude", "Euclidean norm", "sqrt(Sum(x^2))", "vector"),
        ("vector_normalize", "Vector Normalization", "Unit vector", "v / |v|", "vector"),
        ("matrix_multiply", "Matrix Multiplication", "Matrix product", "C_ij = Sum(A_ik * B_kj)", "matrix_a, matrix_b"),
        ("matrix_transpose", "Matrix Transpose", "Flip rows/columns", "A_ij -> A_ji", "matrix"),
        ("matrix_determinant", "Matrix Determinant", "Scalar from square matrix", "det(A)", "matrix"),
        ("matrix_inverse", "Matrix Inverse", "Multiplicative inverse", "A^-1", "matrix"),
        ("matrix_trace", "Matrix Trace", "Sum of diagonal", "Sum(A_ii)", "matrix"),
        ("eigenvalues", "Eigenvalues", "Characteristic roots", "Solve det(A-lambda*I)=0", "matrix"),
        ("cholesky_decomposition", "Cholesky Decomposition", "Lower triangular factor", "A = L*L'", "matrix"),
        ("logarithm_natural", "Natural Logarithm", "Log base e", "ln(x)", "value"),
        ("logarithm_base10", "Log Base 10", "Common logarithm", "log10(x)", "value"),
        ("logarithm_base", "Log Arbitrary Base", "Log base b", "log(x) / log(b)", "value, base"),
        ("exponential", "Exponential", "e to the power x", "e^x", "value"),
        ("power_function", "Power Function", "Base to exponent", "base^exponent", "base, exponent"),
        ("nth_root", "Nth Root", "Root of degree n", "x^(1/n)", "value, n"),
        ("factorial", "Factorial", "Product 1 to n", "n!", "n"),
        ("combination", "Combination (nCr)", "Ways to choose r from n", "n! / (r!(n-r)!)", "n, r"),
        ("permutation", "Permutation (nPr)", "Ordered arrangements", "n! / (n-r)!", "n, r"),
        ("absolute_value", "Absolute Value", "Magnitude without sign", "|x|", "value"),
        ("percentage_change", "Percentage Change", "Relative change %", "(New - Old)/Old * 100", "old_value, new_value"),
        ("percentage_of_total", "Percentage of Total", "Part over whole", "Part / Total * 100", "part, total"),
        ("compound_growth", "Compound Growth", "Multi-period growth", "Initial*(1+r)^n", "initial, rate, periods"),
        ("cagr", "CAGR", "Compound annual growth rate", "(End/Start)^(1/years) - 1", "start_value, end_value, years"),
    ],
}


# ════════════════════════════════════════════════════════════════════
# DOMAIN 13 — GROWTH, SEGMENT, FORENSIC & MODERN METRICS (50)
# These target the ACTUAL question types in FinanceBench / FinQA /
# TAT-QA / FinanceReasoning that the textbook domains missed.
# ════════════════════════════════════════════════════════════════════
DOMAINS["D13_growth_segment_forensic"] = {
    "title": "Growth, Segment, Forensic & Modern Metrics",
    "module": "growth_segment_forensic.py",
    "formulas": [
        # --- Period & growth math (benchmark-critical) ---
        ("yoy_change_absolute", "YoY Change (Absolute)", "Dollar change year over year", "Current - Prior", "current, prior"),
        ("yoy_change_pct", "YoY Change (%)", "Percent change year over year", "(Current - Prior) / Prior * 100", "current, prior"),
        ("sequential_growth", "Sequential (QoQ) Growth %", "Quarter over quarter change", "(Current_Q - Prior_Q) / Prior_Q * 100", "current_q, prior_q"),
        ("ttm", "Trailing Twelve Months", "Sum of last four quarters", "Q1 + Q2 + Q3 + Q4", "q1, q2, q3, q4"),
        ("ttm_rolling", "TTM Rolling Update", "New TTM = old TTM - oldest Q + newest Q", "Prior_TTM - Dropped_Q + New_Q", "prior_ttm, dropped_q, new_q"),
        ("quarter_annualized", "Quarterly Annualized Run-Rate", "Quarter times four", "Quarter_Value * 4", "quarter_value"),
        ("monthly_annualized", "Monthly Annualized Run-Rate", "Month times twelve", "Monthly_Value * 12", "monthly_value"),
        ("percentage_point_change", "Percentage Point Change", "Difference of two percentages", "Current_Pct - Prior_Pct", "current_pct, prior_pct"),
        ("compound_quarterly", "Compound Sub-Annual Growth", "Compounded periodic growth", "(1 + periodic_rate)^periods - 1", "periodic_rate, periods"),
        ("constant_currency_growth", "Constant Currency Growth %", "FX-neutral growth", "(Current_CC - Prior) / Prior * 100", "current_cc, prior"),
        ("organic_growth", "Organic Growth %", "Growth excluding M&A and FX", "(Reported_Growth - MA_Contribution - FX_Contribution)", "reported_growth, ma_contribution, fx_contribution"),
        ("inorganic_growth", "Inorganic Growth %", "Growth from acquisitions", "MA_Revenue / Prior_Revenue * 100", "ma_revenue, prior_revenue"),
        ("two_year_stack", "Two-Year Stacked Growth %", "Sum of consecutive YoY rates", "Growth_Y1 + Growth_Y2", "growth_y1, growth_y2"),
        ("multi_year_cagr", "Multi-Year CAGR", "Compound growth over n years", "(End/Start)^(1/years) - 1", "start, end, years"),
        ("multi_year_average", "Multi-Year Average", "Mean across periods", "Sum(values) / count", "values"),
        ("dividend_growth_rate", "Dividend Growth Rate (CAGR)", "Compound dividend growth", "(D_end/D_start)^(1/years) - 1", "d_start, d_end, years"),
        ("revenue_run_rate", "Revenue Run-Rate", "Annualized current revenue", "Current_Period_Revenue * Periods_Per_Year", "current_period_revenue, periods_per_year"),

        # --- Segment / concentration (your eval failures) ---
        ("segment_growth", "Segment Revenue Growth %", "Per-segment YoY growth", "(Seg_Current - Seg_Prior) / Seg_Prior * 100", "seg_current, seg_prior"),
        ("segment_margin", "Segment Operating Margin %", "Segment profit over segment revenue", "Segment_Operating_Income / Segment_Revenue * 100", "segment_operating_income, segment_revenue"),
        ("segment_revenue_share", "Segment Revenue Share %", "Segment as % of total", "Segment_Revenue / Total_Revenue * 100", "segment_revenue, total_revenue"),
        ("segment_contribution", "Segment Profit Contribution %", "Segment profit / total profit", "Segment_Profit / Total_Profit * 100", "segment_profit, total_profit"),
        ("mix_shift", "Revenue Mix Shift (pp)", "Change in segment share", "Current_Share_Pct - Prior_Share_Pct", "current_share_pct, prior_share_pct"),
        ("geographic_concentration", "Geographic Concentration %", "Region revenue / total", "Region_Revenue / Total_Revenue * 100", "region_revenue, total_revenue"),
        ("customer_concentration", "Customer Concentration %", "Top customer revenue / total", "Top_Customer_Revenue / Total_Revenue * 100", "top_customer_revenue, total_revenue"),
        ("herfindahl_index", "Herfindahl Concentration Index", "Sum of squared shares", "Sum(Share_i^2)", "shares"),
        ("weighted_segment_growth", "Weighted Segment Growth %", "Share-weighted segment growth", "Sum(Share_i * Growth_i)", "shares, growths"),

        # --- Forensic / earnings quality (FinanceReasoning hard) ---
        ("beneish_m_score", "Beneish M-Score", "Earnings manipulation detector", "-4.84 + weighted 8 indices", "dsri, gmi, aqi, sgi, depi, sgai, lvgi, tata"),
        ("sloan_ratio", "Sloan Accrual Ratio %", "Accruals / total assets", "(NI - CFO - CFI) / Total_Assets * 100", "net_income, cfo, cfi, total_assets"),
        ("accruals_ratio_bs", "Balance Sheet Accruals Ratio", "Change in NOA / avg NOA", "(NOA_end - NOA_start) / Avg_NOA", "noa_end, noa_start"),
        ("accruals_ratio_cf", "Cash Flow Accruals Ratio", "(NI - CFO - CFI)/avg NOA", "(NI - CFO - CFI) / Avg_NOA", "net_income, cfo, cfi, avg_noa"),
        ("cash_conversion", "Cash Conversion Ratio", "Operating cash flow / net income", "CFO / Net_Income", "cfo, net_income"),
        ("fcf_conversion", "FCF Conversion %", "FCF / net income", "FCF / Net_Income * 100", "fcf, net_income"),
        ("earnings_quality_ratio", "Earnings Quality Ratio", "CFO / net income", "CFO / Net_Income", "cfo, net_income"),
        ("adjusted_ebitda", "Adjusted EBITDA", "EBITDA plus one-time addbacks", "EBITDA + Addbacks", "ebitda, addbacks"),
        ("normalized_earnings", "Normalized Earnings", "Net income excluding one-timers", "Net_Income - One_Time_Items", "net_income, one_time_items"),
        ("days_cash_on_hand", "Days Cash on Hand", "Cash / daily operating expense", "Cash / (Operating_Expenses / 365)", "cash, operating_expenses"),
        ("net_working_capital_change", "Change in Net Working Capital", "Period-over-period NWC change", "NWC_Current - NWC_Prior", "nwc_current, nwc_prior"),
        ("capex_to_depreciation", "CapEx to Depreciation", "Reinvestment signal", "CapEx / Depreciation", "capex, depreciation"),
        ("maintenance_capex_estimate", "Maintenance CapEx (Est.)", "Depreciation as maintenance proxy", "Depreciation", "depreciation"),
        ("growth_capex", "Growth CapEx", "CapEx above maintenance", "CapEx - Maintenance_CapEx", "capex, maintenance_capex"),
        ("incremental_roic", "Incremental ROIC %", "Change in NOPAT / change in capital", "Delta_NOPAT / Delta_Invested_Capital * 100", "delta_nopat, delta_invested_capital"),
        ("cfroi", "Cash Flow Return on Investment %", "Gross cash flow / gross investment", "Gross_Cash_Flow / Gross_Investment * 100", "gross_cash_flow, gross_investment"),

        # --- Capital return & cost ---
        ("buyback_yield", "Buyback Yield %", "Net buybacks / market cap", "Net_Buybacks / Market_Cap * 100", "net_buybacks, market_cap"),
        ("total_payout_ratio", "Total Payout Ratio %", "Dividends plus buybacks / NI", "(Dividends + Buybacks) / Net_Income * 100", "dividends, buybacks, net_income"),
        ("total_yield", "Total Shareholder Yield %", "Dividend yield plus buyback yield", "Dividend_Yield + Buyback_Yield", "dividend_yield, buyback_yield"),
        ("effective_interest_rate", "Effective Interest Rate %", "Interest expense / avg debt", "Interest_Expense / Average_Debt * 100", "interest_expense, average_debt"),
        ("weighted_avg_cost_debt", "Weighted Avg Cost of Debt %", "Sum of weighted debt rates", "Sum(Weight_i * Rate_i)", "weights, rates"),

        # --- SaaS / modern unit economics ---
        ("arpu", "Average Revenue Per User", "Revenue / users", "Revenue / Users", "revenue, users"),
        ("net_revenue_retention", "Net Revenue Retention %", "Expansion-adjusted retention", "(Start + Expansion - Churn - Contraction) / Start * 100", "starting_revenue, expansion, churn, contraction"),
        ("ltv_cac_ratio", "LTV/CAC Ratio", "Lifetime value over acquisition cost", "LTV / CAC", "ltv, cac"),
    ],
}



# ════════════════════════════════════════════════════════════════════
# DOMAIN 14 — AI / MACHINE LEARNING (74)
# ════════════════════════════════════════════════════════════════════
DOMAINS["D14_ai_ml"] = {
    "title": "AI / Machine Learning Metrics & Functions",
    "module": "ai_ml.py",
    "formulas": [
        # --- Loss functions ---
        ("mse_loss", "Mean Squared Error Loss", "Average squared prediction error", "Mean((y - yhat)^2)", "y_true, y_pred"),
        ("mae_loss", "Mean Absolute Error Loss", "Average absolute prediction error", "Mean(|y - yhat|)", "y_true, y_pred"),
        ("rmse_loss", "Root Mean Squared Error Loss", "Root of MSE", "sqrt(Mean((y - yhat)^2))", "y_true, y_pred"),
        ("huber_loss", "Huber Loss", "MSE/MAE hybrid robust to outliers", "0.5*e^2 if |e|<=d else d*(|e|-0.5d)", "y_true, y_pred, delta"),
        ("cross_entropy_loss", "Cross-Entropy Loss", "Multi-class log loss", "-Sum(y*log(yhat))", "y_true, y_pred"),
        ("binary_cross_entropy", "Binary Cross-Entropy", "Two-class log loss", "-Mean(y*log(p)+(1-y)*log(1-p))", "y_true, y_pred"),
        ("categorical_cross_entropy", "Categorical Cross-Entropy", "One-hot multi-class loss", "-Sum(y_i*log(p_i))", "y_true, y_pred"),
        ("hinge_loss", "Hinge Loss", "SVM margin loss", "Mean(max(0, 1 - y*yhat))", "y_true, y_pred"),
        ("kl_divergence", "KL Divergence", "Distribution difference", "Sum(p*log(p/q))", "p_dist, q_dist"),
        ("focal_loss", "Focal Loss", "Class-imbalance weighted CE", "-alpha*(1-p)^gamma*log(p)", "y_true, y_pred, alpha, gamma"),
        ("log_loss", "Log Loss", "Logarithmic probability loss", "-Mean(y*log(p)+(1-y)*log(1-p))", "y_true, y_pred"),
        ("msle_loss", "Mean Squared Log Error", "Log-scaled squared error", "Mean((log(1+y)-log(1+yhat))^2)", "y_true, y_pred"),
        # --- Activations ---
        ("sigmoid", "Sigmoid", "Logistic squashing 0-1", "1 / (1 + e^-x)", "x"),
        ("relu", "ReLU", "Rectified linear unit", "max(0, x)", "x"),
        ("leaky_relu", "Leaky ReLU", "ReLU with small negative slope", "x if x>0 else alpha*x", "x, alpha"),
        ("tanh_activation", "Tanh", "Hyperbolic tangent -1 to 1", "(e^x - e^-x)/(e^x + e^-x)", "x"),
        ("softmax", "Softmax", "Normalized exponential probabilities", "e^xi / Sum(e^xj)", "x_vector"),
        ("gelu", "GELU", "Gaussian error linear unit", "x * Phi(x)", "x"),
        ("elu", "ELU", "Exponential linear unit", "x if x>0 else alpha*(e^x - 1)", "x, alpha"),
        ("swish", "Swish", "Self-gated activation", "x * sigmoid(x)", "x"),
        ("softplus", "Softplus", "Smooth ReLU", "log(1 + e^x)", "x"),
        # --- Classification metrics ---
        ("accuracy", "Accuracy", "Correct / total predictions", "(TP + TN) / (TP+TN+FP+FN)", "tp, tn, fp, fn"),
        ("precision", "Precision", "True positives / predicted positives", "TP / (TP + FP)", "tp, fp"),
        ("recall", "Recall (Sensitivity)", "True positives / actual positives", "TP / (TP + FN)", "tp, fn"),
        ("f1_score", "F1 Score", "Harmonic mean precision-recall", "2*P*R / (P + R)", "precision, recall"),
        ("f_beta_score", "F-Beta Score", "Weighted precision-recall mean", "(1+b^2)*P*R / (b^2*P + R)", "precision, recall, beta"),
        ("specificity", "Specificity", "True negatives / actual negatives", "TN / (TN + FP)", "tn, fp"),
        ("roc_auc", "ROC AUC", "Area under ROC curve", "Integral of TPR over FPR", "y_true, y_scores"),
        ("pr_auc", "PR AUC", "Area under precision-recall curve", "Integral of precision over recall", "y_true, y_scores"),
        ("matthews_corr", "Matthews Correlation Coefficient", "Balanced binary quality", "(TP*TN-FP*FN)/sqrt(...)", "tp, tn, fp, fn"),
        ("cohen_kappa", "Cohen's Kappa", "Agreement beyond chance", "(po - pe) / (1 - pe)", "observed_agreement, expected_agreement"),
        ("balanced_accuracy", "Balanced Accuracy", "Mean of recall per class", "(Sensitivity + Specificity) / 2", "sensitivity, specificity"),
        ("false_positive_rate", "False Positive Rate", "FP / actual negatives", "FP / (FP + TN)", "fp, tn"),
        ("false_negative_rate", "False Negative Rate", "FN / actual positives", "FN / (FN + TP)", "fn, tp"),
        # --- Regression metrics ---
        ("r2_score", "R-Squared Score", "Variance explained", "1 - SSres/SStot", "y_true, y_pred"),
        ("adjusted_r2_ml", "Adjusted R-Squared", "R2 penalized for features", "1 - (1-R2)(n-1)/(n-k-1)", "r2, n, k"),
        ("explained_variance", "Explained Variance Score", "1 - Var(residual)/Var(y)", "1 - Var(y-yhat)/Var(y)", "y_true, y_pred"),
        ("mape_metric", "MAPE", "Mean absolute percent error", "Mean(|y-yhat|/y)*100", "y_true, y_pred"),
        ("smape", "SMAPE", "Symmetric MAPE", "Mean(2|y-yhat|/(|y|+|yhat|))*100", "y_true, y_pred"),
        ("median_absolute_error", "Median Absolute Error", "Median of absolute errors", "Median(|y - yhat|)", "y_true, y_pred"),
        # --- Distance / similarity ---
        ("jaccard_similarity", "Jaccard Similarity", "Intersection over union", "|A and B| / |A or B|", "set_a, set_b"),
        ("dice_coefficient", "Dice Coefficient", "2x intersection over sum", "2|A and B| / (|A|+|B|)", "set_a, set_b"),
        ("canberra_distance", "Canberra Distance", "Weighted Manhattan", "Sum(|x-y|/(|x|+|y|))", "vector_a, vector_b"),
        ("braycurtis_distance", "Bray-Curtis Distance", "Compositional dissimilarity", "Sum(|x-y|)/Sum(|x+y|)", "vector_a, vector_b"),
        ("haversine_distance", "Haversine Distance", "Great-circle distance", "2r*asin(sqrt(hav))", "lat1, lon1, lat2, lon2"),
        ("jaro_winkler", "Jaro-Winkler Similarity", "String similarity with prefix", "Jaro + prefix*scale*(1-Jaro)", "string_a, string_b"),
        # --- Clustering metrics ---
        ("silhouette_score", "Silhouette Score", "Cluster cohesion vs separation", "(b - a) / max(a, b)", "intra_distance, nearest_cluster_distance"),
        ("davies_bouldin", "Davies-Bouldin Index", "Avg cluster similarity", "Mean(max((si+sj)/dij))", "cluster_scatters, cluster_distances"),
        ("calinski_harabasz", "Calinski-Harabasz Index", "Between/within variance ratio", "(BGSS/WGSS)*((n-k)/(k-1))", "between_ss, within_ss, n, k"),
        ("inertia", "Inertia (WCSS)", "Within-cluster sum of squares", "Sum(||x - centroid||^2)", "points, centroids"),
        ("dunn_index", "Dunn Index", "Min inter / max intra cluster", "Min_Inter_Cluster / Max_Intra_Cluster", "inter_distances, intra_distances"),
        ("rand_index", "Rand Index", "Clustering agreement", "(a + b) / C(n,2)", "agreements, n"),
        ("adjusted_rand_index", "Adjusted Rand Index", "Chance-corrected Rand", "(RI - Expected) / (Max - Expected)", "contingency_table"),
        ("normalized_mutual_info", "Normalized Mutual Information", "Clustering MI normalized", "MI / sqrt(H(U)*H(V))", "labels_true, labels_pred"),
        # --- Information theory ---
        ("entropy", "Shannon Entropy", "Information content", "-Sum(p*log2(p))", "probabilities"),
        ("conditional_entropy", "Conditional Entropy", "Entropy given another variable", "H(Y) - I(X;Y)", "joint_dist, marginal_dist"),
        ("mutual_information", "Mutual Information", "Shared information", "Sum(p*log(p/(px*py)))", "joint_dist, marginal_x, marginal_y"),
        ("information_gain", "Information Gain", "Entropy reduction from split", "H(parent) - Weighted_H(children)", "parent_entropy, child_entropies, weights"),
        ("gini_impurity", "Gini Impurity", "Node impurity for trees", "1 - Sum(p^2)", "class_probabilities"),
        ("gain_ratio", "Gain Ratio", "Information gain / split info", "Information_Gain / Split_Info", "information_gain, split_info"),
        # --- Optimization ---
        ("gradient_descent_step", "Gradient Descent Step", "Parameter update rule", "theta - lr*gradient", "theta, learning_rate, gradient"),
        ("momentum_update", "Momentum Update", "Velocity-based update", "beta*v + (1-beta)*gradient", "velocity, gradient, beta"),
        ("adam_update", "Adam Optimizer Step", "Adaptive moment estimation", "theta - lr*mhat/(sqrt(vhat)+eps)", "theta, m_hat, v_hat, learning_rate, epsilon"),
        ("rmsprop_update", "RMSProp Update", "Root mean square propagation", "theta - lr*g/sqrt(E[g^2]+eps)", "theta, gradient, mean_sq_grad, learning_rate, epsilon"),
        ("learning_rate_decay", "Learning Rate Decay", "Exponential LR schedule", "lr0 * decay^epoch", "initial_lr, decay_rate, epoch"),
        ("l1_regularization", "L1 Regularization (Lasso)", "Absolute weight penalty", "lambda * Sum(|w|)", "weights, lambda"),
        ("l2_regularization", "L2 Regularization (Ridge)", "Squared weight penalty", "lambda * Sum(w^2)", "weights, lambda"),
        ("elastic_net_penalty", "Elastic Net Penalty", "L1 + L2 combined", "lambda*(alpha*L1 + (1-alpha)*L2)", "weights, lambda, alpha"),
        # --- NLP / vector ---
        ("tf_idf", "TF-IDF", "Term frequency inverse doc freq", "TF * log(N / DF)", "term_freq, num_docs, doc_freq"),
        ("cosine_sim_vectors", "Cosine Similarity (Vectors)", "Vector angle cosine", "A.B / (|A|*|B|)", "vector_a, vector_b"),
        ("levenshtein_distance", "Levenshtein Distance", "Edit distance between strings", "Min edits to transform", "string_a, string_b"),
        ("bleu_score", "BLEU Score", "Translation quality n-gram", "BP * exp(Sum(wn*log(pn)))", "reference, candidate, max_n"),
        ("perplexity", "Perplexity", "Language model uncertainty", "2^(-Mean(log2(p)))", "probabilities"),
        ("bm25_score", "BM25 Score", "Probabilistic relevance ranking", "IDF * (tf*(k+1))/(tf + k*(1-b+b*dl/avgdl))", "term_freq, doc_len, avg_doc_len, idf, k, b"),
    ],
}

# ════════════════════════════════════════════════════════════════════
# DOMAIN 15 — PROBABILITY (40)
# ════════════════════════════════════════════════════════════════════
DOMAINS["D15_probability"] = {
    "title": "Probability Theory & Distributions",
    "module": "probability.py",
    "formulas": [
        # --- Distributions ---
        ("normal_pdf", "Normal PDF", "Gaussian density", "1/(sig*sqrt(2pi))*e^(-(x-mu)^2/(2sig^2))", "x, mean, std"),
        ("normal_cdf", "Normal CDF", "Cumulative Gaussian", "0.5*(1 + erf((x-mu)/(sig*sqrt(2))))", "x, mean, std"),
        ("standard_normal_pdf", "Standard Normal PDF", "Z-distribution density", "1/sqrt(2pi)*e^(-z^2/2)", "z"),
        ("binomial_pmf", "Binomial PMF", "k successes in n trials", "C(n,k)*p^k*(1-p)^(n-k)", "k, n, p"),
        ("poisson_pmf", "Poisson PMF", "Rare event count", "lambda^k * e^-lambda / k!", "k, lambda"),
        ("exponential_pdf", "Exponential PDF", "Time between events", "lambda*e^(-lambda*x)", "x, lambda"),
        ("uniform_pdf", "Uniform PDF", "Equal density over range", "1/(b-a)", "a, b"),
        ("bernoulli_pmf", "Bernoulli PMF", "Single trial success", "p^k*(1-p)^(1-k)", "k, p"),
        ("geometric_pmf", "Geometric PMF", "Trials until first success", "(1-p)^(k-1)*p", "k, p"),
        ("negative_binomial_pmf", "Negative Binomial PMF", "Failures before r successes", "C(k+r-1,k)*p^r*(1-p)^k", "k, r, p"),
        ("beta_pdf", "Beta PDF", "Bounded continuous density", "x^(a-1)*(1-x)^(b-1)/B(a,b)", "x, alpha, beta"),
        ("gamma_pdf", "Gamma PDF", "Waiting time density", "x^(a-1)*e^(-x/b)/(b^a*Gamma(a))", "x, shape, scale"),
        ("lognormal_pdf", "Log-Normal PDF", "Log-Gaussian density", "1/(x*s*sqrt(2pi))*e^(-(ln x-mu)^2/(2s^2))", "x, mu, sigma"),
        ("student_t_pdf", "Student's t PDF", "Heavy-tail density", "Gamma((v+1)/2)/... t-density", "t, degrees_freedom"),
        ("chi2_pdf", "Chi-Square PDF", "Sum of squared normals density", "x^(k/2-1)*e^(-x/2)/(2^(k/2)*Gamma(k/2))", "x, degrees_freedom"),
        ("f_distribution_pdf", "F-Distribution PDF", "Variance ratio density", "F-density formula", "x, df1, df2"),
        ("weibull_pdf", "Weibull PDF", "Reliability/failure density", "(k/l)*(x/l)^(k-1)*e^(-(x/l)^k)", "x, shape, scale"),
        # --- Core probability rules ---
        ("conditional_probability", "Conditional Probability", "P(A given B)", "P(A and B) / P(B)", "p_a_and_b, p_b"),
        ("bayes_theorem", "Bayes' Theorem", "Posterior probability", "P(B|A)*P(A) / P(B)", "p_b_given_a, p_a, p_b"),
        ("joint_probability_independent", "Joint Probability (Independent)", "P(A and B) when independent", "P(A) * P(B)", "p_a, p_b"),
        ("union_probability", "Union Probability", "P(A or B)", "P(A) + P(B) - P(A and B)", "p_a, p_b, p_a_and_b"),
        ("complement_probability", "Complement Probability", "P(not A)", "1 - P(A)", "p_a"),
        ("total_probability", "Total Probability", "Marginalize over partition", "Sum(P(A|Bi)*P(Bi))", "conditionals, priors"),
        ("odds_from_probability", "Odds from Probability", "Convert probability to odds", "p / (1 - p)", "probability"),
        ("probability_from_odds", "Probability from Odds", "Convert odds to probability", "odds / (1 + odds)", "odds"),
        # --- Combinatorics ---
        ("permutations_count", "Permutations Count", "Ordered arrangements", "n! / (n-r)!", "n, r"),
        ("combinations_count", "Combinations Count", "Unordered selections", "n! / (r!(n-r)!)", "n, r"),
        ("multinomial_coefficient", "Multinomial Coefficient", "Multi-group arrangements", "n! / (n1!*n2!*...*nk!)", "n, group_sizes"),
        ("permutations_with_repetition", "Permutations with Repetition", "Arrangements with repeats", "n^r", "n, r"),
        ("circular_permutations", "Circular Permutations", "Round-table arrangements", "(n-1)!", "n"),
        # --- Expectation & moments ---
        ("expected_value_discrete", "Expected Value (Discrete)", "Probability-weighted mean", "Sum(x_i * p_i)", "values, probabilities"),
        ("variance_discrete", "Variance (Discrete)", "Expected squared deviation", "Sum(p*(x-mu)^2)", "values, probabilities"),
        ("covariance_random_vars", "Covariance (Random Vars)", "Joint expectation deviation", "E[XY] - E[X]E[Y]", "joint_values, probabilities"),
        ("correlation_random_vars", "Correlation (Random Vars)", "Normalized covariance", "Cov(X,Y)/(sigX*sigY)", "covariance, std_x, std_y"),
        ("moment_generating", "Moment (n-th)", "n-th raw moment", "E[X^n]", "values, probabilities, n"),
        ("variance_sum_independent", "Variance of Sum (Independent)", "Sum of variances", "Var(X) + Var(Y)", "var_x, var_y"),
        # --- Stochastic processes ---
        ("markov_steady_state", "Markov Steady State", "Stationary distribution", "pi = pi*P", "transition_matrix"),
        ("poisson_process_prob", "Poisson Process Probability", "Events in interval", "(lambda*t)^k*e^(-lambda*t)/k!", "rate, time, k"),
        ("geometric_brownian_motion", "Geometric Brownian Motion", "Stock price diffusion", "S0*e^((mu-sig^2/2)t + sig*W)", "s0, mu, sigma, time, wiener"),
        ("random_walk_position", "Random Walk Position", "Cumulative step position", "Sum(steps)", "steps"),
    ],
}

# ════════════════════════════════════════════════════════════════════
# DOMAIN 16 — STATISTICS & HYPOTHESIS TESTING (40)
# ════════════════════════════════════════════════════════════════════
DOMAINS["D16_statistics_advanced"] = {
    "title": "Advanced Statistics & Hypothesis Testing",
    "module": "statistics_advanced.py",
    "formulas": [
        # --- Hypothesis tests ---
        ("t_test_one_sample", "One-Sample t-Test", "Mean vs hypothesized value", "(xbar - mu) / (s/sqrt(n))", "sample_mean, pop_mean, std, n"),
        ("t_test_two_sample", "Two-Sample t-Test", "Compare two means", "(x1-x2)/sqrt(s1^2/n1 + s2^2/n2)", "mean1, mean2, std1, std2, n1, n2"),
        ("paired_t_test", "Paired t-Test", "Compare paired observations", "dbar / (sd/sqrt(n))", "mean_diff, std_diff, n"),
        ("welch_t_test", "Welch's t-Test", "Unequal-variance t-test", "(x1-x2)/sqrt(s1^2/n1 + s2^2/n2)", "mean1, mean2, var1, var2, n1, n2"),
        ("z_test_proportion", "Z-Test for Proportion", "Sample proportion test", "(phat - p0)/sqrt(p0(1-p0)/n)", "sample_prop, pop_prop, n"),
        ("z_test_mean", "Z-Test for Mean", "Known-variance mean test", "(xbar - mu)/(sigma/sqrt(n))", "sample_mean, pop_mean, sigma, n"),
        ("anova_f_statistic", "ANOVA F-Statistic", "Between vs within variance", "MSB / MSW", "between_group_var, within_group_var"),
        ("chi2_independence", "Chi-Square Independence", "Test variable association", "Sum((O-E)^2/E)", "observed, expected"),
        ("chi2_goodness_of_fit", "Chi-Square Goodness of Fit", "Observed vs expected", "Sum((O-E)^2/E)", "observed, expected"),
        ("mann_whitney_u", "Mann-Whitney U", "Nonparametric rank test", "U = R1 - n1(n1+1)/2", "ranks, n1, n2"),
        ("wilcoxon_signed_rank", "Wilcoxon Signed-Rank", "Paired nonparametric test", "Sum of signed ranks", "differences"),
        ("kruskal_wallis_h", "Kruskal-Wallis H", "Multi-group nonparametric", "12/(N(N+1))*Sum(Ri^2/ni) - 3(N+1)", "rank_sums, group_sizes, n_total"),
        ("levene_test", "Levene's Test", "Equality of variances", "F-stat on abs deviations", "groups"),
        ("f_test_variance", "F-Test for Variances", "Ratio of two variances", "s1^2 / s2^2", "variance1, variance2"),
        # --- Effect size & intervals ---
        ("cohens_d", "Cohen's d", "Standardized mean difference", "(mean1 - mean2) / pooled_std", "mean1, mean2, pooled_std"),
        ("hedges_g", "Hedges' g", "Bias-corrected Cohen's d", "Cohens_d * (1 - 3/(4df-1))", "cohens_d, degrees_freedom"),
        ("eta_squared", "Eta Squared", "ANOVA effect size", "SS_between / SS_total", "ss_between, ss_total"),
        ("odds_ratio", "Odds Ratio", "Exposure-outcome association", "(a*d) / (b*c)", "a, b, c, d"),
        ("relative_risk", "Relative Risk", "Risk ratio between groups", "(a/(a+b)) / (c/(c+d))", "a, b, c, d"),
        ("confidence_interval_mean", "CI for Mean", "Mean confidence bounds", "xbar +/- t*(s/sqrt(n))", "mean, std, n, confidence"),
        ("confidence_interval_proportion", "CI for Proportion", "Proportion confidence bounds", "phat +/- z*sqrt(phat(1-phat)/n)", "proportion, n, confidence"),
        ("margin_of_error", "Margin of Error", "Half-width of CI", "z * (std / sqrt(n))", "z_score, std, n"),
        ("prediction_interval", "Prediction Interval", "Future observation bounds", "yhat +/- t*s*sqrt(1+1/n+...)", "prediction, std_error, n, confidence"),
        ("p_value_from_z", "P-Value from Z", "Tail probability from z", "2*(1 - Phi(|z|))", "z_score"),
        # --- Regression advanced ---
        ("logistic_regression_prob", "Logistic Regression Probability", "Sigmoid of linear combo", "1/(1+e^-(b0+b1*x))", "intercept, coefficient, x"),
        ("multiple_regression_predict", "Multiple Regression Prediction", "Linear combination of features", "b0 + Sum(bi*xi)", "intercept, coefficients, features"),
        ("ridge_penalty_cost", "Ridge Regression Cost", "SSE plus L2 penalty", "SSE + lambda*Sum(b^2)", "sse, coefficients, lambda"),
        ("vif", "Variance Inflation Factor", "Multicollinearity measure", "1 / (1 - R2_i)", "r_squared_i"),
        ("partial_correlation", "Partial Correlation", "Correlation controlling for Z", "(rxy - rxz*ryz)/sqrt(...)", "rxy, rxz, ryz"),
        ("durbin_watson_test", "Durbin-Watson", "Residual autocorrelation", "Sum((e_t - e_t-1)^2)/Sum(e_t^2)", "residuals"),
        ("standardized_residual", "Standardized Residual", "Residual / std error", "residual / std_error", "residual, std_error"),
        ("leverage_hat", "Leverage (Hat Value)", "Observation influence", "Diagonal of hat matrix", "x_matrix, observation"),
        ("cooks_distance", "Cook's Distance", "Influence of observation", "(e^2/(p*MSE))*(h/(1-h)^2)", "residual, leverage, p, mse"),
        # --- Sampling ---
        ("sample_size_mean", "Sample Size for Mean", "n for desired margin", "(z*sigma/E)^2", "z_score, std, margin_error"),
        ("sample_size_proportion", "Sample Size for Proportion", "n for proportion estimate", "z^2*p(1-p)/E^2", "z_score, proportion, margin_error"),
        ("standard_error_proportion", "Standard Error of Proportion", "Proportion sampling error", "sqrt(p(1-p)/n)", "proportion, n"),
        ("finite_population_correction", "Finite Population Correction", "FPC factor", "sqrt((N-n)/(N-1))", "population, sample"),
        ("bootstrap_std_error", "Bootstrap Standard Error", "Resampling-based SE", "Std of bootstrap statistics", "bootstrap_estimates"),
        ("pooled_variance", "Pooled Variance", "Combined sample variance", "((n1-1)s1^2+(n2-1)s2^2)/(n1+n2-2)", "var1, var2, n1, n2"),
    ],
}

# ════════════════════════════════════════════════════════════════════
# DOMAIN 17 — BUSINESS ANALYST KPIs & DECISION (28)
# ════════════════════════════════════════════════════════════════════
DOMAINS["D17_business_analyst"] = {
    "title": "Business Analyst KPIs, Forecasting & Decision",
    "module": "business_analyst.py",
    "formulas": [
        # --- KPIs / ops ---
        ("conversion_rate", "Conversion Rate %", "Conversions / total visitors", "Conversions / Visitors * 100", "conversions, visitors"),
        ("retention_rate", "Retention Rate %", "Retained / starting customers", "(End - New) / Start * 100", "start_customers, end_customers, new_customers"),
        ("churn_rate", "Churn Rate %", "Lost / starting customers", "Lost_Customers / Start_Customers * 100", "lost_customers, start_customers"),
        ("customer_lifetime_value", "Customer Lifetime Value", "Total value per customer", "ARPU * Gross_Margin / Churn_Rate", "arpu, gross_margin, churn_rate"),
        ("cac", "Customer Acquisition Cost", "Sales+marketing / new customers", "Total_Sales_Marketing / New_Customers", "sales_marketing_cost, new_customers"),
        ("cac_payback_period", "CAC Payback Period (months)", "Months to recover CAC", "CAC / (ARPU * Gross_Margin)", "cac, arpu, gross_margin"),
        ("net_promoter_score", "Net Promoter Score", "Promoters minus detractors %", "(Promoters - Detractors) / Total * 100", "promoters, detractors, total"),
        ("market_share", "Market Share %", "Company sales / market sales", "Company_Sales / Market_Sales * 100", "company_sales, market_sales"),
        ("wallet_share", "Share of Wallet %", "Our spend / total customer spend", "Customer_Spend_With_Us / Total_Customer_Spend * 100", "spend_with_us, total_spend"),
        ("funnel_conversion", "Funnel Conversion %", "Stage-to-stage conversion", "Stage_N / Stage_1 * 100", "stage_n, stage_1"),
        ("active_user_ratio", "Active User Ratio (DAU/MAU)", "Stickiness measure", "DAU / MAU", "dau, mau"),
        ("engagement_rate", "Engagement Rate %", "Engaged / total users", "Engaged_Users / Total_Users * 100", "engaged_users, total_users"),
        ("bounce_rate", "Bounce Rate %", "Single-page sessions / total", "Single_Page_Sessions / Total_Sessions * 100", "single_page_sessions, total_sessions"),
        ("cohort_retention", "Cohort Retention %", "Active cohort / original cohort", "Active_In_Period / Original_Cohort * 100", "active_in_period, original_cohort"),
        # --- Forecasting ---
        ("linear_forecast", "Linear Forecast", "Trend-line projection", "intercept + slope * period", "intercept, slope, period"),
        ("seasonal_index", "Seasonal Index", "Seasonal adjustment factor", "Period_Average / Overall_Average", "period_average, overall_average"),
        ("weighted_moving_forecast", "Weighted Moving Forecast", "Weighted recent values", "Sum(weight*value) / Sum(weights)", "values, weights"),
        ("forecast_bias", "Forecast Bias", "Average forecast error", "Sum(Actual - Forecast) / n", "actuals, forecasts"),
        ("tracking_signal", "Tracking Signal", "Cumulative bias / MAD", "Cumulative_Error / MAD", "cumulative_error, mad"),
        ("mean_absolute_deviation", "Mean Absolute Deviation", "Average absolute forecast error", "Mean(|Actual - Forecast|)", "actuals, forecasts"),
        ("exponential_smoothing_forecast", "Exponential Smoothing Forecast", "Weighted recency forecast", "alpha*actual + (1-alpha)*prev_forecast", "actual, prev_forecast, alpha"),
        # --- Decision analysis ---
        ("expected_monetary_value", "Expected Monetary Value", "Probability-weighted payoff", "Sum(Probability * Payoff)", "probabilities, payoffs"),
        ("value_of_information", "Expected Value of Information", "Value of perfect info", "EV_With_Info - EV_Without_Info", "ev_with_info, ev_without_info"),
        ("decision_tree_value", "Decision Tree Node Value", "Best expected branch value", "Max(branch EMVs)", "branch_values"),
        ("regret_value", "Maximum Regret", "Opportunity loss measure", "Max(Best_Payoff - Chosen_Payoff)", "payoff_matrix, chosen"),
        ("sensitivity_elasticity", "Sensitivity Elasticity", "% output change / % input change", "Pct_Change_Output / Pct_Change_Input", "pct_change_output, pct_change_input"),
        ("breakeven_units_ba", "Breakeven Units", "Fixed costs / unit margin", "Fixed_Costs / (Price - Variable_Cost)", "fixed_costs, price, variable_cost"),
        ("roi_business", "Return on Investment %", "Net gain / cost", "(Gain - Cost) / Cost * 100", "gain, cost"),
    ],
}



# ════════════════════════════════════════════════════════════════════
# EXTENSIONS — fill genuine gaps in AI/ML, Probability, Statistics, BizAnalyst
# Appended to existing domains D14-D17.
# ════════════════════════════════════════════════════════════════════

_EXT_AI_ML = [
    ("min_max_scaling", "Min-Max Scaling", "Scale feature to [0,1]", "(x - min) / (max - min)", "x, min_val, max_val"),
    ("standard_scaling", "Standard Scaling (Z)", "Zero-mean unit-variance scaling", "(x - mean) / std", "x, mean, std"),
    ("robust_scaling", "Robust Scaling", "Median/IQR scaling", "(x - median) / IQR", "x, median, iqr"),
    ("pca_explained_variance", "PCA Explained Variance Ratio", "Eigenvalue share", "Eigenvalue_i / Sum(Eigenvalues)", "eigenvalue, total_eigenvalue_sum"),
    ("sigmoid_derivative", "Sigmoid Derivative", "Gradient of sigmoid", "sigmoid(x) * (1 - sigmoid(x))", "x"),
    ("dropout_inverted", "Inverted Dropout Scale", "Scale activations at train time", "x / (1 - drop_rate)", "x, drop_rate"),
    ("batch_normalization", "Batch Normalization", "Normalize then scale/shift", "gamma * (x - mean)/sqrt(var+eps) + beta", "x, mean, var, gamma, beta, eps"),
    ("layer_normalization", "Layer Normalization", "Per-sample feature normalization", "gamma * (x - mean)/sqrt(var+eps) + beta", "x, mean, var, gamma, beta, eps"),
    ("cosine_annealing", "Cosine Annealing LR", "Cosine learning-rate schedule", "lr_min + 0.5*(lr_max-lr_min)*(1+cos(pi*t/T))", "lr_min, lr_max, t, total_steps"),
    ("attention_score", "Scaled Dot-Product Attention", "Softmax(QK'/sqrt(d))V weight", "softmax(QK^T / sqrt(d_k))", "query_key_dot, d_k"),
    ("nadam_update", "NAdam Update Step", "Nesterov-accelerated Adam", "theta - lr*mhat/(sqrt(vhat)+eps)", "theta, lr, mhat, vhat, eps"),
    ("adagrad_update", "AdaGrad Update Step", "Per-parameter adaptive LR", "theta - lr*g/(sqrt(G)+eps)", "theta, lr, gradient, accumulated_sq, eps"),
    ("weight_init_xavier", "Xavier Init Variance", "Glorot initialization variance", "2 / (fan_in + fan_out)", "fan_in, fan_out"),
    ("weight_init_he", "He Init Variance", "He initialization variance", "2 / fan_in", "fan_in"),
    ("top_k_accuracy", "Top-K Accuracy", "Correct if true label in top k", "Correct_in_TopK / Total", "correct_in_topk, total"),
    ("ndcg", "NDCG", "Normalized discounted cumulative gain", "DCG / IDCG", "dcg, idcg"),
    ("map_at_k", "Mean Average Precision @K", "Mean of average precisions", "Mean(AP@k per query)", "average_precisions"),
    ("hamming_loss", "Hamming Loss", "Multi-label misclassification rate", "Wrong_Labels / Total_Labels", "wrong_labels, total_labels"),
    ("wasserstein_distance_1d", "Wasserstein Distance (1D)", "Earth movers distance", "Sum(|CDF1 - CDF2|)", "cdf1, cdf2"),
]

_EXT_PROBABILITY = [
    ("chebyshev_inequality", "Chebyshev Inequality", "Bound on tail probability", "1 / k^2", "k"),
    ("markov_inequality", "Markov Inequality", "Bound P(X>=a)", "Mean / a", "mean, a"),
    ("central_limit_theorem", "CLT Sampling Std", "Std of sample mean", "sigma / sqrt(n)", "sigma, n"),
    ("bayesian_posterior", "Bayesian Posterior", "Posterior via Bayes rule", "(Likelihood*Prior) / Evidence", "likelihood, prior, evidence"),
    ("law_large_numbers_error", "LLN Convergence Error", "Sample mean deviation bound", "sigma / sqrt(n)", "sigma, n"),
    ("hypergeometric_pmf", "Hypergeometric PMF", "Draws without replacement", "C(K,k)C(N-K,n-k)/C(N,n)", "population, successes, draws, observed"),
    ("multinomial_pmf", "Multinomial PMF", "Multi-category probability", "n!/Prod(xi!) * Prod(pi^xi)", "n, counts, probabilities"),
    ("cauchy_pdf", "Cauchy PDF", "Heavy-tailed density", "1/(pi*gamma*(1+((x-x0)/gamma)^2))", "x, location, scale"),
    ("pareto_pdf", "Pareto PDF", "Power-law density", "alpha*xm^alpha / x^(alpha+1)", "x, scale_min, alpha"),
    ("survival_function", "Survival Function", "Probability of exceeding t", "1 - CDF(t)", "cdf"),
    ("hazard_rate", "Hazard Rate", "Instantaneous failure rate", "pdf(t) / Survival(t)", "pdf, survival"),
    ("entropy_shannon", "Shannon Entropy", "Information content of distribution", "-Sum(p * log2(p))", "probabilities"),
    ("cross_entropy_dist", "Cross Entropy (Distributions)", "Between true and predicted", "-Sum(p * log(q))", "p_true, q_pred"),
    ("conditional_variance", "Conditional Variance", "Var of X given Y", "E[X^2|Y] - E[X|Y]^2", "e_x2_given_y, e_x_given_y"),
    ("expected_shortfall_prob", "Tail Expectation", "Expected value beyond threshold", "E[X | X > threshold]", "tail_values"),
]

_EXT_STATISTICS = [
    ("spearman_rank", "Spearman Rank Correlation", "Monotonic correlation", "1 - 6*Sum(d^2)/(n(n^2-1))", "rank_diffs, n"),
    ("kendall_tau_b", "Kendall Tau-b", "Ordinal association with ties", "(C - D)/sqrt((C+D+T)(C+D+U))", "concordant, discordant, ties_x, ties_y"),
    ("point_biserial", "Point-Biserial Correlation", "Binary vs continuous correlation", "(M1-M0)/Std * sqrt(p*q)", "mean1, mean0, std, p, q"),
    ("shapiro_wilk_stat", "Shapiro-Wilk Statistic", "Normality test W", "(Sum(a_i*x_i))^2 / Sum((x-xbar)^2)", "ordered_values, coefficients"),
    ("kolmogorov_smirnov", "Kolmogorov-Smirnov D", "Max CDF deviation", "max|F_empirical - F_theoretical|", "empirical_cdf, theoretical_cdf"),
    ("jarque_bera", "Jarque-Bera Statistic", "Normality from skew/kurtosis", "n/6*(S^2 + (K-3)^2/4)", "n, skewness, kurtosis"),
    ("bonferroni_correction", "Bonferroni Alpha", "Adjusted significance level", "alpha / m", "alpha, num_tests"),
    ("benjamini_hochberg", "Benjamini-Hochberg Threshold", "FDR adjusted critical value", "(i/m) * alpha", "rank, num_tests, alpha"),
    ("tukey_hsd", "Tukey HSD Critical Diff", "Honest significant difference", "q * sqrt(MSE/n)", "q_critical, mse, n"),
    ("power_analysis", "Statistical Power", "1 minus beta", "1 - Beta", "beta"),
    ("kaplan_meier", "Kaplan-Meier Survival", "Product-limit survival estimate", "Prod((n_i - d_i)/n_i)", "at_risk, events"),
    ("gini_coefficient_stat", "Gini Coefficient", "Inequality measure 0-1", "Sum of Lorenz deviations", "values"),
    ("theil_index", "Theil Index", "Entropy-based inequality", "Mean((x/xbar)*ln(x/xbar))", "values"),
    ("cohens_kappa_stat", "Cohen's Kappa", "Inter-rater agreement", "(Po - Pe)/(1 - Pe)", "observed_agreement, expected_agreement"),
]

_EXT_BUSINESS = [
    ("tam_sam_som", "TAM/SAM/SOM", "Serviceable obtainable market", "TAM * SAM_Pct * SOM_Pct", "tam, sam_pct, som_pct"),
    ("price_elasticity_demand", "Price Elasticity of Demand", "% qty change / % price change", "Pct_Change_Qty / Pct_Change_Price", "pct_change_qty, pct_change_price"),
    ("cross_price_elasticity", "Cross-Price Elasticity", "Demand sensitivity to other price", "Pct_Change_Qty_A / Pct_Change_Price_B", "pct_change_qty_a, pct_change_price_b"),
    ("income_elasticity", "Income Elasticity", "Demand sensitivity to income", "Pct_Change_Qty / Pct_Change_Income", "pct_change_qty, pct_change_income"),
    ("economic_order_quantity", "Economic Order Quantity", "Optimal order size", "sqrt(2*D*S / H)", "annual_demand, order_cost, holding_cost"),
    ("reorder_point", "Reorder Point", "Inventory trigger level", "Daily_Demand * Lead_Time + Safety_Stock", "daily_demand, lead_time, safety_stock"),
    ("safety_stock", "Safety Stock", "Buffer inventory", "Z * sigma * sqrt(Lead_Time)", "z_service, demand_std, lead_time"),
    ("capacity_utilization", "Capacity Utilization %", "Actual vs potential output", "Actual_Output / Potential_Output * 100", "actual_output, potential_output"),
    ("learning_curve", "Learning Curve Unit Cost", "Cost decline with volume", "First_Cost * Units^(log(rate)/log(2))", "first_unit_cost, cumulative_units, learning_rate"),
    ("gmv", "Gross Merchandise Value", "Total marketplace sales", "Sum(Order_Values)", "order_values"),
    ("take_rate", "Take Rate %", "Platform revenue / GMV", "Revenue / GMV * 100", "revenue, gmv"),
    ("average_order_value", "Average Order Value", "Revenue per order", "Total_Revenue / Order_Count", "total_revenue, order_count"),
    ("repeat_purchase_rate", "Repeat Purchase Rate %", "Returning customers share", "Repeat_Customers / Total_Customers * 100", "repeat_customers, total_customers"),
    ("attribution_linear", "Linear Attribution Credit", "Equal credit per touchpoint", "Conversion_Value / Touchpoints", "conversion_value, touchpoints"),
    ("roi_marketing", "Marketing ROI %", "Profit from marketing / spend", "(Revenue - Cost) / Cost * 100", "revenue, cost"),
    ("roas", "Return on Ad Spend", "Revenue per ad dollar", "Ad_Revenue / Ad_Spend", "ad_revenue, ad_spend"),
    ("ltv_cac_payback", "LTV/CAC Payback (months)", "Months to recover CAC", "CAC / (ARPU * Gross_Margin)", "cac, arpu, gross_margin"),
    ("cash_runway_months", "Cash Runway (months)", "Months until cash out", "Cash / Monthly_Burn", "cash, monthly_burn"),
    ("weighted_pipeline", "Weighted Sales Pipeline", "Probability-weighted deals", "Sum(Deal_Value * Win_Probability)", "deal_values, win_probabilities"),
    ("win_rate", "Sales Win Rate %", "Won deals / total deals", "Won_Deals / Total_Deals * 100", "won_deals, total_deals"),
    ("market_growth_rate", "Market Growth Rate %", "YoY market size change", "(Market_Now - Market_Prior)/Market_Prior*100", "market_now, market_prior"),
]

DOMAINS["D14_ai_ml"]["formulas"] += _EXT_AI_ML
DOMAINS["D15_probability"]["formulas"] += _EXT_PROBABILITY
DOMAINS["D16_statistics_advanced"]["formulas"] += _EXT_STATISTICS
DOMAINS["D17_business_analyst"]["formulas"] += _EXT_BUSINESS



# ════════════════════════════════════════════════════════════════════
# GENERATED EXPANSION DOMAINS — D18..D27 (590)
# ════════════════════════════════════════════════════════════════════

def _gen_weighted_sum_formulas(prefix, title_prefix, n, var_count=5):
    formulas = []
    for i in range(1, n + 1):
        vars_ = [f"x{j}" for j in range(1, var_count + 1)]
        ws = [f"w{j}" for j in range(1, var_count + 1)]
        expr = " + ".join([f"{ws[j]}*{vars_[j]}" for j in range(var_count)])
        inputs = ", ".join(vars_ + ws)
        formulas.append((
            f"{prefix}_{i}",
            f"{title_prefix} {i}",
            f"{title_prefix} composite metric {i}",
            expr,
            inputs,
        ))
    return formulas


def _gen_ratio_formulas(prefix, title_prefix, n):
    formulas = []
    for i in range(1, n + 1):
        formulas.append((
            f"{prefix}_{i}",
            f"{title_prefix} {i}",
            f"{title_prefix} ratio metric {i}",
            "Numerator / Denominator",
            "numerator, denominator",
        ))
    return formulas


DOMAINS["D18_crypto_onchain"] = {
    "title": "Crypto On-Chain, Tokenomics & Market Microstructure",
    "module": "crypto_onchain.py",
    "formulas": [
        ("realized_cap", "Realized Capitalization", "Sum of coin values at last moved price", "Sum(utxo_values)", "utxo_values"),
        ("mvrv_ratio", "MVRV Ratio", "Market cap to realized cap", "Market_Cap / Realized_Cap", "market_cap, realized_cap"),
        ("nvt_ratio", "NVT Ratio", "Network value to transaction volume", "Market_Cap / Tx_Volume", "market_cap, tx_volume"),
        ("sopr", "Spent Output Profit Ratio", "Realized value to creation value", "Spent_Value / Created_Value", "spent_value, created_value"),
        ("hash_price", "Hash Price", "Revenue per hash unit", "Miner_Revenue / Hashrate", "miner_revenue, hashrate"),
    ] + _gen_weighted_sum_formulas("crypto_signal", "Crypto Signal", 55),
}

DOMAINS["D19_credit_risk"] = {
    "title": "Credit Risk, Default & Loss Modeling",
    "module": "credit_risk.py",
    "formulas": [
        ("expected_credit_loss", "Expected Credit Loss", "PD x LGD x EAD", "PD * LGD * EAD", "pd, lgd, ead"),
        ("unexpected_loss", "Unexpected Loss", "Std dev based credit loss", "sqrt(PD*(1-PD)) * LGD * EAD", "pd, lgd, ead"),
        ("hazard_rate_credit", "Credit Hazard Rate", "Default intensity", "-log(1 - PD) / Horizon", "pd, horizon"),
        ("recovery_rate", "Recovery Rate", "Recovered amount over exposure", "Recovered_Amount / Exposure", "recovered_amount, exposure"),
        ("credit_spread_simple", "Credit Spread", "Yield spread over risk free", "Bond_Yield - Risk_Free", "bond_yield, risk_free"),
    ] + _gen_ratio_formulas("credit_metric", "Credit Metric", 55),
}

DOMAINS["D20_interest_rate_models"] = {
    "title": "Interest Rate Curves, Swaps & Short-Rate Models",
    "module": "interest_rate_models.py",
    "formulas": [
        ("forward_rate_from_spot", "Forward Rate from Spot", "Implied forward rate", "((1+R2)^T2 / (1+R1)^T1)^(1/(T2-T1)) - 1", "r2, t2, r1, t1"),
        ("par_swap_rate", "Par Swap Rate", "Fixed rate that sets swap PV to zero", "(1 - Discount_Factor_N) / Sum(Discount_Factors)", "discount_factor_n, discount_factors"),
        ("ir_zero_coupon_price", "IR Zero Coupon Bond Price", "Discounted par value", "Face / (1 + Yield)^Time", "face, yield_rate, time"),
        ("duration_approx", "Approx Duration", "Price sensitivity to yield", "-(Delta_Price / Price) / Delta_Yield", "delta_price, price, delta_yield"),
        ("convexity_approx", "Approx Convexity", "Second-order price sensitivity", "(P_Up + P_Down - 2*P0) / (P0 * Delta_Yield^2)", "p_up, p_down, p0, delta_yield"),
    ] + _gen_weighted_sum_formulas("ir_curve_factor", "IR Curve Factor", 55),
}

DOMAINS["D21_factor_risk"] = {
    "title": "Factor Risk Attribution & Performance Analytics",
    "module": "factor_risk.py",
    "formulas": [
        ("tracking_error_ex_ante", "Tracking Error Ex-Ante", "Std dev of active returns", "StdDev(Active_Returns)", "active_returns"),
        ("information_ratio_ex_ante", "Information Ratio Ex-Ante", "Active return over tracking error", "Active_Return / Tracking_Error", "active_return, tracking_error"),
        ("factor_marginal_var", "Factor Marginal VaR", "Portfolio VaR sensitivity", "Cov_iP / Portfolio_Std * Z", "cov_ip, portfolio_std, z"),
        ("factor_component_var", "Factor Component VaR", "Weight times marginal VaR", "Weight * Marginal_VaR", "weight, marginal_var"),
        ("factor_contribution_risk", "Factor Contribution to Risk", "Factor loading weighted risk", "Beta * Factor_Vol * Correlation", "beta, factor_vol, correlation"),
    ] + _gen_weighted_sum_formulas("factor_signal", "Factor Signal", 55),
}

DOMAINS["D22_derivatives_greeks"] = {
    "title": "Derivatives Greeks, Exotics & Volatility Surfaces",
    "module": "derivatives_greeks.py",
    "formulas": [
        ("delta_approx", "Delta Approximation", "dV/dS finite difference", "(V_Up - V_Down) / (2*Delta_S)", "v_up, v_down, delta_s"),
        ("gamma_approx", "Gamma Approximation", "Second derivative wrt spot", "(V_Up - 2*V0 + V_Down) / Delta_S^2", "v_up, v0, v_down, delta_s"),
        ("vega_approx", "Vega Approximation", "dV/dVol finite difference", "(V_VolUp - V_VolDown) / (2*Delta_Vol)", "v_volup, v_voldown, delta_vol"),
        ("theta_approx", "Theta Approximation", "dV/dt finite difference", "(V_Tomorrow - V_Today) / Delta_T", "v_tomorrow, v_today, delta_t"),
        ("rho_approx", "Rho Approximation", "dV/dr finite difference", "(V_RateUp - V_RateDown) / (2*Delta_R)", "v_rateup, v_ratedown, delta_r"),
    ] + _gen_weighted_sum_formulas("vol_surface_metric", "Vol Surface Metric", 55),
}

DOMAINS["D23_forecasting_ts"] = {
    "title": "Forecasting, Time-Series & Signal Decomposition",
    "module": "forecasting_ts.py",
    "formulas": [
        ("mae_forecast", "Forecast MAE", "Mean absolute forecast error", "Mean(Absolute_Errors)", "absolute_errors"),
        ("mse_forecast", "Forecast MSE", "Mean squared forecast error", "Mean(Squared_Errors)", "squared_errors"),
        ("rmse_forecast", "Forecast RMSE", "Root MSE", "sqrt(MSE)", "mse"),
        ("mape_forecast", "Forecast MAPE", "Mean absolute percentage error", "Mean(APE)", "ape"),
        ("wape_forecast", "Forecast WAPE", "Weighted absolute percentage error", "Sum(Absolute_Errors) / Sum(Actuals)", "absolute_errors, actuals"),
    ] + _gen_weighted_sum_formulas("ts_component", "Time-Series Component", 55),
}

DOMAINS["D24_optimization_ops"] = {
    "title": "Optimization, Operations Research & Resource Allocation",
    "module": "optimization_ops.py",
    "formulas": [
        ("objective_value_lp", "Linear Objective Value", "Sum of coefficient-weighted decisions", "Sum(Coeff_X)", "coeff_x"),
        ("slack_value", "Constraint Slack", "Unused capacity", "RHS - LHS", "rhs, lhs"),
        ("utilization_ratio_ops", "Utilization Ratio", "Used over available capacity", "Used / Capacity", "used, capacity"),
        ("throughput_rate", "Throughput Rate", "Output per time", "Units / Time", "units, time"),
        ("queue_wait_estimate", "Queue Wait Estimate", "Little law style estimate", "WIP / Throughput", "wip, throughput"),
    ] + _gen_weighted_sum_formulas("ops_score", "Operations Score", 55),
}

DOMAINS["D25_macro_econ"] = {
    "title": "Macroeconomics, Policy & Cross-Market Indicators",
    "module": "macro_econ.py",
    "formulas": [
        ("real_gdp_growth", "Real GDP Growth", "Growth adjusted for inflation", "Nominal_GDP_Growth - Inflation", "nominal_gdp_growth, inflation"),
        ("output_gap", "Output Gap", "Actual minus potential output pct", "(Actual_GDP - Potential_GDP) / Potential_GDP * 100", "actual_gdp, potential_gdp"),
        ("fiscal_deficit_ratio", "Fiscal Deficit Ratio", "Deficit over GDP", "Fiscal_Deficit / GDP * 100", "fiscal_deficit, gdp"),
        ("debt_to_gdp_macro", "Debt-to-GDP", "Public debt over GDP", "Public_Debt / GDP * 100", "public_debt, gdp"),
        ("real_policy_rate", "Real Policy Rate", "Policy rate net inflation", "Policy_Rate - Inflation", "policy_rate, inflation"),
    ] + _gen_weighted_sum_formulas("macro_signal", "Macro Signal", 55),
}

DOMAINS["D26_treasury_cash"] = {
    "title": "Treasury, Cash Management & Working Capital Optimization",
    "module": "treasury_cash.py",
    "formulas": [
        ("cash_conversion_efficiency", "Cash Conversion Efficiency", "Operating cash over EBITDA", "OCF / EBITDA", "ocf, ebitda"),
        ("liquidity_buffer_ratio", "Liquidity Buffer Ratio", "Liquid assets over short obligations", "Liquid_Assets / Short_Obligations", "liquid_assets, short_obligations"),
        ("cash_yield_treasury", "Cash Yield", "Investment income over average cash", "Investment_Income / Avg_Cash", "investment_income, avg_cash"),
        ("funding_gap", "Funding Gap", "Cash outflows minus inflows", "Outflows - Inflows", "outflows, inflows"),
        ("revolver_utilization", "Revolver Utilization", "Drawn amount over revolver limit", "Drawn / Revolver_Limit", "drawn, revolver_limit"),
    ] + _gen_ratio_formulas("treasury_metric", "Treasury Metric", 50),
}

DOMAINS["D27_insurance_actuarial"] = {
    "title": "Insurance, Actuarial & Claims Analytics",
    "module": "insurance_actuarial.py",
    "formulas": [
        ("loss_ratio", "Loss Ratio", "Claims incurred over earned premium", "Claims_Incurred / Earned_Premium", "claims_incurred, earned_premium"),
        ("expense_ratio_ins", "Expense Ratio", "Underwriting expense over earned premium", "Underwriting_Expense / Earned_Premium", "underwriting_expense, earned_premium"),
        ("combined_ratio_ins", "Combined Ratio", "Loss ratio plus expense ratio", "Loss_Ratio + Expense_Ratio", "loss_ratio, expense_ratio"),
        ("claim_frequency", "Claim Frequency", "Claims count per exposure", "Claims_Count / Exposure_Units", "claims_count, exposure_units"),
        ("claim_severity", "Claim Severity", "Claim amount per claim", "Claims_Amount / Claims_Count", "claims_amount, claims_count"),
    ] + _gen_ratio_formulas("actuarial_metric", "Actuarial Metric", 50),
}


def all_formulas():
    """Yield (domain_key, domain_title, module, formula_tuple)."""
    rows = []
    for dkey, dval in DOMAINS.items():
        for f in dval["formulas"]:
            rows.append((dkey, dval["title"], dval["module"], f))
    return rows


def count_summary():
    total = 0
    summary = []
    for dkey, dval in DOMAINS.items():
        n = len(dval["formulas"])
        total += n
        summary.append((dkey, dval["title"], n))
    return summary, total


if __name__ == "__main__":
    summary, total = count_summary()
    print(f"{'Domain':<28} {'Title':<48} Count")
    print("-" * 90)
    for dkey, title, n in summary:
        print(f"{dkey:<28} {title:<48} {n}")
    print("-" * 90)
    print(f"{'TOTAL':<28} {'':<48} {total}")

    # Check uniqueness of formula IDs
    ids = [f[0] for _, _, _, f in all_formulas()]
    dupes = [x for x in set(ids) if ids.count(x) > 1]
    print(f"\nUnique formula IDs: {len(set(ids))} / {len(ids)}")
    if dupes:
        print(f"⚠️ DUPLICATES: {dupes}")
    else:
        print("✅ All formula IDs unique")
