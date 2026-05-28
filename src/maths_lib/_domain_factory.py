from __future__ import annotations

from .base import build_formula_callable


def register_domain(module_globals: dict, domain_key: str, domains: dict) -> None:
    block = domains[domain_key]
    module_globals["DOMAIN_KEY"] = domain_key
    module_globals["DOMAIN_TITLE"] = block["title"]
    module_globals["FORMULA_IDS"] = []

    for fid, name, _desc, expr, input_csv in block["formulas"]:
        params = [x.strip() for x in input_csv.split(",") if x.strip()]
        fn = build_formula_callable(fid, name, expr, domain_key, "", params)
        module_globals[fid] = fn
        module_globals["FORMULA_IDS"].append(fid)
