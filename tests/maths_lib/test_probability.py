import pytest

import maths_lib as ml

FORMULA_IDS = ['normal_pdf', 'normal_cdf', 'standard_normal_pdf', 'binomial_pmf', 'poisson_pmf', 'exponential_pdf', 'uniform_pdf', 'bernoulli_pmf', 'geometric_pmf', 'negative_binomial_pmf', 'beta_pdf', 'gamma_pdf', 'lognormal_pdf', 'student_t_pdf', 'chi2_pdf', 'f_distribution_pdf', 'weibull_pdf', 'conditional_probability', 'bayes_theorem', 'joint_probability_independent', 'union_probability', 'complement_probability', 'total_probability', 'odds_from_probability', 'probability_from_odds', 'permutations_count', 'combinations_count', 'multinomial_coefficient', 'permutations_with_repetition', 'circular_permutations', 'expected_value_discrete', 'variance_discrete', 'covariance_random_vars', 'correlation_random_vars', 'moment_generating', 'variance_sum_independent', 'markov_steady_state', 'poisson_process_prob', 'geometric_brownian_motion', 'random_walk_position', 'chebyshev_inequality', 'markov_inequality', 'central_limit_theorem', 'bayesian_posterior', 'law_large_numbers_error', 'hypergeometric_pmf', 'multinomial_pmf', 'cauchy_pdf', 'pareto_pdf', 'survival_function', 'hazard_rate', 'entropy_shannon', 'cross_entropy_dist', 'conditional_variance', 'expected_shortfall_prob']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_probability_count_matches_registry():
    m = __import__(f"maths_lib.probability", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 55


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_probability_all_formulas_execute_deterministically(fid):
    fn = ml.FORMULA_REGISTRY[fid]
    kwargs = _inputs_for(fid)
    r1 = fn(**kwargs)
    r2 = fn(**kwargs)
    assert r1.formula_id == fid
    assert r1.formula_name
    assert r1.expression
    assert r1.domain
    assert r1.inputs_used == kwargs
    assert r1.value == r2.value
    assert r1.valid == r2.valid
