from .base import build_result, formula

DOMAIN_KEY = "D06_fixed_income"
DOMAIN_TITLE = "Fixed Income & Bonds"
FORMULA_IDS = [
    "bond_price",
    "bond_price_clean",
    "bond_price_dirty",
    "accrued_interest",
    "ytm",
    "ytc",
    "ytw",
    "current_yield",
    "coupon_rate",
    "macaulay_duration",
    "modified_duration",
    "effective_duration",
    "dollar_duration",
    "convexity",
    "effective_convexity",
    "dv01",
    "price_change_duration",
    "price_change_convexity",
    "spot_rate",
    "forward_rate",
    "par_yield",
    "zero_coupon_price",
    "discount_factor",
    "bond_equivalent_yield",
    "effective_annual_yield",
    "holding_period_return",
    "realized_compound_yield",
    "z_spread",
    "oas",
    "nominal_spread",
    "g_spread",
    "i_spread",
    "asset_swap_spread",
    "credit_spread",
    "yield_curve_slope",
    "yield_curve_butterfly",
    "key_rate_duration",
    "portfolio_duration",
    "portfolio_convexity",
    "reinvestment_income",
    "interest_on_interest",
    "clean_to_invoice",
    "bond_floor",
    "conversion_value",
    "conversion_premium",
    "tips_principal",
    "real_yield",
    "breakeven_inflation",
    "rolling_yield",
    "expected_loss",
]

@formula("bond_price", "Bond Price", "Sum(C/(1+y)^t) + F/(1+y)^n", DOMAIN_KEY, unit="")
def bond_price(coupon: float | None = None, face: float | None = None, yield_: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="bond_price",
        name="Bond Price",
        expression="Sum(C/(1+y)^t) + F/(1+y)^n",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "coupon": kwargs.get("coupon", coupon),
            "face": kwargs.get("face", face),
            "yield": kwargs.get("yield", yield_),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("bond_price_clean", "Clean Bond Price", "Dirty_Price - Accrued_Interest", DOMAIN_KEY, unit="")
def bond_price_clean(dirty_price: float | None = None, accrued_interest: float | None = None, **kwargs):
    return build_result(
        fid="bond_price_clean",
        name="Clean Bond Price",
        expression="Dirty_Price - Accrued_Interest",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "dirty_price": kwargs.get("dirty_price", dirty_price),
            "accrued_interest": kwargs.get("accrued_interest", accrued_interest),
        },
    )

@formula("bond_price_dirty", "Dirty Bond Price", "Clean_Price + Accrued_Interest", DOMAIN_KEY, unit="")
def bond_price_dirty(clean_price: float | None = None, accrued_interest: float | None = None, **kwargs):
    return build_result(
        fid="bond_price_dirty",
        name="Dirty Bond Price",
        expression="Clean_Price + Accrued_Interest",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "clean_price": kwargs.get("clean_price", clean_price),
            "accrued_interest": kwargs.get("accrued_interest", accrued_interest),
        },
    )

@formula("accrued_interest", "Accrued Interest", "Coupon * Days_Since / Days_Period", DOMAIN_KEY, unit="")
def accrued_interest(coupon: float | None = None, days_since: float | None = None, days_period: float | None = None, **kwargs):
    return build_result(
        fid="accrued_interest",
        name="Accrued Interest",
        expression="Coupon * Days_Since / Days_Period",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "coupon": kwargs.get("coupon", coupon),
            "days_since": kwargs.get("days_since", days_since),
            "days_period": kwargs.get("days_period", days_period),
        },
    )

@formula("ytm", "Yield to Maturity", "Solve y in price equation", DOMAIN_KEY, unit="")
def ytm(price: float | None = None, coupon: float | None = None, face: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="ytm",
        name="Yield to Maturity",
        expression="Solve y in price equation",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "price": kwargs.get("price", price),
            "coupon": kwargs.get("coupon", coupon),
            "face": kwargs.get("face", face),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("ytc", "Yield to Call", "Solve y to call date", DOMAIN_KEY, unit="")
def ytc(price: float | None = None, coupon: float | None = None, call_price: float | None = None, call_periods: float | None = None, **kwargs):
    return build_result(
        fid="ytc",
        name="Yield to Call",
        expression="Solve y to call date",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "price": kwargs.get("price", price),
            "coupon": kwargs.get("coupon", coupon),
            "call_price": kwargs.get("call_price", call_price),
            "call_periods": kwargs.get("call_periods", call_periods),
        },
    )

@formula("ytw", "Yield to Worst", "min(YTM, YTC)", DOMAIN_KEY, unit="")
def ytw(ytm: float | None = None, ytc: float | None = None, **kwargs):
    return build_result(
        fid="ytw",
        name="Yield to Worst",
        expression="min(YTM, YTC)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ytm": kwargs.get("ytm", ytm),
            "ytc": kwargs.get("ytc", ytc),
        },
    )

@formula("current_yield", "Current Yield", "Annual_Coupon / Price", DOMAIN_KEY, unit="")
def current_yield(annual_coupon: float | None = None, price: float | None = None, **kwargs):
    return build_result(
        fid="current_yield",
        name="Current Yield",
        expression="Annual_Coupon / Price",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "annual_coupon": kwargs.get("annual_coupon", annual_coupon),
            "price": kwargs.get("price", price),
        },
    )

@formula("coupon_rate", "Coupon Rate", "Annual_Coupon / Face_Value", DOMAIN_KEY, unit="")
def coupon_rate(annual_coupon: float | None = None, face_value: float | None = None, **kwargs):
    return build_result(
        fid="coupon_rate",
        name="Coupon Rate",
        expression="Annual_Coupon / Face_Value",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "annual_coupon": kwargs.get("annual_coupon", annual_coupon),
            "face_value": kwargs.get("face_value", face_value),
        },
    )

@formula("macaulay_duration", "Macaulay Duration", "Sum(t*PV_CF) / Price", DOMAIN_KEY, unit="")
def macaulay_duration(cash_flows: float | None = None, yield_: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="macaulay_duration",
        name="Macaulay Duration",
        expression="Sum(t*PV_CF) / Price",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cash_flows": kwargs.get("cash_flows", cash_flows),
            "yield": kwargs.get("yield", yield_),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("modified_duration", "Modified Duration", "Macaulay / (1 + y/n)", DOMAIN_KEY, unit="")
def modified_duration(macaulay_duration: float | None = None, yield_: float | None = None, frequency: float | None = None, **kwargs):
    return build_result(
        fid="modified_duration",
        name="Modified Duration",
        expression="Macaulay / (1 + y/n)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "macaulay_duration": kwargs.get("macaulay_duration", macaulay_duration),
            "yield": kwargs.get("yield", yield_),
            "frequency": kwargs.get("frequency", frequency),
        },
    )

@formula("effective_duration", "Effective Duration", "(P- - P+) / (2*P0*dy)", DOMAIN_KEY, unit="")
def effective_duration(price_down: float | None = None, price_up: float | None = None, price_base: float | None = None, yield_change: float | None = None, **kwargs):
    return build_result(
        fid="effective_duration",
        name="Effective Duration",
        expression="(P- - P+) / (2*P0*dy)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "price_down": kwargs.get("price_down", price_down),
            "price_up": kwargs.get("price_up", price_up),
            "price_base": kwargs.get("price_base", price_base),
            "yield_change": kwargs.get("yield_change", yield_change),
        },
    )

@formula("dollar_duration", "Dollar Duration", "Modified_Duration * Price * 0.0001", DOMAIN_KEY, unit="")
def dollar_duration(modified_duration: float | None = None, price: float | None = None, **kwargs):
    return build_result(
        fid="dollar_duration",
        name="Dollar Duration",
        expression="Modified_Duration * Price * 0.0001",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "modified_duration": kwargs.get("modified_duration", modified_duration),
            "price": kwargs.get("price", price),
        },
    )

@formula("convexity", "Convexity", "Sum(t*(t+1)*PV_CF) / (Price*(1+y)^2)", DOMAIN_KEY, unit="")
def convexity(cash_flows: float | None = None, yield_: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="convexity",
        name="Convexity",
        expression="Sum(t*(t+1)*PV_CF) / (Price*(1+y)^2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cash_flows": kwargs.get("cash_flows", cash_flows),
            "yield": kwargs.get("yield", yield_),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("effective_convexity", "Effective Convexity", "(P- + P+ - 2*P0) / (P0*dy^2)", DOMAIN_KEY, unit="")
def effective_convexity(price_down: float | None = None, price_up: float | None = None, price_base: float | None = None, yield_change: float | None = None, **kwargs):
    return build_result(
        fid="effective_convexity",
        name="Effective Convexity",
        expression="(P- + P+ - 2*P0) / (P0*dy^2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "price_down": kwargs.get("price_down", price_down),
            "price_up": kwargs.get("price_up", price_up),
            "price_base": kwargs.get("price_base", price_base),
            "yield_change": kwargs.get("yield_change", yield_change),
        },
    )

