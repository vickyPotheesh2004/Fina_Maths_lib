from .base import build_result, formula

DOMAIN_KEY = "D08_tvm"
DOMAIN_TITLE = "Time Value of Money & Capital Budgeting"
FORMULA_IDS = [
    "present_value",
    "future_value",
    "npv",
    "irr",
    "mirr",
    "xirr",
    "pv_annuity",
    "fv_annuity",
    "pv_annuity_due",
    "fv_annuity_due",
    "perpetuity",
    "growing_perpetuity",
    "growing_annuity_pv",
    "annuity_payment",
    "loan_payment",
    "loan_balance",
    "amortization_interest",
    "amortization_principal",
    "effective_annual_rate",
    "nominal_rate",
    "continuous_compounding",
    "continuous_pv",
    "rule_of_72",
    "rule_of_69",
    "payback_period",
    "discounted_payback",
    "profitability_index",
    "equivalent_annual_cost",
    "equivalent_annual_annuity",
    "crossover_rate",
    "real_rate",
    "fisher_equation",
    "annuity_factor",
    "future_value_factor",
    "present_value_factor",
    "sinking_fund",
    "capital_recovery_factor",
    "deferred_annuity_pv",
    "net_future_value",
    "modified_payback",
    "accounting_rate_of_return",
    "bcr",
    "annualized_return",
    "holding_period_yield",
    "breakeven_interest_rate",
]

@formula("present_value", "Present Value", "FV / (1+r)^n", DOMAIN_KEY, unit="")
def present_value(future_value: float | None = None, rate: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="present_value",
        name="Present Value",
        expression="FV / (1+r)^n",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "future_value": kwargs.get("future_value", future_value),
            "rate": kwargs.get("rate", rate),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("future_value", "Future Value", "PV * (1+r)^n", DOMAIN_KEY, unit="")
def future_value(present_value: float | None = None, rate: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="future_value",
        name="Future Value",
        expression="PV * (1+r)^n",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "present_value": kwargs.get("present_value", present_value),
            "rate": kwargs.get("rate", rate),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("npv", "Net Present Value", "Sum(CF_t/(1+r)^t) - Initial", DOMAIN_KEY, unit="")
def npv(cash_flows: float | None = None, rate: float | None = None, initial_investment: float | None = None, **kwargs):
    return build_result(
        fid="npv",
        name="Net Present Value",
        expression="Sum(CF_t/(1+r)^t) - Initial",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cash_flows": kwargs.get("cash_flows", cash_flows),
            "rate": kwargs.get("rate", rate),
            "initial_investment": kwargs.get("initial_investment", initial_investment),
        },
    )

@formula("irr", "Internal Rate of Return", "Solve r: NPV = 0", DOMAIN_KEY, unit="")
def irr(cash_flows: float | None = None, initial_investment: float | None = None, **kwargs):
    return build_result(
        fid="irr",
        name="Internal Rate of Return",
        expression="Solve r: NPV = 0",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cash_flows": kwargs.get("cash_flows", cash_flows),
            "initial_investment": kwargs.get("initial_investment", initial_investment),
        },
    )

@formula("mirr", "Modified IRR", "(FV_inflows/PV_outflows)^(1/n) - 1", DOMAIN_KEY, unit="")
def mirr(cash_flows: float | None = None, finance_rate: float | None = None, reinvest_rate: float | None = None, **kwargs):
    return build_result(
        fid="mirr",
        name="Modified IRR",
        expression="(FV_inflows/PV_outflows)^(1/n) - 1",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cash_flows": kwargs.get("cash_flows", cash_flows),
            "finance_rate": kwargs.get("finance_rate", finance_rate),
            "reinvest_rate": kwargs.get("reinvest_rate", reinvest_rate),
        },
    )

@formula("xirr", "XIRR (Irregular)", "Solve for rate with dates", DOMAIN_KEY, unit="")
def xirr(cash_flows: float | None = None, dates: float | None = None, **kwargs):
    return build_result(
        fid="xirr",
        name="XIRR (Irregular)",
        expression="Solve for rate with dates",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cash_flows": kwargs.get("cash_flows", cash_flows),
            "dates": kwargs.get("dates", dates),
        },
    )

