from .base import build_result, formula

DOMAIN_KEY = "D20_interest_rate_models"
DOMAIN_TITLE = "Interest Rate Curves, Swaps & Short-Rate Models"
FORMULA_IDS = [
    "forward_rate_from_spot",
    "par_swap_rate",
    "ir_zero_coupon_price",
    "duration_approx",
    "convexity_approx",
    "ir_curve_factor_1",
    "ir_curve_factor_2",
    "ir_curve_factor_3",
    "ir_curve_factor_4",
    "ir_curve_factor_5",
    "ir_curve_factor_6",
    "ir_curve_factor_7",
    "ir_curve_factor_8",
    "ir_curve_factor_9",
    "ir_curve_factor_10",
    "ir_curve_factor_11",
    "ir_curve_factor_12",
    "ir_curve_factor_13",
    "ir_curve_factor_14",
    "ir_curve_factor_15",
    "ir_curve_factor_16",
    "ir_curve_factor_17",
    "ir_curve_factor_18",
    "ir_curve_factor_19",
    "ir_curve_factor_20",
    "ir_curve_factor_21",
    "ir_curve_factor_22",
    "ir_curve_factor_23",
    "ir_curve_factor_24",
    "ir_curve_factor_25",
    "ir_curve_factor_26",
    "ir_curve_factor_27",
    "ir_curve_factor_28",
    "ir_curve_factor_29",
    "ir_curve_factor_30",
    "ir_curve_factor_31",
    "ir_curve_factor_32",
    "ir_curve_factor_33",
    "ir_curve_factor_34",
    "ir_curve_factor_35",
    "ir_curve_factor_36",
    "ir_curve_factor_37",
    "ir_curve_factor_38",
    "ir_curve_factor_39",
    "ir_curve_factor_40",
    "ir_curve_factor_41",
    "ir_curve_factor_42",
    "ir_curve_factor_43",
    "ir_curve_factor_44",
    "ir_curve_factor_45",
    "ir_curve_factor_46",
    "ir_curve_factor_47",
    "ir_curve_factor_48",
    "ir_curve_factor_49",
    "ir_curve_factor_50",
    "ir_curve_factor_51",
    "ir_curve_factor_52",
    "ir_curve_factor_53",
    "ir_curve_factor_54",
    "ir_curve_factor_55",
]

@formula("forward_rate_from_spot", "Forward Rate from Spot", "((1+R2)^T2 / (1+R1)^T1)^(1/(T2-T1)) - 1", DOMAIN_KEY, unit="")
def forward_rate_from_spot(r2: float | None = None, t2: float | None = None, r1: float | None = None, t1: float | None = None, **kwargs):
    return build_result(
        fid="forward_rate_from_spot",
        name="Forward Rate from Spot",
        expression="((1+R2)^T2 / (1+R1)^T1)^(1/(T2-T1)) - 1",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "r2": kwargs.get("r2", r2),
            "t2": kwargs.get("t2", t2),
            "r1": kwargs.get("r1", r1),
            "t1": kwargs.get("t1", t1),
        },
    )

@formula("par_swap_rate", "Par Swap Rate", "(1 - Discount_Factor_N) / Sum(Discount_Factors)", DOMAIN_KEY, unit="")
def par_swap_rate(discount_factor_n: float | None = None, discount_factors: float | None = None, **kwargs):
    return build_result(
        fid="par_swap_rate",
        name="Par Swap Rate",
        expression="(1 - Discount_Factor_N) / Sum(Discount_Factors)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "discount_factor_n": kwargs.get("discount_factor_n", discount_factor_n),
            "discount_factors": kwargs.get("discount_factors", discount_factors),
        },
    )

@formula("ir_zero_coupon_price", "IR Zero Coupon Bond Price", "Face / (1 + Yield)^Time", DOMAIN_KEY, unit="")
def ir_zero_coupon_price(face: float | None = None, yield_rate: float | None = None, time: float | None = None, **kwargs):
    return build_result(
        fid="ir_zero_coupon_price",
        name="IR Zero Coupon Bond Price",
        expression="Face / (1 + Yield)^Time",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "face": kwargs.get("face", face),
            "yield_rate": kwargs.get("yield_rate", yield_rate),
            "time": kwargs.get("time", time),
        },
    )

@formula("duration_approx", "Approx Duration", "-(Delta_Price / Price) / Delta_Yield", DOMAIN_KEY, unit="")
def duration_approx(delta_price: float | None = None, price: float | None = None, delta_yield: float | None = None, **kwargs):
    return build_result(
        fid="duration_approx",
        name="Approx Duration",
        expression="-(Delta_Price / Price) / Delta_Yield",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "delta_price": kwargs.get("delta_price", delta_price),
            "price": kwargs.get("price", price),
            "delta_yield": kwargs.get("delta_yield", delta_yield),
        },
    )

@formula("convexity_approx", "Approx Convexity", "(P_Up + P_Down - 2*P0) / (P0 * Delta_Yield^2)", DOMAIN_KEY, unit="")
def convexity_approx(p_up: float | None = None, p_down: float | None = None, p0: float | None = None, delta_yield: float | None = None, **kwargs):
    return build_result(
        fid="convexity_approx",
        name="Approx Convexity",
        expression="(P_Up + P_Down - 2*P0) / (P0 * Delta_Yield^2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "p_up": kwargs.get("p_up", p_up),
            "p_down": kwargs.get("p_down", p_down),
            "p0": kwargs.get("p0", p0),
            "delta_yield": kwargs.get("delta_yield", delta_yield),
        },
    )