@formula("dv01", "DV01 (PV01)", "Modified_Duration * Price * 0.0001", DOMAIN_KEY, unit="")
def dv01(modified_duration: float | None = None, price: float | None = None, **kwargs):
    return build_result(
        fid="dv01",
        name="DV01 (PV01)",
        expression="Modified_Duration * Price * 0.0001",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "modified_duration": kwargs.get("modified_duration", modified_duration),
            "price": kwargs.get("price", price),
        },
    )

@formula("price_change_duration", "Price Change (Duration)", "-Modified_Duration * Price * dy", DOMAIN_KEY, unit="")
def price_change_duration(modified_duration: float | None = None, price: float | None = None, yield_change: float | None = None, **kwargs):
    return build_result(
        fid="price_change_duration",
        name="Price Change (Duration)",
        expression="-Modified_Duration * Price * dy",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "modified_duration": kwargs.get("modified_duration", modified_duration),
            "price": kwargs.get("price", price),
            "yield_change": kwargs.get("yield_change", yield_change),
        },
    )

@formula("price_change_convexity", "Price Change (Dur+Conv)", "-MD*P*dy + 0.5*Conv*P*dy^2", DOMAIN_KEY, unit="")
def price_change_convexity(modified_duration: float | None = None, convexity: float | None = None, price: float | None = None, yield_change: float | None = None, **kwargs):
    return build_result(
        fid="price_change_convexity",
        name="Price Change (Dur+Conv)",
        expression="-MD*P*dy + 0.5*Conv*P*dy^2",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "modified_duration": kwargs.get("modified_duration", modified_duration),
            "convexity": kwargs.get("convexity", convexity),
            "price": kwargs.get("price", price),
            "yield_change": kwargs.get("yield_change", yield_change),
        },
    )

@formula("spot_rate", "Spot Rate", "(Face/Price)^(1/n) - 1", DOMAIN_KEY, unit="")
def spot_rate(price: float | None = None, face: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="spot_rate",
        name="Spot Rate",
        expression="(Face/Price)^(1/n) - 1",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "price": kwargs.get("price", price),
            "face": kwargs.get("face", face),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("forward_rate", "Forward Rate", "((1+s2)^t2/(1+s1)^t1)^(1/(t2-t1)) - 1", DOMAIN_KEY, unit="")
def forward_rate(spot1: float | None = None, spot2: float | None = None, time1: float | None = None, time2: float | None = None, **kwargs):
    return build_result(
        fid="forward_rate",
        name="Forward Rate",
        expression="((1+s2)^t2/(1+s1)^t1)^(1/(t2-t1)) - 1",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot1": kwargs.get("spot1", spot1),
            "spot2": kwargs.get("spot2", spot2),
            "time1": kwargs.get("time1", time1),
            "time2": kwargs.get("time2", time2),
        },
    )

@formula("par_yield", "Par Yield", "(1 - DF_n) / Sum(DF_i)", DOMAIN_KEY, unit="")
def par_yield(discount_factors: float | None = None, **kwargs):
    return build_result(
        fid="par_yield",
        name="Par Yield",
        expression="(1 - DF_n) / Sum(DF_i)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "discount_factors": kwargs.get("discount_factors", discount_factors),
        },
    )

@formula("zero_coupon_price", "Zero-Coupon Bond Price", "Face / (1+y)^n", DOMAIN_KEY, unit="")
def zero_coupon_price(face: float | None = None, yield_: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="zero_coupon_price",
        name="Zero-Coupon Bond Price",
        expression="Face / (1+y)^n",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "face": kwargs.get("face", face),
            "yield": kwargs.get("yield", yield_),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("discount_factor", "Discount Factor", "1 / (1+r)^t", DOMAIN_KEY, unit="")
def discount_factor(rate: float | None = None, time: float | None = None, **kwargs):
    return build_result(
        fid="discount_factor",
        name="Discount Factor",
        expression="1 / (1+r)^t",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "rate": kwargs.get("rate", rate),
            "time": kwargs.get("time", time),
        },
    )

@formula("bond_equivalent_yield", "Bond Equivalent Yield", "2 * ((1+y_semi) - 1)", DOMAIN_KEY, unit="")
def bond_equivalent_yield(semi_annual_yield: float | None = None, **kwargs):
    return build_result(
        fid="bond_equivalent_yield",
        name="Bond Equivalent Yield",
        expression="2 * ((1+y_semi) - 1)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "semi_annual_yield": kwargs.get("semi_annual_yield", semi_annual_yield),
        },
    )

