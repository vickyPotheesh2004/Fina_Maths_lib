from .base import build_result, formula

DOMAIN_KEY = "D17_business_analyst"
DOMAIN_TITLE = "Business Analyst KPIs, Forecasting & Decision"
FORMULA_IDS = [
    "conversion_rate",
    "retention_rate",
    "churn_rate",
    "customer_lifetime_value",
    "cac",
    "cac_payback_period",
    "net_promoter_score",
    "market_share",
    "wallet_share",
    "funnel_conversion",
    "active_user_ratio",
    "engagement_rate",
    "bounce_rate",
    "cohort_retention",
    "linear_forecast",
    "seasonal_index",
    "weighted_moving_forecast",
    "forecast_bias",
    "tracking_signal",
    "mean_absolute_deviation",
    "exponential_smoothing_forecast",
    "expected_monetary_value",
    "value_of_information",
    "decision_tree_value",
    "regret_value",
    "sensitivity_elasticity",
    "breakeven_units_ba",
    "roi_business",
    "tam_sam_som",
    "price_elasticity_demand",
    "cross_price_elasticity",
    "income_elasticity",
    "economic_order_quantity",
    "reorder_point",
    "safety_stock",
    "capacity_utilization",
    "learning_curve",
    "gmv",
    "take_rate",
    "average_order_value",
    "repeat_purchase_rate",
    "attribution_linear",
    "roi_marketing",
    "roas",
    "ltv_cac_payback",
    "cash_runway_months",
    "weighted_pipeline",
    "win_rate",
    "market_growth_rate",
]

@formula("conversion_rate", "Conversion Rate %", "Conversions / Visitors * 100", DOMAIN_KEY, unit="")
def conversion_rate(conversions: float | None = None, visitors: float | None = None, **kwargs):
    return build_result(
        fid="conversion_rate",
        name="Conversion Rate %",
        expression="Conversions / Visitors * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "conversions": kwargs.get("conversions", conversions),
            "visitors": kwargs.get("visitors", visitors),
        },
    )

@formula("retention_rate", "Retention Rate %", "(End - New) / Start * 100", DOMAIN_KEY, unit="")
def retention_rate(start_customers: float | None = None, end_customers: float | None = None, new_customers: float | None = None, **kwargs):
    return build_result(
        fid="retention_rate",
        name="Retention Rate %",
        expression="(End - New) / Start * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "start_customers": kwargs.get("start_customers", start_customers),
            "end_customers": kwargs.get("end_customers", end_customers),
            "new_customers": kwargs.get("new_customers", new_customers),
        },
    )

@formula("churn_rate", "Churn Rate %", "Lost_Customers / Start_Customers * 100", DOMAIN_KEY, unit="")
def churn_rate(lost_customers: float | None = None, start_customers: float | None = None, **kwargs):
    return build_result(
        fid="churn_rate",
        name="Churn Rate %",
        expression="Lost_Customers / Start_Customers * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "lost_customers": kwargs.get("lost_customers", lost_customers),
            "start_customers": kwargs.get("start_customers", start_customers),
        },
    )

@formula("customer_lifetime_value", "Customer Lifetime Value", "ARPU * Gross_Margin / Churn_Rate", DOMAIN_KEY, unit="")
def customer_lifetime_value(arpu: float | None = None, gross_margin: float | None = None, churn_rate: float | None = None, **kwargs):
    return build_result(
        fid="customer_lifetime_value",
        name="Customer Lifetime Value",
        expression="ARPU * Gross_Margin / Churn_Rate",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "arpu": kwargs.get("arpu", arpu),
            "gross_margin": kwargs.get("gross_margin", gross_margin),
            "churn_rate": kwargs.get("churn_rate", churn_rate),
        },
    )

