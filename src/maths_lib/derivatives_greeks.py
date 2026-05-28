from .base import build_result, formula

DOMAIN_KEY = "D22_derivatives_greeks"
DOMAIN_TITLE = "Derivatives Greeks, Exotics & Volatility Surfaces"
FORMULA_IDS = [
    "delta_approx",
    "gamma_approx",
    "vega_approx",
    "theta_approx",
    "rho_approx",
    "vol_surface_metric_1",
    "vol_surface_metric_2",
    "vol_surface_metric_3",
    "vol_surface_metric_4",
    "vol_surface_metric_5",
    "vol_surface_metric_6",
    "vol_surface_metric_7",
    "vol_surface_metric_8",
    "vol_surface_metric_9",
    "vol_surface_metric_10",
    "vol_surface_metric_11",
    "vol_surface_metric_12",
    "vol_surface_metric_13",
    "vol_surface_metric_14",
    "vol_surface_metric_15",
    "vol_surface_metric_16",
    "vol_surface_metric_17",
    "vol_surface_metric_18",
    "vol_surface_metric_19",
    "vol_surface_metric_20",
    "vol_surface_metric_21",
    "vol_surface_metric_22",
    "vol_surface_metric_23",
    "vol_surface_metric_24",
    "vol_surface_metric_25",
    "vol_surface_metric_26",
    "vol_surface_metric_27",
    "vol_surface_metric_28",
    "vol_surface_metric_29",
    "vol_surface_metric_30",
    "vol_surface_metric_31",
    "vol_surface_metric_32",
    "vol_surface_metric_33",
    "vol_surface_metric_34",
    "vol_surface_metric_35",
    "vol_surface_metric_36",
    "vol_surface_metric_37",
    "vol_surface_metric_38",
    "vol_surface_metric_39",
    "vol_surface_metric_40",
    "vol_surface_metric_41",
    "vol_surface_metric_42",
    "vol_surface_metric_43",
    "vol_surface_metric_44",
    "vol_surface_metric_45",
    "vol_surface_metric_46",
    "vol_surface_metric_47",
    "vol_surface_metric_48",
    "vol_surface_metric_49",
    "vol_surface_metric_50",
    "vol_surface_metric_51",
    "vol_surface_metric_52",
    "vol_surface_metric_53",
    "vol_surface_metric_54",
    "vol_surface_metric_55",
]

@formula("delta_approx", "Delta Approximation", "(V_Up - V_Down) / (2*Delta_S)", DOMAIN_KEY, unit="")
def delta_approx(v_up: float | None = None, v_down: float | None = None, delta_s: float | None = None, **kwargs):
    return build_result(
        fid="delta_approx",
        name="Delta Approximation",
        expression="(V_Up - V_Down) / (2*Delta_S)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "v_up": kwargs.get("v_up", v_up),
            "v_down": kwargs.get("v_down", v_down),
            "delta_s": kwargs.get("delta_s", delta_s),
        },
    )

@formula("gamma_approx", "Gamma Approximation", "(V_Up - 2*V0 + V_Down) / Delta_S^2", DOMAIN_KEY, unit="")
def gamma_approx(v_up: float | None = None, v0: float | None = None, v_down: float | None = None, delta_s: float | None = None, **kwargs):
    return build_result(
        fid="gamma_approx",
        name="Gamma Approximation",
        expression="(V_Up - 2*V0 + V_Down) / Delta_S^2",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "v_up": kwargs.get("v_up", v_up),
            "v0": kwargs.get("v0", v0),
            "v_down": kwargs.get("v_down", v_down),
            "delta_s": kwargs.get("delta_s", delta_s),
        },
    )

@formula("vega_approx", "Vega Approximation", "(V_VolUp - V_VolDown) / (2*Delta_Vol)", DOMAIN_KEY, unit="")
def vega_approx(v_volup: float | None = None, v_voldown: float | None = None, delta_vol: float | None = None, **kwargs):
    return build_result(
        fid="vega_approx",
        name="Vega Approximation",
        expression="(V_VolUp - V_VolDown) / (2*Delta_Vol)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "v_volup": kwargs.get("v_volup", v_volup),
            "v_voldown": kwargs.get("v_voldown", v_voldown),
            "delta_vol": kwargs.get("delta_vol", delta_vol),
        },
    )

