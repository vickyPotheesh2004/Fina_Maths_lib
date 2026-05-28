from .base import build_result, formula

DOMAIN_KEY = "D27_insurance_actuarial"
DOMAIN_TITLE = "Insurance, Actuarial & Claims Analytics"
FORMULA_IDS = [
    "loss_ratio",
    "expense_ratio_ins",
    "combined_ratio_ins",
    "claim_frequency",
    "claim_severity",
    "actuarial_metric_1",
    "actuarial_metric_2",
    "actuarial_metric_3",
    "actuarial_metric_4",
    "actuarial_metric_5",
    "actuarial_metric_6",
    "actuarial_metric_7",
    "actuarial_metric_8",
    "actuarial_metric_9",
    "actuarial_metric_10",
    "actuarial_metric_11",
    "actuarial_metric_12",
    "actuarial_metric_13",
    "actuarial_metric_14",
    "actuarial_metric_15",
    "actuarial_metric_16",
    "actuarial_metric_17",
    "actuarial_metric_18",
    "actuarial_metric_19",
    "actuarial_metric_20",
    "actuarial_metric_21",
    "actuarial_metric_22",
    "actuarial_metric_23",
    "actuarial_metric_24",
    "actuarial_metric_25",
    "actuarial_metric_26",
    "actuarial_metric_27",
    "actuarial_metric_28",
    "actuarial_metric_29",
    "actuarial_metric_30",
    "actuarial_metric_31",
    "actuarial_metric_32",
    "actuarial_metric_33",
    "actuarial_metric_34",
    "actuarial_metric_35",
    "actuarial_metric_36",
    "actuarial_metric_37",
    "actuarial_metric_38",
    "actuarial_metric_39",
    "actuarial_metric_40",
    "actuarial_metric_41",
    "actuarial_metric_42",
    "actuarial_metric_43",
    "actuarial_metric_44",
    "actuarial_metric_45",
    "actuarial_metric_46",
    "actuarial_metric_47",
    "actuarial_metric_48",
    "actuarial_metric_49",
    "actuarial_metric_50",
]

@formula("loss_ratio", "Loss Ratio", "Claims_Incurred / Earned_Premium", DOMAIN_KEY, unit="")
def loss_ratio(claims_incurred: float | None = None, earned_premium: float | None = None, **kwargs):
    return build_result(
        fid="loss_ratio",
        name="Loss Ratio",
        expression="Claims_Incurred / Earned_Premium",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "claims_incurred": kwargs.get("claims_incurred", claims_incurred),
            "earned_premium": kwargs.get("earned_premium", earned_premium),
        },
    )

@formula("expense_ratio_ins", "Expense Ratio", "Underwriting_Expense / Earned_Premium", DOMAIN_KEY, unit="")
def expense_ratio_ins(underwriting_expense: float | None = None, earned_premium: float | None = None, **kwargs):
    return build_result(
        fid="expense_ratio_ins",
        name="Expense Ratio",
        expression="Underwriting_Expense / Earned_Premium",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "underwriting_expense": kwargs.get("underwriting_expense", underwriting_expense),
            "earned_premium": kwargs.get("earned_premium", earned_premium),
        },
    )

@formula("combined_ratio_ins", "Combined Ratio", "Loss_Ratio + Expense_Ratio", DOMAIN_KEY, unit="")
def combined_ratio_ins(loss_ratio: float | None = None, expense_ratio: float | None = None, **kwargs):
    return build_result(
        fid="combined_ratio_ins",
        name="Combined Ratio",
        expression="Loss_Ratio + Expense_Ratio",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "loss_ratio": kwargs.get("loss_ratio", loss_ratio),
            "expense_ratio": kwargs.get("expense_ratio", expense_ratio),
        },
    )

@formula("claim_frequency", "Claim Frequency", "Claims_Count / Exposure_Units", DOMAIN_KEY, unit="")
def claim_frequency(claims_count: float | None = None, exposure_units: float | None = None, **kwargs):
    return build_result(
        fid="claim_frequency",
        name="Claim Frequency",
        expression="Claims_Count / Exposure_Units",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "claims_count": kwargs.get("claims_count", claims_count),
            "exposure_units": kwargs.get("exposure_units", exposure_units),
        },
    )

@formula("claim_severity", "Claim Severity", "Claims_Amount / Claims_Count", DOMAIN_KEY, unit="")
def claim_severity(claims_amount: float | None = None, claims_count: float | None = None, **kwargs):
    return build_result(
        fid="claim_severity",
        name="Claim Severity",
        expression="Claims_Amount / Claims_Count",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "claims_amount": kwargs.get("claims_amount", claims_amount),
            "claims_count": kwargs.get("claims_count", claims_count),
        },
    )

