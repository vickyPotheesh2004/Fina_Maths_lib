from .base import build_result, formula

DOMAIN_KEY = "D18_crypto_onchain"
DOMAIN_TITLE = "Crypto On-Chain, Tokenomics & Market Microstructure"
FORMULA_IDS = [
    "realized_cap",
    "mvrv_ratio",
    "nvt_ratio",
    "sopr",
    "hash_price",
    "crypto_signal_1",
    "crypto_signal_2",
    "crypto_signal_3",
    "crypto_signal_4",
    "crypto_signal_5",
    "crypto_signal_6",
    "crypto_signal_7",
    "crypto_signal_8",
    "crypto_signal_9",
    "crypto_signal_10",
    "crypto_signal_11",
    "crypto_signal_12",
    "crypto_signal_13",
    "crypto_signal_14",
    "crypto_signal_15",
    "crypto_signal_16",
    "crypto_signal_17",
    "crypto_signal_18",
    "crypto_signal_19",
    "crypto_signal_20",
    "crypto_signal_21",
    "crypto_signal_22",
    "crypto_signal_23",
    "crypto_signal_24",
    "crypto_signal_25",
    "crypto_signal_26",
    "crypto_signal_27",
    "crypto_signal_28",
    "crypto_signal_29",
    "crypto_signal_30",
    "crypto_signal_31",
    "crypto_signal_32",
    "crypto_signal_33",
    "crypto_signal_34",
    "crypto_signal_35",
    "crypto_signal_36",
    "crypto_signal_37",
    "crypto_signal_38",
    "crypto_signal_39",
    "crypto_signal_40",
    "crypto_signal_41",
    "crypto_signal_42",
    "crypto_signal_43",
    "crypto_signal_44",
    "crypto_signal_45",
    "crypto_signal_46",
    "crypto_signal_47",
    "crypto_signal_48",
    "crypto_signal_49",
    "crypto_signal_50",
    "crypto_signal_51",
    "crypto_signal_52",
    "crypto_signal_53",
    "crypto_signal_54",
    "crypto_signal_55",
]

@formula("realized_cap", "Realized Capitalization", "Sum(utxo_values)", DOMAIN_KEY, unit="")
def realized_cap(utxo_values: float | None = None, **kwargs):
    return build_result(
        fid="realized_cap",
        name="Realized Capitalization",
        expression="Sum(utxo_values)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "utxo_values": kwargs.get("utxo_values", utxo_values),
        },
    )

@formula("mvrv_ratio", "MVRV Ratio", "Market_Cap / Realized_Cap", DOMAIN_KEY, unit="")
def mvrv_ratio(market_cap: float | None = None, realized_cap: float | None = None, **kwargs):
    return build_result(
        fid="mvrv_ratio",
        name="MVRV Ratio",
        expression="Market_Cap / Realized_Cap",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "market_cap": kwargs.get("market_cap", market_cap),
            "realized_cap": kwargs.get("realized_cap", realized_cap),
        },
    )

@formula("nvt_ratio", "NVT Ratio", "Market_Cap / Tx_Volume", DOMAIN_KEY, unit="")
def nvt_ratio(market_cap: float | None = None, tx_volume: float | None = None, **kwargs):
    return build_result(
        fid="nvt_ratio",
        name="NVT Ratio",
        expression="Market_Cap / Tx_Volume",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "market_cap": kwargs.get("market_cap", market_cap),
            "tx_volume": kwargs.get("tx_volume", tx_volume),
        },
    )

@formula("sopr", "Spent Output Profit Ratio", "Spent_Value / Created_Value", DOMAIN_KEY, unit="")
def sopr(spent_value: float | None = None, created_value: float | None = None, **kwargs):
    return build_result(
        fid="sopr",
        name="Spent Output Profit Ratio",
        expression="Spent_Value / Created_Value",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "spent_value": kwargs.get("spent_value", spent_value),
            "created_value": kwargs.get("created_value", created_value),
        },
    )

@formula("hash_price", "Hash Price", "Miner_Revenue / Hashrate", DOMAIN_KEY, unit="")
def hash_price(miner_revenue: float | None = None, hashrate: float | None = None, **kwargs):
    return build_result(
        fid="hash_price",
        name="Hash Price",
        expression="Miner_Revenue / Hashrate",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "miner_revenue": kwargs.get("miner_revenue", miner_revenue),
            "hashrate": kwargs.get("hashrate", hashrate),
        },
    )

