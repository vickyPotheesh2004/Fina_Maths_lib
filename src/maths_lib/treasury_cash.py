from .base import build_result, formula

DOMAIN_KEY = "D26_treasury_cash"
DOMAIN_TITLE = "Treasury, Cash Management & Working Capital Optimization"
FORMULA_IDS = [
    "cash_conversion_efficiency",
    "liquidity_buffer_ratio",
    "cash_yield_treasury",
    "funding_gap",
    "revolver_utilization",
    "treasury_metric_1",
    "treasury_metric_2",
    "treasury_metric_3",
    "treasury_metric_4",
    "treasury_metric_5",
    "treasury_metric_6",
    "treasury_metric_7",
    "treasury_metric_8",
    "treasury_metric_9",
    "treasury_metric_10",
    "treasury_metric_11",
    "treasury_metric_12",
    "treasury_metric_13",
    "treasury_metric_14",
    "treasury_metric_15",
    "treasury_metric_16",
    "treasury_metric_17",
    "treasury_metric_18",
    "treasury_metric_19",
    "treasury_metric_20",
    "treasury_metric_21",
    "treasury_metric_22",
    "treasury_metric_23",
    "treasury_metric_24",
    "treasury_metric_25",
    "treasury_metric_26",
    "treasury_metric_27",
    "treasury_metric_28",
    "treasury_metric_29",
    "treasury_metric_30",
    "treasury_metric_31",
    "treasury_metric_32",
    "treasury_metric_33",
    "treasury_metric_34",
    "treasury_metric_35",
    "treasury_metric_36",
    "treasury_metric_37",
    "treasury_metric_38",
    "treasury_metric_39",
    "treasury_metric_40",
    "treasury_metric_41",
    "treasury_metric_42",
    "treasury_metric_43",
    "treasury_metric_44",
    "treasury_metric_45",
    "treasury_metric_46",
    "treasury_metric_47",
    "treasury_metric_48",
    "treasury_metric_49",
    "treasury_metric_50",
]

@formula("cash_conversion_efficiency", "Cash Conversion Efficiency", "OCF / EBITDA", DOMAIN_KEY, unit="")
def cash_conversion_efficiency(ocf: float | None = None, ebitda: float | None = None, **kwargs):
    return build_result(
        fid="cash_conversion_efficiency",
        name="Cash Conversion Efficiency",
        expression="OCF / EBITDA",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ocf": kwargs.get("ocf", ocf),
            "ebitda": kwargs.get("ebitda", ebitda),
        },
    )

@formula("liquidity_buffer_ratio", "Liquidity Buffer Ratio", "Liquid_Assets / Short_Obligations", DOMAIN_KEY, unit="")
def liquidity_buffer_ratio(liquid_assets: float | None = None, short_obligations: float | None = None, **kwargs):
    return build_result(
        fid="liquidity_buffer_ratio",
        name="Liquidity Buffer Ratio",
        expression="Liquid_Assets / Short_Obligations",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "liquid_assets": kwargs.get("liquid_assets", liquid_assets),
            "short_obligations": kwargs.get("short_obligations", short_obligations),
        },
    )

@formula("cash_yield_treasury", "Cash Yield", "Investment_Income / Avg_Cash", DOMAIN_KEY, unit="")
def cash_yield_treasury(investment_income: float | None = None, avg_cash: float | None = None, **kwargs):
    return build_result(
        fid="cash_yield_treasury",
        name="Cash Yield",
        expression="Investment_Income / Avg_Cash",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "investment_income": kwargs.get("investment_income", investment_income),
            "avg_cash": kwargs.get("avg_cash", avg_cash),
        },
    )

@formula("funding_gap", "Funding Gap", "Outflows - Inflows", DOMAIN_KEY, unit="")
def funding_gap(outflows: float | None = None, inflows: float | None = None, **kwargs):
    return build_result(
        fid="funding_gap",
        name="Funding Gap",
        expression="Outflows - Inflows",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "outflows": kwargs.get("outflows", outflows),
            "inflows": kwargs.get("inflows", inflows),
        },
    )

@formula("revolver_utilization", "Revolver Utilization", "Drawn / Revolver_Limit", DOMAIN_KEY, unit="")
def revolver_utilization(drawn: float | None = None, revolver_limit: float | None = None, **kwargs):
    return build_result(
        fid="revolver_utilization",
        name="Revolver Utilization",
        expression="Drawn / Revolver_Limit",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "drawn": kwargs.get("drawn", drawn),
            "revolver_limit": kwargs.get("revolver_limit", revolver_limit),
        },
    )

