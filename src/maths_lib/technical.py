from .base import build_result, formula

DOMAIN_KEY = "D04_technical"
DOMAIN_TITLE = "Time-Series & Technical Analysis"
FORMULA_IDS = [
    "sma",
    "ema",
    "wma",
    "dema",
    "tema",
    "hma",
    "kama",
    "vwma",
    "vwap",
    "atr",
    "true_range",
    "bollinger_upper",
    "bollinger_lower",
    "bollinger_width",
    "bollinger_percent_b",
    "keltner_upper",
    "keltner_lower",
    "donchian_upper",
    "donchian_lower",
    "donchian_middle",
    "rsi",
    "stochastic_k",
    "stochastic_d",
    "macd_line",
    "macd_signal",
    "macd_histogram",
    "cci",
    "williams_r",
    "roc",
    "momentum",
    "mfi",
    "adx",
    "plus_di",
    "minus_di",
    "aroon_up",
    "aroon_down",
    "aroon_oscillator",
    "parabolic_sar",
    "obv",
    "chaikin_money_flow",
    "accumulation_distribution",
    "ichimoku_tenkan",
    "ichimoku_kijun",
    "ichimoku_senkou_a",
    "ichimoku_senkou_b",
    "linear_regression_slope",
    "standard_deviation",
    "historical_volatility",
    "variance",
    "beta_coefficient",
    "correlation_coefficient",
    "z_score_price",
    "price_oscillator",
    "trix",
    "ultimate_oscillator",
    "awesome_oscillator",
    "dpo",
    "vortex_positive",
    "vortex_negative",
    "mass_index",
    "force_index",
    "ease_of_movement",
    "klinger_oscillator",
    "chande_momentum",
    "elder_ray_bull",
    "elder_ray_bear",
    "choppiness_index",
    "fisher_transform",
    "coppock_curve",
    "kst_oscillator",
    "ppo",
    "pvo",
    "relative_vigor_index",
    "stochastic_rsi",
    "supertrend",
    "pivot_point",
    "pivot_resistance_1",
    "pivot_support_1",
    "fibonacci_retracement",
    "chandelier_exit_long",
]