@formula("cac", "Customer Acquisition Cost", "Total_Sales_Marketing / New_Customers", DOMAIN_KEY, unit="")
def cac(sales_marketing_cost: float | None = None, new_customers: float | None = None, **kwargs):
    return build_result(
        fid="cac",
        name="Customer Acquisition Cost",
        expression="Total_Sales_Marketing / New_Customers",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "sales_marketing_cost": kwargs.get("sales_marketing_cost", sales_marketing_cost),
            "new_customers": kwargs.get("new_customers", new_customers),
        },
    )

@formula("cac_payback_period", "CAC Payback Period (months)", "CAC / (ARPU * Gross_Margin)", DOMAIN_KEY, unit="")
def cac_payback_period(cac: float | None = None, arpu: float | None = None, gross_margin: float | None = None, **kwargs):
    return build_result(
        fid="cac_payback_period",
        name="CAC Payback Period (months)",
        expression="CAC / (ARPU * Gross_Margin)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cac": kwargs.get("cac", cac),
            "arpu": kwargs.get("arpu", arpu),
            "gross_margin": kwargs.get("gross_margin", gross_margin),
        },
    )

@formula("net_promoter_score", "Net Promoter Score", "(Promoters - Detractors) / Total * 100", DOMAIN_KEY, unit="")
def net_promoter_score(promoters: float | None = None, detractors: float | None = None, total: float | None = None, **kwargs):
    return build_result(
        fid="net_promoter_score",
        name="Net Promoter Score",
        expression="(Promoters - Detractors) / Total * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "promoters": kwargs.get("promoters", promoters),
            "detractors": kwargs.get("detractors", detractors),
            "total": kwargs.get("total", total),
        },
    )

@formula("market_share", "Market Share %", "Company_Sales / Market_Sales * 100", DOMAIN_KEY, unit="")
def market_share(company_sales: float | None = None, market_sales: float | None = None, **kwargs):
    return build_result(
        fid="market_share",
        name="Market Share %",
        expression="Company_Sales / Market_Sales * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "company_sales": kwargs.get("company_sales", company_sales),
            "market_sales": kwargs.get("market_sales", market_sales),
        },
    )

@formula("wallet_share", "Share of Wallet %", "Customer_Spend_With_Us / Total_Customer_Spend * 100", DOMAIN_KEY, unit="")
def wallet_share(spend_with_us: float | None = None, total_spend: float | None = None, **kwargs):
    return build_result(
        fid="wallet_share",
        name="Share of Wallet %",
        expression="Customer_Spend_With_Us / Total_Customer_Spend * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spend_with_us": kwargs.get("spend_with_us", spend_with_us),
            "total_spend": kwargs.get("total_spend", total_spend),
        },
    )

@formula("funnel_conversion", "Funnel Conversion %", "Stage_N / Stage_1 * 100", DOMAIN_KEY, unit="")
def funnel_conversion(stage_n: float | None = None, stage_1: float | None = None, **kwargs):
    return build_result(
        fid="funnel_conversion",
        name="Funnel Conversion %",
        expression="Stage_N / Stage_1 * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "stage_n": kwargs.get("stage_n", stage_n),
            "stage_1": kwargs.get("stage_1", stage_1),
        },
    )

@formula("active_user_ratio", "Active User Ratio (DAU/MAU)", "DAU / MAU", DOMAIN_KEY, unit="")
def active_user_ratio(dau: float | None = None, mau: float | None = None, **kwargs):
    return build_result(
        fid="active_user_ratio",
        name="Active User Ratio (DAU/MAU)",
        expression="DAU / MAU",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "dau": kwargs.get("dau", dau),
            "mau": kwargs.get("mau", mau),
        },
    )

@formula("engagement_rate", "Engagement Rate %", "Engaged_Users / Total_Users * 100", DOMAIN_KEY, unit="")
def engagement_rate(engaged_users: float | None = None, total_users: float | None = None, **kwargs):
    return build_result(
        fid="engagement_rate",
        name="Engagement Rate %",
        expression="Engaged_Users / Total_Users * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "engaged_users": kwargs.get("engaged_users", engaged_users),
            "total_users": kwargs.get("total_users", total_users),
        },
    )