@formula("crypto_signal_1", "Crypto Signal 1", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_1(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_1",
        name="Crypto Signal 1",
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

@formula("crypto_signal_2", "Crypto Signal 2", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_2(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_2",
        name="Crypto Signal 2",
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

@formula("crypto_signal_3", "Crypto Signal 3", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_3(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_3",
        name="Crypto Signal 3",
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

@formula("crypto_signal_4", "Crypto Signal 4", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_4(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_4",
        name="Crypto Signal 4",
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

@formula("crypto_signal_5", "Crypto Signal 5", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_5(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_5",
        name="Crypto Signal 5",
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

@formula("crypto_signal_6", "Crypto Signal 6", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_6(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_6",
        name="Crypto Signal 6",
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

@formula("crypto_signal_7", "Crypto Signal 7", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_7(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_7",
        name="Crypto Signal 7",
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

@formula("crypto_signal_8", "Crypto Signal 8", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_8(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_8",
        name="Crypto Signal 8",
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

@formula("crypto_signal_9", "Crypto Signal 9", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_9(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_9",
        name="Crypto Signal 9",
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

@formula("crypto_signal_10", "Crypto Signal 10", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_10(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_10",
        name="Crypto Signal 10",
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

@formula("crypto_signal_11", "Crypto Signal 11", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_11(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_11",
        name="Crypto Signal 11",
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

@formula("crypto_signal_12", "Crypto Signal 12", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_12(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_12",
        name="Crypto Signal 12",
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

@formula("crypto_signal_13", "Crypto Signal 13", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_13(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_13",
        name="Crypto Signal 13",
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

@formula("crypto_signal_14", "Crypto Signal 14", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_14(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_14",
        name="Crypto Signal 14",
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

@formula("crypto_signal_15", "Crypto Signal 15", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_15(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_15",
        name="Crypto Signal 15",
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

@formula("crypto_signal_16", "Crypto Signal 16", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_16(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_16",
        name="Crypto Signal 16",
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

@formula("crypto_signal_17", "Crypto Signal 17", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_17(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_17",
        name="Crypto Signal 17",
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

@formula("crypto_signal_18", "Crypto Signal 18", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_18(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_18",
        name="Crypto Signal 18",
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

@formula("crypto_signal_19", "Crypto Signal 19", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_19(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_19",
        name="Crypto Signal 19",
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

@formula("crypto_signal_20", "Crypto Signal 20", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_20(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_20",
        name="Crypto Signal 20",
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

@formula("crypto_signal_21", "Crypto Signal 21", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_21(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_21",
        name="Crypto Signal 21",
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

@formula("crypto_signal_22", "Crypto Signal 22", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_22(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_22",
        name="Crypto Signal 22",
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

@formula("crypto_signal_23", "Crypto Signal 23", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_23(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_23",
        name="Crypto Signal 23",
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

@formula("crypto_signal_24", "Crypto Signal 24", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_24(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_24",
        name="Crypto Signal 24",
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

@formula("crypto_signal_25", "Crypto Signal 25", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_25(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_25",
        name="Crypto Signal 25",
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

@formula("crypto_signal_26", "Crypto Signal 26", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_26(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_26",
        name="Crypto Signal 26",
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

@formula("crypto_signal_27", "Crypto Signal 27", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_27(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_27",
        name="Crypto Signal 27",
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

@formula("crypto_signal_28", "Crypto Signal 28", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_28(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_28",
        name="Crypto Signal 28",
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

@formula("crypto_signal_29", "Crypto Signal 29", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_29(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_29",
        name="Crypto Signal 29",
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

@formula("crypto_signal_30", "Crypto Signal 30", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_30(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_30",
        name="Crypto Signal 30",
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

@formula("crypto_signal_31", "Crypto Signal 31", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_31(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_31",
        name="Crypto Signal 31",
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

@formula("crypto_signal_32", "Crypto Signal 32", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_32(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_32",
        name="Crypto Signal 32",
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

@formula("crypto_signal_33", "Crypto Signal 33", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_33(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_33",
        name="Crypto Signal 33",
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

@formula("crypto_signal_34", "Crypto Signal 34", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_34(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_34",
        name="Crypto Signal 34",
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

@formula("crypto_signal_35", "Crypto Signal 35", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_35(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_35",
        name="Crypto Signal 35",
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

@formula("crypto_signal_36", "Crypto Signal 36", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_36(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_36",
        name="Crypto Signal 36",
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

@formula("crypto_signal_37", "Crypto Signal 37", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_37(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_37",
        name="Crypto Signal 37",
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

@formula("crypto_signal_38", "Crypto Signal 38", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_38(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_38",
        name="Crypto Signal 38",
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

@formula("crypto_signal_39", "Crypto Signal 39", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_39(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_39",
        name="Crypto Signal 39",
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

@formula("crypto_signal_40", "Crypto Signal 40", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_40(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_40",
        name="Crypto Signal 40",
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

@formula("crypto_signal_41", "Crypto Signal 41", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_41(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_41",
        name="Crypto Signal 41",
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

@formula("crypto_signal_42", "Crypto Signal 42", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_42(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_42",
        name="Crypto Signal 42",
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

@formula("crypto_signal_43", "Crypto Signal 43", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_43(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_43",
        name="Crypto Signal 43",
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

@formula("crypto_signal_44", "Crypto Signal 44", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_44(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_44",
        name="Crypto Signal 44",
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

@formula("crypto_signal_45", "Crypto Signal 45", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_45(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_45",
        name="Crypto Signal 45",
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

@formula("crypto_signal_46", "Crypto Signal 46", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_46(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_46",
        name="Crypto Signal 46",
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

@formula("crypto_signal_47", "Crypto Signal 47", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_47(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_47",
        name="Crypto Signal 47",
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

@formula("crypto_signal_48", "Crypto Signal 48", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_48(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_48",
        name="Crypto Signal 48",
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

@formula("crypto_signal_49", "Crypto Signal 49", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_49(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_49",
        name="Crypto Signal 49",
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

@formula("crypto_signal_50", "Crypto Signal 50", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_50(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_50",
        name="Crypto Signal 50",
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

@formula("crypto_signal_51", "Crypto Signal 51", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_51(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_51",
        name="Crypto Signal 51",
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

@formula("crypto_signal_52", "Crypto Signal 52", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_52(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_52",
        name="Crypto Signal 52",
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

@formula("crypto_signal_53", "Crypto Signal 53", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_53(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_53",
        name="Crypto Signal 53",
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

@formula("crypto_signal_54", "Crypto Signal 54", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_54(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_54",
        name="Crypto Signal 54",
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

@formula("crypto_signal_55", "Crypto Signal 55", "w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5", DOMAIN_KEY, unit="")
def crypto_signal_55(x1: float | None = None, x2: float | None = None, x3: float | None = None, x4: float | None = None, x5: float | None = None, w1: float | None = None, w2: float | None = None, w3: float | None = None, w4: float | None = None, w5: float | None = None, **kwargs):
    return build_result(
        fid="crypto_signal_55",
        name="Crypto Signal 55",
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