@formula("sma", "Simple Moving Average", "Sum(Prices[-n:]) / n", DOMAIN_KEY, unit="")
def sma(prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="sma",
        name="Simple Moving Average",
        expression="Sum(Prices[-n:]) / n",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("ema", "Exponential Moving Average", "Price*k + EMA_prev*(1-k), k=2/(n+1)", DOMAIN_KEY, unit="")
def ema(prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="ema",
        name="Exponential Moving Average",
        expression="Price*k + EMA_prev*(1-k), k=2/(n+1)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("wma", "Weighted Moving Average", "Sum(Price_i * Weight_i) / Sum(Weights)", DOMAIN_KEY, unit="")
def wma(prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="wma",
        name="Weighted Moving Average",
        expression="Sum(Price_i * Weight_i) / Sum(Weights)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("dema", "Double EMA", "2*EMA - EMA(EMA)", DOMAIN_KEY, unit="")
def dema(prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="dema",
        name="Double EMA",
        expression="2*EMA - EMA(EMA)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("tema", "Triple EMA", "3*EMA1 - 3*EMA2 + EMA3", DOMAIN_KEY, unit="")
def tema(prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="tema",
        name="Triple EMA",
        expression="3*EMA1 - 3*EMA2 + EMA3",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("hma", "Hull Moving Average", "WMA(2*WMA(n/2) - WMA(n), sqrt(n))", DOMAIN_KEY, unit="")
def hma(prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="hma",
        name="Hull Moving Average",
        expression="WMA(2*WMA(n/2) - WMA(n), sqrt(n))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("kama", "Kaufman Adaptive MA", "KAMA_prev + SC*(Price - KAMA_prev)", DOMAIN_KEY, unit="")
def kama(prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="kama",
        name="Kaufman Adaptive MA",
        expression="KAMA_prev + SC*(Price - KAMA_prev)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("vwma", "Volume-Weighted MA", "Sum(Price*Volume) / Sum(Volume)", DOMAIN_KEY, unit="")
def vwma(prices: float | None = None, volumes: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="vwma",
        name="Volume-Weighted MA",
        expression="Sum(Price*Volume) / Sum(Volume)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "volumes": kwargs.get("volumes", volumes),
            "period": kwargs.get("period", period),
        },
    )

@formula("vwap", "Volume-Weighted Avg Price", "Sum(Typical_Price*Volume) / Sum(Volume)", DOMAIN_KEY, unit="")
def vwap(highs: float | None = None, lows: float | None = None, closes: float | None = None, volumes: float | None = None, **kwargs):
    return build_result(
        fid="vwap",
        name="Volume-Weighted Avg Price",
        expression="Sum(Typical_Price*Volume) / Sum(Volume)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "closes": kwargs.get("closes", closes),
            "volumes": kwargs.get("volumes", volumes),
        },
    )

@formula("atr", "Average True Range", "MA(True_Range, n)", DOMAIN_KEY, unit="")
def atr(highs: float | None = None, lows: float | None = None, closes: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="atr",
        name="Average True Range",
        expression="MA(True_Range, n)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "closes": kwargs.get("closes", closes),
            "period": kwargs.get("period", period),
        },
    )

@formula("true_range", "True Range", "max(H-L, abs(H-Cp), abs(L-Cp))", DOMAIN_KEY, unit="")
def true_range(high: float | None = None, low: float | None = None, prev_close: float | None = None, **kwargs):
    return build_result(
        fid="true_range",
        name="True Range",
        expression="max(H-L, abs(H-Cp), abs(L-Cp))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "high": kwargs.get("high", high),
            "low": kwargs.get("low", low),
            "prev_close": kwargs.get("prev_close", prev_close),
        },
    )

@formula("bollinger_upper", "Bollinger Upper Band", "SMA + 2*StdDev", DOMAIN_KEY, unit="")
def bollinger_upper(prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="bollinger_upper",
        name="Bollinger Upper Band",
        expression="SMA + 2*StdDev",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("bollinger_lower", "Bollinger Lower Band", "SMA - 2*StdDev", DOMAIN_KEY, unit="")
def bollinger_lower(prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="bollinger_lower",
        name="Bollinger Lower Band",
        expression="SMA - 2*StdDev",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("bollinger_width", "Bollinger Band Width", "(Upper - Lower) / SMA", DOMAIN_KEY, unit="")
def bollinger_width(prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="bollinger_width",
        name="Bollinger Band Width",
        expression="(Upper - Lower) / SMA",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("bollinger_percent_b", "Bollinger %B", "(Price - Lower) / (Upper - Lower)", DOMAIN_KEY, unit="")
def bollinger_percent_b(price: float | None = None, upper: float | None = None, lower: float | None = None, **kwargs):
    return build_result(
        fid="bollinger_percent_b",
        name="Bollinger %B",
        expression="(Price - Lower) / (Upper - Lower)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "price": kwargs.get("price", price),
            "upper": kwargs.get("upper", upper),
            "lower": kwargs.get("lower", lower),
        },
    )

@formula("keltner_upper", "Keltner Upper Channel", "EMA + Mult*ATR", DOMAIN_KEY, unit="")
def keltner_upper(prices: float | None = None, highs: float | None = None, lows: float | None = None, period: float | None = None, multiplier: float | None = None, **kwargs):
    return build_result(
        fid="keltner_upper",
        name="Keltner Upper Channel",
        expression="EMA + Mult*ATR",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "period": kwargs.get("period", period),
            "multiplier": kwargs.get("multiplier", multiplier),
        },
    )

@formula("keltner_lower", "Keltner Lower Channel", "EMA - Mult*ATR", DOMAIN_KEY, unit="")
def keltner_lower(prices: float | None = None, highs: float | None = None, lows: float | None = None, period: float | None = None, multiplier: float | None = None, **kwargs):
    return build_result(
        fid="keltner_lower",
        name="Keltner Lower Channel",
        expression="EMA - Mult*ATR",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "period": kwargs.get("period", period),
            "multiplier": kwargs.get("multiplier", multiplier),
        },
    )

@formula("donchian_upper", "Donchian Upper Channel", "max(Highs[-n:])", DOMAIN_KEY, unit="")
def donchian_upper(highs: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="donchian_upper",
        name="Donchian Upper Channel",
        expression="max(Highs[-n:])",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "period": kwargs.get("period", period),
        },
    )

@formula("donchian_lower", "Donchian Lower Channel", "min(Lows[-n:])", DOMAIN_KEY, unit="")
def donchian_lower(lows: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="donchian_lower",
        name="Donchian Lower Channel",
        expression="min(Lows[-n:])",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "lows": kwargs.get("lows", lows),
            "period": kwargs.get("period", period),
        },
    )

@formula("donchian_middle", "Donchian Middle", "(Upper + Lower) / 2", DOMAIN_KEY, unit="")
def donchian_middle(highs: float | None = None, lows: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="donchian_middle",
        name="Donchian Middle",
        expression="(Upper + Lower) / 2",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "period": kwargs.get("period", period),
        },
    )