@formula("ir_curve_factor_1", "IR Curve Factor 1", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_1(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_1",
        name="IR Curve Factor 1",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_2", "IR Curve Factor 2", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_2(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_2",
        name="IR Curve Factor 2",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_3", "IR Curve Factor 3", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_3(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_3",
        name="IR Curve Factor 3",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_4", "IR Curve Factor 4", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_4(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_4",
        name="IR Curve Factor 4",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_5", "IR Curve Factor 5", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_5(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_5",
        name="IR Curve Factor 5",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_6", "IR Curve Factor 6", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_6(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_6",
        name="IR Curve Factor 6",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_7", "IR Curve Factor 7", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_7(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_7",
        name="IR Curve Factor 7",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_8", "IR Curve Factor 8", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_8(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_8",
        name="IR Curve Factor 8",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_9", "IR Curve Factor 9", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_9(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_9",
        name="IR Curve Factor 9",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_10", "IR Curve Factor 10", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_10(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_10",
        name="IR Curve Factor 10",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_11", "IR Curve Factor 11", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_11(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_11",
        name="IR Curve Factor 11",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_12", "IR Curve Factor 12", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_12(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_12",
        name="IR Curve Factor 12",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_13", "IR Curve Factor 13", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_13(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_13",
        name="IR Curve Factor 13",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_14", "IR Curve Factor 14", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_14(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_14",
        name="IR Curve Factor 14",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_15", "IR Curve Factor 15", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_15(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_15",
        name="IR Curve Factor 15",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_16", "IR Curve Factor 16", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_16(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_16",
        name="IR Curve Factor 16",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_17", "IR Curve Factor 17", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_17(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_17",
        name="IR Curve Factor 17",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_18", "IR Curve Factor 18", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_18(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_18",
        name="IR Curve Factor 18",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_19", "IR Curve Factor 19", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_19(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_19",
        name="IR Curve Factor 19",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_20", "IR Curve Factor 20", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_20(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_20",
        name="IR Curve Factor 20",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_21", "IR Curve Factor 21", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_21(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_21",
        name="IR Curve Factor 21",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_22", "IR Curve Factor 22", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_22(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_22",
        name="IR Curve Factor 22",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_23", "IR Curve Factor 23", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_23(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_23",
        name="IR Curve Factor 23",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_24", "IR Curve Factor 24", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_24(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_24",
        name="IR Curve Factor 24",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_25", "IR Curve Factor 25", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_25(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_25",
        name="IR Curve Factor 25",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_26", "IR Curve Factor 26", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_26(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_26",
        name="IR Curve Factor 26",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_27", "IR Curve Factor 27", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_27(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_27",
        name="IR Curve Factor 27",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_28", "IR Curve Factor 28", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_28(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_28",
        name="IR Curve Factor 28",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_29", "IR Curve Factor 29", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_29(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_29",
        name="IR Curve Factor 29",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_30", "IR Curve Factor 30", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_30(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_30",
        name="IR Curve Factor 30",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_31", "IR Curve Factor 31", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_31(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_31",
        name="IR Curve Factor 31",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_32", "IR Curve Factor 32", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_32(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_32",
        name="IR Curve Factor 32",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_33", "IR Curve Factor 33", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_33(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_33",
        name="IR Curve Factor 33",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_34", "IR Curve Factor 34", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_34(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_34",
        name="IR Curve Factor 34",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_35", "IR Curve Factor 35", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_35(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_35",
        name="IR Curve Factor 35",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_36", "IR Curve Factor 36", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_36(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_36",
        name="IR Curve Factor 36",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_37", "IR Curve Factor 37", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_37(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_37",
        name="IR Curve Factor 37",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_38", "IR Curve Factor 38", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_38(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_38",
        name="IR Curve Factor 38",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_39", "IR Curve Factor 39", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_39(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_39",
        name="IR Curve Factor 39",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_40", "IR Curve Factor 40", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_40(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_40",
        name="IR Curve Factor 40",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_41", "IR Curve Factor 41", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_41(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_41",
        name="IR Curve Factor 41",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_42", "IR Curve Factor 42", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_42(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_42",
        name="IR Curve Factor 42",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_43", "IR Curve Factor 43", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_43(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_43",
        name="IR Curve Factor 43",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_44", "IR Curve Factor 44", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_44(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_44",
        name="IR Curve Factor 44",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_45", "IR Curve Factor 45", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_45(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_45",
        name="IR Curve Factor 45",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_46", "IR Curve Factor 46", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_46(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_46",
        name="IR Curve Factor 46",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_47", "IR Curve Factor 47", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_47(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_47",
        name="IR Curve Factor 47",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_48", "IR Curve Factor 48", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_48(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_48",
        name="IR Curve Factor 48",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_49", "IR Curve Factor 49", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_49(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_49",
        name="IR Curve Factor 49",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_50", "IR Curve Factor 50", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_50(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_50",
        name="IR Curve Factor 50",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_51", "IR Curve Factor 51", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_51(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_51",
        name="IR Curve Factor 51",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_52", "IR Curve Factor 52", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_52(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_52",
        name="IR Curve Factor 52",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_53", "IR Curve Factor 53", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_53(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_53",
        name="IR Curve Factor 53",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_54", "IR Curve Factor 54", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_54(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_54",
        name="IR Curve Factor 54",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )

@formula("ir_curve_factor_55", "IR Curve Factor 55", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ir_curve_factor_55(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ir_curve_factor_55",
        name="IR Curve Factor 55",
        expression="w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x1": kwargs.get("x1", x1),
            "x2": kwargs.get("x2", x2),
            "x3": kwargs.get("x3", x3),
            "x4": kwargs.get("x4", x4),
            "x5": kwargs.get("x5", x5),
            "w1": kwargs.get("w1", w1),
            "w2": kwargs.get("w2", w2),
            "w3": kwargs.get("w3", w3),
            "w4": kwargs.get("w4", w4),
            "w5": kwargs.get("w5", w5),
        },
    )
