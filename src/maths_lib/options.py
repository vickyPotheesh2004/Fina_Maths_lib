from .base import build_result, formula

DOMAIN_KEY = "D05_options"
DOMAIN_TITLE = "Options Pricing & Derivatives"
FORMULA_IDS = [
    "black_scholes_call",
    "black_scholes_put",
    "bs_d1",
    "bs_d2",
    "bsm_call_dividend",
    "bsm_put_dividend",
    "delta_call",
    "delta_put",
    "gamma",
    "vega",
    "theta_call",
    "theta_put",
    "rho_call",
    "rho_put",
    "vanna",
    "charm",
    "vomma",
    "speed",
    "binomial_call",
    "binomial_put",
    "trinomial_option",
    "monte_carlo_option",
    "implied_volatility",
    "put_call_parity",
    "intrinsic_value_call",
    "intrinsic_value_put",
    "time_value_option",
    "forward_price",
    "futures_price",
    "forward_rate_agreement",
    "swap_fixed_rate",
    "swap_value",
    "call_payoff",
    "put_payoff",
    "straddle_payoff",
    "strangle_payoff",
    "covered_call_return",
    "collar_value",
    "butterfly_payoff",
    "delta_hedge_shares",
    "option_leverage",
    "breakeven_call",
    "breakeven_put",
    "max_pain",
    "historical_var_option",
]

@formula("black_scholes_call", "Black-Scholes Call", "S*N(d1) - K*e^(-rT)*N(d2)", DOMAIN_KEY, unit="")
def black_scholes_call(spot: float | None = None, strike: float | None = None, time: float | None = None, rate: float | None = None, volatility: float | None = None, **kwargs):
    return build_result(
        fid="black_scholes_call",
        name="Black-Scholes Call",
        expression="S*N(d1) - K*e^(-rT)*N(d2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "time": kwargs.get("time", time),
            "rate": kwargs.get("rate", rate),
            "volatility": kwargs.get("volatility", volatility),
        },
    )

@formula("black_scholes_put", "Black-Scholes Put", "K*e^(-rT)*N(-d2) - S*N(-d1)", DOMAIN_KEY, unit="")
def black_scholes_put(spot: float | None = None, strike: float | None = None, time: float | None = None, rate: float | None = None, volatility: float | None = None, **kwargs):
    return build_result(
        fid="black_scholes_put",
        name="Black-Scholes Put",
        expression="K*e^(-rT)*N(-d2) - S*N(-d1)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "time": kwargs.get("time", time),
            "rate": kwargs.get("rate", rate),
            "volatility": kwargs.get("volatility", volatility),
        },
    )

@formula("bs_d1", "Black-Scholes d1", "(ln(S/K)+(r+sig^2/2)T)/(sig*sqrt(T))", DOMAIN_KEY, unit="")
def bs_d1(spot: float | None = None, strike: float | None = None, time: float | None = None, rate: float | None = None, volatility: float | None = None, **kwargs):
    return build_result(
        fid="bs_d1",
        name="Black-Scholes d1",
        expression="(ln(S/K)+(r+sig^2/2)T)/(sig*sqrt(T))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "time": kwargs.get("time", time),
            "rate": kwargs.get("rate", rate),
            "volatility": kwargs.get("volatility", volatility),
        },
    )

@formula("bs_d2", "Black-Scholes d2", "d1 - sig*sqrt(T)", DOMAIN_KEY, unit="")
def bs_d2(d1: float | None = None, volatility: float | None = None, time: float | None = None, **kwargs):
    return build_result(
        fid="bs_d2",
        name="Black-Scholes d2",
        expression="d1 - sig*sqrt(T)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "d1": kwargs.get("d1", d1),
            "volatility": kwargs.get("volatility", volatility),
            "time": kwargs.get("time", time),
        },
    )

@formula("bsm_call_dividend", "BSM Call with Dividend", "S*e^(-qT)*N(d1) - K*e^(-rT)*N(d2)", DOMAIN_KEY, unit="")
def bsm_call_dividend(spot: float | None = None, strike: float | None = None, time: float | None = None, rate: float | None = None, volatility: float | None = None, dividend: float | None = None, **kwargs):
    return build_result(
        fid="bsm_call_dividend",
        name="BSM Call with Dividend",
        expression="S*e^(-qT)*N(d1) - K*e^(-rT)*N(d2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "time": kwargs.get("time", time),
            "rate": kwargs.get("rate", rate),
            "volatility": kwargs.get("volatility", volatility),
            "dividend": kwargs.get("dividend", dividend),
        },
    )