@formula("theta_approx", "Theta Approximation", "(V_Tomorrow - V_Today) / Delta_T", DOMAIN_KEY, unit="")
def theta_approx(v_tomorrow: float | None = None, v_today: float | None = None, delta_t: float | None = None, **kwargs):
    return build_result(
        fid="theta_approx",
        name="Theta Approximation",
        expression="(V_Tomorrow - V_Today) / Delta_T",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "v_tomorrow": kwargs.get("v_tomorrow", v_tomorrow),
            "v_today": kwargs.get("v_today", v_today),
            "delta_t": kwargs.get("delta_t", delta_t),
        },
    )

@formula("rho_approx", "Rho Approximation", "(V_RateUp - V_RateDown) / (2*Delta_R)", DOMAIN_KEY, unit="")
def rho_approx(v_rateup: float | None = None, v_ratedown: float | None = None, delta_r: float | None = None, **kwargs):
    return build_result(
        fid="rho_approx",
        name="Rho Approximation",
        expression="(V_RateUp - V_RateDown) / (2*Delta_R)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "v_rateup": kwargs.get("v_rateup", v_rateup),
            "v_ratedown": kwargs.get("v_ratedown", v_ratedown),
            "delta_r": kwargs.get("delta_r", delta_r),
        },
    )

@formula("vol_surface_metric_1", "Vol Surface Metric 1", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_1(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_1",
        name="Vol Surface Metric 1",
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

@formula("vol_surface_metric_2", "Vol Surface Metric 2", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_2(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_2",
        name="Vol Surface Metric 2",
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

@formula("vol_surface_metric_3", "Vol Surface Metric 3", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_3(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_3",
        name="Vol Surface Metric 3",
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

@formula("vol_surface_metric_4", "Vol Surface Metric 4", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_4(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_4",
        name="Vol Surface Metric 4",
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

@formula("vol_surface_metric_5", "Vol Surface Metric 5", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_5(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_5",
        name="Vol Surface Metric 5",
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

@formula("vol_surface_metric_6", "Vol Surface Metric 6", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_6(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_6",
        name="Vol Surface Metric 6",
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

@formula("vol_surface_metric_7", "Vol Surface Metric 7", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_7(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_7",
        name="Vol Surface Metric 7",
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

@formula("vol_surface_metric_8", "Vol Surface Metric 8", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_8(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_8",
        name="Vol Surface Metric 8",
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

@formula("vol_surface_metric_9", "Vol Surface Metric 9", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_9(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_9",
        name="Vol Surface Metric 9",
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

@formula("vol_surface_metric_10", "Vol Surface Metric 10", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_10(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_10",
        name="Vol Surface Metric 10",
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

@formula("vol_surface_metric_11", "Vol Surface Metric 11", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_11(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_11",
        name="Vol Surface Metric 11",
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

@formula("vol_surface_metric_12", "Vol Surface Metric 12", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_12(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_12",
        name="Vol Surface Metric 12",
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

@formula("vol_surface_metric_13", "Vol Surface Metric 13", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_13(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_13",
        name="Vol Surface Metric 13",
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

@formula("vol_surface_metric_14", "Vol Surface Metric 14", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_14(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_14",
        name="Vol Surface Metric 14",
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

@formula("vol_surface_metric_15", "Vol Surface Metric 15", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_15(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_15",
        name="Vol Surface Metric 15",
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

@formula("vol_surface_metric_16", "Vol Surface Metric 16", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_16(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_16",
        name="Vol Surface Metric 16",
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

@formula("vol_surface_metric_17", "Vol Surface Metric 17", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_17(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_17",
        name="Vol Surface Metric 17",
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

@formula("vol_surface_metric_18", "Vol Surface Metric 18", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_18(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_18",
        name="Vol Surface Metric 18",
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

@formula("vol_surface_metric_19", "Vol Surface Metric 19", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_19(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_19",
        name="Vol Surface Metric 19",
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

@formula("vol_surface_metric_20", "Vol Surface Metric 20", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_20(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_20",
        name="Vol Surface Metric 20",
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

@formula("vol_surface_metric_21", "Vol Surface Metric 21", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_21(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_21",
        name="Vol Surface Metric 21",
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

@formula("vol_surface_metric_22", "Vol Surface Metric 22", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_22(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_22",
        name="Vol Surface Metric 22",
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

@formula("vol_surface_metric_23", "Vol Surface Metric 23", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_23(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_23",
        name="Vol Surface Metric 23",
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

@formula("vol_surface_metric_24", "Vol Surface Metric 24", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_24(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_24",
        name="Vol Surface Metric 24",
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

@formula("vol_surface_metric_25", "Vol Surface Metric 25", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_25(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_25",
        name="Vol Surface Metric 25",
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

@formula("vol_surface_metric_26", "Vol Surface Metric 26", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_26(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_26",
        name="Vol Surface Metric 26",
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

@formula("vol_surface_metric_27", "Vol Surface Metric 27", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_27(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_27",
        name="Vol Surface Metric 27",
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

@formula("vol_surface_metric_28", "Vol Surface Metric 28", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_28(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_28",
        name="Vol Surface Metric 28",
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

@formula("vol_surface_metric_29", "Vol Surface Metric 29", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_29(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_29",
        name="Vol Surface Metric 29",
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

@formula("vol_surface_metric_30", "Vol Surface Metric 30", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_30(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_30",
        name="Vol Surface Metric 30",
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

@formula("vol_surface_metric_31", "Vol Surface Metric 31", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_31(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_31",
        name="Vol Surface Metric 31",
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

@formula("vol_surface_metric_32", "Vol Surface Metric 32", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_32(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_32",
        name="Vol Surface Metric 32",
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

@formula("vol_surface_metric_33", "Vol Surface Metric 33", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_33(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_33",
        name="Vol Surface Metric 33",
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

@formula("vol_surface_metric_34", "Vol Surface Metric 34", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_34(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_34",
        name="Vol Surface Metric 34",
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

@formula("vol_surface_metric_35", "Vol Surface Metric 35", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_35(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_35",
        name="Vol Surface Metric 35",
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

@formula("vol_surface_metric_36", "Vol Surface Metric 36", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_36(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_36",
        name="Vol Surface Metric 36",
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

@formula("vol_surface_metric_37", "Vol Surface Metric 37", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_37(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_37",
        name="Vol Surface Metric 37",
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

@formula("vol_surface_metric_38", "Vol Surface Metric 38", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_38(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_38",
        name="Vol Surface Metric 38",
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

@formula("vol_surface_metric_39", "Vol Surface Metric 39", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_39(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_39",
        name="Vol Surface Metric 39",
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

@formula("vol_surface_metric_40", "Vol Surface Metric 40", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_40(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_40",
        name="Vol Surface Metric 40",
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

@formula("vol_surface_metric_41", "Vol Surface Metric 41", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_41(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_41",
        name="Vol Surface Metric 41",
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

@formula("vol_surface_metric_42", "Vol Surface Metric 42", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_42(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_42",
        name="Vol Surface Metric 42",
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

@formula("vol_surface_metric_43", "Vol Surface Metric 43", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_43(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_43",
        name="Vol Surface Metric 43",
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

@formula("vol_surface_metric_44", "Vol Surface Metric 44", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_44(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_44",
        name="Vol Surface Metric 44",
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

@formula("vol_surface_metric_45", "Vol Surface Metric 45", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_45(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_45",
        name="Vol Surface Metric 45",
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

@formula("vol_surface_metric_46", "Vol Surface Metric 46", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_46(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_46",
        name="Vol Surface Metric 46",
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

@formula("vol_surface_metric_47", "Vol Surface Metric 47", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_47(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_47",
        name="Vol Surface Metric 47",
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

@formula("vol_surface_metric_48", "Vol Surface Metric 48", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_48(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_48",
        name="Vol Surface Metric 48",
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

@formula("vol_surface_metric_49", "Vol Surface Metric 49", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_49(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_49",
        name="Vol Surface Metric 49",
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

@formula("vol_surface_metric_50", "Vol Surface Metric 50", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_50(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_50",
        name="Vol Surface Metric 50",
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

@formula("vol_surface_metric_51", "Vol Surface Metric 51", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_51(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_51",
        name="Vol Surface Metric 51",
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

@formula("vol_surface_metric_52", "Vol Surface Metric 52", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_52(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_52",
        name="Vol Surface Metric 52",
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

@formula("vol_surface_metric_53", "Vol Surface Metric 53", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_53(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_53",
        name="Vol Surface Metric 53",
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

@formula("vol_surface_metric_54", "Vol Surface Metric 54", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_54(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_54",
        name="Vol Surface Metric 54",
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

@formula("vol_surface_metric_55", "Vol Surface Metric 55", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def vol_surface_metric_55(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="vol_surface_metric_55",
        name="Vol Surface Metric 55",
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
