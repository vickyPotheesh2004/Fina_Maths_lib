from .base import build_result, formula

DOMAIN_KEY = "D13_growth_segment_forensic"
DOMAIN_TITLE = "Growth, Segment, Forensic & Modern Metrics"
FORMULA_IDS = [
    "yoy_change_absolute",
    "yoy_change_pct",
    "sequential_growth",
    "ttm",
    "ttm_rolling",
    "quarter_annualized",
    "monthly_annualized",
    "percentage_point_change",
    "compound_quarterly",
    "constant_currency_growth",
    "organic_growth",
    "inorganic_growth",
    "two_year_stack",
    "multi_year_cagr",
    "multi_year_average",
    "dividend_growth_rate",
    "revenue_run_rate",
    "segment_growth",
    "segment_margin",
    "segment_revenue_share",
    "segment_contribution",
    "mix_shift",
    "geographic_concentration",
    "customer_concentration",
    "herfindahl_index",
    "weighted_segment_growth",
    "beneish_m_score",
    "sloan_ratio",
    "accruals_ratio_bs",
    "accruals_ratio_cf",
    "cash_conversion",
    "fcf_conversion",
    "earnings_quality_ratio",
    "adjusted_ebitda",
    "normalized_earnings",
    "days_cash_on_hand",
    "net_working_capital_change",
    "capex_to_depreciation",
    "maintenance_capex_estimate",
    "growth_capex",
    "incremental_roic",
    "cfroi",
    "buyback_yield",
    "total_payout_ratio",
    "total_yield",
    "effective_interest_rate",
    "weighted_avg_cost_debt",
    "arpu",
    "net_revenue_retention",
    "ltv_cac_ratio",
]

@formula("yoy_change_absolute", "YoY Change (Absolute)", "Current - Prior", DOMAIN_KEY, unit="")
def yoy_change_absolute(current: float | None = None, prior: float | None = None, **kwargs):
    return build_result(
        fid="yoy_change_absolute",
        name="YoY Change (Absolute)",
        expression="Current - Prior",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "current": kwargs.get("current", current),
            "prior": kwargs.get("prior", prior),
        },
    )

@formula("yoy_change_pct", "YoY Change (%)", "(Current - Prior) / Prior * 100", DOMAIN_KEY, unit="")
def yoy_change_pct(current: float | None = None, prior: float | None = None, **kwargs):
    return build_result(
        fid="yoy_change_pct",
        name="YoY Change (%)",
        expression="(Current - Prior) / Prior * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "current": kwargs.get("current", current),
            "prior": kwargs.get("prior", prior),
        },
    )

@formula("sequential_growth", "Sequential (QoQ) Growth %", "(Current_Q - Prior_Q) / Prior_Q * 100", DOMAIN_KEY, unit="")
def sequential_growth(current_q: float | None = None, prior_q: float | None = None, **kwargs):
    return build_result(
        fid="sequential_growth",
        name="Sequential (QoQ) Growth %",
        expression="(Current_Q - Prior_Q) / Prior_Q * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "current_q": kwargs.get("current_q", current_q),
            "prior_q": kwargs.get("prior_q", prior_q),
        },
    )

@formula("ttm", "Trailing Twelve Months", "Q1 + Q2 + Q3 + Q4", DOMAIN_KEY, unit="")
def ttm(q1: float | None = None, q2: float | None = None, q3: float | None = None, q4: float | None = None, **kwargs):
    return build_result(
        fid="ttm",
        name="Trailing Twelve Months",
        expression="Q1 + Q2 + Q3 + Q4",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "q1": kwargs.get("q1", q1),
            "q2": kwargs.get("q2", q2),
            "q3": kwargs.get("q3", q3),
            "q4": kwargs.get("q4", q4),
        },
    )

@formula("ttm_rolling", "TTM Rolling Update", "Prior_TTM - Dropped_Q + New_Q", DOMAIN_KEY, unit="")
def ttm_rolling(prior_ttm: float | None = None, dropped_q: float | None = None, new_q: float | None = None, **kwargs):
    return build_result(
        fid="ttm_rolling",
        name="TTM Rolling Update",
        expression="Prior_TTM - Dropped_Q + New_Q",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prior_ttm": kwargs.get("prior_ttm", prior_ttm),
            "dropped_q": kwargs.get("dropped_q", dropped_q),
            "new_q": kwargs.get("new_q", new_q),
        },
    )