@formula("bounce_rate", "Bounce Rate %", "Single_Page_Sessions / Total_Sessions * 100", DOMAIN_KEY, unit="")
def bounce_rate(single_page_sessions: float | None = None, total_sessions: float | None = None, **kwargs):
    return build_result(
        fid="bounce_rate",
        name="Bounce Rate %",
        expression="Single_Page_Sessions / Total_Sessions * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "single_page_sessions": kwargs.get("single_page_sessions", single_page_sessions),
            "total_sessions": kwargs.get("total_sessions", total_sessions),
        },
    )

@formula("cohort_retention", "Cohort Retention %", "Active_In_Period / Original_Cohort * 100", DOMAIN_KEY, unit="")
def cohort_retention(active_in_period: float | None = None, original_cohort: float | None = None, **kwargs):
    return build_result(
        fid="cohort_retention",
        name="Cohort Retention %",
        expression="Active_In_Period / Original_Cohort * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "active_in_period": kwargs.get("active_in_period", active_in_period),
            "original_cohort": kwargs.get("original_cohort", original_cohort),
        },
    )

@formula("linear_forecast", "Linear Forecast", "intercept + slope * period", DOMAIN_KEY, unit="")
def linear_forecast(intercept: float | None = None, slope: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="linear_forecast",
        name="Linear Forecast",
        expression="intercept + slope * period",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "intercept": kwargs.get("intercept", intercept),
            "slope": kwargs.get("slope", slope),
            "period": kwargs.get("period", period),
        },
    )

@formula("seasonal_index", "Seasonal Index", "Period_Average / Overall_Average", DOMAIN_KEY, unit="")
def seasonal_index(period_average: float | None = None, overall_average: float | None = None, **kwargs):
    return build_result(
        fid="seasonal_index",
        name="Seasonal Index",
        expression="Period_Average / Overall_Average",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "period_average": kwargs.get("period_average", period_average),
            "overall_average": kwargs.get("overall_average", overall_average),
        },
    )

@formula("weighted_moving_forecast", "Weighted Moving Forecast", "Sum(weight*value) / Sum(weights)", DOMAIN_KEY, unit="")
def weighted_moving_forecast(values: float | None = None, weights: float | None = None, **kwargs):
    return build_result(
        fid="weighted_moving_forecast",
        name="Weighted Moving Forecast",
        expression="Sum(weight*value) / Sum(weights)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
            "weights": kwargs.get("weights", weights),
        },
    )

@formula("forecast_bias", "Forecast Bias", "Sum(Actual - Forecast) / n", DOMAIN_KEY, unit="")
def forecast_bias(actuals: float | None = None, forecasts: float | None = None, **kwargs):
    return build_result(
        fid="forecast_bias",
        name="Forecast Bias",
        expression="Sum(Actual - Forecast) / n",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "actuals": kwargs.get("actuals", actuals),
            "forecasts": kwargs.get("forecasts", forecasts),
        },
    )

@formula("tracking_signal", "Tracking Signal", "Cumulative_Error / MAD", DOMAIN_KEY, unit="")
def tracking_signal(cumulative_error: float | None = None, mad: float | None = None, **kwargs):
    return build_result(
        fid="tracking_signal",
        name="Tracking Signal",
        expression="Cumulative_Error / MAD",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cumulative_error": kwargs.get("cumulative_error", cumulative_error),
            "mad": kwargs.get("mad", mad),
        },
    )

@formula("mean_absolute_deviation", "Mean Absolute Deviation", "Mean(|Actual - Forecast|)", DOMAIN_KEY, unit="")
def mean_absolute_deviation(actuals: float | None = None, forecasts: float | None = None, **kwargs):
    return build_result(
        fid="mean_absolute_deviation",
        name="Mean Absolute Deviation",
        expression="Mean(|Actual - Forecast|)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "actuals": kwargs.get("actuals", actuals),
            "forecasts": kwargs.get("forecasts", forecasts),
        },
    )

