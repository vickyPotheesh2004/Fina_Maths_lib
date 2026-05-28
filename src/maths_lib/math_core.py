from .base import build_result, formula

DOMAIN_KEY = "D12_math_core"
DOMAIN_TITLE = "Core Math, Trigonometry, Linear Algebra & Geometry"
FORMULA_IDS = [
    "sine",
    "cosine",
    "tangent",
    "arcsine",
    "arccosine",
    "arctangent",
    "atan2",
    "degrees_to_radians",
    "radians_to_degrees",
    "pythagorean",
    "law_of_cosines",
    "law_of_sines",
    "hypotenuse",
    "euclidean_distance",
    "manhattan_distance",
    "cosine_similarity",
    "minkowski_distance",
    "chebyshev_distance",
    "mahalanobis_distance",
    "hamming_distance",
    "dot_product",
    "cross_product_2d",
    "vector_magnitude",
    "vector_normalize",
    "matrix_multiply",
    "matrix_transpose",
    "matrix_determinant",
    "matrix_inverse",
    "matrix_trace",
    "eigenvalues",
    "cholesky_decomposition",
    "logarithm_natural",
    "logarithm_base10",
    "logarithm_base",
    "exponential",
    "power_function",
    "nth_root",
    "factorial",
    "combination",
    "permutation",
    "absolute_value",
    "percentage_change",
    "percentage_of_total",
    "compound_growth",
    "cagr",
]

@formula("sine", "Sine", "sin(theta)", DOMAIN_KEY, unit="")
def sine(angle_radians: float | None = None, **kwargs):
    return build_result(
        fid="sine",
        name="Sine",
        expression="sin(theta)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "angle_radians": kwargs.get("angle_radians", angle_radians),
        },
    )

@formula("cosine", "Cosine", "cos(theta)", DOMAIN_KEY, unit="")
def cosine(angle_radians: float | None = None, **kwargs):
    return build_result(
        fid="cosine",
        name="Cosine",
        expression="cos(theta)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "angle_radians": kwargs.get("angle_radians", angle_radians),
        },
    )

@formula("tangent", "Tangent", "tan(theta)", DOMAIN_KEY, unit="")
def tangent(angle_radians: float | None = None, **kwargs):
    return build_result(
        fid="tangent",
        name="Tangent",
        expression="tan(theta)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "angle_radians": kwargs.get("angle_radians", angle_radians),
        },
    )

@formula("arcsine", "Arcsine", "asin(x)", DOMAIN_KEY, unit="")
def arcsine(value: float | None = None, **kwargs):
    return build_result(
        fid="arcsine",
        name="Arcsine",
        expression="asin(x)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "value": kwargs.get("value", value),
        },
    )

@formula("arccosine", "Arccosine", "acos(x)", DOMAIN_KEY, unit="")
def arccosine(value: float | None = None, **kwargs):
    return build_result(
        fid="arccosine",
        name="Arccosine",
        expression="acos(x)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "value": kwargs.get("value", value),
        },
    )

@formula("arctangent", "Arctangent", "atan(x)", DOMAIN_KEY, unit="")
def arctangent(value: float | None = None, **kwargs):
    return build_result(
        fid="arctangent",
        name="Arctangent",
        expression="atan(x)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "value": kwargs.get("value", value),
        },
    )

@formula("atan2", "Atan2", "atan2(y, x)", DOMAIN_KEY, unit="")
def atan2(y: float | None = None, x: float | None = None, **kwargs):
    return build_result(
        fid="atan2",
        name="Atan2",
        expression="atan2(y, x)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "y": kwargs.get("y", y),
            "x": kwargs.get("x", x),
        },
    )

@formula("degrees_to_radians", "Degrees to Radians", "deg * pi/180", DOMAIN_KEY, unit="")
def degrees_to_radians(degrees: float | None = None, **kwargs):
    return build_result(
        fid="degrees_to_radians",
        name="Degrees to Radians",
        expression="deg * pi/180",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "degrees": kwargs.get("degrees", degrees),
        },
    )

@formula("radians_to_degrees", "Radians to Degrees", "rad * 180/pi", DOMAIN_KEY, unit="")
def radians_to_degrees(radians: float | None = None, **kwargs):
    return build_result(
        fid="radians_to_degrees",
        name="Radians to Degrees",
        expression="rad * 180/pi",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "radians": kwargs.get("radians", radians),
        },
    )

@formula("pythagorean", "Pythagorean Theorem", "sqrt(a^2 + b^2)", DOMAIN_KEY, unit="")
def pythagorean(a: float | None = None, b: float | None = None, **kwargs):
    return build_result(
        fid="pythagorean",
        name="Pythagorean Theorem",
        expression="sqrt(a^2 + b^2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "a": kwargs.get("a", a),
            "b": kwargs.get("b", b),
        },
    )

@formula("law_of_cosines", "Law of Cosines", "sqrt(a^2+b^2-2ab*cos(C))", DOMAIN_KEY, unit="")
def law_of_cosines(a: float | None = None, b: float | None = None, angle_c: float | None = None, **kwargs):
    return build_result(
        fid="law_of_cosines",
        name="Law of Cosines",
        expression="sqrt(a^2+b^2-2ab*cos(C))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "a": kwargs.get("a", a),
            "b": kwargs.get("b", b),
            "angle_c": kwargs.get("angle_c", angle_c),
        },
    )

@formula("law_of_sines", "Law of Sines", "a/sin(A) = b/sin(B)", DOMAIN_KEY, unit="")
def law_of_sines(side_a: float | None = None, angle_a: float | None = None, angle_b: float | None = None, **kwargs):
    return build_result(
        fid="law_of_sines",
        name="Law of Sines",
        expression="a/sin(A) = b/sin(B)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "side_a": kwargs.get("side_a", side_a),
            "angle_a": kwargs.get("angle_a", angle_a),
            "angle_b": kwargs.get("angle_b", angle_b),
        },
    )

@formula("hypotenuse", "Hypotenuse", "sqrt(a^2 + b^2)", DOMAIN_KEY, unit="")
def hypotenuse(a: float | None = None, b: float | None = None, **kwargs):
    return build_result(
        fid="hypotenuse",
        name="Hypotenuse",
        expression="sqrt(a^2 + b^2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "a": kwargs.get("a", a),
            "b": kwargs.get("b", b),
        },
    )

@formula("euclidean_distance", "Euclidean Distance", "sqrt(Sum((x-y)^2))", DOMAIN_KEY, unit="")
def euclidean_distance(point_a: float | None = None, point_b: float | None = None, **kwargs):
    return build_result(
        fid="euclidean_distance",
        name="Euclidean Distance",
        expression="sqrt(Sum((x-y)^2))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "point_a": kwargs.get("point_a", point_a),
            "point_b": kwargs.get("point_b", point_b),
        },
    )

@formula("manhattan_distance", "Manhattan Distance", "Sum(|x-y|)", DOMAIN_KEY, unit="")
def manhattan_distance(point_a: float | None = None, point_b: float | None = None, **kwargs):
    return build_result(
        fid="manhattan_distance",
        name="Manhattan Distance",
        expression="Sum(|x-y|)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "point_a": kwargs.get("point_a", point_a),
            "point_b": kwargs.get("point_b", point_b),
        },
    )

@formula("cosine_similarity", "Cosine Similarity", "A.B / (|A|*|B|)", DOMAIN_KEY, unit="")
def cosine_similarity(vector_a: float | None = None, vector_b: float | None = None, **kwargs):
    return build_result(
        fid="cosine_similarity",
        name="Cosine Similarity",
        expression="A.B / (|A|*|B|)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "vector_a": kwargs.get("vector_a", vector_a),
            "vector_b": kwargs.get("vector_b", vector_b),
        },
    )

@formula("minkowski_distance", "Minkowski Distance", "(Sum(|x-y|^p))^(1/p)", DOMAIN_KEY, unit="")
def minkowski_distance(point_a: float | None = None, point_b: float | None = None, p: float | None = None, **kwargs):
    return build_result(
        fid="minkowski_distance",
        name="Minkowski Distance",
        expression="(Sum(|x-y|^p))^(1/p)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "point_a": kwargs.get("point_a", point_a),
            "point_b": kwargs.get("point_b", point_b),
            "p": kwargs.get("p", p),
        },
    )

@formula("chebyshev_distance", "Chebyshev Distance", "max(|x-y|)", DOMAIN_KEY, unit="")
def chebyshev_distance(point_a: float | None = None, point_b: float | None = None, **kwargs):
    return build_result(
        fid="chebyshev_distance",
        name="Chebyshev Distance",
        expression="max(|x-y|)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "point_a": kwargs.get("point_a", point_a),
            "point_b": kwargs.get("point_b", point_b),
        },
    )

@formula("mahalanobis_distance", "Mahalanobis Distance", "sqrt((x-mu)' Cov^-1 (x-mu))", DOMAIN_KEY, unit="")
def mahalanobis_distance(point: float | None = None, mean: float | None = None, covariance_matrix: float | None = None, **kwargs):
    return build_result(
        fid="mahalanobis_distance",
        name="Mahalanobis Distance",
        expression="sqrt((x-mu)' Cov^-1 (x-mu))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "point": kwargs.get("point", point),
            "mean": kwargs.get("mean", mean),
            "covariance_matrix": kwargs.get("covariance_matrix", covariance_matrix),
        },
    )

@formula("hamming_distance", "Hamming Distance", "Count(x != y)", DOMAIN_KEY, unit="")
def hamming_distance(sequence_a: float | None = None, sequence_b: float | None = None, **kwargs):
    return build_result(
        fid="hamming_distance",
        name="Hamming Distance",
        expression="Count(x != y)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "sequence_a": kwargs.get("sequence_a", sequence_a),
            "sequence_b": kwargs.get("sequence_b", sequence_b),
        },
    )

@formula("dot_product", "Dot Product", "Sum(a_i * b_i)", DOMAIN_KEY, unit="")
def dot_product(vector_a: float | None = None, vector_b: float | None = None, **kwargs):
    return build_result(
        fid="dot_product",
        name="Dot Product",
        expression="Sum(a_i * b_i)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "vector_a": kwargs.get("vector_a", vector_a),
            "vector_b": kwargs.get("vector_b", vector_b),
        },
    )

@formula("cross_product_2d", "Cross Product (2D)", "a_x*b_y - a_y*b_x", DOMAIN_KEY, unit="")
def cross_product_2d(vector_a: float | None = None, vector_b: float | None = None, **kwargs):
    return build_result(
        fid="cross_product_2d",
        name="Cross Product (2D)",
        expression="a_x*b_y - a_y*b_x",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "vector_a": kwargs.get("vector_a", vector_a),
            "vector_b": kwargs.get("vector_b", vector_b),
        },
    )

@formula("vector_magnitude", "Vector Magnitude", "sqrt(Sum(x^2))", DOMAIN_KEY, unit="")
def vector_magnitude(vector: float | None = None, **kwargs):
    return build_result(
        fid="vector_magnitude",
        name="Vector Magnitude",
        expression="sqrt(Sum(x^2))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "vector": kwargs.get("vector", vector),
        },
    )

@formula("vector_normalize", "Vector Normalization", "v / |v|", DOMAIN_KEY, unit="")
def vector_normalize(vector: float | None = None, **kwargs):
    return build_result(
        fid="vector_normalize",
        name="Vector Normalization",
        expression="v / |v|",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "vector": kwargs.get("vector", vector),
        },
    )