@formula("quarter_annualized", "Quarterly Annualized Run-Rate", "Quarter_Value * 4", DOMAIN_KEY, unit="")
def quarter_annualized(quarter_value: float | None = None, **kwargs):
    return build_result(
        fid="quarter_annualized",
        name="Quarterly Annualized Run-Rate",
        expression="Quarter_Value * 4",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "quarter_value": kwargs.get("quarter_value", quarter_value),
        },
    )

@formula("monthly_annualized", "Monthly Annualized Run-Rate", "Monthly_Value * 12", DOMAIN_KEY, unit="")
def monthly_annualized(monthly_value: float | None = None, **kwargs):
    return build_result(
        fid="monthly_annualized",
        name="Monthly Annualized Run-Rate",
        expression="Monthly_Value * 12",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "monthly_value": kwargs.get("monthly_value", monthly_value),
        },
    )

@formula("percentage_point_change", "Percentage Point Change", "Current_Pct - Prior_Pct", DOMAIN_KEY, unit="")
def percentage_point_change(current_pct: float | None = None, prior_pct: float | None = None, **kwargs):
    return build_result(
        fid="percentage_point_change",
        name="Percentage Point Change",
        expression="Current_Pct - Prior_Pct",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "current_pct": kwargs.get("current_pct", current_pct),
            "prior_pct": kwargs.get("prior_pct", prior_pct),
        },
    )

@formula("compound_quarterly", "Compound Sub-Annual Growth", "(1 + periodic_rate)^periods - 1", DOMAIN_KEY, unit="")
def compound_quarterly(periodic_rate: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="compound_quarterly",
        name="Compound Sub-Annual Growth",
        expression="(1 + periodic_rate)^periods - 1",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "periodic_rate": kwargs.get("periodic_rate", periodic_rate),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("constant_currency_growth", "Constant Currency Growth %", "(Current_CC - Prior) / Prior * 100", DOMAIN_KEY, unit="")
def constant_currency_growth(current_cc: float | None = None, prior: float | None = None, **kwargs):
    return build_result(
        fid="constant_currency_growth",
        name="Constant Currency Growth %",
        expression="(Current_CC - Prior) / Prior * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "current_cc": kwargs.get("current_cc", current_cc),
            "prior": kwargs.get("prior", prior),
        },
    )

@formula("organic_growth", "Organic Growth %", "(Reported_Growth - MA_Contribution - FX_Contribution)", DOMAIN_KEY, unit="")
def organic_growth(reported_growth: float | None = None, ma_contribution: float | None = None, fx_contribution: float | None = None, **kwargs):
    return build_result(
        fid="organic_growth",
        name="Organic Growth %",
        expression="(Reported_Growth - MA_Contribution - FX_Contribution)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "reported_growth": kwargs.get("reported_growth", reported_growth),
            "ma_contribution": kwargs.get("ma_contribution", ma_contribution),
            "fx_contribution": kwargs.get("fx_contribution", fx_contribution),
        },
    )

@formula("inorganic_growth", "Inorganic Growth %", "MA_Revenue / Prior_Revenue * 100", DOMAIN_KEY, unit="")
def inorganic_growth(ma_revenue: float | None = None, prior_revenue: float | None = None, **kwargs):
    return build_result(
        fid="inorganic_growth",
        name="Inorganic Growth %",
        expression="MA_Revenue / Prior_Revenue * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ma_revenue": kwargs.get("ma_revenue", ma_revenue),
            "prior_revenue": kwargs.get("prior_revenue", prior_revenue),
        },
    )

@formula("two_year_stack", "Two-Year Stacked Growth %", "Growth_Y1 + Growth_Y2", DOMAIN_KEY, unit="")
def two_year_stack(growth_y1: float | None = None, growth_y2: float | None = None, **kwargs):
    return build_result(
        fid="two_year_stack",
        name="Two-Year Stacked Growth %",
        expression="Growth_Y1 + Growth_Y2",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "growth_y1": kwargs.get("growth_y1", growth_y1),
            "growth_y2": kwargs.get("growth_y2", growth_y2),
        },
    )