@formula("rsi", "Relative Strength Index", "100 - 100/(1 + AvgGain/AvgLoss)", DOMAIN_KEY, unit="")
def rsi(prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="rsi",
        name="Relative Strength Index",
        expression="100 - 100/(1 + AvgGain/AvgLoss)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("stochastic_k", "Stochastic %K", "(Close - LowN) / (HighN - LowN) * 100", DOMAIN_KEY, unit="")
def stochastic_k(highs: float | None = None, lows: float | None = None, closes: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="stochastic_k",
        name="Stochastic %K",
        expression="(Close - LowN) / (HighN - LowN) * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "closes": kwargs.get("closes", closes),
            "period": kwargs.get("period", period),
        },
    )

@formula("stochastic_d", "Stochastic %D", "SMA(%K, 3)", DOMAIN_KEY, unit="")
def stochastic_d(stochastic_k: float | None = None, smoothing: float | None = None, **kwargs):
    return build_result(
        fid="stochastic_d",
        name="Stochastic %D",
        expression="SMA(%K, 3)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "stochastic_k": kwargs.get("stochastic_k", stochastic_k),
            "smoothing": kwargs.get("smoothing", smoothing),
        },
    )

@formula("macd_line", "MACD Line", "EMA(12) - EMA(26)", DOMAIN_KEY, unit="")
def macd_line(prices: float | None = None, **kwargs):
    return build_result(
        fid="macd_line",
        name="MACD Line",
        expression="EMA(12) - EMA(26)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
        },
    )

@formula("macd_signal", "MACD Signal Line", "EMA(MACD, 9)", DOMAIN_KEY, unit="")
def macd_signal(macd_line: float | None = None, **kwargs):
    return build_result(
        fid="macd_signal",
        name="MACD Signal Line",
        expression="EMA(MACD, 9)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "macd_line": kwargs.get("macd_line", macd_line),
        },
    )

@formula("macd_histogram", "MACD Histogram", "MACD_Line - Signal_Line", DOMAIN_KEY, unit="")
def macd_histogram(macd_line: float | None = None, signal_line: float | None = None, **kwargs):
    return build_result(
        fid="macd_histogram",
        name="MACD Histogram",
        expression="MACD_Line - Signal_Line",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "macd_line": kwargs.get("macd_line", macd_line),
            "signal_line": kwargs.get("signal_line", signal_line),
        },
    )

@formula("cci", "Commodity Channel Index", "(TP - SMA_TP) / (0.015*MeanDev)", DOMAIN_KEY, unit="")
def cci(highs: float | None = None, lows: float | None = None, closes: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="cci",
        name="Commodity Channel Index",
        expression="(TP - SMA_TP) / (0.015*MeanDev)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "closes": kwargs.get("closes", closes),
            "period": kwargs.get("period", period),
        },
    )

@formula("williams_r", "Williams %R", "(HighN - Close) / (HighN - LowN) * -100", DOMAIN_KEY, unit="")
def williams_r(highs: float | None = None, lows: float | None = None, closes: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="williams_r",
        name="Williams %R",
        expression="(HighN - Close) / (HighN - LowN) * -100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "closes": kwargs.get("closes", closes),
            "period": kwargs.get("period", period),
        },
    )