@formula("bsm_put_dividend", "BSM Put with Dividend", "K*e^(-rT)*N(-d2) - S*e^(-qT)*N(-d1)", DOMAIN_KEY, unit="")
def bsm_put_dividend(spot: float | None = None, strike: float | None = None, time: float | None = None, rate: float | None = None, volatility: float | None = None, dividend: float | None = None, **kwargs):
    return build_result(
        fid="bsm_put_dividend",
        name="BSM Put with Dividend",
        expression="K*e^(-rT)*N(-d2) - S*e^(-qT)*N(-d1)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "time": kwargs.get("time", time),
            "rate": kwargs.get("rate", rate),
            "volatility": kwargs.get("volatility", volatility),
            "dividend": kwargs.get("dividend", dividend),
        },
    )

@formula("delta_call", "Delta (Call)", "N(d1)", DOMAIN_KEY, unit="")
def delta_call(spot: float | None = None, strike: float | None = None, time: float | None = None, rate: float | None = None, volatility: float | None = None, **kwargs):
    return build_result(
        fid="delta_call",
        name="Delta (Call)",
        expression="N(d1)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "time": kwargs.get("time", time),
            "rate": kwargs.get("rate", rate),
            "volatility": kwargs.get("volatility", volatility),
        },
    )

@formula("delta_put", "Delta (Put)", "N(d1) - 1", DOMAIN_KEY, unit="")
def delta_put(spot: float | None = None, strike: float | None = None, time: float | None = None, rate: float | None = None, volatility: float | None = None, **kwargs):
    return build_result(
        fid="delta_put",
        name="Delta (Put)",
        expression="N(d1) - 1",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "time": kwargs.get("time", time),
            "rate": kwargs.get("rate", rate),
            "volatility": kwargs.get("volatility", volatility),
        },
    )

@formula("gamma", "Gamma", "N'(d1) / (S*sig*sqrt(T))", DOMAIN_KEY, unit="")
def gamma(spot: float | None = None, strike: float | None = None, time: float | None = None, rate: float | None = None, volatility: float | None = None, **kwargs):
    return build_result(
        fid="gamma",
        name="Gamma",
        expression="N'(d1) / (S*sig*sqrt(T))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "time": kwargs.get("time", time),
            "rate": kwargs.get("rate", rate),
            "volatility": kwargs.get("volatility", volatility),
        },
    )

@formula("vega", "Vega", "S*N'(d1)*sqrt(T)", DOMAIN_KEY, unit="")
def vega(spot: float | None = None, strike: float | None = None, time: float | None = None, rate: float | None = None, volatility: float | None = None, **kwargs):
    return build_result(
        fid="vega",
        name="Vega",
        expression="S*N'(d1)*sqrt(T)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "time": kwargs.get("time", time),
            "rate": kwargs.get("rate", rate),
            "volatility": kwargs.get("volatility", volatility),
        },
    )

@formula("theta_call", "Theta (Call)", "Time decay formula", DOMAIN_KEY, unit="")
def theta_call(spot: float | None = None, strike: float | None = None, time: float | None = None, rate: float | None = None, volatility: float | None = None, **kwargs):
    return build_result(
        fid="theta_call",
        name="Theta (Call)",
        expression="Time decay formula",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "time": kwargs.get("time", time),
            "rate": kwargs.get("rate", rate),
            "volatility": kwargs.get("volatility", volatility),
        },
    )

@formula("theta_put", "Theta (Put)", "Time decay formula", DOMAIN_KEY, unit="")
def theta_put(spot: float | None = None, strike: float | None = None, time: float | None = None, rate: float | None = None, volatility: float | None = None, **kwargs):
    return build_result(
        fid="theta_put",
        name="Theta (Put)",
        expression="Time decay formula",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "time": kwargs.get("time", time),
            "rate": kwargs.get("rate", rate),
            "volatility": kwargs.get("volatility", volatility),
        },
    )

