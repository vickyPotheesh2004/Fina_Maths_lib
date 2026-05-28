import pytest

import maths_lib as ml

FORMULA_IDS = ['mse_loss', 'mae_loss', 'rmse_loss', 'huber_loss', 'cross_entropy_loss', 'binary_cross_entropy', 'categorical_cross_entropy', 'hinge_loss', 'kl_divergence', 'focal_loss', 'log_loss', 'msle_loss', 'sigmoid', 'relu', 'leaky_relu', 'tanh_activation', 'softmax', 'gelu', 'elu', 'swish', 'softplus', 'accuracy', 'precision', 'recall', 'f1_score', 'f_beta_score', 'specificity', 'roc_auc', 'pr_auc', 'matthews_corr', 'cohen_kappa', 'balanced_accuracy', 'false_positive_rate', 'false_negative_rate', 'r2_score', 'adjusted_r2_ml', 'explained_variance', 'mape_metric', 'smape', 'median_absolute_error', 'jaccard_similarity', 'dice_coefficient', 'canberra_distance', 'braycurtis_distance', 'haversine_distance', 'jaro_winkler', 'silhouette_score', 'davies_bouldin', 'calinski_harabasz', 'inertia', 'dunn_index', 'rand_index', 'adjusted_rand_index', 'normalized_mutual_info', 'entropy', 'conditional_entropy', 'mutual_information', 'information_gain', 'gini_impurity', 'gain_ratio', 'gradient_descent_step', 'momentum_update', 'adam_update', 'rmsprop_update', 'learning_rate_decay', 'l1_regularization', 'l2_regularization', 'elastic_net_penalty', 'tf_idf', 'cosine_sim_vectors', 'levenshtein_distance', 'bleu_score', 'perplexity', 'bm25_score', 'min_max_scaling', 'standard_scaling', 'robust_scaling', 'pca_explained_variance', 'sigmoid_derivative', 'dropout_inverted', 'batch_normalization', 'layer_normalization', 'cosine_annealing', 'attention_score', 'nadam_update', 'adagrad_update', 'weight_init_xavier', 'weight_init_he', 'top_k_accuracy', 'ndcg', 'map_at_k', 'hamming_loss', 'wasserstein_distance_1d']


def _inputs_for(fid: str):
    row = next(f for _dk, _title, _m, f in ml.all_formulas() if f[0] == fid)
    keys = [k.strip() for k in row[4].split(',') if k.strip()]
    return {k: 10.0 for k in keys}


def test_ai_ml_count_matches_registry():
    m = __import__(f"maths_lib.ai_ml", fromlist=["FORMULA_IDS"])
    assert len(m.FORMULA_IDS) == 93


@pytest.mark.parametrize("fid", FORMULA_IDS)
def test_ai_ml_all_formulas_execute_deterministically(fid):
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
