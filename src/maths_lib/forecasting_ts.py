from .base import build_result, formula

DOMAIN_KEY = "D23_forecasting_ts"
DOMAIN_TITLE = "Forecasting, Time-Series & Signal Decomposition"
FORMULA_IDS = [
    "mae_forecast",
    "mse_forecast",
    "rmse_forecast",
    "mape_forecast",
    "wape_forecast",
    "ts_component_1",
    "ts_component_2",
    "ts_component_3",
    "ts_component_4",
    "ts_component_5",
    "ts_component_6",
    "ts_component_7",
    "ts_component_8",
    "ts_component_9",
    "ts_component_10",
    "ts_component_11",
    "ts_component_12",
    "ts_component_13",
    "ts_component_14",
    "ts_component_15",
    "ts_component_16",
    "ts_component_17",
    "ts_component_18",
    "ts_component_19",
    "ts_component_20",
    "ts_component_21",
    "ts_component_22",
    "ts_component_23",
    "ts_component_24",
    "ts_component_25",
    "ts_component_26",
    "ts_component_27",
    "ts_component_28",
    "ts_component_29",
    "ts_component_30",
    "ts_component_31",
    "ts_component_32",
    "ts_component_33",
    "ts_component_34",
    "ts_component_35",
    "ts_component_36",
    "ts_component_37",
    "ts_component_38",
    "ts_component_39",
    "ts_component_40",
    "ts_component_41",
    "ts_component_42",
    "ts_component_43",
    "ts_component_44",
    "ts_component_45",
    "ts_component_46",
    "ts_component_47",
    "ts_component_48",
    "ts_component_49",
    "ts_component_50",
    "ts_component_51",
    "ts_component_52",
    "ts_component_53",
    "ts_component_54",
    "ts_component_55",
]

@formula("mae_forecast", "Forecast MAE", "Mean(Absolute_Errors)", DOMAIN_KEY, unit="")
def mae_forecast(absolute_errors: float | None = None, **kwargs):
    return build_result(
        fid="mae_forecast",
        name="Forecast MAE",
        expression="Mean(Absolute_Errors)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "absolute_errors": kwargs.get("absolute_errors", absolute_errors),
        },
    )

@formula("mse_forecast", "Forecast MSE", "Mean(Squared_Errors)", DOMAIN_KEY, unit="")
def mse_forecast(squared_errors: float | None = None, **kwargs):
    return build_result(
        fid="mse_forecast",
        name="Forecast MSE",
        expression="Mean(Squared_Errors)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "squared_errors": kwargs.get("squared_errors", squared_errors),
        },
    )

@formula("rmse_forecast", "Forecast RMSE", "sqrt(MSE)", DOMAIN_KEY, unit="")
def rmse_forecast(mse: float | None = None, **kwargs):
    return build_result(
        fid="rmse_forecast",
        name="Forecast RMSE",
        expression="sqrt(MSE)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "mse": kwargs.get("mse", mse),
        },
    )

@formula("mape_forecast", "Forecast MAPE", "Mean(APE)", DOMAIN_KEY, unit="")
def mape_forecast(ape: float | None = None, **kwargs):
    return build_result(
        fid="mape_forecast",
        name="Forecast MAPE",
        expression="Mean(APE)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ape": kwargs.get("ape", ape),
        },
    )

@formula("wape_forecast", "Forecast WAPE", "Sum(Absolute_Errors) / Sum(Actuals)", DOMAIN_KEY, unit="")
def wape_forecast(absolute_errors: float | None = None, actuals: float | None = None, **kwargs):
    return build_result(
        fid="wape_forecast",
        name="Forecast WAPE",
        expression="Sum(Absolute_Errors) / Sum(Actuals)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "absolute_errors": kwargs.get("absolute_errors", absolute_errors),
            "actuals": kwargs.get("actuals", actuals),
        },
    )