@formula("rho_call", "Rho (Call)", "K*T*e^(-rT)*N(d2)", DOMAIN_KEY, unit="")
def rho_call(spot: float | None = None, strike: float | None = None, time: float | None = None, rate: float | None = None, volatility: float | None = None, **kwargs):
    return build_result(
        fid="rho_call",
        name="Rho (Call)",
        expression="K*T*e^(-rT)*N(d2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "time": kwargs.get("time", time),
            "rate": kwargs.get("rate", rate),
            "volatility": kwargs.get("volatility", volatility),
        },
    )

@formula("rho_put", "Rho (Put)", "-K*T*e^(-rT)*N(-d2)", DOMAIN_KEY, unit="")
def rho_put(spot: float | None = None, strike: float | None = None, time: float | None = None, rate: float | None = None, volatility: float | None = None, **kwargs):
    return build_result(
        fid="rho_put",
        name="Rho (Put)",
        expression="-K*T*e^(-rT)*N(-d2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "time": kwargs.get("time", time),
            "rate": kwargs.get("rate", rate),
            "volatility": kwargs.get("volatility", volatility),
        },
    )

@formula("vanna", "Vanna", "d(Delta)/d(vol)", DOMAIN_KEY, unit="")
def vanna(spot: float | None = None, strike: float | None = None, time: float | None = None, rate: float | None = None, volatility: float | None = None, **kwargs):
    return build_result(
        fid="vanna",
        name="Vanna",
        expression="d(Delta)/d(vol)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "time": kwargs.get("time", time),
            "rate": kwargs.get("rate", rate),
            "volatility": kwargs.get("volatility", volatility),
        },
    )

@formula("charm", "Charm", "d(Delta)/d(time)", DOMAIN_KEY, unit="")
def charm(spot: float | None = None, strike: float | None = None, time: float | None = None, rate: float | None = None, volatility: float | None = None, **kwargs):
    return build_result(
        fid="charm",
        name="Charm",
        expression="d(Delta)/d(time)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "time": kwargs.get("time", time),
            "rate": kwargs.get("rate", rate),
            "volatility": kwargs.get("volatility", volatility),
        },
    )

@formula("vomma", "Vomma", "d(Vega)/d(vol)", DOMAIN_KEY, unit="")
def vomma(spot: float | None = None, strike: float | None = None, time: float | None = None, rate: float | None = None, volatility: float | None = None, **kwargs):
    return build_result(
        fid="vomma",
        name="Vomma",
        expression="d(Vega)/d(vol)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "time": kwargs.get("time", time),
            "rate": kwargs.get("rate", rate),
            "volatility": kwargs.get("volatility", volatility),
        },
    )

@formula("speed", "Speed", "d(Gamma)/d(S)", DOMAIN_KEY, unit="")
def speed(spot: float | None = None, strike: float | None = None, time: float | None = None, rate: float | None = None, volatility: float | None = None, **kwargs):
    return build_result(
        fid="speed",
        name="Speed",
        expression="d(Gamma)/d(S)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "time": kwargs.get("time", time),
            "rate": kwargs.get("rate", rate),
            "volatility": kwargs.get("volatility", volatility),
        },
    )

@formula("binomial_call", "Binomial Call (CRR)", "Cox-Ross-Rubinstein backward induction", DOMAIN_KEY, unit="")
def binomial_call(spot: float | None = None, strike: float | None = None, time: float | None = None, rate: float | None = None, volatility: float | None = None, steps: float | None = None, **kwargs):
    return build_result(
        fid="binomial_call",
        name="Binomial Call (CRR)",
        expression="Cox-Ross-Rubinstein backward induction",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "time": kwargs.get("time", time),
            "rate": kwargs.get("rate", rate),
            "volatility": kwargs.get("volatility", volatility),
            "steps": kwargs.get("steps", steps),
        },
    )

@formula("binomial_put", "Binomial Put (CRR)", "CRR backward induction", DOMAIN_KEY, unit="")
def binomial_put(spot: float | None = None, strike: float | None = None, time: float | None = None, rate: float | None = None, volatility: float | None = None, steps: float | None = None, **kwargs):
    return build_result(
        fid="binomial_put",
        name="Binomial Put (CRR)",
        expression="CRR backward induction",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "time": kwargs.get("time", time),
            "rate": kwargs.get("rate", rate),
            "volatility": kwargs.get("volatility", volatility),
            "steps": kwargs.get("steps", steps),
        },
    )

