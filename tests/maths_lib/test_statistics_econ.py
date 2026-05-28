import pytest

import maths_lib as ml

FORMULA_IDS = ['arithmetic_mean', 'geometric_mean', 'harmonic_mean', 'weighted_mean', 'median', 'mode', 'range_stat', 'variance_population', 'variance_sample', 'standard_deviation_pop', 'standard_deviation_sample', 'coefficient_variation', 'skewness', 'kurtosis', 'excess_kurtosis', 'covariance_stat', 'pearson_correlation', 'spearman_correlation', 'linear_regression_beta', 'linear_regression_alpha', 'r_squared', 'adjusted_r_squared', 'standard_error', 'standard_error_regression', 't_statistic', 'z_score', 'confidence_interval', 'chi_square_stat', 'f_statistic', 'percentile', 'quartile', 'interquartile_range', 'autocorrelation', 'moving_average_forecast', 'exponential_smoothing', 'holt_linear_trend', 'holt_winters', 'ar1_model', 'durbin_watson', 'mean_absolute_error', 'mean_squared_error', 'rmse', 'mape', 'theil_u', 'garch_volatility']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_statistics_econ_count_matches_registry():
    m = __import__(f"maths_lib.statistics_econ", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 45


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_statistics_econ_all_formulas_execute_deterministically(fid):
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