@formula("matrix_multiply", "Matrix Multiplication", "C_ij = Sum(A_ik * B_kj)", DOMAIN_KEY, unit="")
def matrix_multiply(matrix_a: float | None = None, matrix_b: float | None = None, **kwargs):
    return build_result(
        fid="matrix_multiply",
        name="Matrix Multiplication",
        expression="C_ij = Sum(A_ik * B_kj)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "matrix_a": kwargs.get("matrix_a", matrix_a),
            "matrix_b": kwargs.get("matrix_b", matrix_b),
        },
    )

@formula("matrix_transpose", "Matrix Transpose", "A_ij -> A_ji", DOMAIN_KEY, unit="")
def matrix_transpose(matrix: float | None = None, **kwargs):
    return build_result(
        fid="matrix_transpose",
        name="Matrix Transpose",
        expression="A_ij -> A_ji",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "matrix": kwargs.get("matrix", matrix),
        },
    )

@formula("matrix_determinant", "Matrix Determinant", "det(A)", DOMAIN_KEY, unit="")
def matrix_determinant(matrix: float | None = None, **kwargs):
    return build_result(
        fid="matrix_determinant",
        name="Matrix Determinant",
        expression="det(A)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "matrix": kwargs.get("matrix", matrix),
        },
    )

@formula("matrix_inverse", "Matrix Inverse", "A^-1", DOMAIN_KEY, unit="")
def matrix_inverse(matrix: float | None = None, **kwargs):
    return build_result(
        fid="matrix_inverse",
        name="Matrix Inverse",
        expression="A^-1",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "matrix": kwargs.get("matrix", matrix),
        },
    )

@formula("matrix_trace", "Matrix Trace", "Sum(A_ii)", DOMAIN_KEY, unit="")
def matrix_trace(matrix: float | None = None, **kwargs):
    return build_result(
        fid="matrix_trace",
        name="Matrix Trace",
        expression="Sum(A_ii)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "matrix": kwargs.get("matrix", matrix),
        },
    )

@formula("eigenvalues", "Eigenvalues", "Solve det(A-lambda*I)=0", DOMAIN_KEY, unit="")
def eigenvalues(matrix: float | None = None, **kwargs):
    return build_result(
        fid="eigenvalues",
        name="Eigenvalues",
        expression="Solve det(A-lambda*I)=0",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "matrix": kwargs.get("matrix", matrix),
        },
    )

@formula("cholesky_decomposition", "Cholesky Decomposition", "A = L*L'", DOMAIN_KEY, unit="")
def cholesky_decomposition(matrix: float | None = None, **kwargs):
    return build_result(
        fid="cholesky_decomposition",
        name="Cholesky Decomposition",
        expression="A = L*L'",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "matrix": kwargs.get("matrix", matrix),
        },
    )

@formula("logarithm_natural", "Natural Logarithm", "ln(x)", DOMAIN_KEY, unit="")
def logarithm_natural(value: float | None = None, **kwargs):
    return build_result(
        fid="logarithm_natural",
        name="Natural Logarithm",
        expression="ln(x)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "value": kwargs.get("value", value),
        },
    )

@formula("logarithm_base10", "Log Base 10", "log10(x)", DOMAIN_KEY, unit="")
def logarithm_base10(value: float | None = None, **kwargs):
    return build_result(
        fid="logarithm_base10",
        name="Log Base 10",
        expression="log10(x)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "value": kwargs.get("value", value),
        },
    )

@formula("logarithm_base", "Log Arbitrary Base", "log(x) / log(b)", DOMAIN_KEY, unit="")
def logarithm_base(value: float | None = None, base: float | None = None, **kwargs):
    return build_result(
        fid="logarithm_base",
        name="Log Arbitrary Base",
        expression="log(x) / log(b)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "value": kwargs.get("value", value),
            "base": kwargs.get("base", base),
        },
    )

@formula("exponential", "Exponential", "e^x", DOMAIN_KEY, unit="")
def exponential(value: float | None = None, **kwargs):
    return build_result(
        fid="exponential",
        name="Exponential",
        expression="e^x",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "value": kwargs.get("value", value),
        },
    )