@formula("pv_annuity", "PV of Annuity", "PMT * (1-(1+r)^-n)/r", DOMAIN_KEY, unit="")
def pv_annuity(payment: float | None = None, rate: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="pv_annuity",
        name="PV of Annuity",
        expression="PMT * (1-(1+r)^-n)/r",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "payment": kwargs.get("payment", payment),
            "rate": kwargs.get("rate", rate),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("fv_annuity", "FV of Annuity", "PMT * ((1+r)^n - 1)/r", DOMAIN_KEY, unit="")
def fv_annuity(payment: float | None = None, rate: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="fv_annuity",
        name="FV of Annuity",
        expression="PMT * ((1+r)^n - 1)/r",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "payment": kwargs.get("payment", payment),
            "rate": kwargs.get("rate", rate),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("pv_annuity_due", "PV of Annuity Due", "PV_Annuity * (1+r)", DOMAIN_KEY, unit="")
def pv_annuity_due(payment: float | None = None, rate: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="pv_annuity_due",
        name="PV of Annuity Due",
        expression="PV_Annuity * (1+r)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "payment": kwargs.get("payment", payment),
            "rate": kwargs.get("rate", rate),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("fv_annuity_due", "FV of Annuity Due", "FV_Annuity * (1+r)", DOMAIN_KEY, unit="")
def fv_annuity_due(payment: float | None = None, rate: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="fv_annuity_due",
        name="FV of Annuity Due",
        expression="FV_Annuity * (1+r)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "payment": kwargs.get("payment", payment),
            "rate": kwargs.get("rate", rate),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("perpetuity", "Perpetuity Value", "PMT / r", DOMAIN_KEY, unit="")
def perpetuity(payment: float | None = None, rate: float | None = None, **kwargs):
    return build_result(
        fid="perpetuity",
        name="Perpetuity Value",
        expression="PMT / r",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "payment": kwargs.get("payment", payment),
            "rate": kwargs.get("rate", rate),
        },
    )

@formula("growing_perpetuity", "Growing Perpetuity", "PMT / (r - g)", DOMAIN_KEY, unit="")
def growing_perpetuity(payment: float | None = None, rate: float | None = None, growth: float | None = None, **kwargs):
    return build_result(
        fid="growing_perpetuity",
        name="Growing Perpetuity",
        expression="PMT / (r - g)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "payment": kwargs.get("payment", payment),
            "rate": kwargs.get("rate", rate),
            "growth": kwargs.get("growth", growth),
        },
    )

@formula("growing_annuity_pv", "PV Growing Annuity", "PMT/(r-g)*(1-((1+g)/(1+r))^n)", DOMAIN_KEY, unit="")
def growing_annuity_pv(payment: float | None = None, rate: float | None = None, growth: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="growing_annuity_pv",
        name="PV Growing Annuity",
        expression="PMT/(r-g)*(1-((1+g)/(1+r))^n)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "payment": kwargs.get("payment", payment),
            "rate": kwargs.get("rate", rate),
            "growth": kwargs.get("growth", growth),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("annuity_payment", "Annuity Payment (PMT)", "PV*r / (1-(1+r)^-n)", DOMAIN_KEY, unit="")
def annuity_payment(present_value: float | None = None, rate: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="annuity_payment",
        name="Annuity Payment (PMT)",
        expression="PV*r / (1-(1+r)^-n)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "present_value": kwargs.get("present_value", present_value),
            "rate": kwargs.get("rate", rate),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("loan_payment", "Loan Payment", "P*r / (1-(1+r)^-n)", DOMAIN_KEY, unit="")
def loan_payment(principal: float | None = None, rate: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="loan_payment",
        name="Loan Payment",
        expression="P*r / (1-(1+r)^-n)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "principal": kwargs.get("principal", principal),
            "rate": kwargs.get("rate", rate),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("loan_balance", "Remaining Loan Balance", "P*(1+r)^k - PMT*((1+r)^k-1)/r", DOMAIN_KEY, unit="")
def loan_balance(principal: float | None = None, rate: float | None = None, payment: float | None = None, periods_paid: float | None = None, **kwargs):
    return build_result(
        fid="loan_balance",
        name="Remaining Loan Balance",
        expression="P*(1+r)^k - PMT*((1+r)^k-1)/r",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "principal": kwargs.get("principal", principal),
            "rate": kwargs.get("rate", rate),
            "payment": kwargs.get("payment", payment),
            "periods_paid": kwargs.get("periods_paid", periods_paid),
        },
    )

@formula("amortization_interest", "Amortization Interest Portion", "Balance * Rate", DOMAIN_KEY, unit="")
def amortization_interest(balance: float | None = None, rate: float | None = None, **kwargs):
    return build_result(
        fid="amortization_interest",
        name="Amortization Interest Portion",
        expression="Balance * Rate",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "balance": kwargs.get("balance", balance),
            "rate": kwargs.get("rate", rate),
        },
    )

@formula("amortization_principal", "Amortization Principal Portion", "Payment - Interest", DOMAIN_KEY, unit="")
def amortization_principal(payment: float | None = None, interest: float | None = None, **kwargs):
    return build_result(
        fid="amortization_principal",
        name="Amortization Principal Portion",
        expression="Payment - Interest",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "payment": kwargs.get("payment", payment),
            "interest": kwargs.get("interest", interest),
        },
    )

@formula("effective_annual_rate", "Effective Annual Rate", "(1 + r/n)^n - 1", DOMAIN_KEY, unit="")
def effective_annual_rate(nominal_rate: float | None = None, frequency: float | None = None, **kwargs):
    return build_result(
        fid="effective_annual_rate",
        name="Effective Annual Rate",
        expression="(1 + r/n)^n - 1",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "nominal_rate": kwargs.get("nominal_rate", nominal_rate),
            "frequency": kwargs.get("frequency", frequency),
        },
    )

@formula("nominal_rate", "Nominal Rate from EAR", "n*((1+EAR)^(1/n) - 1)", DOMAIN_KEY, unit="")
def nominal_rate(ear: float | None = None, frequency: float | None = None, **kwargs):
    return build_result(
        fid="nominal_rate",
        name="Nominal Rate from EAR",
        expression="n*((1+EAR)^(1/n) - 1)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ear": kwargs.get("ear", ear),
            "frequency": kwargs.get("frequency", frequency),
        },
    )