@formula("effective_annual_yield", "Effective Annual Yield", "(1 + y/n)^n - 1", DOMAIN_KEY, unit="")
def effective_annual_yield(yield_: float | None = None, frequency: float | None = None, **kwargs):
    return build_result(
        fid="effective_annual_yield",
        name="Effective Annual Yield",
        expression="(1 + y/n)^n - 1",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "yield": kwargs.get("yield", yield_),
            "frequency": kwargs.get("frequency", frequency),
        },
    )

@formula("holding_period_return", "Holding Period Return %", "(End + Coupons - Start) / Start * 100", DOMAIN_KEY, unit="")
def holding_period_return(start_price: float | None = None, end_price: float | None = None, coupons: float | None = None, **kwargs):
    return build_result(
        fid="holding_period_return",
        name="Holding Period Return %",
        expression="(End + Coupons - Start) / Start * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "start_price": kwargs.get("start_price", start_price),
            "end_price": kwargs.get("end_price", end_price),
            "coupons": kwargs.get("coupons", coupons),
        },
    )

@formula("realized_compound_yield", "Realized Compound Yield", "(Total_FV / Price)^(1/n) - 1", DOMAIN_KEY, unit="")
def realized_compound_yield(price: float | None = None, total_fv: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="realized_compound_yield",
        name="Realized Compound Yield",
        expression="(Total_FV / Price)^(1/n) - 1",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "price": kwargs.get("price", price),
            "total_fv": kwargs.get("total_fv", total_fv),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("z_spread", "Z-Spread", "Spread making PV = price", DOMAIN_KEY, unit="")
def z_spread(price: float | None = None, cash_flows: float | None = None, spot_rates: float | None = None, **kwargs):
    return build_result(
        fid="z_spread",
        name="Z-Spread",
        expression="Spread making PV = price",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "price": kwargs.get("price", price),
            "cash_flows": kwargs.get("cash_flows", cash_flows),
            "spot_rates": kwargs.get("spot_rates", spot_rates),
        },
    )

@formula("oas", "Option-Adjusted Spread", "Z_Spread - Option_Cost", DOMAIN_KEY, unit="")
def oas(z_spread: float | None = None, option_cost: float | None = None, **kwargs):
    return build_result(
        fid="oas",
        name="Option-Adjusted Spread",
        expression="Z_Spread - Option_Cost",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "z_spread": kwargs.get("z_spread", z_spread),
            "option_cost": kwargs.get("option_cost", option_cost),
        },
    )

@formula("nominal_spread", "Nominal Spread", "Bond_YTM - Benchmark_YTM", DOMAIN_KEY, unit="")
def nominal_spread(bond_ytm: float | None = None, benchmark_ytm: float | None = None, **kwargs):
    return build_result(
        fid="nominal_spread",
        name="Nominal Spread",
        expression="Bond_YTM - Benchmark_YTM",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "bond_ytm": kwargs.get("bond_ytm", bond_ytm),
            "benchmark_ytm": kwargs.get("benchmark_ytm", benchmark_ytm),
        },
    )

@formula("g_spread", "G-Spread", "Bond_Yield - Interpolated_Govt", DOMAIN_KEY, unit="")
def g_spread(bond_yield: float | None = None, govt_yield: float | None = None, **kwargs):
    return build_result(
        fid="g_spread",
        name="G-Spread",
        expression="Bond_Yield - Interpolated_Govt",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "bond_yield": kwargs.get("bond_yield", bond_yield),
            "govt_yield": kwargs.get("govt_yield", govt_yield),
        },
    )

@formula("i_spread", "I-Spread", "Bond_Yield - Swap_Rate", DOMAIN_KEY, unit="")
def i_spread(bond_yield: float | None = None, swap_rate: float | None = None, **kwargs):
    return build_result(
        fid="i_spread",
        name="I-Spread",
        expression="Bond_Yield - Swap_Rate",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "bond_yield": kwargs.get("bond_yield", bond_yield),
            "swap_rate": kwargs.get("swap_rate", swap_rate),
        },
    )

@formula("asset_swap_spread", "Asset Swap Spread", "Asset swap calculation", DOMAIN_KEY, unit="")
def asset_swap_spread(bond_price: float | None = None, coupon: float | None = None, swap_rate: float | None = None, **kwargs):
    return build_result(
        fid="asset_swap_spread",
        name="Asset Swap Spread",
        expression="Asset swap calculation",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "bond_price": kwargs.get("bond_price", bond_price),
            "coupon": kwargs.get("coupon", coupon),
            "swap_rate": kwargs.get("swap_rate", swap_rate),
        },
    )

