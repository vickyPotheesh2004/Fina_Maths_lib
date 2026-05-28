from .base import build_result, formula

DOMAIN_KEY = "D19_credit_risk"
DOMAIN_TITLE = "Credit Risk, Default & Loss Modeling"
FORMULA_IDS = [
    "expected_credit_loss",
    "unexpected_loss",
    "hazard_rate_credit",
    "recovery_rate",
    "credit_spread_simple",
    "credit_metric_1",
    "credit_metric_2",
    "credit_metric_3",
    "credit_metric_4",
    "credit_metric_5",
    "credit_metric_6",
    "credit_metric_7",
    "credit_metric_8",
    "credit_metric_9",
    "credit_metric_10",
    "credit_metric_11",
    "credit_metric_12",
    "credit_metric_13",
    "credit_metric_14",
    "credit_metric_15",
    "credit_metric_16",
    "credit_metric_17",
    "credit_metric_18",
    "credit_metric_19",
    "credit_metric_20",
    "credit_metric_21",
    "credit_metric_22",
    "credit_metric_23",
    "credit_metric_24",
    "credit_metric_25",
    "credit_metric_26",
    "credit_metric_27",
    "credit_metric_28",
    "credit_metric_29",
    "credit_metric_30",
    "credit_metric_31",
    "credit_metric_32",
    "credit_metric_33",
    "credit_metric_34",
    "credit_metric_35",
    "credit_metric_36",
    "credit_metric_37",
    "credit_metric_38",
    "credit_metric_39",
    "credit_metric_40",
    "credit_metric_41",
    "credit_metric_42",
    "credit_metric_43",
    "credit_metric_44",
    "credit_metric_45",
    "credit_metric_46",
    "credit_metric_47",
    "credit_metric_48",
    "credit_metric_49",
    "credit_metric_50",
    "credit_metric_51",
    "credit_metric_52",
    "credit_metric_53",
    "credit_metric_54",
    "credit_metric_55",
]

@formula("expected_credit_loss", "Expected Credit Loss", "PD * LGD * EAD", DOMAIN_KEY, unit="")
def expected_credit_loss(pd: float | None = None, lgd: float | None = None, ead: float | None = None, **kwargs):
    return build_result(
        fid="expected_credit_loss",
        name="Expected Credit Loss",
        expression="PD * LGD * EAD",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "pd": kwargs.get("pd", pd),
            "lgd": kwargs.get("lgd", lgd),
            "ead": kwargs.get("ead", ead),
        },
    )

@formula("unexpected_loss", "Unexpected Loss", "sqrt(PD*(1-PD)) * LGD * EAD", DOMAIN_KEY, unit="")
def unexpected_loss(pd: float | None = None, lgd: float | None = None, ead: float | None = None, **kwargs):
    return build_result(
        fid="unexpected_loss",
        name="Unexpected Loss",
        expression="sqrt(PD*(1-PD)) * LGD * EAD",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "pd": kwargs.get("pd", pd),
            "lgd": kwargs.get("lgd", lgd),
            "ead": kwargs.get("ead", ead),
        },
    )

@formula("hazard_rate_credit", "Credit Hazard Rate", "-log(1 - PD) / Horizon", DOMAIN_KEY, unit="")
def hazard_rate_credit(pd: float | None = None, horizon: float | None = None, **kwargs):
    return build_result(
        fid="hazard_rate_credit",
        name="Credit Hazard Rate",
        expression="-log(1 - PD) / Horizon",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "pd": kwargs.get("pd", pd),
            "horizon": kwargs.get("horizon", horizon),
        },
    )

@formula("recovery_rate", "Recovery Rate", "Recovered_Amount / Exposure", DOMAIN_KEY, unit="")
def recovery_rate(recovered_amount: float | None = None, exposure: float | None = None, **kwargs):
    return build_result(
        fid="recovery_rate",
        name="Recovery Rate",
        expression="Recovered_Amount / Exposure",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "recovered_amount": kwargs.get("recovered_amount", recovered_amount),
            "exposure": kwargs.get("exposure", exposure),
        },
    )

@formula("credit_spread_simple", "Credit Spread", "Bond_Yield - Risk_Free", DOMAIN_KEY, unit="")
def credit_spread_simple(bond_yield: float | None = None, risk_free: float | None = None, **kwargs):
    return build_result(
        fid="credit_spread_simple",
        name="Credit Spread",
        expression="Bond_Yield - Risk_Free",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "bond_yield": kwargs.get("bond_yield", bond_yield),
            "risk_free": kwargs.get("risk_free", risk_free),
        },
    )