@formula("multi_year_cagr", "Multi-Year CAGR", "(End/Start)^(1/years) - 1", DOMAIN_KEY, unit="")
def multi_year_cagr(start: float | None = None, end: float | None = None, years: float | None = None, **kwargs):
    return build_result(
        fid="multi_year_cagr",
        name="Multi-Year CAGR",
        expression="(End/Start)^(1/years) - 1",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "start": kwargs.get("start", start),
            "end": kwargs.get("end", end),
            "years": kwargs.get("years", years),
        },
    )

@formula("multi_year_average", "Multi-Year Average", "Sum(values) / count", DOMAIN_KEY, unit="")
def multi_year_average(values: float | None = None, **kwargs):
    return build_result(
        fid="multi_year_average",
        name="Multi-Year Average",
        expression="Sum(values) / count",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
        },
    )

@formula("dividend_growth_rate", "Dividend Growth Rate (CAGR)", "(D_end/D_start)^(1/years) - 1", DOMAIN_KEY, unit="")
def dividend_growth_rate(d_start: float | None = None, d_end: float | None = None, years: float | None = None, **kwargs):
    return build_result(
        fid="dividend_growth_rate",
        name="Dividend Growth Rate (CAGR)",
        expression="(D_end/D_start)^(1/years) - 1",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "d_start": kwargs.get("d_start", d_start),
            "d_end": kwargs.get("d_end", d_end),
            "years": kwargs.get("years", years),
        },
    )

@formula("revenue_run_rate", "Revenue Run-Rate", "Current_Period_Revenue * Periods_Per_Year", DOMAIN_KEY, unit="")
def revenue_run_rate(current_period_revenue: float | None = None, periods_per_year: float | None = None, **kwargs):
    return build_result(
        fid="revenue_run_rate",
        name="Revenue Run-Rate",
        expression="Current_Period_Revenue * Periods_Per_Year",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "current_period_revenue": kwargs.get("current_period_revenue", current_period_revenue),
            "periods_per_year": kwargs.get("periods_per_year", periods_per_year),
        },
    )

@formula("segment_growth", "Segment Revenue Growth %", "(Seg_Current - Seg_Prior) / Seg_Prior * 100", DOMAIN_KEY, unit="")
def segment_growth(seg_current: float | None = None, seg_prior: float | None = None, **kwargs):
    return build_result(
        fid="segment_growth",
        name="Segment Revenue Growth %",
        expression="(Seg_Current - Seg_Prior) / Seg_Prior * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "seg_current": kwargs.get("seg_current", seg_current),
            "seg_prior": kwargs.get("seg_prior", seg_prior),
        },
    )

@formula("segment_margin", "Segment Operating Margin %", "Segment_Operating_Income / Segment_Revenue * 100", DOMAIN_KEY, unit="")
def segment_margin(segment_operating_income: float | None = None, segment_revenue: float | None = None, **kwargs):
    return build_result(
        fid="segment_margin",
        name="Segment Operating Margin %",
        expression="Segment_Operating_Income / Segment_Revenue * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "segment_operating_income": kwargs.get("segment_operating_income", segment_operating_income),
            "segment_revenue": kwargs.get("segment_revenue", segment_revenue),
        },
    )

@formula("segment_revenue_share", "Segment Revenue Share %", "Segment_Revenue / Total_Revenue * 100", DOMAIN_KEY, unit="")
def segment_revenue_share(segment_revenue: float | None = None, total_revenue: float | None = None, **kwargs):
    return build_result(
        fid="segment_revenue_share",
        name="Segment Revenue Share %",
        expression="Segment_Revenue / Total_Revenue * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "segment_revenue": kwargs.get("segment_revenue", segment_revenue),
            "total_revenue": kwargs.get("total_revenue", total_revenue),
        },
    )

@formula("segment_contribution", "Segment Profit Contribution %", "Segment_Profit / Total_Profit * 100", DOMAIN_KEY, unit="")
def segment_contribution(segment_profit: float | None = None, total_profit: float | None = None, **kwargs):
    return build_result(
        fid="segment_contribution",
        name="Segment Profit Contribution %",
        expression="Segment_Profit / Total_Profit * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "segment_profit": kwargs.get("segment_profit", segment_profit),
            "total_profit": kwargs.get("total_profit", total_profit),
        },
    )

@formula("mix_shift", "Revenue Mix Shift (pp)", "Current_Share_Pct - Prior_Share_Pct", DOMAIN_KEY, unit="")
def mix_shift(current_share_pct: float | None = None, prior_share_pct: float | None = None, **kwargs):
    return build_result(
        fid="mix_shift",
        name="Revenue Mix Shift (pp)",
        expression="Current_Share_Pct - Prior_Share_Pct",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "current_share_pct": kwargs.get("current_share_pct", current_share_pct),
            "prior_share_pct": kwargs.get("prior_share_pct", prior_share_pct),
        },
    )

@formula("geographic_concentration", "Geographic Concentration %", "Region_Revenue / Total_Revenue * 100", DOMAIN_KEY, unit="")
def geographic_concentration(region_revenue: float | None = None, total_revenue: float | None = None, **kwargs):
    return build_result(
        fid="geographic_concentration",
        name="Geographic Concentration %",
        expression="Region_Revenue / Total_Revenue * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "region_revenue": kwargs.get("region_revenue", region_revenue),
            "total_revenue": kwargs.get("total_revenue", total_revenue),
        },
    )

@formula("customer_concentration", "Customer Concentration %", "Top_Customer_Revenue / Total_Revenue * 100", DOMAIN_KEY, unit="")
def customer_concentration(top_customer_revenue: float | None = None, total_revenue: float | None = None, **kwargs):
    return build_result(
        fid="customer_concentration",
        name="Customer Concentration %",
        expression="Top_Customer_Revenue / Total_Revenue * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "top_customer_revenue": kwargs.get("top_customer_revenue", top_customer_revenue),
            "total_revenue": kwargs.get("total_revenue", total_revenue),
        },
    )

@formula("herfindahl_index", "Herfindahl Concentration Index", "Sum(Share_i^2)", DOMAIN_KEY, unit="")
def herfindahl_index(shares: float | None = None, **kwargs):
    return build_result(
        fid="herfindahl_index",
        name="Herfindahl Concentration Index",
        expression="Sum(Share_i^2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "shares": kwargs.get("shares", shares),
        },
    )

@formula("weighted_segment_growth", "Weighted Segment Growth %", "Sum(Share_i * Growth_i)", DOMAIN_KEY, unit="")
def weighted_segment_growth(shares: float | None = None, growths: float | None = None, **kwargs):
    return build_result(
        fid="weighted_segment_growth",
        name="Weighted Segment Growth %",
        expression="Sum(Share_i * Growth_i)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "shares": kwargs.get("shares", shares),
            "growths": kwargs.get("growths", growths),
        },
    )

@formula("beneish_m_score", "Beneish M-Score", "-4.84 + weighted 8 indices", DOMAIN_KEY, unit="")
def beneish_m_score(dsri: float | None = None, gmi: float | None = None, aqi: float | None = None, sgi: float | None = None, depi: float | None = None, sgai: float | None = None, lvgi: float | None = None, tata: float | None = None, **kwargs):
    return build_result(
        fid="beneish_m_score",
        name="Beneish M-Score",
        expression="-4.84 + weighted 8 indices",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "dsri": kwargs.get("dsri", dsri),
            "gmi": kwargs.get("gmi", gmi),
            "aqi": kwargs.get("aqi", aqi),
            "sgi": kwargs.get("sgi", sgi),
            "depi": kwargs.get("depi", depi),
            "sgai": kwargs.get("sgai", sgai),
            "lvgi": kwargs.get("lvgi", lvgi),
            "tata": kwargs.get("tata", tata),
        },
    )