@formula("continuous_compounding", "Continuous Compounding FV", "PV * e^(rt)", DOMAIN_KEY, unit="")
def continuous_compounding(present_value: float | None = None, rate: float | None = None, time: float | None = None, **kwargs):
    return build_result(
        fid="continuous_compounding",
        name="Continuous Compounding FV",
        expression="PV * e^(rt)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "present_value": kwargs.get("present_value", present_value),
            "rate": kwargs.get("rate", rate),
            "time": kwargs.get("time", time),
        },
    )

@formula("continuous_pv", "Continuous Compounding PV", "FV * e^(-rt)", DOMAIN_KEY, unit="")
def continuous_pv(future_value: float | None = None, rate: float | None = None, time: float | None = None, **kwargs):
    return build_result(
        fid="continuous_pv",
        name="Continuous Compounding PV",
        expression="FV * e^(-rt)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "future_value": kwargs.get("future_value", future_value),
            "rate": kwargs.get("rate", rate),
            "time": kwargs.get("time", time),
        },
    )

@formula("rule_of_72", "Rule of 72", "72 / Rate_Percent", DOMAIN_KEY, unit="")
def rule_of_72(rate_percent: float | None = None, **kwargs):
    return build_result(
        fid="rule_of_72",
        name="Rule of 72",
        expression="72 / Rate_Percent",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "rate_percent": kwargs.get("rate_percent", rate_percent),
        },
    )

@formula("rule_of_69", "Rule of 69.3", "69.3 / Rate_Percent", DOMAIN_KEY, unit="")
def rule_of_69(rate_percent: float | None = None, **kwargs):
    return build_result(
        fid="rule_of_69",
        name="Rule of 69.3",
        expression="69.3 / Rate_Percent",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "rate_percent": kwargs.get("rate_percent", rate_percent),
        },
    )

@formula("payback_period", "Payback Period", "Years until cumulative CF = 0", DOMAIN_KEY, unit="")
def payback_period(cash_flows: float | None = None, initial_investment: float | None = None, **kwargs):
    return build_result(
        fid="payback_period",
        name="Payback Period",
        expression="Years until cumulative CF = 0",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cash_flows": kwargs.get("cash_flows", cash_flows),
            "initial_investment": kwargs.get("initial_investment", initial_investment),
        },
    )

@formula("discounted_payback", "Discounted Payback Period", "Years until discounted cum = 0", DOMAIN_KEY, unit="")
def discounted_payback(cash_flows: float | None = None, rate: float | None = None, initial_investment: float | None = None, **kwargs):
    return build_result(
        fid="discounted_payback",
        name="Discounted Payback Period",
        expression="Years until discounted cum = 0",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cash_flows": kwargs.get("cash_flows", cash_flows),
            "rate": kwargs.get("rate", rate),
            "initial_investment": kwargs.get("initial_investment", initial_investment),
        },
    )