@formula("credit_spread", "Credit Spread", "Corporate_Yield - Treasury_Yield", DOMAIN_KEY, unit="")
def credit_spread(corporate_yield: float | None = None, treasury_yield: float | None = None, **kwargs):
    return build_result(
        fid="credit_spread",
        name="Credit Spread",
        expression="Corporate_Yield - Treasury_Yield",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "corporate_yield": kwargs.get("corporate_yield", corporate_yield),
            "treasury_yield": kwargs.get("treasury_yield", treasury_yield),
        },
    )

@formula("yield_curve_slope", "Yield Curve Slope", "Long_Yield - Short_Yield", DOMAIN_KEY, unit="")
def yield_curve_slope(long_yield: float | None = None, short_yield: float | None = None, **kwargs):
    return build_result(
        fid="yield_curve_slope",
        name="Yield Curve Slope",
        expression="Long_Yield - Short_Yield",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "long_yield": kwargs.get("long_yield", long_yield),
            "short_yield": kwargs.get("short_yield", short_yield),
        },
    )

@formula("yield_curve_butterfly", "Yield Curve Butterfly", "2*Mid - Short - Long", DOMAIN_KEY, unit="")
def yield_curve_butterfly(short_yield: float | None = None, mid_yield: float | None = None, long_yield: float | None = None, **kwargs):
    return build_result(
        fid="yield_curve_butterfly",
        name="Yield Curve Butterfly",
        expression="2*Mid - Short - Long",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "short_yield": kwargs.get("short_yield", short_yield),
            "mid_yield": kwargs.get("mid_yield", mid_yield),
            "long_yield": kwargs.get("long_yield", long_yield),
        },
    )

@formula("key_rate_duration", "Key Rate Duration", "Price sensitivity to key rate", DOMAIN_KEY, unit="")
def key_rate_duration(price_changes: float | None = None, yield_change: float | None = None, **kwargs):
    return build_result(
        fid="key_rate_duration",
        name="Key Rate Duration",
        expression="Price sensitivity to key rate",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "price_changes": kwargs.get("price_changes", price_changes),
            "yield_change": kwargs.get("yield_change", yield_change),
        },
    )

@formula("portfolio_duration", "Portfolio Duration", "Sum(Weight_i * Duration_i)", DOMAIN_KEY, unit="")
def portfolio_duration(weights: float | None = None, durations: float | None = None, **kwargs):
    return build_result(
        fid="portfolio_duration",
        name="Portfolio Duration",
        expression="Sum(Weight_i * Duration_i)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "weights": kwargs.get("weights", weights),
            "durations": kwargs.get("durations", durations),
        },
    )

@formula("portfolio_convexity", "Portfolio Convexity", "Sum(Weight_i * Convexity_i)", DOMAIN_KEY, unit="")
def portfolio_convexity(weights: float | None = None, convexities: float | None = None, **kwargs):
    return build_result(
        fid="portfolio_convexity",
        name="Portfolio Convexity",
        expression="Sum(Weight_i * Convexity_i)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "weights": kwargs.get("weights", weights),
            "convexities": kwargs.get("convexities", convexities),
        },
    )

@formula("reinvestment_income", "Reinvestment Income", "Sum(C*(1+r)^(n-t))", DOMAIN_KEY, unit="")
def reinvestment_income(coupon: float | None = None, rate: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="reinvestment_income",
        name="Reinvestment Income",
        expression="Sum(C*(1+r)^(n-t))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "coupon": kwargs.get("coupon", coupon),
            "rate": kwargs.get("rate", rate),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("interest_on_interest", "Interest on Interest", "Reinvestment_Income - Total_Coupons", DOMAIN_KEY, unit="")
def interest_on_interest(reinvestment_income: float | None = None, total_coupons: float | None = None, **kwargs):
    return build_result(
        fid="interest_on_interest",
        name="Interest on Interest",
        expression="Reinvestment_Income - Total_Coupons",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "reinvestment_income": kwargs.get("reinvestment_income", reinvestment_income),
            "total_coupons": kwargs.get("total_coupons", total_coupons),
        },
    )

