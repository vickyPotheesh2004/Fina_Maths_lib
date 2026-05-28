import pytest

import maths_lib as ml

FORMULA_IDS = ['sine', 'cosine', 'tangent', 'arcsine', 'arccosine', 'arctangent', 'atan2', 'degrees_to_radians', 'radians_to_degrees', 'pythagorean', 'law_of_cosines', 'law_of_sines', 'hypotenuse', 'euclidean_distance', 'manhattan_distance', 'cosine_similarity', 'minkowski_distance', 'chebyshev_distance', 'mahalanobis_distance', 'hamming_distance', 'dot_product', 'cross_product_2d', 'vector_magnitude', 'vector_normalize', 'matrix_multiply', 'matrix_transpose', 'matrix_determinant', 'matrix_inverse', 'matrix_trace', 'eigenvalues', 'cholesky_decomposition', 'logarithm_natural', 'logarithm_base10', 'logarithm_base', 'exponential', 'power_function', 'nth_root', 'factorial', 'combination', 'permutation', 'absolute_value', 'percentage_change', 'percentage_of_total', 'compound_growth', 'cagr']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_math_core_count_matches_registry():
    m = __import__(f"maths_lib.math_core", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 45


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_math_core_all_formulas_execute_deterministically(fid):
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
