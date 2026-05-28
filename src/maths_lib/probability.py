from .base import build_result, formula

DOMAIN_KEY = "D15_probability"
DOMAIN_TITLE = "Probability Theory & Distributions"
FORMULA_IDS = [
    "normal_pdf",
    "normal_cdf",
    "standard_normal_pdf",
    "binomial_pmf",
    "poisson_pmf",
    "exponential_pdf",
    "uniform_pdf",
    "bernoulli_pmf",
    "geometric_pmf",
    "negative_binomial_pmf",
    "beta_pdf",
    "gamma_pdf",
    "lognormal_pdf",
    "student_t_pdf",
    "chi2_pdf",
    "f_distribution_pdf",
    "weibull_pdf",
    "conditional_probability",
    "bayes_theorem",
    "joint_probability_independent",
    "union_probability",
    "complement_probability",
    "total_probability",
    "odds_from_probability",
    "probability_from_odds",
    "permutations_count",
    "combinations_count",
    "multinomial_coefficient",
    "permutations_with_repetition",
    "circular_permutations",
    "expected_value_discrete",
    "variance_discrete",
    "covariance_random_vars",
    "correlation_random_vars",
    "moment_generating",
    "variance_sum_independent",
    "markov_steady_state",
    "poisson_process_prob",
    "geometric_brownian_motion",
    "random_walk_position",
    "chebyshev_inequality",
    "markov_inequality",
    "central_limit_theorem",
    "bayesian_posterior",
    "law_large_numbers_error",
    "hypergeometric_pmf",
    "multinomial_pmf",
    "cauchy_pdf",
    "pareto_pdf",
    "survival_function",
    "hazard_rate",
    "entropy_shannon",
    "cross_entropy_dist",
    "conditional_variance",
    "expected_shortfall_prob",
]

@formula("normal_pdf", "Normal PDF", "1/(sig*sqrt(2pi))*e^(-(x-mu)^2/(2sig^2))", DOMAIN_KEY, unit="")
def normal_pdf(x: float | None = None, mean: float | None = None, std: float | None = None, **kwargs):
    return build_result(
        fid="normal_pdf",
        name="Normal PDF",
        expression="1/(sig*sqrt(2pi))*e^(-(x-mu)^2/(2sig^2))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
            "mean": kwargs.get("mean", mean),
            "std": kwargs.get("std", std),
        },
    )

@formula("normal_cdf", "Normal CDF", "0.5*(1 + erf((x-mu)/(sig*sqrt(2))))", DOMAIN_KEY, unit="")
def normal_cdf(x: float | None = None, mean: float | None = None, std: float | None = None, **kwargs):
    return build_result(
        fid="normal_cdf",
        name="Normal CDF",
        expression="0.5*(1 + erf((x-mu)/(sig*sqrt(2))))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
            "mean": kwargs.get("mean", mean),
            "std": kwargs.get("std", std),
        },
    )

@formula("standard_normal_pdf", "Standard Normal PDF", "1/sqrt(2pi)*e^(-z^2/2)", DOMAIN_KEY, unit="")
def standard_normal_pdf(z: float | None = None, **kwargs):
    return build_result(
        fid="standard_normal_pdf",
        name="Standard Normal PDF",
        expression="1/sqrt(2pi)*e^(-z^2/2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "z": kwargs.get("z", z),
        },
    )

@formula("binomial_pmf", "Binomial PMF", "C(n,k)*p^k*(1-p)^(n-k)", DOMAIN_KEY, unit="")
def binomial_pmf(k: float | None = None, n: float | None = None, p: float | None = None, **kwargs):
    return build_result(
        fid="binomial_pmf",
        name="Binomial PMF",
        expression="C(n,k)*p^k*(1-p)^(n-k)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "k": kwargs.get("k", k),
            "n": kwargs.get("n", n),
            "p": kwargs.get("p", p),
        },
    )

@formula("poisson_pmf", "Poisson PMF", "lambda^k * e^-lambda / k!", DOMAIN_KEY, unit="")
def poisson_pmf(k: float | None = None, lambda_: float | None = None, **kwargs):
    return build_result(
        fid="poisson_pmf",
        name="Poisson PMF",
        expression="lambda^k * e^-lambda / k!",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "k": kwargs.get("k", k),
            "lambda": kwargs.get("lambda", lambda_),
        },
    )

@formula("exponential_pdf", "Exponential PDF", "lambda*e^(-lambda*x)", DOMAIN_KEY, unit="")
def exponential_pdf(x: float | None = None, lambda_: float | None = None, **kwargs):
    return build_result(
        fid="exponential_pdf",
        name="Exponential PDF",
        expression="lambda*e^(-lambda*x)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
            "lambda": kwargs.get("lambda", lambda_),
        },
    )

@formula("uniform_pdf", "Uniform PDF", "1/(b-a)", DOMAIN_KEY, unit="")
def uniform_pdf(a: float | None = None, b: float | None = None, **kwargs):
    return build_result(
        fid="uniform_pdf",
        name="Uniform PDF",
        expression="1/(b-a)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "a": kwargs.get("a", a),
            "b": kwargs.get("b", b),
        },
    )

@formula("bernoulli_pmf", "Bernoulli PMF", "p^k*(1-p)^(1-k)", DOMAIN_KEY, unit="")
def bernoulli_pmf(k: float | None = None, p: float | None = None, **kwargs):
    return build_result(
        fid="bernoulli_pmf",
        name="Bernoulli PMF",
        expression="p^k*(1-p)^(1-k)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "k": kwargs.get("k", k),
            "p": kwargs.get("p", p),
        },
    )

@formula("geometric_pmf", "Geometric PMF", "(1-p)^(k-1)*p", DOMAIN_KEY, unit="")
def geometric_pmf(k: float | None = None, p: float | None = None, **kwargs):
    return build_result(
        fid="geometric_pmf",
        name="Geometric PMF",
        expression="(1-p)^(k-1)*p",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "k": kwargs.get("k", k),
            "p": kwargs.get("p", p),
        },
    )

@formula("negative_binomial_pmf", "Negative Binomial PMF", "C(k+r-1,k)*p^r*(1-p)^k", DOMAIN_KEY, unit="")
def negative_binomial_pmf(k: float | None = None, r: float | None = None, p: float | None = None, **kwargs):
    return build_result(
        fid="negative_binomial_pmf",
        name="Negative Binomial PMF",
        expression="C(k+r-1,k)*p^r*(1-p)^k",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "k": kwargs.get("k", k),
            "r": kwargs.get("r", r),
            "p": kwargs.get("p", p),
        },
    )

@formula("beta_pdf", "Beta PDF", "x^(a-1)*(1-x)^(b-1)/B(a,b)", DOMAIN_KEY, unit="")
def beta_pdf(x: float | None = None, alpha: float | None = None, beta: float | None = None, **kwargs):
    return build_result(
        fid="beta_pdf",
        name="Beta PDF",
        expression="x^(a-1)*(1-x)^(b-1)/B(a,b)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
            "alpha": kwargs.get("alpha", alpha),
            "beta": kwargs.get("beta", beta),
        },
    )

@formula("gamma_pdf", "Gamma PDF", "x^(a-1)*e^(-x/b)/(b^a*Gamma(a))", DOMAIN_KEY, unit="")
def gamma_pdf(x: float | None = None, shape: float | None = None, scale: float | None = None, **kwargs):
    return build_result(
        fid="gamma_pdf",
        name="Gamma PDF",
        expression="x^(a-1)*e^(-x/b)/(b^a*Gamma(a))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
            "shape": kwargs.get("shape", shape),
            "scale": kwargs.get("scale", scale),
        },
    )

@formula("lognormal_pdf", "Log-Normal PDF", "1/(x*s*sqrt(2pi))*e^(-(ln x-mu)^2/(2s^2))", DOMAIN_KEY, unit="")
def lognormal_pdf(x: float | None = None, mu: float | None = None, sigma: float | None = None, **kwargs):
    return build_result(
        fid="lognormal_pdf",
        name="Log-Normal PDF",
        expression="1/(x*s*sqrt(2pi))*e^(-(ln x-mu)^2/(2s^2))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
            "mu": kwargs.get("mu", mu),
            "sigma": kwargs.get("sigma", sigma),
        },
    )

@formula("student_t_pdf", "Student's t PDF", "Gamma((v+1)/2)/... t-density", DOMAIN_KEY, unit="")
def student_t_pdf(t: float | None = None, degrees_freedom: float | None = None, **kwargs):
    return build_result(
        fid="student_t_pdf",
        name="Student's t PDF",
        expression="Gamma((v+1)/2)/... t-density",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "t": kwargs.get("t", t),
            "degrees_freedom": kwargs.get("degrees_freedom", degrees_freedom),
        },
    )

@formula("chi2_pdf", "Chi-Square PDF", "x^(k/2-1)*e^(-x/2)/(2^(k/2)*Gamma(k/2))", DOMAIN_KEY, unit="")
def chi2_pdf(x: float | None = None, degrees_freedom: float | None = None, **kwargs):
    return build_result(
        fid="chi2_pdf",
        name="Chi-Square PDF",
        expression="x^(k/2-1)*e^(-x/2)/(2^(k/2)*Gamma(k/2))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
            "degrees_freedom": kwargs.get("degrees_freedom", degrees_freedom),
        },
    )

@formula("f_distribution_pdf", "F-Distribution PDF", "F-density formula", DOMAIN_KEY, unit="")
def f_distribution_pdf(x: float | None = None, df1: float | None = None, df2: float | None = None, **kwargs):
    return build_result(
        fid="f_distribution_pdf",
        name="F-Distribution PDF",
        expression="F-density formula",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
            "df1": kwargs.get("df1", df1),
            "df2": kwargs.get("df2", df2),
        },
    )

@formula("weibull_pdf", "Weibull PDF", "(k/l)*(x/l)^(k-1)*e^(-(x/l)^k)", DOMAIN_KEY, unit="")
def weibull_pdf(x: float | None = None, shape: float | None = None, scale: float | None = None, **kwargs):
    return build_result(
        fid="weibull_pdf",
        name="Weibull PDF",
        expression="(k/l)*(x/l)^(k-1)*e^(-(x/l)^k)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
            "shape": kwargs.get("shape", shape),
            "scale": kwargs.get("scale", scale),
        },
    )

@formula("conditional_probability", "Conditional Probability", "P(A and B) / P(B)", DOMAIN_KEY, unit="")
def conditional_probability(p_a_and_b: float | None = None, p_b: float | None = None, **kwargs):
    return build_result(
        fid="conditional_probability",
        name="Conditional Probability",
        expression="P(A and B) / P(B)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "p_a_and_b": kwargs.get("p_a_and_b", p_a_and_b),
            "p_b": kwargs.get("p_b", p_b),
        },
    )

@formula("bayes_theorem", "Bayes' Theorem", "P(B|A)*P(A) / P(B)", DOMAIN_KEY, unit="")
def bayes_theorem(p_b_given_a: float | None = None, p_a: float | None = None, p_b: float | None = None, **kwargs):
    return build_result(
        fid="bayes_theorem",
        name="Bayes' Theorem",
        expression="P(B|A)*P(A) / P(B)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "p_b_given_a": kwargs.get("p_b_given_a", p_b_given_a),
            "p_a": kwargs.get("p_a", p_a),
            "p_b": kwargs.get("p_b", p_b),
        },
    )

@formula("joint_probability_independent", "Joint Probability (Independent)", "P(A) * P(B)", DOMAIN_KEY, unit="")
def joint_probability_independent(p_a: float | None = None, p_b: float | None = None, **kwargs):
    return build_result(
        fid="joint_probability_independent",
        name="Joint Probability (Independent)",
        expression="P(A) * P(B)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "p_a": kwargs.get("p_a", p_a),
            "p_b": kwargs.get("p_b", p_b),
        },
    )

@formula("union_probability", "Union Probability", "P(A) + P(B) - P(A and B)", DOMAIN_KEY, unit="")
def union_probability(p_a: float | None = None, p_b: float | None = None, p_a_and_b: float | None = None, **kwargs):
    return build_result(
        fid="union_probability",
        name="Union Probability",
        expression="P(A) + P(B) - P(A and B)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "p_a": kwargs.get("p_a", p_a),
            "p_b": kwargs.get("p_b", p_b),
            "p_a_and_b": kwargs.get("p_a_and_b", p_a_and_b),
        },
    )

@formula("complement_probability", "Complement Probability", "1 - P(A)", DOMAIN_KEY, unit="")
def complement_probability(p_a: float | None = None, **kwargs):
    return build_result(
        fid="complement_probability",
        name="Complement Probability",
        expression="1 - P(A)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "p_a": kwargs.get("p_a", p_a),
        },
    )

@formula("total_probability", "Total Probability", "Sum(P(A|Bi)*P(Bi))", DOMAIN_KEY, unit="")
def total_probability(conditionals: float | None = None, priors: float | None = None, **kwargs):
    return build_result(
        fid="total_probability",
        name="Total Probability",
        expression="Sum(P(A|Bi)*P(Bi))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "conditionals": kwargs.get("conditionals", conditionals),
            "priors": kwargs.get("priors", priors),
        },
    )

@formula("odds_from_probability", "Odds from Probability", "p / (1 - p)", DOMAIN_KEY, unit="")
def odds_from_probability(probability: float | None = None, **kwargs):
    return build_result(
        fid="odds_from_probability",
        name="Odds from Probability",
        expression="p / (1 - p)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "probability": kwargs.get("probability", probability),
        },
    )

@formula("probability_from_odds", "Probability from Odds", "odds / (1 + odds)", DOMAIN_KEY, unit="")
def probability_from_odds(odds: float | None = None, **kwargs):
    return build_result(
        fid="probability_from_odds",
        name="Probability from Odds",
        expression="odds / (1 + odds)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "odds": kwargs.get("odds", odds),
        },
    )

@formula("permutations_count", "Permutations Count", "n! / (n-r)!", DOMAIN_KEY, unit="")
def permutations_count(n: float | None = None, r: float | None = None, **kwargs):
    return build_result(
        fid="permutations_count",
        name="Permutations Count",
        expression="n! / (n-r)!",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "n": kwargs.get("n", n),
            "r": kwargs.get("r", r),
        },
    )

@formula("combinations_count", "Combinations Count", "n! / (r!(n-r)!)", DOMAIN_KEY, unit="")
def combinations_count(n: float | None = None, r: float | None = None, **kwargs):
    return build_result(
        fid="combinations_count",
        name="Combinations Count",
        expression="n! / (r!(n-r)!)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "n": kwargs.get("n", n),
            "r": kwargs.get("r", r),
        },
    )

@formula("multinomial_coefficient", "Multinomial Coefficient", "n! / (n1!*n2!*...*nk!)", DOMAIN_KEY, unit="")
def multinomial_coefficient(n: float | None = None, group_sizes: float | None = None, **kwargs):
    return build_result(
        fid="multinomial_coefficient",
        name="Multinomial Coefficient",
        expression="n! / (n1!*n2!*...*nk!)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "n": kwargs.get("n", n),
            "group_sizes": kwargs.get("group_sizes", group_sizes),
        },
    )

@formula("permutations_with_repetition", "Permutations with Repetition", "n^r", DOMAIN_KEY, unit="")
def permutations_with_repetition(n: float | None = None, r: float | None = None, **kwargs):
    return build_result(
        fid="permutations_with_repetition",
        name="Permutations with Repetition",
        expression="n^r",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "n": kwargs.get("n", n),
            "r": kwargs.get("r", r),
        },
    )

@formula("circular_permutations", "Circular Permutations", "(n-1)!", DOMAIN_KEY, unit="")
def circular_permutations(n: float | None = None, **kwargs):
    return build_result(
        fid="circular_permutations",
        name="Circular Permutations",
        expression="(n-1)!",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "n": kwargs.get("n", n),
        },
    )

@formula("expected_value_discrete", "Expected Value (Discrete)", "Sum(x_i * p_i)", DOMAIN_KEY, unit="")
def expected_value_discrete(values: float | None = None, probabilities: float | None = None, **kwargs):
    return build_result(
        fid="expected_value_discrete",
        name="Expected Value (Discrete)",
        expression="Sum(x_i * p_i)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
            "probabilities": kwargs.get("probabilities", probabilities),
        },
    )

@formula("variance_discrete", "Variance (Discrete)", "Sum(p*(x-mu)^2)", DOMAIN_KEY, unit="")
def variance_discrete(values: float | None = None, probabilities: float | None = None, **kwargs):
    return build_result(
        fid="variance_discrete",
        name="Variance (Discrete)",
        expression="Sum(p*(x-mu)^2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
            "probabilities": kwargs.get("probabilities", probabilities),
        },
    )

@formula("covariance_random_vars", "Covariance (Random Vars)", "E[XY] - E[X]E[Y]", DOMAIN_KEY, unit="")
def covariance_random_vars(joint_values: float | None = None, probabilities: float | None = None, **kwargs):
    return build_result(
        fid="covariance_random_vars",
        name="Covariance (Random Vars)",
        expression="E[XY] - E[X]E[Y]",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "joint_values": kwargs.get("joint_values", joint_values),
            "probabilities": kwargs.get("probabilities", probabilities),
        },
    )

@formula("correlation_random_vars", "Correlation (Random Vars)", "Cov(X,Y)/(sigX*sigY)", DOMAIN_KEY, unit="")
def correlation_random_vars(covariance: float | None = None, std_x: float | None = None, std_y: float | None = None, **kwargs):
    return build_result(
        fid="correlation_random_vars",
        name="Correlation (Random Vars)",
        expression="Cov(X,Y)/(sigX*sigY)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "covariance": kwargs.get("covariance", covariance),
            "std_x": kwargs.get("std_x", std_x),
            "std_y": kwargs.get("std_y", std_y),
        },
    )

@formula("moment_generating", "Moment (n-th)", "E[X^n]", DOMAIN_KEY, unit="")
def moment_generating(values: float | None = None, probabilities: float | None = None, n: float | None = None, **kwargs):
    return build_result(
        fid="moment_generating",
        name="Moment (n-th)",
        expression="E[X^n]",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "values": kwargs.get("values", values),
            "probabilities": kwargs.get("probabilities", probabilities),
            "n": kwargs.get("n", n),
        },
    )

@formula("variance_sum_independent", "Variance of Sum (Independent)", "Var(X) + Var(Y)", DOMAIN_KEY, unit="")
def variance_sum_independent(var_x: float | None = None, var_y: float | None = None, **kwargs):
    return build_result(
        fid="variance_sum_independent",
        name="Variance of Sum (Independent)",
        expression="Var(X) + Var(Y)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "var_x": kwargs.get("var_x", var_x),
            "var_y": kwargs.get("var_y", var_y),
        },
    )

@formula("markov_steady_state", "Markov Steady State", "pi = pi*P", DOMAIN_KEY, unit="")
def markov_steady_state(transition_matrix: float | None = None, **kwargs):
    return build_result(
        fid="markov_steady_state",
        name="Markov Steady State",
        expression="pi = pi*P",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "transition_matrix": kwargs.get("transition_matrix", transition_matrix),
        },
    )

@formula("poisson_process_prob", "Poisson Process Probability", "(lambda*t)^k*e^(-lambda*t)/k!", DOMAIN_KEY, unit="")
def poisson_process_prob(rate: float | None = None, time: float | None = None, k: float | None = None, **kwargs):
    return build_result(
        fid="poisson_process_prob",
        name="Poisson Process Probability",
        expression="(lambda*t)^k*e^(-lambda*t)/k!",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "rate": kwargs.get("rate", rate),
            "time": kwargs.get("time", time),
            "k": kwargs.get("k", k),
        },
    )

@formula("geometric_brownian_motion", "Geometric Brownian Motion", "S0*e^((mu-sig^2/2)t + sig*W)", DOMAIN_KEY, unit="")
def geometric_brownian_motion(s0: float | None = None, mu: float | None = None, sigma: float | None = None, time: float | None = None, wiener: float | None = None, **kwargs):
    return build_result(
        fid="geometric_brownian_motion",
        name="Geometric Brownian Motion",
        expression="S0*e^((mu-sig^2/2)t + sig*W)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "s0": kwargs.get("s0", s0),
            "mu": kwargs.get("mu", mu),
            "sigma": kwargs.get("sigma", sigma),
            "time": kwargs.get("time", time),
            "wiener": kwargs.get("wiener", wiener),
        },
    )

@formula("random_walk_position", "Random Walk Position", "Sum(steps)", DOMAIN_KEY, unit="")
def random_walk_position(steps: float | None = None, **kwargs):
    return build_result(
        fid="random_walk_position",
        name="Random Walk Position",
        expression="Sum(steps)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "steps": kwargs.get("steps", steps),
        },
    )

@formula("chebyshev_inequality", "Chebyshev Inequality", "1 / k^2", DOMAIN_KEY, unit="")
def chebyshev_inequality(k: float | None = None, **kwargs):
    return build_result(
        fid="chebyshev_inequality",
        name="Chebyshev Inequality",
        expression="1 / k^2",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "k": kwargs.get("k", k),
        },
    )

@formula("markov_inequality", "Markov Inequality", "Mean / a", DOMAIN_KEY, unit="")
def markov_inequality(mean: float | None = None, a: float | None = None, **kwargs):
    return build_result(
        fid="markov_inequality",
        name="Markov Inequality",
        expression="Mean / a",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "mean": kwargs.get("mean", mean),
            "a": kwargs.get("a", a),
        },
    )

@formula("central_limit_theorem", "CLT Sampling Std", "sigma / sqrt(n)", DOMAIN_KEY, unit="")
def central_limit_theorem(sigma: float | None = None, n: float | None = None, **kwargs):
    return build_result(
        fid="central_limit_theorem",
        name="CLT Sampling Std",
        expression="sigma / sqrt(n)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "sigma": kwargs.get("sigma", sigma),
            "n": kwargs.get("n", n),
        },
    )

@formula("bayesian_posterior", "Bayesian Posterior", "(Likelihood*Prior) / Evidence", DOMAIN_KEY, unit="")
def bayesian_posterior(likelihood: float | None = None, prior: float | None = None, evidence: float | None = None, **kwargs):
    return build_result(
        fid="bayesian_posterior",
        name="Bayesian Posterior",
        expression="(Likelihood*Prior) / Evidence",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "likelihood": kwargs.get("likelihood", likelihood),
            "prior": kwargs.get("prior", prior),
            "evidence": kwargs.get("evidence", evidence),
        },
    )

@formula("law_large_numbers_error", "LLN Convergence Error", "sigma / sqrt(n)", DOMAIN_KEY, unit="")
def law_large_numbers_error(sigma: float | None = None, n: float | None = None, **kwargs):
    return build_result(
        fid="law_large_numbers_error",
        name="LLN Convergence Error",
        expression="sigma / sqrt(n)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "sigma": kwargs.get("sigma", sigma),
            "n": kwargs.get("n", n),
        },
    )

@formula("hypergeometric_pmf", "Hypergeometric PMF", "C(K,k)C(N-K,n-k)/C(N,n)", DOMAIN_KEY, unit="")
def hypergeometric_pmf(population: float | None = None, successes: float | None = None, draws: float | None = None, observed: float | None = None, **kwargs):
    return build_result(
        fid="hypergeometric_pmf",
        name="Hypergeometric PMF",
        expression="C(K,k)C(N-K,n-k)/C(N,n)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "population": kwargs.get("population", population),
            "successes": kwargs.get("successes", successes),
            "draws": kwargs.get("draws", draws),
            "observed": kwargs.get("observed", observed),
        },
    )

@formula("multinomial_pmf", "Multinomial PMF", "n!/Prod(xi!) * Prod(pi^xi)", DOMAIN_KEY, unit="")
def multinomial_pmf(n: float | None = None, counts: float | None = None, probabilities: float | None = None, **kwargs):
    return build_result(
        fid="multinomial_pmf",
        name="Multinomial PMF",
        expression="n!/Prod(xi!) * Prod(pi^xi)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "n": kwargs.get("n", n),
            "counts": kwargs.get("counts", counts),
            "probabilities": kwargs.get("probabilities", probabilities),
        },
    )

@formula("cauchy_pdf", "Cauchy PDF", "1/(pi*gamma*(1+((x-x0)/gamma)^2))", DOMAIN_KEY, unit="")
def cauchy_pdf(x: float | None = None, location: float | None = None, scale: float | None = None, **kwargs):
    return build_result(
        fid="cauchy_pdf",
        name="Cauchy PDF",
        expression="1/(pi*gamma*(1+((x-x0)/gamma)^2))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
            "location": kwargs.get("location", location),
            "scale": kwargs.get("scale", scale),
        },
    )

@formula("pareto_pdf", "Pareto PDF", "alpha*xm^alpha / x^(alpha+1)", DOMAIN_KEY, unit="")
def pareto_pdf(x: float | None = None, scale_min: float | None = None, alpha: float | None = None, **kwargs):
    return build_result(
        fid="pareto_pdf",
        name="Pareto PDF",
        expression="alpha*xm^alpha / x^(alpha+1)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
            "scale_min": kwargs.get("scale_min", scale_min),
            "alpha": kwargs.get("alpha", alpha),
        },
    )

@formula("survival_function", "Survival Function", "1 - CDF(t)", DOMAIN_KEY, unit="")
def survival_function(cdf: float | None = None, **kwargs):
    return build_result(
        fid="survival_function",
        name="Survival Function",
        expression="1 - CDF(t)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cdf": kwargs.get("cdf", cdf),
        },
    )

@formula("hazard_rate", "Hazard Rate", "pdf(t) / Survival(t)", DOMAIN_KEY, unit="")
def hazard_rate(pdf: float | None = None, survival: float | None = None, **kwargs):
    return build_result(
        fid="hazard_rate",
        name="Hazard Rate",
        expression="pdf(t) / Survival(t)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "pdf": kwargs.get("pdf", pdf),
            "survival": kwargs.get("survival", survival),
        },
    )

@formula("entropy_shannon", "Shannon Entropy", "-Sum(p * log2(p))", DOMAIN_KEY, unit="")
def entropy_shannon(probabilities: float | None = None, **kwargs):
    return build_result(
        fid="entropy_shannon",
        name="Shannon Entropy",
        expression="-Sum(p * log2(p))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "probabilities": kwargs.get("probabilities", probabilities),
        },
    )

@formula("cross_entropy_dist", "Cross Entropy (Distributions)", "-Sum(p * log(q))", DOMAIN_KEY, unit="")
def cross_entropy_dist(p_true: float | None = None, q_pred: float | None = None, **kwargs):
    return build_result(
        fid="cross_entropy_dist",
        name="Cross Entropy (Distributions)",
        expression="-Sum(p * log(q))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "p_true": kwargs.get("p_true", p_true),
            "q_pred": kwargs.get("q_pred", q_pred),
        },
    )

@formula("conditional_variance", "Conditional Variance", "E[X^2|Y] - E[X|Y]^2", DOMAIN_KEY, unit="")
def conditional_variance(e_x2_given_y: float | None = None, e_x_given_y: float | None = None, **kwargs):
    return build_result(
        fid="conditional_variance",
        name="Conditional Variance",
        expression="E[X^2|Y] - E[X|Y]^2",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "e_x2_given_y": kwargs.get("e_x2_given_y", e_x2_given_y),
            "e_x_given_y": kwargs.get("e_x_given_y", e_x_given_y),
        },
    )

@formula("expected_shortfall_prob", "Tail Expectation", "E[X | X > threshold]", DOMAIN_KEY, unit="")
def expected_shortfall_prob(tail_values: float | None = None, **kwargs):
    return build_result(
        fid="expected_shortfall_prob",
        name="Tail Expectation",
        expression="E[X | X > threshold]",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "tail_values": kwargs.get("tail_values", tail_values),
        },
    )