@formula("clean_to_invoice", "Invoice Price", "Clean_Price*Factor + Accrued", DOMAIN_KEY, unit="")
def clean_to_invoice(clean_price: float | None = None, conversion_factor: float | None = None, accrued: float | None = None, **kwargs):
    return build_result(
        fid="clean_to_invoice",
        name="Invoice Price",
        expression="Clean_Price*Factor + Accrued",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "clean_price": kwargs.get("clean_price", clean_price),
            "conversion_factor": kwargs.get("conversion_factor", conversion_factor),
            "accrued": kwargs.get("accrued", accrued),
        },
    )

@formula("bond_floor", "Convertible Bond Floor", "PV of bond cash flows", DOMAIN_KEY, unit="")
def bond_floor(coupon: float | None = None, face: float | None = None, yield_: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="bond_floor",
        name="Convertible Bond Floor",
        expression="PV of bond cash flows",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "coupon": kwargs.get("coupon", coupon),
            "face": kwargs.get("face", face),
            "yield": kwargs.get("yield", yield_),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("conversion_value", "Conversion Value", "Conversion_Ratio * Stock_Price", DOMAIN_KEY, unit="")
def conversion_value(conversion_ratio: float | None = None, stock_price: float | None = None, **kwargs):
    return build_result(
        fid="conversion_value",
        name="Conversion Value",
        expression="Conversion_Ratio * Stock_Price",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "conversion_ratio": kwargs.get("conversion_ratio", conversion_ratio),
            "stock_price": kwargs.get("stock_price", stock_price),
        },
    )

@formula("conversion_premium", "Conversion Premium %", "(Bond_Price - Conv_Value) / Conv_Value * 100", DOMAIN_KEY, unit="")
def conversion_premium(bond_price: float | None = None, conversion_value: float | None = None, **kwargs):
    return build_result(
        fid="conversion_premium",
        name="Conversion Premium %",
        expression="(Bond_Price - Conv_Value) / Conv_Value * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "bond_price": kwargs.get("bond_price", bond_price),
            "conversion_value": kwargs.get("conversion_value", conversion_value),
        },
    )

@formula("tips_principal", "TIPS Adjusted Principal", "Face * Index_Ratio", DOMAIN_KEY, unit="")
def tips_principal(face: float | None = None, index_ratio: float | None = None, **kwargs):
    return build_result(
        fid="tips_principal",
        name="TIPS Adjusted Principal",
        expression="Face * Index_Ratio",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "face": kwargs.get("face", face),
            "index_ratio": kwargs.get("index_ratio", index_ratio),
        },
    )

@formula("real_yield", "Real Yield", "Nominal_Yield - Inflation_Rate", DOMAIN_KEY, unit="")
def real_yield(nominal_yield: float | None = None, inflation_rate: float | None = None, **kwargs):
    return build_result(
        fid="real_yield",
        name="Real Yield",
        expression="Nominal_Yield - Inflation_Rate",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "nominal_yield": kwargs.get("nominal_yield", nominal_yield),
            "inflation_rate": kwargs.get("inflation_rate", inflation_rate),
        },
    )

@formula("breakeven_inflation", "Breakeven Inflation Rate", "Nominal_Yield - Real_Yield", DOMAIN_KEY, unit="")
def breakeven_inflation(nominal_yield: float | None = None, real_yield: float | None = None, **kwargs):
    return build_result(
        fid="breakeven_inflation",
        name="Breakeven Inflation Rate",
        expression="Nominal_Yield - Real_Yield",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "nominal_yield": kwargs.get("nominal_yield", nominal_yield),
            "real_yield": kwargs.get("real_yield", real_yield),
        },
    )

@formula("rolling_yield", "Rolling Yield (Carry+Roll)", "Carry + Rolldown", DOMAIN_KEY, unit="")
def rolling_yield(carry: float | None = None, rolldown: float | None = None, **kwargs):
    return build_result(
        fid="rolling_yield",
        name="Rolling Yield (Carry+Roll)",
        expression="Carry + Rolldown",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "carry": kwargs.get("carry", carry),
            "rolldown": kwargs.get("rolldown", rolldown),
        },
    )

@formula("expected_loss", "Expected Loss (Credit)", "PD * LGD * EAD", DOMAIN_KEY, unit="")
def expected_loss(pd: float | None = None, lgd: float | None = None, ead: float | None = None, **kwargs):
    return build_result(
        fid="expected_loss",
        name="Expected Loss (Credit)",
        expression="PD * LGD * EAD",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "pd": kwargs.get("pd", pd),
            "lgd": kwargs.get("lgd", lgd),
            "ead": kwargs.get("ead", ead),
        },
    )