@formula("exponential_smoothing_forecast", "Exponential Smoothing Forecast", "alpha*actual + (1-alpha)*prev_forecast", DOMAIN_KEY, unit="")
def exponential_smoothing_forecast(actual: float | None = None, prev_forecast: float | None = None, alpha: float | None = None, **kwargs):
    return build_result(
        fid="exponential_smoothing_forecast",
        name="Exponential Smoothing Forecast",
        expression="alpha*actual + (1-alpha)*prev_forecast",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "actual": kwargs.get("actual", actual),
            "prev_forecast": kwargs.get("prev_forecast", prev_forecast),
            "alpha": kwargs.get("alpha", alpha),
        },
    )

@formula("expected_monetary_value", "Expected Monetary Value", "Sum(Probability * Payoff)", DOMAIN_KEY, unit="")
def expected_monetary_value(probabilities: float | None = None, payoffs: float | None = None, **kwargs):
    return build_result(
        fid="expected_monetary_value",
        name="Expected Monetary Value",
        expression="Sum(Probability * Payoff)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "probabilities": kwargs.get("probabilities", probabilities),
            "payoffs": kwargs.get("payoffs", payoffs),
        },
    )

@formula("value_of_information", "Expected Value of Information", "EV_With_Info - EV_Without_Info", DOMAIN_KEY, unit="")
def value_of_information(ev_with_info: float | None = None, ev_without_info: float | None = None, **kwargs):
    return build_result(
        fid="value_of_information",
        name="Expected Value of Information",
        expression="EV_With_Info - EV_Without_Info",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ev_with_info": kwargs.get("ev_with_info", ev_with_info),
            "ev_without_info": kwargs.get("ev_without_info", ev_without_info),
        },
    )

@formula("decision_tree_value", "Decision Tree Node Value", "Max(branch EMVs)", DOMAIN_KEY, unit="")
def decision_tree_value(branch_values: float | None = None, **kwargs):
    return build_result(
        fid="decision_tree_value",
        name="Decision Tree Node Value",
        expression="Max(branch EMVs)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "branch_values": kwargs.get("branch_values", branch_values),
        },
    )

@formula("regret_value", "Maximum Regret", "Max(Best_Payoff - Chosen_Payoff)", DOMAIN_KEY, unit="")
def regret_value(payoff_matrix: float | None = None, chosen: float | None = None, **kwargs):
    return build_result(
        fid="regret_value",
        name="Maximum Regret",
        expression="Max(Best_Payoff - Chosen_Payoff)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "payoff_matrix": kwargs.get("payoff_matrix", payoff_matrix),
            "chosen": kwargs.get("chosen", chosen),
        },
    )

@formula("sensitivity_elasticity", "Sensitivity Elasticity", "Pct_Change_Output / Pct_Change_Input", DOMAIN_KEY, unit="")
def sensitivity_elasticity(pct_change_output: float | None = None, pct_change_input: float | None = None, **kwargs):
    return build_result(
        fid="sensitivity_elasticity",
        name="Sensitivity Elasticity",
        expression="Pct_Change_Output / Pct_Change_Input",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "pct_change_output": kwargs.get("pct_change_output", pct_change_output),
            "pct_change_input": kwargs.get("pct_change_input", pct_change_input),
        },
    )

@formula("breakeven_units_ba", "Breakeven Units", "Fixed_Costs / (Price - Variable_Cost)", DOMAIN_KEY, unit="")
def breakeven_units_ba(fixed_costs: float | None = None, price: float | None = None, variable_cost: float | None = None, **kwargs):
    return build_result(
        fid="breakeven_units_ba",
        name="Breakeven Units",
        expression="Fixed_Costs / (Price - Variable_Cost)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "fixed_costs": kwargs.get("fixed_costs", fixed_costs),
            "price": kwargs.get("price", price),
            "variable_cost": kwargs.get("variable_cost", variable_cost),
        },
    )