@formula("trinomial_option", "Trinomial Option", "Trinomial backward induction", DOMAIN_KEY, unit="")
def trinomial_option(spot: float | None = None, strike: float | None = None, time: float | None = None, rate: float | None = None, volatility: float | None = None, steps: float | None = None, **kwargs):
    return build_result(
        fid="trinomial_option",
        name="Trinomial Option",
        expression="Trinomial backward induction",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "time": kwargs.get("time", time),
            "rate": kwargs.get("rate", rate),
            "volatility": kwargs.get("volatility", volatility),
            "steps": kwargs.get("steps", steps),
        },
    )

@formula("monte_carlo_option", "Monte Carlo Option", "Mean(discounted payoffs)", DOMAIN_KEY, unit="")
def monte_carlo_option(spot: float | None = None, strike: float | None = None, time: float | None = None, rate: float | None = None, volatility: float | None = None, simulations: float | None = None, **kwargs):
    return build_result(
        fid="monte_carlo_option",
        name="Monte Carlo Option",
        expression="Mean(discounted payoffs)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "time": kwargs.get("time", time),
            "rate": kwargs.get("rate", rate),
            "volatility": kwargs.get("volatility", volatility),
            "simulations": kwargs.get("simulations", simulations),
        },
    )

@formula("implied_volatility", "Implied Volatility", "Newton-Raphson solve for sigma", DOMAIN_KEY, unit="")
def implied_volatility(option_price: float | None = None, spot: float | None = None, strike: float | None = None, time: float | None = None, rate: float | None = None, **kwargs):
    return build_result(
        fid="implied_volatility",
        name="Implied Volatility",
        expression="Newton-Raphson solve for sigma",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "option_price": kwargs.get("option_price", option_price),
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "time": kwargs.get("time", time),
            "rate": kwargs.get("rate", rate),
        },
    )

@formula("put_call_parity", "Put-Call Parity", "Call - Put = Spot - PV(Strike)", DOMAIN_KEY, unit="")
def put_call_parity(call: float | None = None, put: float | None = None, spot: float | None = None, strike: float | None = None, rate: float | None = None, time: float | None = None, **kwargs):
    return build_result(
        fid="put_call_parity",
        name="Put-Call Parity",
        expression="Call - Put = Spot - PV(Strike)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "call": kwargs.get("call", call),
            "put": kwargs.get("put", put),
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "rate": kwargs.get("rate", rate),
            "time": kwargs.get("time", time),
        },
    )

@formula("intrinsic_value_call", "Call Intrinsic Value", "max(Spot - Strike, 0)", DOMAIN_KEY, unit="")
def intrinsic_value_call(spot: float | None = None, strike: float | None = None, **kwargs):
    return build_result(
        fid="intrinsic_value_call",
        name="Call Intrinsic Value",
        expression="max(Spot - Strike, 0)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
        },
    )

@formula("intrinsic_value_put", "Put Intrinsic Value", "max(Strike - Spot, 0)", DOMAIN_KEY, unit="")
def intrinsic_value_put(spot: float | None = None, strike: float | None = None, **kwargs):
    return build_result(
        fid="intrinsic_value_put",
        name="Put Intrinsic Value",
        expression="max(Strike - Spot, 0)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
        },
    )

@formula("time_value_option", "Option Time Value", "Option_Price - Intrinsic_Value", DOMAIN_KEY, unit="")
def time_value_option(option_price: float | None = None, intrinsic_value: float | None = None, **kwargs):
    return build_result(
        fid="time_value_option",
        name="Option Time Value",
        expression="Option_Price - Intrinsic_Value",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "option_price": kwargs.get("option_price", option_price),
            "intrinsic_value": kwargs.get("intrinsic_value", intrinsic_value),
        },
    )

@formula("forward_price", "Forward Price", "S*e^(rT)", DOMAIN_KEY, unit="")
def forward_price(spot: float | None = None, rate: float | None = None, time: float | None = None, **kwargs):
    return build_result(
        fid="forward_price",
        name="Forward Price",
        expression="S*e^(rT)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "rate": kwargs.get("rate", rate),
            "time": kwargs.get("time", time),
        },
    )