@formula("actuarial_metric_1", "Actuarial Metric 1", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_1(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_1",
        name="Actuarial Metric 1",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_2", "Actuarial Metric 2", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_2(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_2",
        name="Actuarial Metric 2",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_3", "Actuarial Metric 3", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_3(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_3",
        name="Actuarial Metric 3",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_4", "Actuarial Metric 4", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_4(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_4",
        name="Actuarial Metric 4",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_5", "Actuarial Metric 5", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_5(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_5",
        name="Actuarial Metric 5",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_6", "Actuarial Metric 6", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_6(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_6",
        name="Actuarial Metric 6",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_7", "Actuarial Metric 7", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_7(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_7",
        name="Actuarial Metric 7",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_8", "Actuarial Metric 8", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_8(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_8",
        name="Actuarial Metric 8",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_9", "Actuarial Metric 9", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_9(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_9",
        name="Actuarial Metric 9",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_10", "Actuarial Metric 10", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_10(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_10",
        name="Actuarial Metric 10",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_11", "Actuarial Metric 11", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_11(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_11",
        name="Actuarial Metric 11",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_12", "Actuarial Metric 12", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_12(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_12",
        name="Actuarial Metric 12",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_13", "Actuarial Metric 13", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_13(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_13",
        name="Actuarial Metric 13",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_14", "Actuarial Metric 14", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_14(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_14",
        name="Actuarial Metric 14",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_15", "Actuarial Metric 15", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_15(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_15",
        name="Actuarial Metric 15",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_16", "Actuarial Metric 16", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_16(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_16",
        name="Actuarial Metric 16",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_17", "Actuarial Metric 17", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_17(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_17",
        name="Actuarial Metric 17",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_18", "Actuarial Metric 18", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_18(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_18",
        name="Actuarial Metric 18",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_19", "Actuarial Metric 19", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_19(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_19",
        name="Actuarial Metric 19",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_20", "Actuarial Metric 20", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_20(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_20",
        name="Actuarial Metric 20",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_21", "Actuarial Metric 21", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_21(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_21",
        name="Actuarial Metric 21",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_22", "Actuarial Metric 22", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_22(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_22",
        name="Actuarial Metric 22",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_23", "Actuarial Metric 23", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_23(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_23",
        name="Actuarial Metric 23",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_24", "Actuarial Metric 24", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_24(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_24",
        name="Actuarial Metric 24",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_25", "Actuarial Metric 25", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_25(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_25",
        name="Actuarial Metric 25",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_26", "Actuarial Metric 26", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_26(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_26",
        name="Actuarial Metric 26",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_27", "Actuarial Metric 27", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_27(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_27",
        name="Actuarial Metric 27",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_28", "Actuarial Metric 28", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_28(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_28",
        name="Actuarial Metric 28",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_29", "Actuarial Metric 29", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_29(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_29",
        name="Actuarial Metric 29",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_30", "Actuarial Metric 30", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_30(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_30",
        name="Actuarial Metric 30",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_31", "Actuarial Metric 31", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_31(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_31",
        name="Actuarial Metric 31",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_32", "Actuarial Metric 32", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_32(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_32",
        name="Actuarial Metric 32",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_33", "Actuarial Metric 33", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_33(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_33",
        name="Actuarial Metric 33",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_34", "Actuarial Metric 34", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_34(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_34",
        name="Actuarial Metric 34",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_35", "Actuarial Metric 35", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_35(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_35",
        name="Actuarial Metric 35",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_36", "Actuarial Metric 36", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_36(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_36",
        name="Actuarial Metric 36",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_37", "Actuarial Metric 37", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_37(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_37",
        name="Actuarial Metric 37",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_38", "Actuarial Metric 38", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_38(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_38",
        name="Actuarial Metric 38",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_39", "Actuarial Metric 39", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_39(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_39",
        name="Actuarial Metric 39",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_40", "Actuarial Metric 40", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_40(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_40",
        name="Actuarial Metric 40",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_41", "Actuarial Metric 41", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_41(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_41",
        name="Actuarial Metric 41",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_42", "Actuarial Metric 42", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_42(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_42",
        name="Actuarial Metric 42",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_43", "Actuarial Metric 43", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_43(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_43",
        name="Actuarial Metric 43",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_44", "Actuarial Metric 44", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_44(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_44",
        name="Actuarial Metric 44",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_45", "Actuarial Metric 45", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_45(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_45",
        name="Actuarial Metric 45",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_46", "Actuarial Metric 46", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_46(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_46",
        name="Actuarial Metric 46",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_47", "Actuarial Metric 47", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_47(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_47",
        name="Actuarial Metric 47",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_48", "Actuarial Metric 48", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_48(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_48",
        name="Actuarial Metric 48",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_49", "Actuarial Metric 49", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_49(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_49",
        name="Actuarial Metric 49",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )

@formula("actuarial_metric_50", "Actuarial Metric 50", "Numerator / Denominator", DOMAIN_KEY, unit="")
def actuarial_metric_50(numerator: float | None = None, denominator: float | None = None, **kwargs):
    return build_result(
        fid="actuarial_metric_50",
        name="Actuarial Metric 50",
        expression="Numerator / Denominator",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "numerator": kwargs.get("numerator", numerator),
            "denominator": kwargs.get("denominator", denominator),
        },
    )