@formula("treasury_metric_1", "Treasury Metric 1", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_1(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_1",
        name="Treasury Metric 1",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_2", "Treasury Metric 2", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_2(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_2",
        name="Treasury Metric 2",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_3", "Treasury Metric 3", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_3(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_3",
        name="Treasury Metric 3",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_4", "Treasury Metric 4", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_4(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_4",
        name="Treasury Metric 4",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_5", "Treasury Metric 5", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_5(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_5",
        name="Treasury Metric 5",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_6", "Treasury Metric 6", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_6(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_6",
        name="Treasury Metric 6",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_7", "Treasury Metric 7", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_7(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_7",
        name="Treasury Metric 7",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_8", "Treasury Metric 8", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_8(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_8",
        name="Treasury Metric 8",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_9", "Treasury Metric 9", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_9(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_9",
        name="Treasury Metric 9",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_10", "Treasury Metric 10", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_10(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_10",
        name="Treasury Metric 10",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_11", "Treasury Metric 11", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_11(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_11",
        name="Treasury Metric 11",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_12", "Treasury Metric 12", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_12(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_12",
        name="Treasury Metric 12",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_13", "Treasury Metric 13", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_13(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_13",
        name="Treasury Metric 13",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_14", "Treasury Metric 14", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_14(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_14",
        name="Treasury Metric 14",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_15", "Treasury Metric 15", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_15(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_15",
        name="Treasury Metric 15",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_16", "Treasury Metric 16", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_16(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_16",
        name="Treasury Metric 16",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_17", "Treasury Metric 17", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_17(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_17",
        name="Treasury Metric 17",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_18", "Treasury Metric 18", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_18(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_18",
        name="Treasury Metric 18",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_19", "Treasury Metric 19", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_19(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_19",
        name="Treasury Metric 19",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_20", "Treasury Metric 20", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_20(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_20",
        name="Treasury Metric 20",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_21", "Treasury Metric 21", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_21(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_21",
        name="Treasury Metric 21",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_22", "Treasury Metric 22", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_22(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_22",
        name="Treasury Metric 22",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_23", "Treasury Metric 23", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_23(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_23",
        name="Treasury Metric 23",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_24", "Treasury Metric 24", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_24(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_24",
        name="Treasury Metric 24",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_25", "Treasury Metric 25", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_25(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_25",
        name="Treasury Metric 25",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_26", "Treasury Metric 26", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_26(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_26",
        name="Treasury Metric 26",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_27", "Treasury Metric 27", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_27(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_27",
        name="Treasury Metric 27",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_28", "Treasury Metric 28", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_28(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_28",
        name="Treasury Metric 28",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_29", "Treasury Metric 29", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_29(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_29",
        name="Treasury Metric 29",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_30", "Treasury Metric 30", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_30(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_30",
        name="Treasury Metric 30",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_31", "Treasury Metric 31", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_31(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_31",
        name="Treasury Metric 31",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_32", "Treasury Metric 32", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_32(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_32",
        name="Treasury Metric 32",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_33", "Treasury Metric 33", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_33(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_33",
        name="Treasury Metric 33",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_34", "Treasury Metric 34", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_34(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_34",
        name="Treasury Metric 34",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_35", "Treasury Metric 35", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_35(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_35",
        name="Treasury Metric 35",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_36", "Treasury Metric 36", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_36(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_36",
        name="Treasury Metric 36",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_37", "Treasury Metric 37", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_37(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_37",
        name="Treasury Metric 37",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_38", "Treasury Metric 38", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_38(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_38",
        name="Treasury Metric 38",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_39", "Treasury Metric 39", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_39(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_39",
        name="Treasury Metric 39",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_40", "Treasury Metric 40", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_40(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_40",
        name="Treasury Metric 40",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_41", "Treasury Metric 41", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_41(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_41",
        name="Treasury Metric 41",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_42", "Treasury Metric 42", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_42(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_42",
        name="Treasury Metric 42",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_43", "Treasury Metric 43", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_43(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_43",
        name="Treasury Metric 43",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_44", "Treasury Metric 44", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_44(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_44",
        name="Treasury Metric 44",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_45", "Treasury Metric 45", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_45(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_45",
        name="Treasury Metric 45",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_46", "Treasury Metric 46", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_46(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_46",
        name="Treasury Metric 46",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_47", "Treasury Metric 47", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_47(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_47",
        name="Treasury Metric 47",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_48", "Treasury Metric 48", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_48(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_48",
        name="Treasury Metric 48",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_49", "Treasury Metric 49", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_49(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_49",
        name="Treasury Metric 49",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("treasury_metric_50", "Treasury Metric 50", "Numerator / Denominator", DOMAIN_KEY, unit="")
def treasury_metric_50(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="treasury_metric_50",
        name="Treasury Metric 50",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )
