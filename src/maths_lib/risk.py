from .base import build_result, formula

DOMAIN_KEY = "D07_risk"
DOMAIN_TITLE = "Risk Management & Portfolio Theory"
FORMULA_IDS = [
    "var_historical",
    "var_parametric",
    "var_monte_carlo",
    "cvar",
    "expected_shortfall",
    "sharpe_ratio",
    "sortino_ratio",
    "treynor_ratio",
    "information_ratio",
    "jensens_alpha",
    "calmar_ratio",
    "sterling_ratio",
    "max_drawdown",
    "drawdown_duration",
    "beta",
    "alpha",
    "tracking_error",
    "downside_deviation",
    "semi_variance",
    "covariance",
    "correlation",
    "portfolio_return",
    "portfolio_variance",
    "portfolio_std",
    "portfolio_beta",
    "minimum_variance_weight",
    "efficient_frontier_return",
    "capital_allocation_line",
    "capital_market_line",
    "security_market_line",
    "diversification_ratio",
    "risk_parity_weight",
    "marginal_var",
    "component_var",
    "incremental_var",
    "ulcer_index",
    "gain_to_pain",
    "omega_ratio",
    "kappa_ratio",
    "upside_potential_ratio",
    "value_at_risk_normal",
    "conditional_drawdown",
    "pain_index",
    "burke_ratio",
    "m2_measure",
    "active_premium",
    "hurst_exponent",
    "kelly_criterion",
    "risk_of_ruin",
    "expected_value",
]

@formula("var_historical", "VaR (Historical)", "Percentile(Returns, 1-conf)", DOMAIN_KEY, unit="")
def var_historical(returns: float | None = None, confidence: float | None = None, **kwargs):
    return build_result(
        fid="var_historical",
        name="VaR (Historical)",
        expression="Percentile(Returns, 1-conf)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "returns": kwargs.get("returns", returns),
            "confidence": kwargs.get("confidence", confidence),
        },
    )

@formula("var_parametric", "VaR (Parametric)", "-(mu + z*sigma)*Value", DOMAIN_KEY, unit="")
def var_parametric(mean: float | None = None, std: float | None = None, confidence: float | None = None, value: float | None = None, **kwargs):
    return build_result(
        fid="var_parametric",
        name="VaR (Parametric)",
        expression="-(mu + z*sigma)*Value",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "mean": kwargs.get("mean", mean),
            "std": kwargs.get("std", std),
            "confidence": kwargs.get("confidence", confidence),
            "value": kwargs.get("value", value),
        },
    )

@formula("var_monte_carlo", "VaR (Monte Carlo)", "Percentile of simulated P&L", DOMAIN_KEY, unit="")
def var_monte_carlo(returns: float | None = None, confidence: float | None = None, simulations: float | None = None, **kwargs):
    return build_result(
        fid="var_monte_carlo",
        name="VaR (Monte Carlo)",
        expression="Percentile of simulated P&L",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "returns": kwargs.get("returns", returns),
            "confidence": kwargs.get("confidence", confidence),
            "simulations": kwargs.get("simulations", simulations),
        },
    )

@formula("cvar", "Conditional VaR (ES)", "Mean(Losses > VaR)", DOMAIN_KEY, unit="")
def cvar(returns: float | None = None, confidence: float | None = None, **kwargs):
    return build_result(
        fid="cvar",
        name="Conditional VaR (ES)",
        expression="Mean(Losses > VaR)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "returns": kwargs.get("returns", returns),
            "confidence": kwargs.get("confidence", confidence),
        },
    )

@formula("expected_shortfall", "Expected Shortfall", "Mean(Returns below VaR)", DOMAIN_KEY, unit="")
def expected_shortfall(returns: float | None = None, confidence: float | None = None, **kwargs):
    return build_result(
        fid="expected_shortfall",
        name="Expected Shortfall",
        expression="Mean(Returns below VaR)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "returns": kwargs.get("returns", returns),
            "confidence": kwargs.get("confidence", confidence),
        },
    )

@formula("sharpe_ratio", "Sharpe Ratio", "(Return - Rf) / StdDev", DOMAIN_KEY, unit="")
def sharpe_ratio(returns: float | None = None, risk_free: float | None = None, std: float | None = None, **kwargs):
    return build_result(
        fid="sharpe_ratio",
        name="Sharpe Ratio",
        expression="(Return - Rf) / StdDev",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "returns": kwargs.get("returns", returns),
            "risk_free": kwargs.get("risk_free", risk_free),
            "std": kwargs.get("std", std),
        },
    )