@formula("profitability_index", "Profitability Index", "PV_Inflows / Initial_Investment", DOMAIN_KEY, unit="")
def profitability_index(pv_inflows: float | None = None, initial_investment: float | None = None, **kwargs):
    return build_result(
        fid="profitability_index",
        name="Profitability Index",
        expression="PV_Inflows / Initial_Investment",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "pv_inflows": kwargs.get("pv_inflows", pv_inflows),
            "initial_investment": kwargs.get("initial_investment", initial_investment),
        },
    )

@formula("equivalent_annual_cost", "Equivalent Annual Cost", "NPV / Annuity_Factor", DOMAIN_KEY, unit="")
def equivalent_annual_cost(npv: float | None = None, rate: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="equivalent_annual_cost",
        name="Equivalent Annual Cost",
        expression="NPV / Annuity_Factor",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "npv": kwargs.get("npv", npv),
            "rate": kwargs.get("rate", rate),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("equivalent_annual_annuity", "Equivalent Annual Annuity", "NPV * r / (1-(1+r)^-n)", DOMAIN_KEY, unit="")
def equivalent_annual_annuity(npv: float | None = None, rate: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="equivalent_annual_annuity",
        name="Equivalent Annual Annuity",
        expression="NPV * r / (1-(1+r)^-n)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "npv": kwargs.get("npv", npv),
            "rate": kwargs.get("rate", rate),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("crossover_rate", "Crossover Rate", "IRR of CF differences", DOMAIN_KEY, unit="")
def crossover_rate(cash_flows_a: float | None = None, cash_flows_b: float | None = None, **kwargs):
    return build_result(
        fid="crossover_rate",
        name="Crossover Rate",
        expression="IRR of CF differences",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cash_flows_a": kwargs.get("cash_flows_a", cash_flows_a),
            "cash_flows_b": kwargs.get("cash_flows_b", cash_flows_b),
        },
    )

@formula("real_rate", "Real Rate of Return", "(1+nominal)/(1+inflation) - 1", DOMAIN_KEY, unit="")
def real_rate(nominal_rate: float | None = None, inflation_rate: float | None = None, **kwargs):
    return build_result(
        fid="real_rate",
        name="Real Rate of Return",
        expression="(1+nominal)/(1+inflation) - 1",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "nominal_rate": kwargs.get("nominal_rate", nominal_rate),
            "inflation_rate": kwargs.get("inflation_rate", inflation_rate),
        },
    )

@formula("fisher_equation", "Fisher Equation", "(1+real)*(1+inflation) - 1", DOMAIN_KEY, unit="")
def fisher_equation(real_rate: float | None = None, inflation_rate: float | None = None, **kwargs):
    return build_result(
        fid="fisher_equation",
        name="Fisher Equation",
        expression="(1+real)*(1+inflation) - 1",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "real_rate": kwargs.get("real_rate", real_rate),
            "inflation_rate": kwargs.get("inflation_rate", inflation_rate),
        },
    )