@formula("roc", "Rate of Change %", "(Price - Price_n) / Price_n * 100", DOMAIN_KEY, unit="")
def roc(prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="roc",
        name="Rate of Change %",
        expression="(Price - Price_n) / Price_n * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("momentum", "Momentum", "Price - Price_n", DOMAIN_KEY, unit="")
def momentum(prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="momentum",
        name="Momentum",
        expression="Price - Price_n",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("mfi", "Money Flow Index", "100 - 100/(1 + PosFlow/NegFlow)", DOMAIN_KEY, unit="")
def mfi(highs: float | None = None, lows: float | None = None, closes: float | None = None, volumes: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="mfi",
        name="Money Flow Index",
        expression="100 - 100/(1 + PosFlow/NegFlow)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "closes": kwargs.get("closes", closes),
            "volumes": kwargs.get("volumes", volumes),
            "period": kwargs.get("period", period),
        },
    )

@formula("adx", "Average Directional Index", "MA(DX, n)", DOMAIN_KEY, unit="")
def adx(highs: float | None = None, lows: float | None = None, closes: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="adx",
        name="Average Directional Index",
        expression="MA(DX, n)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "closes": kwargs.get("closes", closes),
            "period": kwargs.get("period", period),
        },
    )

@formula("plus_di", "Plus Directional Indicator", "100 * EMA(+DM) / ATR", DOMAIN_KEY, unit="")
def plus_di(highs: float | None = None, lows: float | None = None, closes: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="plus_di",
        name="Plus Directional Indicator",
        expression="100 * EMA(+DM) / ATR",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "closes": kwargs.get("closes", closes),
            "period": kwargs.get("period", period),
        },
    )

@formula("minus_di", "Minus Directional Indicator", "100 * EMA(-DM) / ATR", DOMAIN_KEY, unit="")
def minus_di(highs: float | None = None, lows: float | None = None, closes: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="minus_di",
        name="Minus Directional Indicator",
        expression="100 * EMA(-DM) / ATR",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "closes": kwargs.get("closes", closes),
            "period": kwargs.get("period", period),
        },
    )

@formula("aroon_up", "Aroon Up", "(n - PeriodsSinceHigh) / n * 100", DOMAIN_KEY, unit="")
def aroon_up(highs: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="aroon_up",
        name="Aroon Up",
        expression="(n - PeriodsSinceHigh) / n * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "period": kwargs.get("period", period),
        },
    )

@formula("aroon_down", "Aroon Down", "(n - PeriodsSinceLow) / n * 100", DOMAIN_KEY, unit="")
def aroon_down(lows: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="aroon_down",
        name="Aroon Down",
        expression="(n - PeriodsSinceLow) / n * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "lows": kwargs.get("lows", lows),
            "period": kwargs.get("period", period),
        },
    )

@formula("aroon_oscillator", "Aroon Oscillator", "Aroon_Up - Aroon_Down", DOMAIN_KEY, unit="")
def aroon_oscillator(highs: float | None = None, lows: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="aroon_oscillator",
        name="Aroon Oscillator",
        expression="Aroon_Up - Aroon_Down",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "period": kwargs.get("period", period),
        },
    )

@formula("parabolic_sar", "Parabolic SAR", "SAR_prev + AF*(EP - SAR_prev)", DOMAIN_KEY, unit="")
def parabolic_sar(highs: float | None = None, lows: float | None = None, acceleration: float | None = None, **kwargs):
    return build_result(
        fid="parabolic_sar",
        name="Parabolic SAR",
        expression="SAR_prev + AF*(EP - SAR_prev)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "acceleration": kwargs.get("acceleration", acceleration),
        },
    )

@formula("obv", "On-Balance Volume", "Sum(Volume * Sign(Price_Change))", DOMAIN_KEY, unit="")
def obv(closes: float | None = None, volumes: float | None = None, **kwargs):
    return build_result(
        fid="obv",
        name="On-Balance Volume",
        expression="Sum(Volume * Sign(Price_Change))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "closes": kwargs.get("closes", closes),
            "volumes": kwargs.get("volumes", volumes),
        },
    )