@formula("power_function", "Power Function", "base^exponent", DOMAIN_KEY, unit="")
def power_function(base: float | None = None, exponent: float | None = None, **kwargs):
    return build_result(
        fid="power_function",
        name="Power Function",
        expression="base^exponent",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "base": kwargs.get("base", base),
            "exponent": kwargs.get("exponent", exponent),
        },
    )

@formula("nth_root", "Nth Root", "x^(1/n)", DOMAIN_KEY, unit="")
def nth_root(value: float | None = None, n: float | None = None, **kwargs):
    return build_result(
        fid="nth_root",
        name="Nth Root",
        expression="x^(1/n)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "value": kwargs.get("value", value),
            "n": kwargs.get("n", n),
        },
    )

@formula("factorial", "Factorial", "n!", DOMAIN_KEY, unit="")
def factorial(n: float | None = None, **kwargs):
    return build_result(
        fid="factorial",
        name="Factorial",
        expression="n!",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "n": kwargs.get("n", n),
        },
    )

@formula("combination", "Combination (nCr)", "n! / (r!(n-r)!)", DOMAIN_KEY, unit="")
def combination(n: float | None = None, r: float | None = None, **kwargs):
    return build_result(
        fid="combination",
        name="Combination (nCr)",
        expression="n! / (r!(n-r)!)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "n": kwargs.get("n", n),
            "r": kwargs.get("r", r),
        },
    )

@formula("permutation", "Permutation (nPr)", "n! / (n-r)!", DOMAIN_KEY, unit="")
def permutation(n: float | None = None, r: float | None = None, **kwargs):
    return build_result(
        fid="permutation",
        name="Permutation (nPr)",
        expression="n! / (n-r)!",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "n": kwargs.get("n", n),
            "r": kwargs.get("r", r),
        },
    )

@formula("absolute_value", "Absolute Value", "|x|", DOMAIN_KEY, unit="")
def absolute_value(value: float | None = None, **kwargs):
    return build_result(
        fid="absolute_value",
        name="Absolute Value",
        expression="|x|",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "value": kwargs.get("value", value),
        },
    )

@formula("percentage_change", "Percentage Change", "(New - Old)/Old * 100", DOMAIN_KEY, unit="")
def percentage_change(old_value: float | None = None, new_value: float | None = None, **kwargs):
    return build_result(
        fid="percentage_change",
        name="Percentage Change",
        expression="(New - Old)/Old * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "old_value": kwargs.get("old_value", old_value),
            "new_value": kwargs.get("new_value", new_value),
        },
    )

@formula("percentage_of_total", "Percentage of Total", "Part / Total * 100", DOMAIN_KEY, unit="")
def percentage_of_total(part: float | None = None, total: float | None = None, **kwargs):
    return build_result(
        fid="percentage_of_total",
        name="Percentage of Total",
        expression="Part / Total * 100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "part": kwargs.get("part", part),
            "total": kwargs.get("total", total),
        },
    )

@formula("compound_growth", "Compound Growth", "Initial*(1+r)^n", DOMAIN_KEY, unit="")
def compound_growth(initial: float | None = None, rate: float | None = None, periods: float | None = None, **kwargs):
    return build_result(
        fid="compound_growth",
        name="Compound Growth",
        expression="Initial*(1+r)^n",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "initial": kwargs.get("initial", initial),
            "rate": kwargs.get("rate", rate),
            "periods": kwargs.get("periods", periods),
        },
    )

@formula("cagr", "CAGR", "(End/Start)^(1/years) - 1", DOMAIN_KEY, unit="")
def cagr(start_value: float | None = None, end_value: float | None = None, years: float | None = None, **kwargs):
    return build_result(
        fid="cagr",
        name="CAGR",
        expression="(End/Start)^(1/years) - 1",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "start_value": kwargs.get("start_value", start_value),
            "end_value": kwargs.get("end_value", end_value),
            "years": kwargs.get("years", years),
        },
    )