@formula("roi_business", "Return on Investment %", "(Gain - Cost) / Cost * 100", DOMAIN_KEY, unit="")
def roi_business(gain: float | None = None, cost: float | None = None, **kwargs):
    return build_result(
        fid="roi_business",
        name="Return on Investment %",
        expression="(Gain - Cost) / Cost * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "gain": kwargs.get("gain", gain),
            "cost": kwargs.get("cost", cost),
        },
    )

@formula("tam_sam_som", "TAM/SAM/SOM", "TAM * SAM_Pct * SOM_Pct", DOMAIN_KEY, unit="")
def tam_sam_som(tam: float | None = None, sam_pct: float | None = None, som_pct: float | None = None, **kwargs):
    return build_result(
        fid="tam_sam_som",
        name="TAM/SAM/SOM",
        expression="TAM * SAM_Pct * SOM_Pct",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "tam": kwargs.get("tam", tam),
            "sam_pct": kwargs.get("sam_pct", sam_pct),
            "som_pct": kwargs.get("som_pct", som_pct),
        },
    )

@formula("price_elasticity_demand", "Price Elasticity of Demand", "Pct_Change_Qty / Pct_Change_Price", DOMAIN_KEY, unit="")
def price_elasticity_demand(pct_change_qty: float | None = None, pct_change_price: float | None = None, **kwargs):
    return build_result(
        fid="price_elasticity_demand",
        name="Price Elasticity of Demand",
        expression="Pct_Change_Qty / Pct_Change_Price",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "pct_change_qty": kwargs.get("pct_change_qty", pct_change_qty),
            "pct_change_price": kwargs.get("pct_change_price", pct_change_price),
        },
    )

@formula("cross_price_elasticity", "Cross-Price Elasticity", "Pct_Change_Qty_A / Pct_Change_Price_B", DOMAIN_KEY, unit="")
def cross_price_elasticity(pct_change_qty_a: float | None = None, pct_change_price_b: float | None = None, **kwargs):
    return build_result(
        fid="cross_price_elasticity",
        name="Cross-Price Elasticity",
        expression="Pct_Change_Qty_A / Pct_Change_Price_B",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "pct_change_qty_a": kwargs.get("pct_change_qty_a", pct_change_qty_a),
            "pct_change_price_b": kwargs.get("pct_change_price_b", pct_change_price_b),
        },
    )

@formula("income_elasticity", "Income Elasticity", "Pct_Change_Qty / Pct_Change_Income", DOMAIN_KEY, unit="")
def income_elasticity(pct_change_qty: float | None = None, pct_change_income: float | None = None, **kwargs):
    return build_result(
        fid="income_elasticity",
        name="Income Elasticity",
        expression="Pct_Change_Qty / Pct_Change_Income",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "pct_change_qty": kwargs.get("pct_change_qty", pct_change_qty),
            "pct_change_income": kwargs.get("pct_change_income", pct_change_income),
        },
    )

@formula("economic_order_quantity", "Economic Order Quantity", "sqrt(2*D*S / H)", DOMAIN_KEY, unit="")
def economic_order_quantity(annual_demand: float | None = None, order_cost: float | None = None, holding_cost: float | None = None, **kwargs):
    return build_result(
        fid="economic_order_quantity",
        name="Economic Order Quantity",
        expression="sqrt(2*D*S / H)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "annual_demand": kwargs.get("annual_demand", annual_demand),
            "order_cost": kwargs.get("order_cost", order_cost),
            "holding_cost": kwargs.get("holding_cost", holding_cost),
        },
    )

@formula("reorder_point", "Reorder Point", "Daily_Demand * Lead_Time + Safety_Stock", DOMAIN_KEY, unit="")
def reorder_point(daily_demand: float | None = None, lead_time: float | None = None, safety_stock: float | None = None, **kwargs):
    return build_result(
        fid="reorder_point",
        name="Reorder Point",
        expression="Daily_Demand * Lead_Time + Safety_Stock",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "daily_demand": kwargs.get("daily_demand", daily_demand),
            "lead_time": kwargs.get("lead_time", lead_time),
            "safety_stock": kwargs.get("safety_stock", safety_stock),
        },
    )