@formula("chaikin_money_flow", "Chaikin Money Flow", "Sum(MFV) / Sum(Volume)", DOMAIN_KEY, unit="")
def chaikin_money_flow(highs: float | None = None, lows: float | None = None, closes: float | None = None, volumes: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="chaikin_money_flow",
        name="Chaikin Money Flow",
        expression="Sum(MFV) / Sum(Volume)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "closes": kwargs.get("closes", closes),
            "volumes": kwargs.get("volumes", volumes),
            "period": kwargs.get("period", period),
        },
    )

@formula("accumulation_distribution", "Accumulation/Distribution", "Prev_AD + MFV", DOMAIN_KEY, unit="")
def accumulation_distribution(highs: float | None = None, lows: float | None = None, closes: float | None = None, volumes: float | None = None, **kwargs):
    return build_result(
        fid="accumulation_distribution",
        name="Accumulation/Distribution",
        expression="Prev_AD + MFV",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "closes": kwargs.get("closes", closes),
            "volumes": kwargs.get("volumes", volumes),
        },
    )

@formula("ichimoku_tenkan", "Ichimoku Tenkan-sen", "(High9 + Low9) / 2", DOMAIN_KEY, unit="")
def ichimoku_tenkan(highs: float | None = None, lows: float | None = None, **kwargs):
    return build_result(
        fid="ichimoku_tenkan",
        name="Ichimoku Tenkan-sen",
        expression="(High9 + Low9) / 2",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
        },
    )

@formula("ichimoku_kijun", "Ichimoku Kijun-sen", "(High26 + Low26) / 2", DOMAIN_KEY, unit="")
def ichimoku_kijun(highs: float | None = None, lows: float | None = None, **kwargs):
    return build_result(
        fid="ichimoku_kijun",
        name="Ichimoku Kijun-sen",
        expression="(High26 + Low26) / 2",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
        },
    )

@formula("ichimoku_senkou_a", "Ichimoku Senkou Span A", "(Tenkan + Kijun) / 2", DOMAIN_KEY, unit="")
def ichimoku_senkou_a(tenkan: float | None = None, kijun: float | None = None, **kwargs):
    return build_result(
        fid="ichimoku_senkou_a",
        name="Ichimoku Senkou Span A",
        expression="(Tenkan + Kijun) / 2",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "tenkan": kwargs.get("tenkan", tenkan),
            "kijun": kwargs.get("kijun", kijun),
        },
    )

@formula("ichimoku_senkou_b", "Ichimoku Senkou Span B", "(High52 + Low52) / 2", DOMAIN_KEY, unit="")
def ichimoku_senkou_b(highs: float | None = None, lows: float | None = None, **kwargs):
    return build_result(
        fid="ichimoku_senkou_b",
        name="Ichimoku Senkou Span B",
        expression="(High52 + Low52) / 2",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
        },
    )