@formula("credit_metric_1", "Credit Metric 1", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_1(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_1",
        name="Credit Metric 1",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_2", "Credit Metric 2", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_2(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_2",
        name="Credit Metric 2",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_3", "Credit Metric 3", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_3(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_3",
        name="Credit Metric 3",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_4", "Credit Metric 4", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_4(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_4",
        name="Credit Metric 4",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_5", "Credit Metric 5", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_5(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_5",
        name="Credit Metric 5",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_6", "Credit Metric 6", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_6(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_6",
        name="Credit Metric 6",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_7", "Credit Metric 7", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_7(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_7",
        name="Credit Metric 7",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_8", "Credit Metric 8", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_8(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_8",
        name="Credit Metric 8",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_9", "Credit Metric 9", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_9(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_9",
        name="Credit Metric 9",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_10", "Credit Metric 10", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_10(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_10",
        name="Credit Metric 10",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_11", "Credit Metric 11", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_11(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_11",
        name="Credit Metric 11",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_12", "Credit Metric 12", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_12(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_12",
        name="Credit Metric 12",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_13", "Credit Metric 13", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_13(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_13",
        name="Credit Metric 13",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_14", "Credit Metric 14", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_14(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_14",
        name="Credit Metric 14",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_15", "Credit Metric 15", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_15(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_15",
        name="Credit Metric 15",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_16", "Credit Metric 16", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_16(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_16",
        name="Credit Metric 16",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_17", "Credit Metric 17", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_17(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_17",
        name="Credit Metric 17",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_18", "Credit Metric 18", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_18(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_18",
        name="Credit Metric 18",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_19", "Credit Metric 19", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_19(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_19",
        name="Credit Metric 19",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_20", "Credit Metric 20", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_20(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_20",
        name="Credit Metric 20",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_21", "Credit Metric 21", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_21(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_21",
        name="Credit Metric 21",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_22", "Credit Metric 22", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_22(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_22",
        name="Credit Metric 22",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_23", "Credit Metric 23", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_23(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_23",
        name="Credit Metric 23",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_24", "Credit Metric 24", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_24(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_24",
        name="Credit Metric 24",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_25", "Credit Metric 25", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_25(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_25",
        name="Credit Metric 25",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_26", "Credit Metric 26", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_26(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_26",
        name="Credit Metric 26",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_27", "Credit Metric 27", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_27(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_27",
        name="Credit Metric 27",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_28", "Credit Metric 28", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_28(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_28",
        name="Credit Metric 28",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_29", "Credit Metric 29", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_29(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_29",
        name="Credit Metric 29",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_30", "Credit Metric 30", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_30(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_30",
        name="Credit Metric 30",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_31", "Credit Metric 31", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_31(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_31",
        name="Credit Metric 31",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_32", "Credit Metric 32", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_32(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_32",
        name="Credit Metric 32",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_33", "Credit Metric 33", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_33(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_33",
        name="Credit Metric 33",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_34", "Credit Metric 34", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_34(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_34",
        name="Credit Metric 34",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_35", "Credit Metric 35", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_35(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_35",
        name="Credit Metric 35",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_36", "Credit Metric 36", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_36(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_36",
        name="Credit Metric 36",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_37", "Credit Metric 37", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_37(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_37",
        name="Credit Metric 37",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_38", "Credit Metric 38", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_38(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_38",
        name="Credit Metric 38",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_39", "Credit Metric 39", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_39(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_39",
        name="Credit Metric 39",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_40", "Credit Metric 40", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_40(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_40",
        name="Credit Metric 40",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_41", "Credit Metric 41", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_41(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_41",
        name="Credit Metric 41",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_42", "Credit Metric 42", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_42(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_42",
        name="Credit Metric 42",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_43", "Credit Metric 43", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_43(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_43",
        name="Credit Metric 43",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_44", "Credit Metric 44", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_44(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_44",
        name="Credit Metric 44",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_45", "Credit Metric 45", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_45(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_45",
        name="Credit Metric 45",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_46", "Credit Metric 46", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_46(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_46",
        name="Credit Metric 46",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_47", "Credit Metric 47", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_47(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_47",
        name="Credit Metric 47",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_48", "Credit Metric 48", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_48(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_48",
        name="Credit Metric 48",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_49", "Credit Metric 49", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_49(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_49",
        name="Credit Metric 49",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_50", "Credit Metric 50", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_50(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_50",
        name="Credit Metric 50",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_51", "Credit Metric 51", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_51(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_51",
        name="Credit Metric 51",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_52", "Credit Metric 52", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_52(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_52",
        name="Credit Metric 52",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_53", "Credit Metric 53", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_53(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_53",
        name="Credit Metric 53",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_54", "Credit Metric 54", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_54(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_54",
        name="Credit Metric 54",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("credit_metric_55", "Credit Metric 55", "Numerator / Denominator", DOMAIN_KEY, unit="")
def credit_metric_55(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="credit_metric_55",
        name="Credit Metric 55",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )
