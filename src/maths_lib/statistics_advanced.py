from .base import build_result, formula

DOMAIN_KEY = "D16_statistics_advanced"
DOMAIN_TITLE = "Advanced Statistics & Hypothesis Testing"
FORMULA_IDS = [
    "t_test_one_sample",
    "t_test_two_sample",
    "paired_t_test",
    "welch_t_test",
    "z_test_proportion",
    "z_test_mean",
    "anova_f_statistic",
    "chi2_independence",
    "chi2_goodness_of_fit",
    "mann_whitney_u",
    "wilcoxon_signed_rank",
    "kruskal_wallis_h",
    "levene_test",
    "f_test_variance",
    "cohens_d",
    "hedges_g",
    "eta_squared",
    "odds_ratio",
    "relative_risk",
    "confidence_interval_mean",
    "confidence_interval_proportion",
    "margin_of_error",
    "prediction_interval",
    "p_value_from_z",
    "logistic_regression_prob",
    "multiple_regression_predict",
    "ridge_penalty_cost",
    "vif",
    "partial_correlation",
    "durbin_watson_test",
    "standardized_residual",
    "leverage_hat",
    "cooks_distance",
    "sample_size_mean",
    "sample_size_proportion",
    "standard_error_proportion",
    "finite_population_correction",
    "bootstrap_std_error",
    "pooled_variance",
    "spearman_rank",
    "kendall_tau_b",
    "point_biserial",
    "shapiro_wilk_stat",
    "kolmogorov_smirnov",
    "jarque_bera",
    "bonferroni_correction",
    "benjamini_hochberg",
    "tukey_hsd",
    "power_analysis",
    "kaplan_meier",
    "gini_coefficient_stat",
    "theil_index",
    "cohens_kappa_stat",
]

@formula("t_test_one_sample", "One-Sample t-Test", "(xbar - mu) / (s/sqrt(n))", DOMAIN_KEY, unit="")
def t_test_one_sample(sample_mean: float | None = None, pop_mean: float | None = None, std: float | None = None, n: float | None = None, **kwargs):
    return build_result(
        fid="t_test_one_sample",
        name="One-Sample t-Test",
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

@formula("t_test_two_sample", "Two-Sample t-Test", "(x1-x2)/sqrt(s1^2/n1 + s2^2/n2)", DOMAIN_KEY, unit="")
def t_test_two_sample(mean1: float | None = None, mean2: float | None = None, std1: float | None = None, std2: float | None = None, n1: float | None = None, n2: float | None = None, **kwargs):
    return build_result(
        fid="t_test_two_sample",
        name="Two-Sample t-Test",
        expression="(x1-x2)/sqrt(s1^2/n1 + s2^2/n2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "mean1": kwargs.get("mean1", mean1),
            "mean2": kwargs.get("mean2", mean2),
            "std1": kwargs.get("std1", std1),
            "std2": kwargs.get("std2", std2),
            "n1": kwargs.get("n1", n1),
            "n2": kwargs.get("n2", n2),
        },
    )

@formula("paired_t_test", "Paired t-Test", "dbar / (sd/sqrt(n))", DOMAIN_KEY, unit="")
def paired_t_test(mean_diff: float | None = None, std_diff: float | None = None, n: float | None = None, **kwargs):
    return build_result(
        fid="paired_t_test",
        name="Paired t-Test",
        expression="dbar / (sd/sqrt(n))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "mean_diff": kwargs.get("mean_diff", mean_diff),
            "std_diff": kwargs.get("std_diff", std_diff),
            "n": kwargs.get("n", n),
        },
    )

@formula("welch_t_test", "Welch's t-Test", "(x1-x2)/sqrt(s1^2/n1 + s2^2/n2)", DOMAIN_KEY, unit="")
def welch_t_test(mean1: float | None = None, mean2: float | None = None, var1: float | None = None, var2: float | None = None, n1: float | None = None, n2: float | None = None, **kwargs):
    return build_result(
        fid="welch_t_test",
        name="Welch's t-Test",
        expression="(x1-x2)/sqrt(s1^2/n1 + s2^2/n2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "mean1": kwargs.get("mean1", mean1),
            "mean2": kwargs.get("mean2", mean2),
            "var1": kwargs.get("var1", var1),
            "var2": kwargs.get("var2", var2),
            "n1": kwargs.get("n1", n1),
            "n2": kwargs.get("n2", n2),
        },
    )

@formula("z_test_proportion", "Z-Test for Proportion", "(phat - p0)/sqrt(p0(1-p0)/n)", DOMAIN_KEY, unit="")
def z_test_proportion(sample_prop: float | None = None, pop_prop: float | None = None, n: float | None = None, **kwargs):
    return build_result(
        fid="z_test_proportion",
        name="Z-Test for Proportion",
        expression="(phat - p0)/sqrt(p0(1-p0)/n)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "sample_prop": kwargs.get("sample_prop", sample_prop),
            "pop_prop": kwargs.get("pop_prop", pop_prop),
            "n": kwargs.get("n", n),
        },
    )

@formula("z_test_mean", "Z-Test for Mean", "(xbar - mu)/(sigma/sqrt(n))", DOMAIN_KEY, unit="")
def z_test_mean(sample_mean: float | None = None, pop_mean: float | None = None, sigma: float | None = None, n: float | None = None, **kwargs):
    return build_result(
        fid="z_test_mean",
        name="Z-Test for Mean",
        expression="(xbar - mu)/(sigma/sqrt(n))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "sample_mean": kwargs.get("sample_mean", sample_mean),
            "pop_mean": kwargs.get("pop_mean", pop_mean),
            "sigma": kwargs.get("sigma", sigma),
            "n": kwargs.get("n", n),
        },
    )

@formula("anova_f_statistic", "ANOVA F-Statistic", "MSB / MSW", DOMAIN_KEY, unit="")
def anova_f_statistic(between_group_var: float | None = None, within_group_var: float | None = None, **kwargs):
    return build_result(
        fid="anova_f_statistic",
        name="ANOVA F-Statistic",
        expression="MSB / MSW",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "between_group_var": kwargs.get("between_group_var", between_group_var),
            "within_group_var": kwargs.get("within_group_var", within_group_var),
        },
    )

@formula("chi2_independence", "Chi-Square Independence", "Sum((O-E)^2/E)", DOMAIN_KEY, unit="")
def chi2_independence(observed: float | None = None, expected: float | None = None, **kwargs):
    return build_result(
        fid="chi2_independence",
        name="Chi-Square Independence",
        expression="Sum((O-E)^2/E)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "observed": kwargs.get("observed", observed),
            "expected": kwargs.get("expected", expected),
        },
    )

@formula("chi2_goodness_of_fit", "Chi-Square Goodness of Fit", "Sum((O-E)^2/E)", DOMAIN_KEY, unit="")
def chi2_goodness_of_fit(observed: float | None = None, expected: float | None = None, **kwargs):
    return build_result(
        fid="chi2_goodness_of_fit",
        name="Chi-Square Goodness of Fit",
        expression="Sum((O-E)^2/E)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "observed": kwargs.get("observed", observed),
            "expected": kwargs.get("expected", expected),
        },
    )

@formula("mann_whitney_u", "Mann-Whitney U", "U = R1 - n1(n1+1)/2", DOMAIN_KEY, unit="")
def mann_whitney_u(ranks: float | None = None, n1: float | None = None, n2: float | None = None, **kwargs):
    return build_result(
        fid="mann_whitney_u",
        name="Mann-Whitney U",
        expression="U = R1 - n1(n1+1)/2",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ranks": kwargs.get("ranks", ranks),
            "n1": kwargs.get("n1", n1),
            "n2": kwargs.get("n2", n2),
        },
    )

@formula("wilcoxon_signed_rank", "Wilcoxon Signed-Rank", "Sum of signed ranks", DOMAIN_KEY, unit="")
def wilcoxon_signed_rank(differences: float | None = None, **kwargs):
    return build_result(
        fid="wilcoxon_signed_rank",
        name="Wilcoxon Signed-Rank",
        expression="Sum of signed ranks",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "differences": kwargs.get("differences", differences),
        },
    )

@formula("kruskal_wallis_h", "Kruskal-Wallis H", "12/(N(N+1))*Sum(Ri^2/ni) - 3(N+1)", DOMAIN_KEY, unit="")
def kruskal_wallis_h(rank_sums: float | None = None, group_sizes: float | None = None, n_total: float | None = None, **kwargs):
    return build_result(
        fid="kruskal_wallis_h",
        name="Kruskal-Wallis H",
        expression="12/(N(N+1))*Sum(Ri^2/ni) - 3(N+1)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "rank_sums": kwargs.get("rank_sums", rank_sums),
            "group_sizes": kwargs.get("group_sizes", group_sizes),
            "n_total": kwargs.get("n_total", n_total),
        },
    )

@formula("levene_test", "Levene's Test", "F-stat on abs deviations", DOMAIN_KEY, unit="")
def levene_test(groups: float | None = None, **kwargs):
    return build_result(
        fid="levene_test",
        name="Levene's Test",
        expression="F-stat on abs deviations",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "groups": kwargs.get("groups", groups),
        },
    )

@formula("f_test_variance", "F-Test for Variances", "s1^2 / s2^2", DOMAIN_KEY, unit="")
def f_test_variance(variance1: float | None = None, variance2: float | None = None, **kwargs):
    return build_result(
        fid="f_test_variance",
        name="F-Test for Variances",
        expression="s1^2 / s2^2",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "variance1": kwargs.get("variance1", variance1),
            "variance2": kwargs.get("variance2", variance2),
        },
    )

@formula("cohens_d", "Cohen's d", "(mean1 - mean2) / pooled_std", DOMAIN_KEY, unit="")
def cohens_d(mean1: float | None = None, mean2: float | None = None, pooled_std: float | None = None, **kwargs):
    return build_result(
        fid="cohens_d",
        name="Cohen's d",
        expression="(mean1 - mean2) / pooled_std",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "mean1": kwargs.get("mean1", mean1),
            "mean2": kwargs.get("mean2", mean2),
            "pooled_std": kwargs.get("pooled_std", pooled_std),
        },
    )

@formula("hedges_g", "Hedges' g", "Cohens_d * (1 - 3/(4df-1))", DOMAIN_KEY, unit="")
def hedges_g(cohens_d: float | None = None, degrees_freedom: float | None = None, **kwargs):
    return build_result(
        fid="hedges_g",
        name="Hedges' g",
        expression="Cohens_d * (1 - 3/(4df-1))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cohens_d": kwargs.get("cohens_d", cohens_d),
            "degrees_freedom": kwargs.get("degrees_freedom", degrees_freedom),
        },
    )

@formula("eta_squared", "Eta Squared", "SS_between / SS_total", DOMAIN_KEY, unit="")
def eta_squared(ss_between: float | None = None, ss_total: float | None = None, **kwargs):
    return build_result(
        fid="eta_squared",
        name="Eta Squared",
        expression="SS_between / SS_total",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ss_between": kwargs.get("ss_between", ss_between),
            "ss_total": kwargs.get("ss_total", ss_total),
        },
    )

@formula("odds_ratio", "Odds Ratio", "(a*d) / (b*c)", DOMAIN_KEY, unit="")
def odds_ratio(a: float | None = None, b: float | None = None, c: float | None = None, d: float | None = None, **kwargs):
    return build_result(
        fid="odds_ratio",
        name="Odds Ratio",
        expression="(a*d) / (b*c)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "a": kwargs.get("a", a),
            "b": kwargs.get("b", b),
            "c": kwargs.get("c", c),
            "d": kwargs.get("d", d),
        },
    )

@formula("relative_risk", "Relative Risk", "(a/(a+b)) / (c/(c+d))", DOMAIN_KEY, unit="")
def relative_risk(a: float | None = None, b: float | None = None, c: float | None = None, d: float | None = None, **kwargs):
    return build_result(
        fid="relative_risk",
        name="Relative Risk",
        expression="(a/(a+b)) / (c/(c+d))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "a": kwargs.get("a", a),
            "b": kwargs.get("b", b),
            "c": kwargs.get("c", c),
            "d": kwargs.get("d", d),
        },
    )

@formula("confidence_interval_mean", "CI for Mean", "xbar +/- t*(s/sqrt(n))", DOMAIN_KEY, unit="")
def confidence_interval_mean(mean: float | None = None, std: float | None = None, n: float | None = None, confidence: float | None = None, **kwargs):
    return build_result(
        fid="confidence_interval_mean",
        name="CI for Mean",
        expression="xbar +/- t*(s/sqrt(n))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "mean": kwargs.get("mean", mean),
            "std": kwargs.get("std", std),
            "n": kwargs.get("n", n),
            "confidence": kwargs.get("confidence", confidence),
        },
    )

@formula("confidence_interval_proportion", "CI for Proportion", "phat +/- z*sqrt(phat(1-phat)/n)", DOMAIN_KEY, unit="")
def confidence_interval_proportion(proportion: float | None = None, n: float | None = None, confidence: float | None = None, **kwargs):
    return build_result(
        fid="confidence_interval_proportion",
        name="CI for Proportion",
        expression="phat +/- z*sqrt(phat(1-phat)/n)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "proportion": kwargs.get("proportion", proportion),
            "n": kwargs.get("n", n),
            "confidence": kwargs.get("confidence", confidence),
        },
    )

@formula("margin_of_error", "Margin of Error", "z * (std / sqrt(n))", DOMAIN_KEY, unit="")
def margin_of_error(z_score: float | None = None, std: float | None = None, n: float | None = None, **kwargs):
    return build_result(
        fid="margin_of_error",
        name="Margin of Error",
        expression="z * (std / sqrt(n))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "z_score": kwargs.get("z_score", z_score),
            "std": kwargs.get("std", std),
            "n": kwargs.get("n", n),
        },
    )

@formula("prediction_interval", "Prediction Interval", "yhat +/- t*s*sqrt(1+1/n+...)", DOMAIN_KEY, unit="")
def prediction_interval(prediction: float | None = None, std_error: float | None = None, n: float | None = None, confidence: float | None = None, **kwargs):
    return build_result(
        fid="prediction_interval",
        name="Prediction Interval",
        expression="yhat +/- t*s*sqrt(1+1/n+...)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prediction": kwargs.get("prediction", prediction),
            "std_error": kwargs.get("std_error", std_error),
            "n": kwargs.get("n", n),
            "confidence": kwargs.get("confidence", confidence),
        },
    )

@formula("p_value_from_z", "P-Value from Z", "2*(1 - Phi(|z|))", DOMAIN_KEY, unit="")
def p_value_from_z(z_score: float | None = None, **kwargs):
    return build_result(
        fid="p_value_from_z",
        name="P-Value from Z",
        expression="2*(1 - Phi(|z|))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "z_score": kwargs.get("z_score", z_score),
        },
    )

@formula("logistic_regression_prob", "Logistic Regression Probability", "1/(1+e^-(b0+b1*x))", DOMAIN_KEY, unit="")
def logistic_regression_prob(intercept: float | None = None, coefficient: float | None = None, x: float | None = None, **kwargs):
    return build_result(
        fid="logistic_regression_prob",
        name="Logistic Regression Probability",
        expression="1/(1+e^-(b0+b1*x))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "intercept": kwargs.get("intercept", intercept),
            "coefficient": kwargs.get("coefficient", coefficient),
            "x": kwargs.get("x", x),
        },
    )

@formula("multiple_regression_predict", "Multiple Regression Prediction", "b0 + Sum(bi*xi)", DOMAIN_KEY, unit="")
def multiple_regression_predict(intercept: float | None = None, coefficients: float | None = None, features: float | None = None, **kwargs):
    return build_result(
        fid="multiple_regression_predict",
        name="Multiple Regression Prediction",
        expression="b0 + Sum(bi*xi)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "intercept": kwargs.get("intercept", intercept),
            "coefficients": kwargs.get("coefficients", coefficients),
            "features": kwargs.get("features", features),
        },
    )

@formula("ridge_penalty_cost", "Ridge Regression Cost", "SSE + lambda*Sum(b^2)", DOMAIN_KEY, unit="")
def ridge_penalty_cost(sse: float | None = None, coefficients: float | None = None, lambda_: float | None = None, **kwargs):
    return build_result(
        fid="ridge_penalty_cost",
        name="Ridge Regression Cost",
        expression="SSE + lambda*Sum(b^2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "sse": kwargs.get("sse", sse),
            "coefficients": kwargs.get("coefficients", coefficients),
            "lambda": kwargs.get("lambda", lambda_),
        },
    )

@formula("vif", "Variance Inflation Factor", "1 / (1 - R2_i)", DOMAIN_KEY, unit="")
def vif(r_squared_i: float | None = None, **kwargs):
    return build_result(
        fid="vif",
        name="Variance Inflation Factor",
        expression="1 / (1 - R2_i)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "r_squared_i": kwargs.get("r_squared_i", r_squared_i),
        },
    )

@formula("partial_correlation", "Partial Correlation", "(rxy - rxz*ryz)/sqrt(...)", DOMAIN_KEY, unit="")
def partial_correlation(rxy: float | None = None, rxz: float | None = None, ryz: float | None = None, **kwargs):
    return build_result(
        fid="partial_correlation",
        name="Partial Correlation",
        expression="(rxy - rxz*ryz)/sqrt(...)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "rxy": kwargs.get("rxy", rxy),
            "rxz": kwargs.get("rxz", rxz),
            "ryz": kwargs.get("ryz", ryz),
        },
    )

@formula("durbin_watson_test", "Durbin-Watson", "Sum((e_t - e_t-1)^2)/Sum(e_t^2)", DOMAIN_KEY, unit="")
def durbin_watson_test(residuals: float | None = None, **kwargs):
    return build_result(
        fid="durbin_watson_test",
        name="Durbin-Watson",
        expression="Sum((e_t - e_t-1)^2)/Sum(e_t^2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "residuals": kwargs.get("residuals", residuals),
        },
    )

@formula("standardized_residual", "Standardized Residual", "residual / std_error", DOMAIN_KEY, unit="")
def standardized_residual(residual: float | None = None, std_error: float | None = None, **kwargs):
    return build_result(
        fid="standardized_residual",
        name="Standardized Residual",
        expression="residual / std_error",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "residual": kwargs.get("residual", residual),
            "std_error": kwargs.get("std_error", std_error),
        },
    )

@formula("leverage_hat", "Leverage (Hat Value)", "Diagonal of hat matrix", DOMAIN_KEY, unit="")
def leverage_hat(x_matrix: float | None = None, observation: float | None = None, **kwargs):
    return build_result(
        fid="leverage_hat",
        name="Leverage (Hat Value)",
        expression="Diagonal of hat matrix",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x_matrix": kwargs.get("x_matrix", x_matrix),
            "observation": kwargs.get("observation", observation),
        },
    )

@formula("cooks_distance", "Cook's Distance", "(e^2/(p*MSE))*(h/(1-h)^2)", DOMAIN_KEY, unit="")
def cooks_distance(residual: float | None = None, leverage: float | None = None, p: float | None = None, mse: float | None = None, **kwargs):
    return build_result(
        fid="cooks_distance",
        name="Cook's Distance",
        expression="(e^2/(p*MSE))*(h/(1-h)^2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "residual": kwargs.get("residual", residual),
            "leverage": kwargs.get("leverage", leverage),
            "p": kwargs.get("p", p),
            "mse": kwargs.get("mse", mse),
        },
    )

@formula("sample_size_mean", "Sample Size for Mean", "(z*sigma/E)^2", DOMAIN_KEY, unit="")
def sample_size_mean(z_score: float | None = None, std: float | None = None, margin_error: float | None = None, **kwargs):
    return build_result(
        fid="sample_size_mean",
        name="Sample Size for Mean",
        expression="(z*sigma/E)^2",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "z_score": kwargs.get("z_score", z_score),
            "std": kwargs.get("std", std),
            "margin_error": kwargs.get("margin_error", margin_error),
        },
    )

@formula("sample_size_proportion", "Sample Size for Proportion", "z^2*p(1-p)/E^2", DOMAIN_KEY, unit="")
def sample_size_proportion(z_score: float | None = None, proportion: float | None = None, margin_error: float | None = None, **kwargs):
    return build_result(
        fid="sample_size_proportion",
        name="Sample Size for Proportion",
        expression="z^2*p(1-p)/E^2",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "z_score": kwargs.get("z_score", z_score),
            "proportion": kwargs.get("proportion", proportion),
            "margin_error": kwargs.get("margin_error", margin_error),
        },
    )

@formula("standard_error_proportion", "Standard Error of Proportion", "sqrt(p(1-p)/n)", DOMAIN_KEY, unit="")
def standard_error_proportion(proportion: float | None = None, n: float | None = None, **kwargs):
    return build_result(
        fid="standard_error_proportion",
        name="Standard Error of Proportion",
        expression="sqrt(p(1-p)/n)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "proportion": kwargs.get("proportion", proportion),
            "n": kwargs.get("n", n),
        },
    )

@formula("finite_population_correction", "Finite Population Correction", "sqrt((N-n)/(N-1))", DOMAIN_KEY, unit="")
def finite_population_correction(population: float | None = None, sample: float | None = None, **kwargs):
    return build_result(
        fid="finite_population_correction",
        name="Finite Population Correction",
        expression="sqrt((N-n)/(N-1))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "population": kwargs.get("population", population),
            "sample": kwargs.get("sample", sample),
        },
    )

@formula("bootstrap_std_error", "Bootstrap Standard Error", "Std of bootstrap statistics", DOMAIN_KEY, unit="")
def bootstrap_std_error(bootstrap_estimates: float | None = None, **kwargs):
    return build_result(
        fid="bootstrap_std_error",
        name="Bootstrap Standard Error",
        expression="Std of bootstrap statistics",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "bootstrap_estimates": kwargs.get("bootstrap_estimates", bootstrap_estimates),
        },
    )

@formula("pooled_variance", "Pooled Variance", "((n1-1)s1^2+(n2-1)s2^2)/(n1+n2-2)", DOMAIN_KEY, unit="")
def pooled_variance(var1: float | None = None, var2: float | None = None, n1: float | None = None, n2: float | None = None, **kwargs):
    return build_result(
        fid="pooled_variance",
        name="Pooled Variance",
        expression="((n1-1)s1^2+(n2-1)s2^2)/(n1+n2-2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "var1": kwargs.get("var1", var1),
            "var2": kwargs.get("var2", var2),
            "n1": kwargs.get("n1", n1),
            "n2": kwargs.get("n2", n2),
        },
    )

@formula("spearman_rank", "Spearman Rank Correlation", "1 - 6*Sum(d^2)/(n(n^2-1))", DOMAIN_KEY, unit="")
def spearman_rank(rank_diffs: float | None = None, n: float | None = None, **kwargs):
    return build_result(
        fid="spearman_rank",
        name="Spearman Rank Correlation",
        expression="1 - 6*Sum(d^2)/(n(n^2-1))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "rank_diffs": kwargs.get("rank_diffs", rank_diffs),
            "n": kwargs.get("n", n),
        },
    )

@formula("kendall_tau_b", "Kendall Tau-b", "(C - D)/sqrt((C+D+T)(C+D+U))", DOMAIN_KEY, unit="")
def kendall_tau_b(concordant: float | None = None, discordant: float | None = None, ties_x: float | None = None, ties_y: float | None = None, **kwargs):
    return build_result(
        fid="kendall_tau_b",
        name="Kendall Tau-b",
        expression="(C - D)/sqrt((C+D+T)(C+D+U))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "concordant": kwargs.get("concordant", concordant),
            "discordant": kwargs.get("discordant", discordant),
            "ties_x": kwargs.get("ties_x", ties_x),
            "ties_y": kwargs.get("ties_y", ties_y),
        },
    )

@formula("point_biserial", "Point-Biserial Correlation", "(M1-M0)/Std * sqrt(p*q)", DOMAIN_KEY, unit="")
def point_biserial(mean1: float | None = None, mean0: float | None = None, std: float | None = None, p: float | None = None, q: float | None = None, **kwargs):
    return build_result(
        fid="point_biserial",
        name="Point-Biserial Correlation",
        expression="(M1-M0)/Std * sqrt(p*q)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "mean1": kwargs.get("mean1", mean1),
            "mean0": kwargs.get("mean0", mean0),
            "std": kwargs.get("std", std),
            "p": kwargs.get("p", p),
            "q": kwargs.get("q", q),
        },
    )

@formula("shapiro_wilk_stat", "Shapiro-Wilk Statistic", "(Sum(a_i*x_i))^2 / Sum((x-xbar)^2)", DOMAIN_KEY, unit="")
def shapiro_wilk_stat(ordered_values: float | None = None, coefficients: float | None = None, **kwargs):
    return build_result(
        fid="shapiro_wilk_stat",
        name="Shapiro-Wilk Statistic",
        expression="(Sum(a_i*x_i))^2 / Sum((x-xbar)^2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "ordered_values": kwargs.get("ordered_values", ordered_values),
            "coefficients": kwargs.get("coefficients", coefficients),
        },
    )

@formula("kolmogorov_smirnov", "Kolmogorov-Smirnov D", "max|F_empirical - F_theoretical|", DOMAIN_KEY, unit="")
def kolmogorov_smirnov(empirical_cdf: float | None = None, theoretical_cdf: float | None = None, **kwargs):
    return build_result(
        fid="kolmogorov_smirnov",
        name="Kolmogorov-Smirnov D",
        expression="max|F_empirical - F_theoretical|",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "empirical_cdf": kwargs.get("empirical_cdf", empirical_cdf),
            "theoretical_cdf": kwargs.get("theoretical_cdf", theoretical_cdf),
        },
    )