@formula("futures_price", "Futures Price", "S*e^((r+storage-yield)T)", DOMAIN_KEY, unit="")
def futures_price(spot: float | None = None, rate: float | None = None, storage: float | None = None, yield_: float | None = None, time: float | None = None, **kwargs):
    return build_result(
        fid="futures_price",
        name="Futures Price",
        expression="S*e^((r+storage-yield)T)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "rate": kwargs.get("rate", rate),
            "storage": kwargs.get("storage", storage),
            "yield": kwargs.get("yield", yield_),
            "time": kwargs.get("time", time),
        },
    )

@formula("forward_rate_agreement", "FRA Value", "Notional*(Ref - FRA)*Days/360", DOMAIN_KEY, unit="")
def forward_rate_agreement(notional: float | None = None, ref_rate: float | None = None, fra_rate: float | None = None, days: float | None = None, **kwargs):
    return build_result(
        fid="forward_rate_agreement",
        name="FRA Value",
        expression="Notional*(Ref - FRA)*Days/360",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "notional": kwargs.get("notional", notional),
            "ref_rate": kwargs.get("ref_rate", ref_rate),
            "fra_rate": kwargs.get("fra_rate", fra_rate),
            "days": kwargs.get("days", days),
        },
    )

@formula("swap_fixed_rate", "Swap Fixed Rate", "(1 - DF_n) / Sum(DF_i)", DOMAIN_KEY, unit="")
def swap_fixed_rate(discount_factors: float | None = None, **kwargs):
    return build_result(
        fid="swap_fixed_rate",
        name="Swap Fixed Rate",
        expression="(1 - DF_n) / Sum(DF_i)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "discount_factors": kwargs.get("discount_factors", discount_factors),
        },
    )

@formula("swap_value", "Interest Rate Swap Value", "PV_Fixed - PV_Floating", DOMAIN_KEY, unit="")
def swap_value(pv_fixed: float | None = None, pv_floating: float | None = None, **kwargs):
    return build_result(
        fid="swap_value",
        name="Interest Rate Swap Value",
        expression="PV_Fixed - PV_Floating",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "pv_fixed": kwargs.get("pv_fixed", pv_fixed),
            "pv_floating": kwargs.get("pv_floating", pv_floating),
        },
    )

@formula("call_payoff", "Call Payoff at Expiry", "max(S - K, 0) - Premium", DOMAIN_KEY, unit="")
def call_payoff(spot: float | None = None, strike: float | None = None, premium: float | None = None, **kwargs):
    return build_result(
        fid="call_payoff",
        name="Call Payoff at Expiry",
        expression="max(S - K, 0) - Premium",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "premium": kwargs.get("premium", premium),
        },
    )

@formula("put_payoff", "Put Payoff at Expiry", "max(K - S, 0) - Premium", DOMAIN_KEY, unit="")
def put_payoff(spot: float | None = None, strike: float | None = None, premium: float | None = None, **kwargs):
    return build_result(
        fid="put_payoff",
        name="Put Payoff at Expiry",
        expression="max(K - S, 0) - Premium",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "premium": kwargs.get("premium", premium),
        },
    )

@formula("straddle_payoff", "Straddle Payoff", "|S - K| - Total_Premium", DOMAIN_KEY, unit="")
def straddle_payoff(spot: float | None = None, strike: float | None = None, total_premium: float | None = None, **kwargs):
    return build_result(
        fid="straddle_payoff",
        name="Straddle Payoff",
        expression="|S - K| - Total_Premium",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "total_premium": kwargs.get("total_premium", total_premium),
        },
    )

@formula("strangle_payoff", "Strangle Payoff", "max(S-Kc,0)+max(Kp-S,0)-Prem", DOMAIN_KEY, unit="")
def strangle_payoff(spot: float | None = None, strike_call: float | None = None, strike_put: float | None = None, premium: float | None = None, **kwargs):
    return build_result(
        fid="strangle_payoff",
        name="Strangle Payoff",
        expression="max(S-Kc,0)+max(Kp-S,0)-Prem",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike_call": kwargs.get("strike_call", strike_call),
            "strike_put": kwargs.get("strike_put", strike_put),
            "premium": kwargs.get("premium", premium),
        },
    )

@formula("covered_call_return", "Covered Call Return", "(Premium + max(K-S,0)) / S", DOMAIN_KEY, unit="")
def covered_call_return(spot: float | None = None, strike: float | None = None, premium: float | None = None, **kwargs):
    return build_result(
        fid="covered_call_return",
        name="Covered Call Return",
        expression="(Premium + max(K-S,0)) / S",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strike": kwargs.get("strike", strike),
            "premium": kwargs.get("premium", premium),
        },
    )