@formula("linear_regression_slope", "Linear Regression Slope", "Slope of best-fit line", DOMAIN_KEY, unit="")
def linear_regression_slope(prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="linear_regression_slope",
        name="Linear Regression Slope",
        expression="Slope of best-fit line",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("standard_deviation", "Rolling Standard Deviation", "sqrt(Sum((x-mean)^2)/n)", DOMAIN_KEY, unit="")
def standard_deviation(prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="standard_deviation",
        name="Rolling Standard Deviation",
        expression="sqrt(Sum((x-mean)^2)/n)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("historical_volatility", "Historical Volatility %", "StdDev(LogReturns) * sqrt(252)", DOMAIN_KEY, unit="")
def historical_volatility(prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="historical_volatility",
        name="Historical Volatility %",
        expression="StdDev(LogReturns) * sqrt(252)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("variance", "Rolling Variance", "Sum((x-mean)^2) / n", DOMAIN_KEY, unit="")
def variance(prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="variance",
        name="Rolling Variance",
        expression="Sum((x-mean)^2) / n",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("beta_coefficient", "Beta Coefficient", "Cov(Stock,Market) / Var(Market)", DOMAIN_KEY, unit="")
def beta_coefficient(stock_returns: float | None = None, market_returns: float | None = None, **kwargs):
    return build_result(
        fid="beta_coefficient",
        name="Beta Coefficient",
        expression="Cov(Stock,Market) / Var(Market)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "stock_returns": kwargs.get("stock_returns", stock_returns),
            "market_returns": kwargs.get("market_returns", market_returns),
        },
    )

@formula("correlation_coefficient", "Correlation Coefficient", "Cov(X,Y) / (StdX * StdY)", DOMAIN_KEY, unit="")
def correlation_coefficient(series_x: float | None = None, series_y: float | None = None, **kwargs):
    return build_result(
        fid="correlation_coefficient",
        name="Correlation Coefficient",
        expression="Cov(X,Y) / (StdX * StdY)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "series_x": kwargs.get("series_x", series_x),
            "series_y": kwargs.get("series_y", series_y),
        },
    )

@formula("z_score_price", "Price Z-Score", "(Price - Mean) / StdDev", DOMAIN_KEY, unit="")
def z_score_price(prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="z_score_price",
        name="Price Z-Score",
        expression="(Price - Mean) / StdDev",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("price_oscillator", "Price Oscillator %", "(FastMA - SlowMA) / SlowMA * 100", DOMAIN_KEY, unit="")
def price_oscillator(prices: float | None = None, fast: float | None = None, slow: float | None = None, **kwargs):
    return build_result(
        fid="price_oscillator",
        name="Price Oscillator %",
        expression="(FastMA - SlowMA) / SlowMA * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "fast": kwargs.get("fast", fast),
            "slow": kwargs.get("slow", slow),
        },
    )

@formula("trix", "TRIX", "ROC of Triple_EMA", DOMAIN_KEY, unit="")
def trix(prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="trix",
        name="TRIX",
        expression="ROC of Triple_EMA",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("ultimate_oscillator", "Ultimate Oscillator", "100 * Weighted_BP_Sum / TR_Sum", DOMAIN_KEY, unit="")
def ultimate_oscillator(highs: float | None = None, lows: float | None = None, closes: float | None = None, **kwargs):
    return build_result(
        fid="ultimate_oscillator",
        name="Ultimate Oscillator",
        expression="100 * Weighted_BP_Sum / TR_Sum",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "closes": kwargs.get("closes", closes),
        },
    )

@formula("awesome_oscillator", "Awesome Oscillator", "SMA(MP,5) - SMA(MP,34)", DOMAIN_KEY, unit="")
def awesome_oscillator(highs: float | None = None, lows: float | None = None, **kwargs):
    return build_result(
        fid="awesome_oscillator",
        name="Awesome Oscillator",
        expression="SMA(MP,5) - SMA(MP,34)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
        },
    )

@formula("dpo", "Detrended Price Oscillator", "Price - SMA_shifted", DOMAIN_KEY, unit="")
def dpo(prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="dpo",
        name="Detrended Price Oscillator",
        expression="Price - SMA_shifted",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("vortex_positive", "Vortex Indicator +VI", "Sum(+VM) / Sum(TR)", DOMAIN_KEY, unit="")
def vortex_positive(highs: float | None = None, lows: float | None = None, closes: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="vortex_positive",
        name="Vortex Indicator +VI",
        expression="Sum(+VM) / Sum(TR)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "closes": kwargs.get("closes", closes),
            "period": kwargs.get("period", period),
        },
    )

@formula("vortex_negative", "Vortex Indicator -VI", "Sum(-VM) / Sum(TR)", DOMAIN_KEY, unit="")
def vortex_negative(highs: float | None = None, lows: float | None = None, closes: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="vortex_negative",
        name="Vortex Indicator -VI",
        expression="Sum(-VM) / Sum(TR)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "closes": kwargs.get("closes", closes),
            "period": kwargs.get("period", period),
        },
    )

@formula("mass_index", "Mass Index", "Sum(EMA9_HL / EMA9_EMA9_HL)", DOMAIN_KEY, unit="")
def mass_index(highs: float | None = None, lows: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="mass_index",
        name="Mass Index",
        expression="Sum(EMA9_HL / EMA9_EMA9_HL)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "period": kwargs.get("period", period),
        },
    )

@formula("force_index", "Force Index", "(Close - Prev_Close) * Volume", DOMAIN_KEY, unit="")
def force_index(closes: float | None = None, volumes: float | None = None, **kwargs):
    return build_result(
        fid="force_index",
        name="Force Index",
        expression="(Close - Prev_Close) * Volume",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "closes": kwargs.get("closes", closes),
            "volumes": kwargs.get("volumes", volumes),
        },
    )