@formula("sortino_ratio", "Sortino Ratio", "(Return - Rf) / Downside_Dev", DOMAIN_KEY, unit="")
def sortino_ratio(returns: float | None = None, risk_free: float | None = None, downside_deviation: float | None = None, **kwargs):
    return build_result(
        fid="sortino_ratio",
        name="Sortino Ratio",
        expression="(Return - Rf) / Downside_Dev",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "returns": kwargs.get("returns", returns),
            "risk_free": kwargs.get("risk_free", risk_free),
            "downside_deviation": kwargs.get("downside_deviation", downside_deviation),
        },
    )

@formula("treynor_ratio", "Treynor Ratio", "(Return - Rf) / Beta", DOMAIN_KEY, unit="")
def treynor_ratio(returns: float | None = None, risk_free: float | None = None, beta: float | None = None, **kwargs):
    return build_result(
        fid="treynor_ratio",
        name="Treynor Ratio",
        expression="(Return - Rf) / Beta",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "returns": kwargs.get("returns", returns),
            "risk_free": kwargs.get("risk_free", risk_free),
            "beta": kwargs.get("beta", beta),
        },
    )

@formula("information_ratio", "Information Ratio", "(Return - Benchmark) / Tracking_Error", DOMAIN_KEY, unit="")
def information_ratio(returns: float | None = None, benchmark: float | None = None, tracking_error: float | None = None, **kwargs):
    return build_result(
        fid="information_ratio",
        name="Information Ratio",
        expression="(Return - Benchmark) / Tracking_Error",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "returns": kwargs.get("returns", returns),
            "benchmark": kwargs.get("benchmark", benchmark),
            "tracking_error": kwargs.get("tracking_error", tracking_error),
        },
    )

@formula("jensens_alpha", "Jensen's Alpha", "Return - (Rf + Beta*(Rm-Rf))", DOMAIN_KEY, unit="")
def jensens_alpha(returns: float | None = None, risk_free: float | None = None, beta: float | None = None, market_return: float | None = None, **kwargs):
    return build_result(
        fid="jensens_alpha",
        name="Jensen's Alpha",
        expression="Return - (Rf + Beta*(Rm-Rf))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "returns": kwargs.get("returns", returns),
            "risk_free": kwargs.get("risk_free", risk_free),
            "beta": kwargs.get("beta", beta),
            "market_return": kwargs.get("market_return", market_return),
        },
    )

@formula("calmar_ratio", "Calmar Ratio", "Annual_Return / Max_Drawdown", DOMAIN_KEY, unit="")
def calmar_ratio(annual_return: float | None = None, max_drawdown: float | None = None, **kwargs):
    return build_result(
        fid="calmar_ratio",
        name="Calmar Ratio",
        expression="Annual_Return / Max_Drawdown",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "annual_return": kwargs.get("annual_return", annual_return),
            "max_drawdown": kwargs.get("max_drawdown", max_drawdown),
        },
    )

@formula("sterling_ratio", "Sterling Ratio", "Annual_Return / Avg_Drawdown", DOMAIN_KEY, unit="")
def sterling_ratio(annual_return: float | None = None, avg_drawdown: float | None = None, **kwargs):
    return build_result(
        fid="sterling_ratio",
        name="Sterling Ratio",
        expression="Annual_Return / Avg_Drawdown",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "annual_return": kwargs.get("annual_return", annual_return),
            "avg_drawdown": kwargs.get("avg_drawdown", avg_drawdown),
        },
    )

@formula("max_drawdown", "Maximum Drawdown %", "(Trough - Peak) / Peak * 100", DOMAIN_KEY, unit="")
def max_drawdown(prices: float | None = None, **kwargs):
    return build_result(
        fid="max_drawdown",
        name="Maximum Drawdown %",
        expression="(Trough - Peak) / Peak * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
        },
    )

@formula("drawdown_duration", "Drawdown Duration", "Periods from peak to recovery", DOMAIN_KEY, unit="")
def drawdown_duration(prices: float | None = None, **kwargs):
    return build_result(
        fid="drawdown_duration",
        name="Drawdown Duration",
        expression="Periods from peak to recovery",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
        },
    )

@formula("beta", "Beta", "Cov(Stock,Market) / Var(Market)", DOMAIN_KEY, unit="")
def beta(stock_returns: float | None = None, market_returns: float | None = None, **kwargs):
    return build_result(
        fid="beta",
        name="Beta",
        expression="Cov(Stock,Market) / Var(Market)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "stock_returns": kwargs.get("stock_returns", stock_returns),
            "market_returns": kwargs.get("market_returns", market_returns),
        },
    )

@formula("alpha", "Alpha", "Return - Benchmark_Return", DOMAIN_KEY, unit="")
def alpha(returns: float | None = None, benchmark_return: float | None = None, **kwargs):
    return build_result(
        fid="alpha",
        name="Alpha",
        expression="Return - Benchmark_Return",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "returns": kwargs.get("returns", returns),
            "benchmark_return": kwargs.get("benchmark_return", benchmark_return),
        },
    )

@formula("tracking_error", "Tracking Error", "StdDev(Portfolio - Benchmark)", DOMAIN_KEY, unit="")
def tracking_error(portfolio_returns: float | None = None, benchmark_returns: float | None = None, **kwargs):
    return build_result(
        fid="tracking_error",
        name="Tracking Error",
        expression="StdDev(Portfolio - Benchmark)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "portfolio_returns": kwargs.get("portfolio_returns", portfolio_returns),
            "benchmark_returns": kwargs.get("benchmark_returns", benchmark_returns),
        },
    )

@formula("downside_deviation", "Downside Deviation", "sqrt(Mean(min(0, R-MAR)^2))", DOMAIN_KEY, unit="")
def downside_deviation(returns: float | None = None, min_acceptable_return: float | None = None, **kwargs):
    return build_result(
        fid="downside_deviation",
        name="Downside Deviation",
        expression="sqrt(Mean(min(0, R-MAR)^2))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "returns": kwargs.get("returns", returns),
            "min_acceptable_return": kwargs.get("min_acceptable_return", min_acceptable_return),
        },
    )

@formula("semi_variance", "Semi-Variance", "Mean((min(0, R-mean))^2)", DOMAIN_KEY, unit="")
def semi_variance(returns: float | None = None, **kwargs):
    return build_result(
        fid="semi_variance",
        name="Semi-Variance",
        expression="Mean((min(0, R-mean))^2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "returns": kwargs.get("returns", returns),
        },
    )

@formula("covariance", "Covariance", "Mean((X-Xbar)(Y-Ybar))", DOMAIN_KEY, unit="")
def covariance(series_x: float | None = None, series_y: float | None = None, **kwargs):
    return build_result(
        fid="covariance",
        name="Covariance",
        expression="Mean((X-Xbar)(Y-Ybar))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "series_x": kwargs.get("series_x", series_x),
            "series_y": kwargs.get("series_y", series_y),
        },
    )

@formula("correlation", "Correlation", "Cov(X,Y) / (StdX*StdY)", DOMAIN_KEY, unit="")
def correlation(series_x: float | None = None, series_y: float | None = None, **kwargs):
    return build_result(
        fid="correlation",
        name="Correlation",
        expression="Cov(X,Y) / (StdX*StdY)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "series_x": kwargs.get("series_x", series_x),
            "series_y": kwargs.get("series_y", series_y),
        },
    )

@formula("portfolio_return", "Portfolio Return", "Sum(Weight_i * Return_i)", DOMAIN_KEY, unit="")
def portfolio_return(weights: float | None = None, returns: float | None = None, **kwargs):
    return build_result(
        fid="portfolio_return",
        name="Portfolio Return",
        expression="Sum(Weight_i * Return_i)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "weights": kwargs.get("weights", weights),
            "returns": kwargs.get("returns", returns),
        },
    )

@formula("portfolio_variance", "Portfolio Variance", "w1^2*v1 + w2^2*v2 + 2*w1*w2*cov", DOMAIN_KEY, unit="")
def portfolio_variance(weights: float | None = None, variances: float | None = None, covariance: float | None = None, **kwargs):
    return build_result(
        fid="portfolio_variance",
        name="Portfolio Variance",
        expression="w1^2*v1 + w2^2*v2 + 2*w1*w2*cov",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "weights": kwargs.get("weights", weights),
            "variances": kwargs.get("variances", variances),
            "covariance": kwargs.get("covariance", covariance),
        },
    )

@formula("portfolio_std", "Portfolio Std Dev", "sqrt(Portfolio_Variance)", DOMAIN_KEY, unit="")
def portfolio_std(portfolio_variance: float | None = None, **kwargs):
    return build_result(
        fid="portfolio_std",
        name="Portfolio Std Dev",
        expression="sqrt(Portfolio_Variance)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "portfolio_variance": kwargs.get("portfolio_variance", portfolio_variance),
        },
    )

@formula("portfolio_beta", "Portfolio Beta", "Sum(Weight_i * Beta_i)", DOMAIN_KEY, unit="")
def portfolio_beta(weights: float | None = None, betas: float | None = None, **kwargs):
    return build_result(
        fid="portfolio_beta",
        name="Portfolio Beta",
        expression="Sum(Weight_i * Beta_i)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "weights": kwargs.get("weights", weights),
            "betas": kwargs.get("betas", betas),
        },
    )

@formula("minimum_variance_weight", "Min Variance Weight", "(v2-cov)/(v1+v2-2*cov)", DOMAIN_KEY, unit="")
def minimum_variance_weight(variance1: float | None = None, variance2: float | None = None, covariance: float | None = None, **kwargs):
    return build_result(
        fid="minimum_variance_weight",
        name="Min Variance Weight",
        expression="(v2-cov)/(v1+v2-2*cov)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "variance1": kwargs.get("variance1", variance1),
            "variance2": kwargs.get("variance2", variance2),
            "covariance": kwargs.get("covariance", covariance),
        },
    )

@formula("efficient_frontier_return", "Efficient Frontier Return", "Quadratic optimization", DOMAIN_KEY, unit="")
def efficient_frontier_return(returns: float | None = None, covariance_matrix: float | None = None, target_risk: float | None = None, **kwargs):
    return build_result(
        fid="efficient_frontier_return",
        name="Efficient Frontier Return",
        expression="Quadratic optimization",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "returns": kwargs.get("returns", returns),
            "covariance_matrix": kwargs.get("covariance_matrix", covariance_matrix),
            "target_risk": kwargs.get("target_risk", target_risk),
        },
    )

@formula("capital_allocation_line", "Capital Allocation Line", "Rf + Sharpe * Sigma", DOMAIN_KEY, unit="")
def capital_allocation_line(risk_free: float | None = None, sharpe: float | None = None, sigma: float | None = None, **kwargs):
    return build_result(
        fid="capital_allocation_line",
        name="Capital Allocation Line",
        expression="Rf + Sharpe * Sigma",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "risk_free": kwargs.get("risk_free", risk_free),
            "sharpe": kwargs.get("sharpe", sharpe),
            "sigma": kwargs.get("sigma", sigma),
        },
    )

@formula("capital_market_line", "Capital Market Line", "Rf + ((Rm-Rf)/SigmaM)*Sigma", DOMAIN_KEY, unit="")
def capital_market_line(risk_free: float | None = None, market_return: float | None = None, market_std: float | None = None, portfolio_std: float | None = None, **kwargs):
    return build_result(
        fid="capital_market_line",
        name="Capital Market Line",
        expression="Rf + ((Rm-Rf)/SigmaM)*Sigma",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "risk_free": kwargs.get("risk_free", risk_free),
            "market_return": kwargs.get("market_return", market_return),
            "market_std": kwargs.get("market_std", market_std),
            "portfolio_std": kwargs.get("portfolio_std", portfolio_std),
        },
    )

@formula("security_market_line", "Security Market Line", "Rf + Beta*(Rm - Rf)", DOMAIN_KEY, unit="")
def security_market_line(risk_free: float | None = None, beta: float | None = None, market_return: float | None = None, **kwargs):
    return build_result(
        fid="security_market_line",
        name="Security Market Line",
        expression="Rf + Beta*(Rm - Rf)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "risk_free": kwargs.get("risk_free", risk_free),
            "beta": kwargs.get("beta", beta),
            "market_return": kwargs.get("market_return", market_return),
        },
    )

@formula("diversification_ratio", "Diversification Ratio", "Sum(w*sigma) / Portfolio_Sigma", DOMAIN_KEY, unit="")
def diversification_ratio(weights: float | None = None, volatilities: float | None = None, portfolio_std: float | None = None, **kwargs):
    return build_result(
        fid="diversification_ratio",
        name="Diversification Ratio",
        expression="Sum(w*sigma) / Portfolio_Sigma",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "weights": kwargs.get("weights", weights),
            "volatilities": kwargs.get("volatilities", volatilities),
            "portfolio_std": kwargs.get("portfolio_std", portfolio_std),
        },
    )

@formula("risk_parity_weight", "Risk Parity Weight", "Inverse vol weighting", DOMAIN_KEY, unit="")
def risk_parity_weight(volatilities: float | None = None, **kwargs):
    return build_result(
        fid="risk_parity_weight",
        name="Risk Parity Weight",
        expression="Inverse vol weighting",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "volatilities": kwargs.get("volatilities", volatilities),
        },
    )

@formula("marginal_var", "Marginal VaR", "d(VaR)/d(weight)", DOMAIN_KEY, unit="")
def marginal_var(weights: float | None = None, covariance_matrix: float | None = None, position: float | None = None, **kwargs):
    return build_result(
        fid="marginal_var",
        name="Marginal VaR",
        expression="d(VaR)/d(weight)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "weights": kwargs.get("weights", weights),
            "covariance_matrix": kwargs.get("covariance_matrix", covariance_matrix),
            "position": kwargs.get("position", position),
        },
    )

@formula("component_var", "Component VaR", "Marginal_VaR * Position", DOMAIN_KEY, unit="")
def component_var(marginal_var: float | None = None, position_value: float | None = None, **kwargs):
    return build_result(
        fid="component_var",
        name="Component VaR",
        expression="Marginal_VaR * Position",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "marginal_var": kwargs.get("marginal_var", marginal_var),
            "position_value": kwargs.get("position_value", position_value),
        },
    )

@formula("incremental_var", "Incremental VaR", "VaR_with - VaR_without", DOMAIN_KEY, unit="")
def incremental_var(var_with: float | None = None, var_without: float | None = None, **kwargs):
    return build_result(
        fid="incremental_var",
        name="Incremental VaR",
        expression="VaR_with - VaR_without",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "var_with": kwargs.get("var_with", var_with),
            "var_without": kwargs.get("var_without", var_without),
        },
    )

@formula("ulcer_index", "Ulcer Index", "sqrt(Mean(Drawdown^2))", DOMAIN_KEY, unit="")
def ulcer_index(prices: float | None = None, **kwargs):
    return build_result(
        fid="ulcer_index",
        name="Ulcer Index",
        expression="sqrt(Mean(Drawdown^2))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
        },
    )

@formula("gain_to_pain", "Gain to Pain Ratio", "Sum(Returns) / abs(Sum(Losses))", DOMAIN_KEY, unit="")
def gain_to_pain(returns: float | None = None, **kwargs):
    return build_result(
        fid="gain_to_pain",
        name="Gain to Pain Ratio",
        expression="Sum(Returns) / abs(Sum(Losses))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "returns": kwargs.get("returns", returns),
        },
    )

@formula("omega_ratio", "Omega Ratio", "Sum(Gains) / Sum(Losses) above threshold", DOMAIN_KEY, unit="")
def omega_ratio(returns: float | None = None, threshold: float | None = None, **kwargs):
    return build_result(
        fid="omega_ratio",
        name="Omega Ratio",
        expression="Sum(Gains) / Sum(Losses) above threshold",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "returns": kwargs.get("returns", returns),
            "threshold": kwargs.get("threshold", threshold),
        },
    )

@formula("kappa_ratio", "Kappa Ratio", "(Return - MAR) / LPM^(1/n)", DOMAIN_KEY, unit="")
def kappa_ratio(returns: float | None = None, min_acceptable_return: float | None = None, order: float | None = None, **kwargs):
    return build_result(
        fid="kappa_ratio",
        name="Kappa Ratio",
        expression="(Return - MAR) / LPM^(1/n)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "returns": kwargs.get("returns", returns),
            "min_acceptable_return": kwargs.get("min_acceptable_return", min_acceptable_return),
            "order": kwargs.get("order", order),
        },
    )

@formula("upside_potential_ratio", "Upside Potential Ratio", "Upside / Downside_Deviation", DOMAIN_KEY, unit="")
def upside_potential_ratio(returns: float | None = None, min_acceptable_return: float | None = None, **kwargs):
    return build_result(
        fid="upside_potential_ratio",
        name="Upside Potential Ratio",
        expression="Upside / Downside_Deviation",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "returns": kwargs.get("returns", returns),
            "min_acceptable_return": kwargs.get("min_acceptable_return", min_acceptable_return),
        },
    )