@formula("safety_stock", "Safety Stock", "Z * sigma * sqrt(Lead_Time)", DOMAIN_KEY, unit="")
def safety_stock(z_service: float | None = None, demand_std: float | None = None, lead_time: float | None = None, **kwargs):
    return build_result(
        fid="safety_stock",
        name="Safety Stock",
        expression="Z * sigma * sqrt(Lead_Time)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "z_service": kwargs.get("z_service", z_service),
            "demand_std": kwargs.get("demand_std", demand_std),
            "lead_time": kwargs.get("lead_time", lead_time),
        },
    )

@formula("capacity_utilization", "Capacity Utilization %", "Actual_Output / Potential_Output * 100", DOMAIN_KEY, unit="")
def capacity_utilization(actual_output: float | None = None, potential_output: float | None = None, **kwargs):
    return build_result(
        fid="capacity_utilization",
        name="Capacity Utilization %",
        expression="Actual_Output / Potential_Output * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "actual_output": kwargs.get("actual_output", actual_output),
            "potential_output": kwargs.get("potential_output", potential_output),
        },
    )

@formula("learning_curve", "Learning Curve Unit Cost", "First_Cost * Units^(log(rate)/log(2))", DOMAIN_KEY, unit="")
def learning_curve(first_unit_cost: float | None = None, cumulative_units: float | None = None, learning_rate: float | None = None, **kwargs):
    return build_result(
        fid="learning_curve",
        name="Learning Curve Unit Cost",
        expression="First_Cost * Units^(log(rate)/log(2))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "first_unit_cost": kwargs.get("first_unit_cost", first_unit_cost),
            "cumulative_units": kwargs.get("cumulative_units", cumulative_units),
            "learning_rate": kwargs.get("learning_rate", learning_rate),
        },
    )

@formula("gmv", "Gross Merchandise Value", "Sum(Order_Values)", DOMAIN_KEY, unit="")
def gmv(order_values: float | None = None, **kwargs):
    return build_result(
        fid="gmv",
        name="Gross Merchandise Value",
        expression="Sum(Order_Values)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "order_values": kwargs.get("order_values", order_values),
        },
    )

@formula("take_rate", "Take Rate %", "Revenue / GMV * 100", DOMAIN_KEY, unit="")
def take_rate(revenue: float | None = None, gmv: float | None = None, **kwargs):
    return build_result(
        fid="take_rate",
        name="Take Rate %",
        expression="Revenue / GMV * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "revenue": kwargs.get("revenue", revenue),
            "gmv": kwargs.get("gmv", gmv),
        },
    )

@formula("average_order_value", "Average Order Value", "Total_Revenue / Order_Count", DOMAIN_KEY, unit="")
def average_order_value(total_revenue: float | None = None, order_count: float | None = None, **kwargs):
    return build_result(
        fid="average_order_value",
        name="Average Order Value",
        expression="Total_Revenue / Order_Count",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "total_revenue": kwargs.get("total_revenue", total_revenue),
            "order_count": kwargs.get("order_count", order_count),
        },
    )

@formula("repeat_purchase_rate", "Repeat Purchase Rate %", "Repeat_Customers / Total_Customers * 100", DOMAIN_KEY, unit="")
def repeat_purchase_rate(repeat_customers: float | None = None, total_customers: float | None = None, **kwargs):
    return build_result(
        fid="repeat_purchase_rate",
        name="Repeat Purchase Rate %",
        expression="Repeat_Customers / Total_Customers * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "repeat_customers": kwargs.get("repeat_customers", repeat_customers),
            "total_customers": kwargs.get("total_customers", total_customers),
        },
    )