@formula("sloan_ratio", "Sloan Accrual Ratio %", "(NI - CFO - CFI) / Total_Assets * 100", DOMAIN_KEY, unit="")
def sloan_ratio(net_income: float | None = None, cfo: float | None = None, cfi: float | None = None, total_assets: float | None = None, **kwargs):
    return build_result(
        fid="sloan_ratio",
        name="Sloan Accrual Ratio %",
        expression="(NI - CFO - CFI) / Total_Assets * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_income": kwargs.get("net_income", net_income),
            "cfo": kwargs.get("cfo", cfo),
            "cfi": kwargs.get("cfi", cfi),
            "total_assets": kwargs.get("total_assets", total_assets),
        },
    )

@formula("accruals_ratio_bs", "Balance Sheet Accruals Ratio", "(NOA_end - NOA_start) / Avg_NOA", DOMAIN_KEY, unit="")
def accruals_ratio_bs(noa_end: float | None = None, noa_start: float | None = None, **kwargs):
    return build_result(
        fid="accruals_ratio_bs",
        name="Balance Sheet Accruals Ratio",
        expression="(NOA_end - NOA_start) / Avg_NOA",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "noa_end": kwargs.get("noa_end", noa_end),
            "noa_start": kwargs.get("noa_start", noa_start),
        },
    )

@formula("accruals_ratio_cf", "Cash Flow Accruals Ratio", "(NI - CFO - CFI) / Avg_NOA", DOMAIN_KEY, unit="")
def accruals_ratio_cf(net_income: float | None = None, cfo: float | None = None, cfi: float | None = None, avg_noa: float | None = None, **kwargs):
    return build_result(
        fid="accruals_ratio_cf",
        name="Cash Flow Accruals Ratio",
        expression="(NI - CFO - CFI) / Avg_NOA",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_income": kwargs.get("net_income", net_income),
            "cfo": kwargs.get("cfo", cfo),
            "cfi": kwargs.get("cfi", cfi),
            "avg_noa": kwargs.get("avg_noa", avg_noa),
        },
    )

@formula("cash_conversion", "Cash Conversion Ratio", "CFO / Net_Income", DOMAIN_KEY, unit="")
def cash_conversion(cfo: float | None = None, net_income: float | None = None, **kwargs):
    return build_result(
        fid="cash_conversion",
        name="Cash Conversion Ratio",
        expression="CFO / Net_Income",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cfo": kwargs.get("cfo", cfo),
            "net_income": kwargs.get("net_income", net_income),
        },
    )

@formula("fcf_conversion", "FCF Conversion %", "FCF / Net_Income * 100", DOMAIN_KEY, unit="")
def fcf_conversion(fcf: float | None = None, net_income: float | None = None, **kwargs):
    return build_result(
        fid="fcf_conversion",
        name="FCF Conversion %",
        expression="FCF / Net_Income * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "fcf": kwargs.get("fcf", fcf),
            "net_income": kwargs.get("net_income", net_income),
        },
    )

@formula("earnings_quality_ratio", "Earnings Quality Ratio", "CFO / Net_Income", DOMAIN_KEY, unit="")
def earnings_quality_ratio(cfo: float | None = None, net_income: float | None = None, **kwargs):
    return build_result(
        fid="earnings_quality_ratio",
        name="Earnings Quality Ratio",
        expression="CFO / Net_Income",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cfo": kwargs.get("cfo", cfo),
            "net_income": kwargs.get("net_income", net_income),
        },
    )

@formula("adjusted_ebitda", "Adjusted EBITDA", "EBITDA + Addbacks", DOMAIN_KEY, unit="")
def adjusted_ebitda(ebitda: float | None = None, addbacks: float | None = None, **kwargs):
    return build_result(
        fid="adjusted_ebitda",
        name="Adjusted EBITDA",
        expression="EBITDA + Addbacks",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ebitda": kwargs.get("ebitda", ebitda),
            "addbacks": kwargs.get("addbacks", addbacks),
        },
    )

@formula("normalized_earnings", "Normalized Earnings", "Net_Income - One_Time_Items", DOMAIN_KEY, unit="")
def normalized_earnings(net_income: float | None = None, one_time_items: float | None = None, **kwargs):
    return build_result(
        fid="normalized_earnings",
        name="Normalized Earnings",
        expression="Net_Income - One_Time_Items",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_income": kwargs.get("net_income", net_income),
            "one_time_items": kwargs.get("one_time_items", one_time_items),
        },
    )