@formula("jarque_bera", "Jarque-Bera Statistic", "n/6*(S^2 + (K-3)^2/4)", DOMAIN_KEY, unit="")
def jarque_bera(n: float | None = None, skewness: float | None = None, kurtosis: float | None = None, **kwargs):
    return build_result(
        fid="jarque_bera",
        name="Jarque-Bera Statistic",
        expression="n/6*(S^2 + (K-3)^2/4)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "n": kwargs.get("n", n),
            "skewness": kwargs.get("skewness", skewness),
            "kurtosis": kwargs.get("kurtosis", kurtosis),
        },
    )

@formula("bonferroni_correction", "Bonferroni Alpha", "alpha / m", DOMAIN_KEY, unit="")
def bonferroni_correction(alpha: float | None = None, num_tests: float | None = None, **kwargs):
    return build_result(
        fid="bonferroni_correction",
        name="Bonferroni Alpha",
        expression="alpha / m",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "alpha": kwargs.get("alpha", alpha),
            "num_tests": kwargs.get("num_tests", num_tests),
        },
    )

@formula("benjamini_hochberg", "Benjamini-Hochberg Threshold", "(i/m) * alpha", DOMAIN_KEY, unit="")
def benjamini_hochberg(rank: float | None = None, num_tests: float | None = None, alpha: float | None = None, **kwargs):
    return build_result(
        fid="benjamini_hochberg",
        name="Benjamini-Hochberg Threshold",
        expression="(i/m) * alpha",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "rank": kwargs.get("rank", rank),
            "num_tests": kwargs.get("num_tests", num_tests),
            "alpha": kwargs.get("alpha", alpha),
        },
    )

@formula("tukey_hsd", "Tukey HSD Critical Diff", "q * sqrt(MSE/n)", DOMAIN_KEY, unit="")
def tukey_hsd(q_critical: float | None = None, mse: float | None = None, n: float | None = None, **kwargs):
    return build_result(
        fid="tukey_hsd",
        name="Tukey HSD Critical Diff",
        expression="q * sqrt(MSE/n)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "q_critical": kwargs.get("q_critical", q_critical),
            "mse": kwargs.get("mse", mse),
            "n": kwargs.get("n", n),
        },
    )

@formula("power_analysis", "Statistical Power", "1 - Beta", DOMAIN_KEY, unit="")
def power_analysis(beta: float | None = None, **kwargs):
    return build_result(
        fid="power_analysis",
        name="Statistical Power",
        expression="1 - Beta",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "beta": kwargs.get("beta", beta),
        },
    )

@formula("kaplan_meier", "Kaplan-Meier Survival", "Prod((n_i - d_i)/n_i)", DOMAIN_KEY, unit="")
def kaplan_meier(at_risk: float | None = None, events: float | None = None, **kwargs):
    return build_result(
        fid="kaplan_meier",
        name="Kaplan-Meier Survival",
        expression="Prod((n_i - d_i)/n_i)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "at_risk": kwargs.get("at_risk", at_risk),
            "events": kwargs.get("events", events),
        },
    )

@formula("gini_coefficient_stat", "Gini Coefficient", "Sum of Lorenz deviations", DOMAIN_KEY, unit="")
def gini_coefficient_stat(values: float | None = None, **kwargs):
    return build_result(
        fid="gini_coefficient_stat",
        name="Gini Coefficient",
        expression="Sum of Lorenz deviations",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
        },
    )

@formula("theil_index", "Theil Index", "Mean((x/xbar)*ln(x/xbar))", DOMAIN_KEY, unit="")
def theil_index(values: float | None = None, **kwargs):
    return build_result(
        fid="theil_index",
        name="Theil Index",
        expression="Mean((x/xbar)*ln(x/xbar))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
        },
    )

@formula("cohens_kappa_stat", "Cohen's Kappa", "(Po - Pe)/(1 - Pe)", DOMAIN_KEY, unit="")
def cohens_kappa_stat(observed_agreement: float | None = None, expected_agreement: float | None = None, **kwargs):
    return build_result(
        fid="cohens_kappa_stat",
        name="Cohen's Kappa",
        expression="(Po - Pe)/(1 - Pe)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "observed_agreement": kwargs.get("observed_agreement", observed_agreement),
            "expected_agreement": kwargs.get("expected_agreement", expected_agreement),
        },
    )
