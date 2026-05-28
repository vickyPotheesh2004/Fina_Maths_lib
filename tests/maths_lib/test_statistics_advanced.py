import pytest

import maths_lib as ml

FORMULA_IDS = ['t_test_one_sample', 't_test_two_sample', 'paired_t_test', 'welch_t_test', 'z_test_proportion', 'z_test_mean', 'anova_f_statistic', 'chi2_independence', 'chi2_goodness_of_fit', 'mann_whitney_u', 'wilcoxon_signed_rank', 'kruskal_wallis_h', 'levene_test', 'f_test_variance', 'cohens_d', 'hedges_g', 'eta_squared', 'odds_ratio', 'relative_risk', 'confidence_interval_mean', 'confidence_interval_proportion', 'margin_of_error', 'prediction_interval', 'p_value_from_z', 'logistic_regression_prob', 'multiple_regression_predict', 'ridge_penalty_cost', 'vif', 'partial_correlation', 'durbin_watson_test', 'standardized_residual', 'leverage_hat', 'cooks_distance', 'sample_size_mean', 'sample_size_proportion', 'standard_error_proportion', 'finite_population_correction', 'bootstrap_std_error', 'pooled_variance', 'spearman_rank', 'kendall_tau_b', 'point_biserial', 'shapiro_wilk_stat', 'kolmogorov_smirnov', 'jarque_bera', 'bonferroni_correction', 'benjamini_hochberg', 'tukey_hsd', 'power_analysis', 'kaplan_meier', 'gini_coefficient_stat', 'theil_index', 'cohens_kappa_stat']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_statistics_advanced_count_matches_registry():
    m = __import__(f"maths_lib.statistics_advanced", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 53


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_statistics_advanced_all_formulas_execute_deterministically(fid):
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
