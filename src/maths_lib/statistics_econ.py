from .base import build_result, formula

DOMAIN_KEY = "D11_statistics"
DOMAIN_TITLE = "Statistics & Econometrics"
FORMULA_IDS = [
    "arithmetic_mean",
    "geometric_mean",
    "harmonic_mean",
    "weighted_mean",
    "median",
    "mode",
    "range_stat",
    "variance_population",
    "variance_sample",
    "standard_deviation_pop",
    "standard_deviation_sample",
    "coefficient_variation",
    "skewness",
    "kurtosis",
    "excess_kurtosis",
    "covariance_stat",
    "pearson_correlation",
    "spearman_correlation",
    "linear_regression_beta",
    "linear_regression_alpha",
    "r_squared",
    "adjusted_r_squared",
    "standard_error",
    "standard_error_regression",
    "t_statistic",
    "z_score",
    "confidence_interval",
    "chi_square_stat",
    "f_statistic",
    "percentile",
    "quartile",
    "interquartile_range",
    "autocorrelation",
    "moving_average_forecast",
    "exponential_smoothing",
    "holt_linear_trend",
    "holt_winters",
    "ar1_model",
    "durbin_watson",
    "mean_absolute_error",
    "mean_squared_error",
    "rmse",
    "mape",
    "theil_u",
    "garch_volatility",
]

@formula("arithmetic_mean", "Arithmetic Mean", "Sum(x) / n", DOMAIN_KEY, unit="")
def arithmetic_mean(values: float | None = None, **kwargs):
    return build_result(
        fid="arithmetic_mean",
        name="Arithmetic Mean",
        expression="Sum(x) / n",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
        },
    )

@formula("geometric_mean", "Geometric Mean", "(Prod(x))^(1/n)", DOMAIN_KEY, unit="")
def geometric_mean(values: float | None = None, **kwargs):
    return build_result(
        fid="geometric_mean",
        name="Geometric Mean",
        expression="(Prod(x))^(1/n)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
        },
    )

@formula("harmonic_mean", "Harmonic Mean", "n / Sum(1/x)", DOMAIN_KEY, unit="")
def harmonic_mean(values: float | None = None, **kwargs):
    return build_result(
        fid="harmonic_mean",
        name="Harmonic Mean",
        expression="n / Sum(1/x)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
        },
    )

@formula("weighted_mean", "Weighted Mean", "Sum(w*x) / Sum(w)", DOMAIN_KEY, unit="")
def weighted_mean(values: float | None = None, weights: float | None = None, **kwargs):
    return build_result(
        fid="weighted_mean",
        name="Weighted Mean",
        expression="Sum(w*x) / Sum(w)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
            "weights": kwargs.get("weights", weights),
        },
    )

@formula("median", "Median", "Middle of sorted values", DOMAIN_KEY, unit="")
def median(values: float | None = None, **kwargs):
    return build_result(
        fid="median",
        name="Median",
        expression="Middle of sorted values",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
        },
    )

@formula("mode", "Mode", "Most common value", DOMAIN_KEY, unit="")
def mode(values: float | None = None, **kwargs):
    return build_result(
        fid="mode",
        name="Mode",
        expression="Most common value",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
        },
    )

@formula("range_stat", "Range", "Max - Min", DOMAIN_KEY, unit="")
def range_stat(values: float | None = None, **kwargs):
    return build_result(
        fid="range_stat",
        name="Range",
        expression="Max - Min",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
        },
    )

@formula("variance_population", "Population Variance", "Sum((x-mu)^2) / N", DOMAIN_KEY, unit="")
def variance_population(values: float | None = None, **kwargs):
    return build_result(
        fid="variance_population",
        name="Population Variance",
        expression="Sum((x-mu)^2) / N",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
        },
    )

@formula("variance_sample", "Sample Variance", "Sum((x-xbar)^2) / (n-1)", DOMAIN_KEY, unit="")
def variance_sample(values: float | None = None, **kwargs):
    return build_result(
        fid="variance_sample",
        name="Sample Variance",
        expression="Sum((x-xbar)^2) / (n-1)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
        },
    )

@formula("standard_deviation_pop", "Population Std Dev", "sqrt(Population_Variance)", DOMAIN_KEY, unit="")
def standard_deviation_pop(values: float | None = None, **kwargs):
    return build_result(
        fid="standard_deviation_pop",
        name="Population Std Dev",
        expression="sqrt(Population_Variance)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
        },
    )

@formula("standard_deviation_sample", "Sample Std Dev", "sqrt(Sample_Variance)", DOMAIN_KEY, unit="")
def standard_deviation_sample(values: float | None = None, **kwargs):
    return build_result(
        fid="standard_deviation_sample",
        name="Sample Std Dev",
        expression="sqrt(Sample_Variance)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
        },
    )

@formula("coefficient_variation", "Coefficient of Variation", "StdDev / Mean", DOMAIN_KEY, unit="")
def coefficient_variation(values: float | None = None, **kwargs):
    return build_result(
        fid="coefficient_variation",
        name="Coefficient of Variation",
        expression="StdDev / Mean",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
        },
    )

@formula("skewness", "Skewness", "E[(x-mu)^3] / sigma^3", DOMAIN_KEY, unit="")
def skewness(values: float | None = None, **kwargs):
    return build_result(
        fid="skewness",
        name="Skewness",
        expression="E[(x-mu)^3] / sigma^3",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
        },
    )

@formula("kurtosis", "Kurtosis", "E[(x-mu)^4] / sigma^4", DOMAIN_KEY, unit="")
def kurtosis(values: float | None = None, **kwargs):
    return build_result(
        fid="kurtosis",
        name="Kurtosis",
        expression="E[(x-mu)^4] / sigma^4",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
        },
    )

@formula("excess_kurtosis", "Excess Kurtosis", "Kurtosis - 3", DOMAIN_KEY, unit="")
def excess_kurtosis(values: float | None = None, **kwargs):
    return build_result(
        fid="excess_kurtosis",
        name="Excess Kurtosis",
        expression="Kurtosis - 3",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
        },
    )

@formula("covariance_stat", "Covariance", "Sum((x-xbar)(y-ybar))/(n-1)", DOMAIN_KEY, unit="")
def covariance_stat(series_x: float | None = None, series_y: float | None = None, **kwargs):
    return build_result(
        fid="covariance_stat",
        name="Covariance",
        expression="Sum((x-xbar)(y-ybar))/(n-1)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "series_x": kwargs.get("series_x", series_x),
            "series_y": kwargs.get("series_y", series_y),
        },
    )

@formula("pearson_correlation", "Pearson Correlation", "Cov(X,Y)/(SdX*SdY)", DOMAIN_KEY, unit="")
def pearson_correlation(series_x: float | None = None, series_y: float | None = None, **kwargs):
    return build_result(
        fid="pearson_correlation",
        name="Pearson Correlation",
        expression="Cov(X,Y)/(SdX*SdY)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "series_x": kwargs.get("series_x", series_x),
            "series_y": kwargs.get("series_y", series_y),
        },
    )

@formula("spearman_correlation", "Spearman Correlation", "1 - 6*Sum(d^2)/(n(n^2-1))", DOMAIN_KEY, unit="")
def spearman_correlation(series_x: float | None = None, series_y: float | None = None, **kwargs):
    return build_result(
        fid="spearman_correlation",
        name="Spearman Correlation",
        expression="1 - 6*Sum(d^2)/(n(n^2-1))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "series_x": kwargs.get("series_x", series_x),
            "series_y": kwargs.get("series_y", series_y),
        },
    )

@formula("linear_regression_beta", "Regression Slope (Beta)", "Cov(X,Y) / Var(X)", DOMAIN_KEY, unit="")
def linear_regression_beta(series_x: float | None = None, series_y: float | None = None, **kwargs):
    return build_result(
        fid="linear_regression_beta",
        name="Regression Slope (Beta)",
        expression="Cov(X,Y) / Var(X)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "series_x": kwargs.get("series_x", series_x),
            "series_y": kwargs.get("series_y", series_y),
        },
    )

@formula("linear_regression_alpha", "Regression Intercept", "Ybar - Beta*Xbar", DOMAIN_KEY, unit="")
def linear_regression_alpha(series_x: float | None = None, series_y: float | None = None, **kwargs):
    return build_result(
        fid="linear_regression_alpha",
        name="Regression Intercept",
        expression="Ybar - Beta*Xbar",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "series_x": kwargs.get("series_x", series_x),
            "series_y": kwargs.get("series_y", series_y),
        },
    )

@formula("r_squared", "R-Squared", "1 - SSres/SStot", DOMAIN_KEY, unit="")
def r_squared(actual: float | None = None, predicted: float | None = None, **kwargs):
    return build_result(
        fid="r_squared",
        name="R-Squared",
        expression="1 - SSres/SStot",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "actual": kwargs.get("actual", actual),
            "predicted": kwargs.get("predicted", predicted),
        },
    )

@formula("adjusted_r_squared", "Adjusted R-Squared", "1 - (1-R2)(n-1)/(n-k-1)", DOMAIN_KEY, unit="")
def adjusted_r_squared(r_squared: float | None = None, n: float | None = None, predictors: float | None = None, **kwargs):
    return build_result(
        fid="adjusted_r_squared",
        name="Adjusted R-Squared",
        expression="1 - (1-R2)(n-1)/(n-k-1)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "r_squared": kwargs.get("r_squared", r_squared),
            "n": kwargs.get("n", n),
            "predictors": kwargs.get("predictors", predictors),
        },
    )

@formula("standard_error", "Standard Error", "StdDev / sqrt(n)", DOMAIN_KEY, unit="")
def standard_error(values: float | None = None, **kwargs):
    return build_result(
        fid="standard_error",
        name="Standard Error",
        expression="StdDev / sqrt(n)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
        },
    )

@formula("standard_error_regression", "Standard Error of Regression", "sqrt(SSres/(n-2))", DOMAIN_KEY, unit="")
def standard_error_regression(residuals: float | None = None, n: float | None = None, **kwargs):
    return build_result(
        fid="standard_error_regression",
        name="Standard Error of Regression",
        expression="sqrt(SSres/(n-2))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "residuals": kwargs.get("residuals", residuals),
            "n": kwargs.get("n", n),
        },
    )

@formula("t_statistic", "T-Statistic", "(xbar - mu) / (s/sqrt(n))", DOMAIN_KEY, unit="")
def t_statistic(sample_mean: float | None = None, pop_mean: float | None = None, std: float | None = None, n: float | None = None, **kwargs):
    return build_result(
        fid="t_statistic",
        name="T-Statistic",
        expression="(xbar - mu) / (s/sqrt(n))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "sample_mean": kwargs.get("sample_mean", sample_mean),
            "pop_mean": kwargs.get("pop_mean", pop_mean),
            "std": kwargs.get("std", std),
            "n": kwargs.get("n", n),
        },
    )

@formula("z_score", "Z-Score", "(x - mu) / sigma", DOMAIN_KEY, unit="")
def z_score(value: float | None = None, mean: float | None = None, std: float | None = None, **kwargs):
    return build_result(
        fid="z_score",
        name="Z-Score",
        expression="(x - mu) / sigma",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "value": kwargs.get("value", value),
            "mean": kwargs.get("mean", mean),
            "std": kwargs.get("std", std),
        },
    )

@formula("confidence_interval", "Confidence Interval", "mean +/- z*(s/sqrt(n))", DOMAIN_KEY, unit="")
def confidence_interval(mean: float | None = None, std: float | None = None, n: float | None = None, confidence: float | None = None, **kwargs):
    return build_result(
        fid="confidence_interval",
        name="Confidence Interval",
        expression="mean +/- z*(s/sqrt(n))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "mean": kwargs.get("mean", mean),
            "std": kwargs.get("std", std),
            "n": kwargs.get("n", n),
            "confidence": kwargs.get("confidence", confidence),
        },
    )

@formula("chi_square_stat", "Chi-Square Statistic", "Sum((O-E)^2 / E)", DOMAIN_KEY, unit="")
def chi_square_stat(observed: float | None = None, expected: float | None = None, **kwargs):
    return build_result(
        fid="chi_square_stat",
        name="Chi-Square Statistic",
        expression="Sum((O-E)^2 / E)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "observed": kwargs.get("observed", observed),
            "expected": kwargs.get("expected", expected),
        },
    )

@formula("f_statistic", "F-Statistic", "Var1 / Var2", DOMAIN_KEY, unit="")
def f_statistic(variance1: float | None = None, variance2: float | None = None, **kwargs):
    return build_result(
        fid="f_statistic",
        name="F-Statistic",
        expression="Var1 / Var2",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "variance1": kwargs.get("variance1", variance1),
            "variance2": kwargs.get("variance2", variance2),
        },
    )

@formula("percentile", "Percentile", "Interpolated rank value", DOMAIN_KEY, unit="")
def percentile(values: float | None = None, percentile: float | None = None, **kwargs):
    return build_result(
        fid="percentile",
        name="Percentile",
        expression="Interpolated rank value",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
            "percentile": kwargs.get("percentile", percentile),
        },
    )

@formula("quartile", "Quartile", "Percentile at 25/50/75", DOMAIN_KEY, unit="")
def quartile(values: float | None = None, quartile_number: float | None = None, **kwargs):
    return build_result(
        fid="quartile",
        name="Quartile",
        expression="Percentile at 25/50/75",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
            "quartile_number": kwargs.get("quartile_number", quartile_number),
        },
    )

@formula("interquartile_range", "Interquartile Range (IQR)", "Q3 - Q1", DOMAIN_KEY, unit="")
def interquartile_range(values: float | None = None, **kwargs):
    return build_result(
        fid="interquartile_range",
        name="Interquartile Range (IQR)",
        expression="Q3 - Q1",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
        },
    )

@formula("autocorrelation", "Autocorrelation", "Corr(x_t, x_t-k)", DOMAIN_KEY, unit="")
def autocorrelation(series: float | None = None, lag: float | None = None, **kwargs):
    return build_result(
        fid="autocorrelation",
        name="Autocorrelation",
        expression="Corr(x_t, x_t-k)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "series": kwargs.get("series", series),
            "lag": kwargs.get("lag", lag),
        },
    )

@formula("moving_average_forecast", "Moving Average Forecast", "Mean(last n values)", DOMAIN_KEY, unit="")
def moving_average_forecast(values: float | None = None, window: float | None = None, **kwargs):
    return build_result(
        fid="moving_average_forecast",
        name="Moving Average Forecast",
        expression="Mean(last n values)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
            "window": kwargs.get("window", window),
        },
    )

@formula("exponential_smoothing", "Exponential Smoothing", "alpha*x + (1-alpha)*prev", DOMAIN_KEY, unit="")
def exponential_smoothing(values: float | None = None, alpha: float | None = None, **kwargs):
    return build_result(
        fid="exponential_smoothing",
        name="Exponential Smoothing",
        expression="alpha*x + (1-alpha)*prev",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
            "alpha": kwargs.get("alpha", alpha),
        },
    )

@formula("holt_linear_trend", "Holt's Linear Trend", "Level + Trend smoothing", DOMAIN_KEY, unit="")
def holt_linear_trend(values: float | None = None, alpha: float | None = None, beta: float | None = None, **kwargs):
    return build_result(
        fid="holt_linear_trend",
        name="Holt's Linear Trend",
        expression="Level + Trend smoothing",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
            "alpha": kwargs.get("alpha", alpha),
            "beta": kwargs.get("beta", beta),
        },
    )

@formula("holt_winters", "Holt-Winters Seasonal", "Triple exponential smoothing", DOMAIN_KEY, unit="")
def holt_winters(values: float | None = None, alpha: float | None = None, beta: float | None = None, gamma: float | None = None, season_length: float | None = None, **kwargs):
    return build_result(
        fid="holt_winters",
        name="Holt-Winters Seasonal",
        expression="Triple exponential smoothing",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
            "alpha": kwargs.get("alpha", alpha),
            "beta": kwargs.get("beta", beta),
            "gamma": kwargs.get("gamma", gamma),
            "season_length": kwargs.get("season_length", season_length),
        },
    )

@formula("ar1_model", "AR(1) Model", "c + phi*x_prev + error", DOMAIN_KEY, unit="")
def ar1_model(series: float | None = None, phi: float | None = None, constant: float | None = None, **kwargs):
    return build_result(
        fid="ar1_model",
        name="AR(1) Model",
        expression="c + phi*x_prev + error",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "series": kwargs.get("series", series),
            "phi": kwargs.get("phi", phi),
            "constant": kwargs.get("constant", constant),
        },
    )

@formula("durbin_watson", "Durbin-Watson Statistic", "Sum((e_t-e_t-1)^2)/Sum(e_t^2)", DOMAIN_KEY, unit="")
def durbin_watson(residuals: float | None = None, **kwargs):
    return build_result(
        fid="durbin_watson",
        name="Durbin-Watson Statistic",
        expression="Sum((e_t-e_t-1)^2)/Sum(e_t^2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "residuals": kwargs.get("residuals", residuals),
        },
    )

@formula("mean_absolute_error", "Mean Absolute Error", "Mean(|actual - predicted|)", DOMAIN_KEY, unit="")
def mean_absolute_error(actual: float | None = None, predicted: float | None = None, **kwargs):
    return build_result(
        fid="mean_absolute_error",
        name="Mean Absolute Error",
        expression="Mean(|actual - predicted|)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "actual": kwargs.get("actual", actual),
            "predicted": kwargs.get("predicted", predicted),
        },
    )

@formula("mean_squared_error", "Mean Squared Error", "Mean((actual - predicted)^2)", DOMAIN_KEY, unit="")
def mean_squared_error(actual: float | None = None, predicted: float | None = None, **kwargs):
    return build_result(
        fid="mean_squared_error",
        name="Mean Squared Error",
        expression="Mean((actual - predicted)^2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "actual": kwargs.get("actual", actual),
            "predicted": kwargs.get("predicted", predicted),
        },
    )

@formula("rmse", "Root Mean Squared Error", "sqrt(MSE)", DOMAIN_KEY, unit="")
def rmse(actual: float | None = None, predicted: float | None = None, **kwargs):
    return build_result(
        fid="rmse",
        name="Root Mean Squared Error",
        expression="sqrt(MSE)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "actual": kwargs.get("actual", actual),
            "predicted": kwargs.get("predicted", predicted),
        },
    )

@formula("mape", "Mean Absolute Percentage Error", "Mean(|actual-pred|/actual)*100", DOMAIN_KEY, unit="")
def mape(actual: float | None = None, predicted: float | None = None, **kwargs):
    return build_result(
        fid="mape",
        name="Mean Absolute Percentage Error",
        expression="Mean(|actual-pred|/actual)*100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "actual": kwargs.get("actual", actual),
            "predicted": kwargs.get("predicted", predicted),
        },
    )

@formula("theil_u", "Theil's U Statistic", "RMSE / (RMSE_actual + RMSE_pred)", DOMAIN_KEY, unit="")
def theil_u(actual: float | None = None, predicted: float | None = None, **kwargs):
    return build_result(
        fid="theil_u",
        name="Theil's U Statistic",
        expression="RMSE / (RMSE_actual + RMSE_pred)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "actual": kwargs.get("actual", actual),
            "predicted": kwargs.get("predicted", predicted),
        },
    )

@formula("garch_volatility", "GARCH(1,1) Volatility", "omega + alpha*r^2 + beta*var_prev", DOMAIN_KEY, unit="")
def garch_volatility(returns: float | None = None, omega: float | None = None, alpha: float | None = None, beta: float | None = None, **kwargs):
    return build_result(
        fid="garch_volatility",
        name="GARCH(1,1) Volatility",
        expression="omega + alpha*r^2 + beta*var_prev",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "returns": kwargs.get("returns", returns),
            "omega": kwargs.get("omega", omega),
            "alpha": kwargs.get("alpha", alpha),
            "beta": kwargs.get("beta", beta),
        },
    )
