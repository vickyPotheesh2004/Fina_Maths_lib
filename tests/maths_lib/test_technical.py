import pytest

import maths_lib as ml

FORMULA_IDS = ['sma', 'ema', 'wma', 'dema', 'tema', 'hma', 'kama', 'vwma', 'vwap', 'atr', 'true_range', 'bollinger_upper', 'bollinger_lower', 'bollinger_width', 'bollinger_percent_b', 'keltner_upper', 'keltner_lower', 'donchian_upper', 'donchian_lower', 'donchian_middle', 'rsi', 'stochastic_k', 'stochastic_d', 'macd_line', 'macd_signal', 'macd_histogram', 'cci', 'williams_r', 'roc', 'momentum', 'mfi', 'adx', 'plus_di', 'minus_di', 'aroon_up', 'aroon_down', 'aroon_oscillator', 'parabolic_sar', 'obv', 'chaikin_money_flow', 'accumulation_distribution', 'ichimoku_tenkan', 'ichimoku_kijun', 'ichimoku_senkou_a', 'ichimoku_senkou_b', 'linear_regression_slope', 'standard_deviation', 'historical_volatility', 'variance', 'beta_coefficient', 'correlation_coefficient', 'z_score_price', 'price_oscillator', 'trix', 'ultimate_oscillator', 'awesome_oscillator', 'dpo', 'vortex_positive', 'vortex_negative', 'mass_index', 'force_index', 'ease_of_movement', 'klinger_oscillator', 'chande_momentum', 'elder_ray_bull', 'elder_ray_bear', 'choppiness_index', 'fisher_transform', 'coppock_curve', 'kst_oscillator', 'ppo', 'pvo', 'relative_vigor_index', 'stochastic_rsi', 'supertrend', 'pivot_point', 'pivot_resistance_1', 'pivot_support_1', 'fibonacci_retracement', 'chandelier_exit_long']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_technical_count_matches_registry():
    m = __import__(f"maths_lib.technical", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 80


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_technical_all_formulas_execute_deterministically(fid):
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