@formula("attribution_linear", "Linear Attribution Credit", "Conversion_Value / Touchpoints", DOMAIN_KEY, unit="")
def attribution_linear(conversion_value: float | None = None, touchpoints: float | None = None, **kwargs):
    return build_result(
        fid="attribution_linear",
        name="Linear Attribution Credit",
        expression="Conversion_Value / Touchpoints",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "conversion_value": kwargs.get("conversion_value", conversion_value),
            "touchpoints": kwargs.get("touchpoints", touchpoints),
        },
    )

@formula("roi_marketing", "Marketing ROI %", "(Revenue - Cost) / Cost * 100", DOMAIN_KEY, unit="")
def roi_marketing(revenue: float | None = None, cost: float | None = None, **kwargs):
    return build_result(
        fid="roi_marketing",
        name="Marketing ROI %",
        expression="(Revenue - Cost) / Cost * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "revenue": kwargs.get("revenue", revenue),
            "cost": kwargs.get("cost", cost),
        },
    )

@formula("roas", "Return on Ad Spend", "Ad_Revenue / Ad_Spend", DOMAIN_KEY, unit="")
def roas(ad_revenue: float | None = None, ad_spend: float | None = None, **kwargs):
    return build_result(
        fid="roas",
        name="Return on Ad Spend",
        expression="Ad_Revenue / Ad_Spend",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ad_revenue": kwargs.get("ad_revenue", ad_revenue),
            "ad_spend": kwargs.get("ad_spend", ad_spend),
        },
    )

@formula("ltv_cac_payback", "LTV/CAC Payback (months)", "CAC / (ARPU * Gross_Margin)", DOMAIN_KEY, unit="")
def ltv_cac_payback(cac: float | None = None, arpu: float | None = None, gross_margin: float | None = None, **kwargs):
    return build_result(
        fid="ltv_cac_payback",
        name="LTV/CAC Payback (months)",
        expression="CAC / (ARPU * Gross_Margin)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cac": kwargs.get("cac", cac),
            "arpu": kwargs.get("arpu", arpu),
            "gross_margin": kwargs.get("gross_margin", gross_margin),
        },
    )

@formula("cash_runway_months", "Cash Runway (months)", "Cash / Monthly_Burn", DOMAIN_KEY, unit="")
def cash_runway_months(cash: float | None = None, monthly_burn: float | None = None, **kwargs):
    return build_result(
        fid="cash_runway_months",
        name="Cash Runway (months)",
        expression="Cash / Monthly_Burn",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cash": kwargs.get("cash", cash),
            "monthly_burn": kwargs.get("monthly_burn", monthly_burn),
        },
    )

@formula("weighted_pipeline", "Weighted Sales Pipeline", "Sum(Deal_Value * Win_Probability)", DOMAIN_KEY, unit="")
def weighted_pipeline(deal_values: float | None = None, win_probabilities: float | None = None, **kwargs):
    return build_result(
        fid="weighted_pipeline",
        name="Weighted Sales Pipeline",
        expression="Sum(Deal_Value * Win_Probability)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "deal_values": kwargs.get("deal_values", deal_values),
            "win_probabilities": kwargs.get("win_probabilities", win_probabilities),
        },
    )

@formula("win_rate", "Sales Win Rate %", "Won_Deals / Total_Deals * 100", DOMAIN_KEY, unit="")
def win_rate(won_deals: float | None = None, total_deals: float | None = None, **kwargs):
    return build_result(
        fid="win_rate",
        name="Sales Win Rate %",
        expression="Won_Deals / Total_Deals * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "won_deals": kwargs.get("won_deals", won_deals),
            "total_deals": kwargs.get("total_deals", total_deals),
        },
    )

@formula("market_growth_rate", "Market Growth Rate %", "(Market_Now - Market_Prior)/Market_Prior*100", DOMAIN_KEY, unit="")
def market_growth_rate(market_now: float | None = None, market_prior: float | None = None, **kwargs):
    return build_result(
        fid="market_growth_rate",
        name="Market Growth Rate %",
        expression="(Market_Now - Market_Prior)/Market_Prior*100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "market_now": kwargs.get("market_now", market_now),
            "market_prior": kwargs.get("market_prior", market_prior),
        },
    )