@formula("days_cash_on_hand", "Days Cash on Hand", "Cash / (Operating_Expenses / 365)", DOMAIN_KEY, unit="")
def days_cash_on_hand(cash: float | None = None, operating_expenses: float | None = None, **kwargs):
    return build_result(
        fid="days_cash_on_hand",
        name="Days Cash on Hand",
        expression="Cash / (Operating_Expenses / 365)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cash": kwargs.get("cash", cash),
            "operating_expenses": kwargs.get("operating_expenses", operating_expenses),
        },
    )

@formula("net_working_capital_change", "Change in Net Working Capital", "NWC_Current - NWC_Prior", DOMAIN_KEY, unit="")
def net_working_capital_change(nwc_current: float | None = None, nwc_prior: float | None = None, **kwargs):
    return build_result(
        fid="net_working_capital_change",
        name="Change in Net Working Capital",
        expression="NWC_Current - NWC_Prior",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "nwc_current": kwargs.get("nwc_current", nwc_current),
            "nwc_prior": kwargs.get("nwc_prior", nwc_prior),
        },
    )

@formula("capex_to_depreciation", "CapEx to Depreciation", "CapEx / Depreciation", DOMAIN_KEY, unit="")
def capex_to_depreciation(capex: float | None = None, depreciation: float | None = None, **kwargs):
    return build_result(
        fid="capex_to_depreciation",
        name="CapEx to Depreciation",
        expression="CapEx / Depreciation",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "capex": kwargs.get("capex", capex),
            "depreciation": kwargs.get("depreciation", depreciation),
        },
    )

@formula("maintenance_capex_estimate", "Maintenance CapEx (Est.)", "Depreciation", DOMAIN_KEY, unit="")
def maintenance_capex_estimate(depreciation: float | None = None, **kwargs):
    return build_result(
        fid="maintenance_capex_estimate",
        name="Maintenance CapEx (Est.)",
        expression="Depreciation",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "depreciation": kwargs.get("depreciation", depreciation),
        },
    )

@formula("growth_capex", "Growth CapEx", "CapEx - Maintenance_CapEx", DOMAIN_KEY, unit="")
def growth_capex(capex: float | None = None, maintenance_capex: float | None = None, **kwargs):
    return build_result(
        fid="growth_capex",
        name="Growth CapEx",
        expression="CapEx - Maintenance_CapEx",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "capex": kwargs.get("capex", capex),
            "maintenance_capex": kwargs.get("maintenance_capex", maintenance_capex),
        },
    )

@formula("incremental_roic", "Incremental ROIC %", "Delta_NOPAT / Delta_Invested_Capital * 100", DOMAIN_KEY, unit="")
def incremental_roic(delta_nopat: float | None = None, delta_invested_capital: float | None = None, **kwargs):
    return build_result(
        fid="incremental_roic",
        name="Incremental ROIC %",
        expression="Delta_NOPAT / Delta_Invested_Capital * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "delta_nopat": kwargs.get("delta_nopat", delta_nopat),
            "delta_invested_capital": kwargs.get("delta_invested_capital", delta_invested_capital),
        },
    )

@formula("cfroi", "Cash Flow Return on Investment %", "Gross_Cash_Flow / Gross_Investment * 100", DOMAIN_KEY, unit="")
def cfroi(gross_cash_flow: float | None = None, gross_investment: float | None = None, **kwargs):
    return build_result(
        fid="cfroi",
        name="Cash Flow Return on Investment %",
        expression="Gross_Cash_Flow / Gross_Investment * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "gross_cash_flow": kwargs.get("gross_cash_flow", gross_cash_flow),
            "gross_investment": kwargs.get("gross_investment", gross_investment),
        },
    )