@formula("annuity_factor", "Annuity Factor", "(1-(1+r)^-n) / r", DOMAIN_KEY, unit="")
def annuity_factor(rate: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="annuity_factor",
        name="Annuity Factor",
        expression="(1-(1+r)^-n) / r",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "rate": kwargs.get("rate", rate),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("future_value_factor", "Future Value Factor", "(1+r)^n", DOMAIN_KEY, unit="")
def future_value_factor(rate: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="future_value_factor",
        name="Future Value Factor",
        expression="(1+r)^n",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "rate": kwargs.get("rate", rate),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("present_value_factor", "Present Value Factor", "1 / (1+r)^n", DOMAIN_KEY, unit="")
def present_value_factor(rate: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="present_value_factor",
        name="Present Value Factor",
        expression="1 / (1+r)^n",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "rate": kwargs.get("rate", rate),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("sinking_fund", "Sinking Fund Payment", "FV*r / ((1+r)^n - 1)", DOMAIN_KEY, unit="")
def sinking_fund(future_value: float | None = None, rate: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="sinking_fund",
        name="Sinking Fund Payment",
        expression="FV*r / ((1+r)^n - 1)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "future_value": kwargs.get("future_value", future_value),
            "rate": kwargs.get("rate", rate),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("capital_recovery_factor", "Capital Recovery Factor", "r / (1-(1+r)^-n)", DOMAIN_KEY, unit="")
def capital_recovery_factor(rate: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="capital_recovery_factor",
        name="Capital Recovery Factor",
        expression="r / (1-(1+r)^-n)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "rate": kwargs.get("rate", rate),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("deferred_annuity_pv", "Deferred Annuity PV", "PV_Annuity / (1+r)^defer", DOMAIN_KEY, unit="")
def deferred_annuity_pv(payment: float | None = None, rate: float | None = None, periods: float | None = None, deferral: float | None = None, **kwargs):
    return build_result(
        fid="deferred_annuity_pv",
        name="Deferred Annuity PV",
        expression="PV_Annuity / (1+r)^defer",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "payment": kwargs.get("payment", payment),
            "rate": kwargs.get("rate", rate),
            "periods": kwargs.get("periods", periods),
            "deferral": kwargs.get("deferral", deferral),
        },
    )

@formula("net_future_value", "Net Future Value", "Sum(CF_t * (1+r)^(n-t))", DOMAIN_KEY, unit="")
def net_future_value(cash_flows: float | None = None, rate: float | None = None, **kwargs):
    return build_result(
        fid="net_future_value",
        name="Net Future Value",
        expression="Sum(CF_t * (1+r)^(n-t))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cash_flows": kwargs.get("cash_flows", cash_flows),
            "rate": kwargs.get("rate", rate),
        },
    )

@formula("modified_payback", "Modified Payback", "Adjusted payback period", DOMAIN_KEY, unit="")
def modified_payback(cash_flows: float | None = None, terminal_value: float | None = None, **kwargs):
    return build_result(
        fid="modified_payback",
        name="Modified Payback",
        expression="Adjusted payback period",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cash_flows": kwargs.get("cash_flows", cash_flows),
            "terminal_value": kwargs.get("terminal_value", terminal_value),
        },
    )

@formula("accounting_rate_of_return", "Accounting Rate of Return", "Avg_Profit / Avg_Investment * 100", DOMAIN_KEY, unit="")
def accounting_rate_of_return(average_profit: float | None = None, average_investment: float | None = None, **kwargs):
    return build_result(
        fid="accounting_rate_of_return",
        name="Accounting Rate of Return",
        expression="Avg_Profit / Avg_Investment * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "average_profit": kwargs.get("average_profit", average_profit),
            "average_investment": kwargs.get("average_investment", average_investment),
        },
    )

@formula("bcr", "Benefit-Cost Ratio", "PV_Benefits / PV_Costs", DOMAIN_KEY, unit="")
def bcr(pv_benefits: float | None = None, pv_costs: float | None = None, **kwargs):
    return build_result(
        fid="bcr",
        name="Benefit-Cost Ratio",
        expression="PV_Benefits / PV_Costs",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "pv_benefits": kwargs.get("pv_benefits", pv_benefits),
            "pv_costs": kwargs.get("pv_costs", pv_costs),
        },
    )

@formula("annualized_return", "Annualized Return", "(End/Start)^(1/years) - 1", DOMAIN_KEY, unit="")
def annualized_return(start_value: float | None = None, end_value: float | None = None, years: float | None = None, **kwargs):
    return build_result(
        fid="annualized_return",
        name="Annualized Return",
        expression="(End/Start)^(1/years) - 1",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "start_value": kwargs.get("start_value", start_value),
            "end_value": kwargs.get("end_value", end_value),
            "years": kwargs.get("years", years),
        },
    )

@formula("holding_period_yield", "Holding Period Yield %", "(End + Income - Start)/Start*100", DOMAIN_KEY, unit="")
def holding_period_yield(start_value: float | None = None, end_value: float | None = None, income: float | None = None, **kwargs):
    return build_result(
        fid="holding_period_yield",
        name="Holding Period Yield %",
        expression="(End + Income - Start)/Start*100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "start_value": kwargs.get("start_value", start_value),
            "end_value": kwargs.get("end_value", end_value),
            "income": kwargs.get("income", income),
        },
    )

@formula("breakeven_interest_rate", "Breakeven Interest Rate", "Rate where NPV = 0", DOMAIN_KEY, unit="")
def breakeven_interest_rate(cash_flows: float | None = None, **kwargs):
    return build_result(
        fid="breakeven_interest_rate",
        name="Breakeven Interest Rate",
        expression="Rate where NPV = 0",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cash_flows": kwargs.get("cash_flows", cash_flows),
        },
    )