@formula("ts_component_1", "Time-Series Component 1", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_1(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_1",
        name="Time-Series Component 1",
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

@formula("ts_component_2", "Time-Series Component 2", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_2(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_2",
        name="Time-Series Component 2",
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

@formula("ts_component_3", "Time-Series Component 3", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_3(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_3",
        name="Time-Series Component 3",
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

@formula("ts_component_4", "Time-Series Component 4", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_4(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_4",
        name="Time-Series Component 4",
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

@formula("ts_component_5", "Time-Series Component 5", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_5(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_5",
        name="Time-Series Component 5",
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

@formula("ts_component_6", "Time-Series Component 6", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_6(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_6",
        name="Time-Series Component 6",
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

@formula("ts_component_7", "Time-Series Component 7", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_7(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_7",
        name="Time-Series Component 7",
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

@formula("ts_component_8", "Time-Series Component 8", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_8(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_8",
        name="Time-Series Component 8",
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

@formula("ts_component_9", "Time-Series Component 9", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_9(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_9",
        name="Time-Series Component 9",
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

@formula("ts_component_10", "Time-Series Component 10", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_10(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_10",
        name="Time-Series Component 10",
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

@formula("ts_component_11", "Time-Series Component 11", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_11(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_11",
        name="Time-Series Component 11",
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

@formula("ts_component_12", "Time-Series Component 12", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_12(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_12",
        name="Time-Series Component 12",
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

@formula("ts_component_13", "Time-Series Component 13", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_13(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_13",
        name="Time-Series Component 13",
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

@formula("ts_component_14", "Time-Series Component 14", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_14(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_14",
        name="Time-Series Component 14",
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

@formula("ts_component_15", "Time-Series Component 15", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_15(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_15",
        name="Time-Series Component 15",
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

@formula("ts_component_16", "Time-Series Component 16", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_16(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_16",
        name="Time-Series Component 16",
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

@formula("ts_component_17", "Time-Series Component 17", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_17(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_17",
        name="Time-Series Component 17",
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

@formula("ts_component_18", "Time-Series Component 18", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_18(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_18",
        name="Time-Series Component 18",
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

@formula("ts_component_19", "Time-Series Component 19", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_19(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_19",
        name="Time-Series Component 19",
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

@formula("ts_component_20", "Time-Series Component 20", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_20(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_20",
        name="Time-Series Component 20",
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

@formula("ts_component_21", "Time-Series Component 21", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_21(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_21",
        name="Time-Series Component 21",
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

@formula("ts_component_22", "Time-Series Component 22", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_22(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_22",
        name="Time-Series Component 22",
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

@formula("ts_component_23", "Time-Series Component 23", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_23(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_23",
        name="Time-Series Component 23",
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

@formula("ts_component_24", "Time-Series Component 24", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_24(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_24",
        name="Time-Series Component 24",
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

@formula("ts_component_25", "Time-Series Component 25", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_25(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_25",
        name="Time-Series Component 25",
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

@formula("ts_component_26", "Time-Series Component 26", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_26(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_26",
        name="Time-Series Component 26",
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

@formula("ts_component_27", "Time-Series Component 27", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_27(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_27",
        name="Time-Series Component 27",
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

@formula("ts_component_28", "Time-Series Component 28", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_28(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_28",
        name="Time-Series Component 28",
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

@formula("ts_component_29", "Time-Series Component 29", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_29(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_29",
        name="Time-Series Component 29",
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

@formula("ts_component_30", "Time-Series Component 30", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_30(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_30",
        name="Time-Series Component 30",
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

@formula("ts_component_31", "Time-Series Component 31", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_31(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_31",
        name="Time-Series Component 31",
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

@formula("ts_component_32", "Time-Series Component 32", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_32(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_32",
        name="Time-Series Component 32",
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

@formula("ts_component_33", "Time-Series Component 33", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_33(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_33",
        name="Time-Series Component 33",
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

@formula("ts_component_34", "Time-Series Component 34", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_34(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_34",
        name="Time-Series Component 34",
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

@formula("ts_component_35", "Time-Series Component 35", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_35(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_35",
        name="Time-Series Component 35",
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

@formula("ts_component_36", "Time-Series Component 36", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_36(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_36",
        name="Time-Series Component 36",
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

@formula("ts_component_37", "Time-Series Component 37", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_37(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_37",
        name="Time-Series Component 37",
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

@formula("ts_component_38", "Time-Series Component 38", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_38(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_38",
        name="Time-Series Component 38",
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

@formula("ts_component_39", "Time-Series Component 39", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_39(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_39",
        name="Time-Series Component 39",
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

@formula("ts_component_40", "Time-Series Component 40", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_40(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_40",
        name="Time-Series Component 40",
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

@formula("ts_component_41", "Time-Series Component 41", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_41(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_41",
        name="Time-Series Component 41",
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

@formula("ts_component_42", "Time-Series Component 42", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_42(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_42",
        name="Time-Series Component 42",
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

@formula("ts_component_43", "Time-Series Component 43", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_43(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_43",
        name="Time-Series Component 43",
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

@formula("ts_component_44", "Time-Series Component 44", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_44(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_44",
        name="Time-Series Component 44",
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

@formula("ts_component_45", "Time-Series Component 45", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_45(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_45",
        name="Time-Series Component 45",
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

@formula("ts_component_46", "Time-Series Component 46", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_46(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_46",
        name="Time-Series Component 46",
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

@formula("ts_component_47", "Time-Series Component 47", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_47(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_47",
        name="Time-Series Component 47",
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

@formula("ts_component_48", "Time-Series Component 48", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_48(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_48",
        name="Time-Series Component 48",
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

@formula("ts_component_49", "Time-Series Component 49", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_49(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_49",
        name="Time-Series Component 49",
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

@formula("ts_component_50", "Time-Series Component 50", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_50(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_50",
        name="Time-Series Component 50",
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

@formula("ts_component_51", "Time-Series Component 51", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_51(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_51",
        name="Time-Series Component 51",
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

@formula("ts_component_52", "Time-Series Component 52", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_52(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_52",
        name="Time-Series Component 52",
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

@formula("ts_component_53", "Time-Series Component 53", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_53(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_53",
        name="Time-Series Component 53",
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

@formula("ts_component_54", "Time-Series Component 54", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_54(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_54",
        name="Time-Series Component 54",
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

@formula("ts_component_55", "Time-Series Component 55", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def ts_component_55(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="ts_component_55",
        name="Time-Series Component 55",
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