@formula("ease_of_movement", "Ease of Movement", "Distance_Moved / Box_Ratio", DOMAIN_KEY, unit="")
def ease_of_movement(highs: float | None = None, lows: float | None = None, volumes: float | None = None, **kwargs):
    return build_result(
        fid="ease_of_movement",
        name="Ease of Movement",
        expression="Distance_Moved / Box_Ratio",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "volumes": kwargs.get("volumes", volumes),
        },
    )

@formula("klinger_oscillator", "Klinger Oscillator", "EMA34(VF) - EMA55(VF)", DOMAIN_KEY, unit="")
def klinger_oscillator(highs: float | None = None, lows: float | None = None, closes: float | None = None, volumes: float | None = None, **kwargs):
    return build_result(
        fid="klinger_oscillator",
        name="Klinger Oscillator",
        expression="EMA34(VF) - EMA55(VF)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "closes": kwargs.get("closes", closes),
            "volumes": kwargs.get("volumes", volumes),
        },
    )

@formula("chande_momentum", "Chande Momentum Oscillator", "(Su - Sd) / (Su + Sd) * 100", DOMAIN_KEY, unit="")
def chande_momentum(prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="chande_momentum",
        name="Chande Momentum Oscillator",
        expression="(Su - Sd) / (Su + Sd) * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("elder_ray_bull", "Elder Ray Bull Power", "High - EMA", DOMAIN_KEY, unit="")
def elder_ray_bull(highs: float | None = None, prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="elder_ray_bull",
        name="Elder Ray Bull Power",
        expression="High - EMA",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("elder_ray_bear", "Elder Ray Bear Power", "Low - EMA", DOMAIN_KEY, unit="")
def elder_ray_bear(lows: float | None = None, prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="elder_ray_bear",
        name="Elder Ray Bear Power",
        expression="Low - EMA",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "lows": kwargs.get("lows", lows),
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("choppiness_index", "Choppiness Index", "100*log10(SumATR/Range)/log10(n)", DOMAIN_KEY, unit="")
def choppiness_index(highs: float | None = None, lows: float | None = None, closes: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="choppiness_index",
        name="Choppiness Index",
        expression="100*log10(SumATR/Range)/log10(n)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "closes": kwargs.get("closes", closes),
            "period": kwargs.get("period", period),
        },
    )

@formula("fisher_transform", "Fisher Transform", "0.5*ln((1+x)/(1-x))", DOMAIN_KEY, unit="")
def fisher_transform(prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="fisher_transform",
        name="Fisher Transform",
        expression="0.5*ln((1+x)/(1-x))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("coppock_curve", "Coppock Curve", "WMA10(ROC14 + ROC11)", DOMAIN_KEY, unit="")
def coppock_curve(prices: float | None = None, **kwargs):
    return build_result(
        fid="coppock_curve",
        name="Coppock Curve",
        expression="WMA10(ROC14 + ROC11)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
        },
    )

@formula("kst_oscillator", "Know Sure Thing", "Sum(weighted smoothed ROCs)", DOMAIN_KEY, unit="")
def kst_oscillator(prices: float | None = None, **kwargs):
    return build_result(
        fid="kst_oscillator",
        name="Know Sure Thing",
        expression="Sum(weighted smoothed ROCs)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
        },
    )

@formula("ppo", "Percentage Price Oscillator", "(EMA12 - EMA26) / EMA26 * 100", DOMAIN_KEY, unit="")
def ppo(prices: float | None = None, **kwargs):
    return build_result(
        fid="ppo",
        name="Percentage Price Oscillator",
        expression="(EMA12 - EMA26) / EMA26 * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
        },
    )

@formula("pvo", "Percentage Volume Oscillator", "(EMA12_V - EMA26_V) / EMA26_V * 100", DOMAIN_KEY, unit="")
def pvo(volumes: float | None = None, **kwargs):
    return build_result(
        fid="pvo",
        name="Percentage Volume Oscillator",
        expression="(EMA12_V - EMA26_V) / EMA26_V * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "volumes": kwargs.get("volumes", volumes),
        },
    )