@formula("buyback_yield", "Buyback Yield %", "Net_Buybacks / Market_Cap * 100", DOMAIN_KEY, unit="")
def buyback_yield(net_buybacks: float | None = None, market_cap: float | None = None, **kwargs):
    return build_result(
        fid="buyback_yield",
        name="Buyback Yield %",
        expression="Net_Buybacks / Market_Cap * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "net_buybacks": kwargs.get("net_buybacks", net_buybacks),
            "market_cap": kwargs.get("market_cap", market_cap),
        },
    )

@formula("total_payout_ratio", "Total Payout Ratio %", "(Dividends + Buybacks) / Net_Income * 100", DOMAIN_KEY, unit="")
def total_payout_ratio(dividends: float | None = None, buybacks: float | None = None, net_income: float | None = None, **kwargs):
    return build_result(
        fid="total_payout_ratio",
        name="Total Payout Ratio %",
        expression="(Dividends + Buybacks) / Net_Income * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "dividends": kwargs.get("dividends", dividends),
            "buybacks": kwargs.get("buybacks", buybacks),
            "net_income": kwargs.get("net_income", net_income),
        },
    )

@formula("total_yield", "Total Shareholder Yield %", "Dividend_Yield + Buyback_Yield", DOMAIN_KEY, unit="")
def total_yield(dividend_yield: float | None = None, buyback_yield: float | None = None, **kwargs):
    return build_result(
        fid="total_yield",
        name="Total Shareholder Yield %",
        expression="Dividend_Yield + Buyback_Yield",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "dividend_yield": kwargs.get("dividend_yield", dividend_yield),
            "buyback_yield": kwargs.get("buyback_yield", buyback_yield),
        },
    )

@formula("effective_interest_rate", "Effective Interest Rate %", "Interest_Expense / Average_Debt * 100", DOMAIN_KEY, unit="")
def effective_interest_rate(interest_expense: float | None = None, average_debt: float | None = None, **kwargs):
    return build_result(
        fid="effective_interest_rate",
        name="Effective Interest Rate %",
        expression="Interest_Expense / Average_Debt * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "interest_expense": kwargs.get("interest_expense", interest_expense),
            "average_debt": kwargs.get("average_debt", average_debt),
        },
    )

@formula("weighted_avg_cost_debt", "Weighted Avg Cost of Debt %", "Sum(Weight_i * Rate_i)", DOMAIN_KEY, unit="")
def weighted_avg_cost_debt(weights: float | None = None, rates: float | None = None, **kwargs):
    return build_result(
        fid="weighted_avg_cost_debt",
        name="Weighted Avg Cost of Debt %",
        expression="Sum(Weight_i * Rate_i)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "weights": kwargs.get("weights", weights),
            "rates": kwargs.get("rates", rates),
        },
    )

@formula("arpu", "Average Revenue Per User", "Revenue / Users", DOMAIN_KEY, unit="")
def arpu(revenue: float | None = None, users: float | None = None, **kwargs):
    return build_result(
        fid="arpu",
        name="Average Revenue Per User",
        expression="Revenue / Users",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "revenue": kwargs.get("revenue", revenue),
            "users": kwargs.get("users", users),
        },
    )

@formula("net_revenue_retention", "Net Revenue Retention %", "(Start + Expansion - Churn - Contraction) / Start * 100", DOMAIN_KEY, unit="")
def net_revenue_retention(starting_revenue: float | None = None, expansion: float | None = None, churn: float | None = None, contraction: float | None = None, **kwargs):
    return build_result(
        fid="net_revenue_retention",
        name="Net Revenue Retention %",
        expression="(Start + Expansion - Churn - Contraction) / Start * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "starting_revenue": kwargs.get("starting_revenue", starting_revenue),
            "expansion": kwargs.get("expansion", expansion),
            "churn": kwargs.get("churn", churn),
            "contraction": kwargs.get("contraction", contraction),
        },
    )

@formula("ltv_cac_ratio", "LTV/CAC Ratio", "LTV / CAC", DOMAIN_KEY, unit="")
def ltv_cac_ratio(ltv: float | None = None, cac: float | None = None, **kwargs):
    return build_result(
        fid="ltv_cac_ratio",
        name="LTV/CAC Ratio",
        expression="LTV / CAC",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ltv": kwargs.get("ltv", ltv),
            "cac": kwargs.get("cac", cac),
        },
    )