@formula("collar_value", "Collar Value", "Long put + short call payoff", DOMAIN_KEY, unit="")
def collar_value(spot: float | None = None, put_strike: float | None = None, call_strike: float | None = None, net_premium: float | None = None, **kwargs):
    return build_result(
        fid="collar_value",
        name="Collar Value",
        expression="Long put + short call payoff",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "put_strike": kwargs.get("put_strike", put_strike),
            "call_strike": kwargs.get("call_strike", call_strike),
            "net_premium": kwargs.get("net_premium", net_premium),
        },
    )

@formula("butterfly_payoff", "Butterfly Spread Payoff", "Combined option payoff", DOMAIN_KEY, unit="")
def butterfly_payoff(spot: float | None = None, strikes: float | None = None, premiums: float | None = None, **kwargs):
    return build_result(
        fid="butterfly_payoff",
        name="Butterfly Spread Payoff",
        expression="Combined option payoff",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spot": kwargs.get("spot", spot),
            "strikes": kwargs.get("strikes", strikes),
            "premiums": kwargs.get("premiums", premiums),
        },
    )

@formula("delta_hedge_shares", "Delta Hedge Shares", "-Delta * Contracts * 100", DOMAIN_KEY, unit="")
def delta_hedge_shares(delta: float | None = None, contracts: float | None = None, **kwargs):
    return build_result(
        fid="delta_hedge_shares",
        name="Delta Hedge Shares",
        expression="-Delta * Contracts * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "delta": kwargs.get("delta", delta),
            "contracts": kwargs.get("contracts", contracts),
        },
    )

@formula("option_leverage", "Option Leverage (Lambda)", "Delta * S / Option_Price", DOMAIN_KEY, unit="")
def option_leverage(delta: float | None = None, spot: float | None = None, option_price: float | None = None, **kwargs):
    return build_result(
        fid="option_leverage",
        name="Option Leverage (Lambda)",
        expression="Delta * S / Option_Price",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "delta": kwargs.get("delta", delta),
            "spot": kwargs.get("spot", spot),
            "option_price": kwargs.get("option_price", option_price),
        },
    )

@formula("breakeven_call", "Call Breakeven", "Strike + Premium", DOMAIN_KEY, unit="")
def breakeven_call(strike: float | None = None, premium: float | None = None, **kwargs):
    return build_result(
        fid="breakeven_call",
        name="Call Breakeven",
        expression="Strike + Premium",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "strike": kwargs.get("strike", strike),
            "premium": kwargs.get("premium", premium),
        },
    )

@formula("breakeven_put", "Put Breakeven", "Strike - Premium", DOMAIN_KEY, unit="")
def breakeven_put(strike: float | None = None, premium: float | None = None, **kwargs):
    return build_result(
        fid="breakeven_put",
        name="Put Breakeven",
        expression="Strike - Premium",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "strike": kwargs.get("strike", strike),
            "premium": kwargs.get("premium", premium),
        },
    )

@formula("max_pain", "Max Pain Price", "Strike minimizing total payout", DOMAIN_KEY, unit="")
def max_pain(strikes: float | None = None, open_interest: float | None = None, **kwargs):
    return build_result(
        fid="max_pain",
        name="Max Pain Price",
        expression="Strike minimizing total payout",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "strikes": kwargs.get("strikes", strikes),
            "open_interest": kwargs.get("open_interest", open_interest),
        },
    )

@formula("historical_var_option", "Option Position VaR", "Delta-gamma VaR approximation", DOMAIN_KEY, unit="")
def historical_var_option(delta: float | None = None, gamma: float | None = None, spot: float | None = None, volatility: float | None = None, confidence: float | None = None, **kwargs):
    return build_result(
        fid="historical_var_option",
        name="Option Position VaR",
        expression="Delta-gamma VaR approximation",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "delta": kwargs.get("delta", delta),
            "gamma": kwargs.get("gamma", gamma),
            "spot": kwargs.get("spot", spot),
            "volatility": kwargs.get("volatility", volatility),
            "confidence": kwargs.get("confidence", confidence),
        },
    )
