from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional
import math
import re
import statistics


@dataclass
class FormulaResult:
    value: Any
    formula_id: str
    formula_name: str
    expression: str
    inputs_used: Dict[str, Any]
    unit: str = ""
    domain: str = ""
    valid: bool = True
    error: Optional[str] = None


RUNTIME_FORMULA_REGISTRY: Dict[str, Dict[str, Any]] = {}


def formula(fid: str, name: str, expression: str, domain: str, unit: str = ""):
    def _wrap(fn):
        RUNTIME_FORMULA_REGISTRY[fid] = {
            "fn": fn,
            "name": name,
            "expression": expression,
            "domain": domain,
            "unit": unit,
            "inputs": list(fn.__code__.co_varnames[:fn.__code__.co_argcount]),
        }
        return fn
    return _wrap


def safe_div(numerator: Any, denominator: Any):
    if denominator in (0, None):
        return None
    return numerator / denominator


def _sum_fn(x):
    if isinstance(x, (list, tuple)):
        return float(sum(x))
    return float(x)


def _mean_fn(x):
    if isinstance(x, (list, tuple)) and len(x) > 0:
        return float(sum(x)) / len(x)
    return float(x)


def _prod_fn(x):
    if isinstance(x, (list, tuple)):
        p = 1.0
        for v in x:
            p *= float(v)
        return p
    return float(x)


def _sqrt_fn(x):
    if x is None or x < 0:
        return None
    return math.sqrt(x)


def _softmax(x):
    if not isinstance(x, (list, tuple)) or not x:
        return 1.0
    exps = [math.exp(v) for v in x]
    d = sum(exps)
    return [v / d for v in exps] if d else [0.0 for _ in exps]


def evaluate_expression(expression: str, inputs: Dict[str, Any]):
    expr = expression.replace("^", "**")
    expr = re.sub(r"\bSum\(", "sum_fn(", expr)
    expr = re.sub(r"\bMean\(", "mean_fn(", expr)
    expr = re.sub(r"\bProd\(", "prod_fn(", expr)
    expr = expr.replace("StdDev", "stddev")
    # Support implicit multiplication often used in formula notation like N(N+1) and )(.
    expr = re.sub(r"(\d)\(", r"\1*(", expr)
    expr = re.sub(r"\)\(", r")*(", expr)

    env = {
        "sum_fn": _sum_fn,
        "mean_fn": _mean_fn,
        "prod_fn": _prod_fn,
        "sqrt": _sqrt_fn,
        "log": math.log,
        "log2": math.log2,
        "exp": math.exp,
        "abs": abs,
        "max": max,
        "min": min,
        "cos": math.cos,
        "sin": math.sin,
        "tan": math.tan,
        "pi": math.pi,
        "e": math.e,
        "softmax": _softmax,
        "stddev": lambda s: statistics.pstdev(s) if isinstance(s, (list, tuple)) and len(s) > 1 else 0.0,
        **inputs,
    }

    try:
        value = eval(expr, {"__builtins__": {}}, env)
        if isinstance(value, complex):
            return None, False, "complex result not supported"
        return value, value is not None, None
    except ZeroDivisionError:
        return None, False, "division by zero"
    except Exception as exc:
        return None, False, f"evaluation error: {exc}"


def build_result(fid: str, name: str, expression: str, domain: str, unit: str, inputs: Dict[str, Any]) -> FormulaResult:
    value, valid, error = evaluate_expression(expression, inputs)
    return FormulaResult(
        value=value,
        formula_id=fid,
        formula_name=name,
        expression=expression,
        inputs_used=inputs,
        unit=unit,
        domain=domain,
        valid=valid,
        error=error,
    )