@formula("relative_vigor_index", "Relative Vigor Index", "SMA(Close-Open) / SMA(High-Low)", DOMAIN_KEY, unit="")
def relative_vigor_index(opens: float | None = None, highs: float | None = None, lows: float | None = None, closes: float | None = None, **kwargs):
    return build_result(
        fid="relative_vigor_index",
        name="Relative Vigor Index",
        expression="SMA(Close-Open) / SMA(High-Low)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "opens": kwargs.get("opens", opens),
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "closes": kwargs.get("closes", closes),
        },
    )

@formula("stochastic_rsi", "Stochastic RSI", "(RSI - MinRSI) / (MaxRSI - MinRSI)", DOMAIN_KEY, unit="")
def stochastic_rsi(prices: float | None = None, period: float | None = None, **kwargs):
    return build_result(
        fid="stochastic_rsi",
        name="Stochastic RSI",
        expression="(RSI - MinRSI) / (MaxRSI - MinRSI)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "prices": kwargs.get("prices", prices),
            "period": kwargs.get("period", period),
        },
    )

@formula("supertrend", "SuperTrend", "Based on ATR bands", DOMAIN_KEY, unit="")
def supertrend(highs: float | None = None, lows: float | None = None, closes: float | None = None, period: float | None = None, multiplier: float | None = None, **kwargs):
    return build_result(
        fid="supertrend",
        name="SuperTrend",
        expression="Based on ATR bands",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "closes": kwargs.get("closes", closes),
            "period": kwargs.get("period", period),
            "multiplier": kwargs.get("multiplier", multiplier),
        },
    )

@formula("pivot_point", "Pivot Point", "(High + Low + Close) / 3", DOMAIN_KEY, unit="")
def pivot_point(high: float | None = None, low: float | None = None, close: float | None = None, **kwargs):
    return build_result(
        fid="pivot_point",
        name="Pivot Point",
        expression="(High + Low + Close) / 3",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "high": kwargs.get("high", high),
            "low": kwargs.get("low", low),
            "close": kwargs.get("close", close),
        },
    )

@formula("pivot_resistance_1", "Pivot R1", "2*Pivot - Low", DOMAIN_KEY, unit="")
def pivot_resistance_1(pivot: float | None = None, low: float | None = None, **kwargs):
    return build_result(
        fid="pivot_resistance_1",
        name="Pivot R1",
        expression="2*Pivot - Low",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "pivot": kwargs.get("pivot", pivot),
            "low": kwargs.get("low", low),
        },
    )

@formula("pivot_support_1", "Pivot S1", "2*Pivot - High", DOMAIN_KEY, unit="")
def pivot_support_1(pivot: float | None = None, high: float | None = None, **kwargs):
    return build_result(
        fid="pivot_support_1",
        name="Pivot S1",
        expression="2*Pivot - High",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "pivot": kwargs.get("pivot", pivot),
            "high": kwargs.get("high", high),
        },
    )

@formula("fibonacci_retracement", "Fibonacci Retracement", "High - (High-Low)*Ratio", DOMAIN_KEY, unit="")
def fibonacci_retracement(high: float | None = None, low: float | None = None, ratio: float | None = None, **kwargs):
    return build_result(
        fid="fibonacci_retracement",
        name="Fibonacci Retracement",
        expression="High - (High-Low)*Ratio",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "high": kwargs.get("high", high),
            "low": kwargs.get("low", low),
            "ratio": kwargs.get("ratio", ratio),
        },
    )

@formula("chandelier_exit_long", "Chandelier Exit Long", "HighN - ATR*Multiplier", DOMAIN_KEY, unit="")
def chandelier_exit_long(highs: float | None = None, lows: float | None = None, closes: float | None = None, period: float | None = None, multiplier: float | None = None, **kwargs):
    return build_result(
        fid="chandelier_exit_long",
        name="Chandelier Exit Long",
        expression="HighN - ATR*Multiplier",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "highs": kwargs.get("highs", highs),
            "lows": kwargs.get("lows", lows),
            "closes": kwargs.get("closes", closes),
            "period": kwargs.get("period", period),
            "multiplier": kwargs.get("multiplier", multiplier),
        },
    )