@formula("value_at_risk_normal", "Parametric VaR (Normal)", "Value * z * sigma * sqrt(t)", DOMAIN_KEY, unit="")
def value_at_risk_normal(value: float | None = None, confidence: float | None = None, sigma: float | None = None, time: float | None = None, **kwargs):
    return build_result(
        fid="value_at_risk_normal",
        name="Parametric VaR (Normal)",
        expression="Value * z * sigma * sqrt(t)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "value": kwargs.get("value", value),
            "confidence": kwargs.get("confidence", confidence),
            "sigma": kwargs.get("sigma", sigma),
            "time": kwargs.get("time", time),
        },
    )

@formula("conditional_drawdown", "Conditional Drawdown at Risk", "Mean of worst drawdowns", DOMAIN_KEY, unit="")
def conditional_drawdown(prices: float | None = None, confidence: float | None = None, **kwargs):
    return build_result(
        fid="conditional_drawdown",
        name="Conditional Drawdown at Risk",
        expression="Mean of worst drawdowns",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "confidence": kwargs.get("confidence", confidence),
        },
    )

@formula("pain_index", "Pain Index", "Mean(Drawdowns)", DOMAIN_KEY, unit="")
def pain_index(prices: float | None = None, **kwargs):
    return build_result(
        fid="pain_index",
        name="Pain Index",
        expression="Mean(Drawdowns)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
        },
    )

@formula("burke_ratio", "Burke Ratio", "Return / sqrt(Sum(DD^2))", DOMAIN_KEY, unit="")
def burke_ratio(returns: float | None = None, drawdowns: float | None = None, **kwargs):
    return build_result(
        fid="burke_ratio",
        name="Burke Ratio",
        expression="Return / sqrt(Sum(DD^2))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "returns": kwargs.get("returns", returns),
            "drawdowns": kwargs.get("drawdowns", drawdowns),
        },
    )

@formula("m2_measure", "M-Squared (M2)", "Rf + Sharpe * Market_Std", DOMAIN_KEY, unit="")
def m2_measure(sharpe: float | None = None, market_std: float | None = None, risk_free: float | None = None, **kwargs):
    return build_result(
        fid="m2_measure",
        name="M-Squared (M2)",
        expression="Rf + Sharpe * Market_Std",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "sharpe": kwargs.get("sharpe", sharpe),
            "market_std": kwargs.get("market_std", market_std),
            "risk_free": kwargs.get("risk_free", risk_free),
        },
    )

@formula("active_premium", "Active Premium", "Annual_Return - Benchmark_Return", DOMAIN_KEY, unit="")
def active_premium(annual_return: float | None = None, benchmark_return: float | None = None, **kwargs):
    return build_result(
        fid="active_premium",
        name="Active Premium",
        expression="Annual_Return - Benchmark_Return",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "annual_return": kwargs.get("annual_return", annual_return),
            "benchmark_return": kwargs.get("benchmark_return", benchmark_return),
        },
    )

@formula("hurst_exponent", "Hurst Exponent", "Rescaled range analysis", DOMAIN_KEY, unit="")
def hurst_exponent(prices: float | None = None, **kwargs):
    return build_result(
        fid="hurst_exponent",
        name="Hurst Exponent",
        expression="Rescaled range analysis",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
        },
    )

@formula("kelly_criterion", "Kelly Criterion", "(p*b - q) / b", DOMAIN_KEY, unit="")
def kelly_criterion(win_prob: float | None = None, win_loss_ratio: float | None = None, **kwargs):
    return build_result(
        fid="kelly_criterion",
        name="Kelly Criterion",
        expression="(p*b - q) / b",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "win_prob": kwargs.get("win_prob", win_prob),
            "win_loss_ratio": kwargs.get("win_loss_ratio", win_loss_ratio),
        },
    )

@formula("risk_of_ruin", "Risk of Ruin", "((1-edge)/(1+edge))^units", DOMAIN_KEY, unit="")
def risk_of_ruin(edge: float | None = None, capital_units: float | None = None, **kwargs):
    return build_result(
        fid="risk_of_ruin",
        name="Risk of Ruin",
        expression="((1-edge)/(1+edge))^units",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "edge": kwargs.get("edge", edge),
            "capital_units": kwargs.get("capital_units", capital_units),
        },
    )

@formula("expected_value", "Expected Value", "Sum(Probability_i * Outcome_i)", DOMAIN_KEY, unit="")
def expected_value(probabilities: float | None = None, outcomes: float | None = None, **kwargs):
    return build_result(
        fid="expected_value",
        name="Expected Value",
        expression="Sum(Probability_i * Outcome_i)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "probabilities": kwargs.get("probabilities", probabilities),
            "outcomes": kwargs.get("outcomes", outcomes),
        },
    )
