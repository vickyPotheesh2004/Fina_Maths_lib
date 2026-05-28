from .base import build_result, formula

DOMAIN_KEY = "D14_ai_ml"
DOMAIN_TITLE = "AI / Machine Learning Metrics & Functions"
FORMULA_IDS = [
    "mse_loss",
    "mae_loss",
    "rmse_loss",
    "huber_loss",
    "cross_entropy_loss",
    "binary_cross_entropy",
    "categorical_cross_entropy",
    "hinge_loss",
    "kl_divergence",
    "focal_loss",
    "log_loss",
    "msle_loss",
    "sigmoid",
    "relu",
    "leaky_relu",
    "tanh_activation",
    "softmax",
    "gelu",
    "elu",
    "swish",
    "softplus",
    "accuracy",
    "precision",
    "recall",
    "f1_score",
    "f_beta_score",
    "specificity",
    "roc_auc",
    "pr_auc",
    "matthews_corr",
    "cohen_kappa",
    "balanced_accuracy",
    "false_positive_rate",
    "false_negative_rate",
    "r2_score",
    "adjusted_r2_ml",
    "explained_variance",
    "mape_metric",
    "smape",
    "median_absolute_error",
    "jaccard_similarity",
    "dice_coefficient",
    "canberra_distance",
    "braycurtis_distance",
    "haversine_distance",
    "jaro_winkler",
    "silhouette_score",
    "davies_bouldin",
    "calinski_harabasz",
    "inertia",
    "dunn_index",
    "rand_index",
    "adjusted_rand_index",
    "normalized_mutual_info",
    "entropy",
    "conditional_entropy",
    "mutual_information",
    "information_gain",
    "gini_impurity",
    "gain_ratio",
    "gradient_descent_step",
    "momentum_update",
    "adam_update",
    "rmsprop_update",
    "learning_rate_decay",
    "l1_regularization",
    "l2_regularization",
    "elastic_net_penalty",
    "tf_idf",
    "cosine_sim_vectors",
    "levenshtein_distance",
    "bleu_score",
    "perplexity",
    "bm25_score",
    "min_max_scaling",
    "standard_scaling",
    "robust_scaling",
    "pca_explained_variance",
    "sigmoid_derivative",
    "dropout_inverted",
    "batch_normalization",
    "layer_normalization",
    "cosine_annealing",
    "attention_score",
    "nadam_update",
    "adagrad_update",
    "weight_init_xavier",
    "weight_init_he",
    "top_k_accuracy",
    "ndcg",
    "map_at_k",
    "hamming_loss",
    "wasserstein_distance_1d",
]

@formula("mse_loss", "Mean Squared Error Loss", "Mean((y - yhat)^2)", DOMAIN_KEY, unit="")
def mse_loss(y_true: float | None = None, y_pred: float | None = None, **kwargs):
    return build_result(
        fid="mse_loss",
        name="Mean Squared Error Loss",
        expression="Mean((y - yhat)^2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "y_true": kwargs.get("y_true", y_true),
            "y_pred": kwargs.get("y_pred", y_pred),
        },
    )

@formula("mae_loss", "Mean Absolute Error Loss", "Mean(|y - yhat|)", DOMAIN_KEY, unit="")
def mae_loss(y_true: float | None = None, y_pred: float | None = None, **kwargs):
    return build_result(
        fid="mae_loss",
        name="Mean Absolute Error Loss",
        expression="Mean(|y - yhat|)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "y_true": kwargs.get("y_true", y_true),
            "y_pred": kwargs.get("y_pred", y_pred),
        },
    )

@formula("rmse_loss", "Root Mean Squared Error Loss", "sqrt(Mean((y - yhat)^2))", DOMAIN_KEY, unit="")
def rmse_loss(y_true: float | None = None, y_pred: float | None = None, **kwargs):
    return build_result(
        fid="rmse_loss",
        name="Root Mean Squared Error Loss",
        expression="sqrt(Mean((y - yhat)^2))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "y_true": kwargs.get("y_true", y_true),
            "y_pred": kwargs.get("y_pred", y_pred),
        },
    )

@formula("huber_loss", "Huber Loss", "0.5*e^2 if |e|<=d else d*(|e|-0.5d)", DOMAIN_KEY, unit="")
def huber_loss(y_true: float | None = None, y_pred: float | None = None, delta: float | None = None, **kwargs):
    return build_result(
        fid="huber_loss",
        name="Huber Loss",
        expression="0.5*e^2 if |e|<=d else d*(|e|-0.5d)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "y_true": kwargs.get("y_true", y_true),
            "y_pred": kwargs.get("y_pred", y_pred),
            "delta": kwargs.get("delta", delta),
        },
    )

@formula("cross_entropy_loss", "Cross-Entropy Loss", "-Sum(y*log(yhat))", DOMAIN_KEY, unit="")
def cross_entropy_loss(y_true: float | None = None, y_pred: float | None = None, **kwargs):
    return build_result(
        fid="cross_entropy_loss",
        name="Cross-Entropy Loss",
        expression="-Sum(y*log(yhat))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "y_true": kwargs.get("y_true", y_true),
            "y_pred": kwargs.get("y_pred", y_pred),
        },
    )

@formula("binary_cross_entropy", "Binary Cross-Entropy", "-Mean(y*log(p)+(1-y)*log(1-p))", DOMAIN_KEY, unit="")
def binary_cross_entropy(y_true: float | None = None, y_pred: float | None = None, **kwargs):
    return build_result(
        fid="binary_cross_entropy",
        name="Binary Cross-Entropy",
        expression="-Mean(y*log(p)+(1-y)*log(1-p))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "y_true": kwargs.get("y_true", y_true),
            "y_pred": kwargs.get("y_pred", y_pred),
        },
    )

@formula("categorical_cross_entropy", "Categorical Cross-Entropy", "-Sum(y_i*log(p_i))", DOMAIN_KEY, unit="")
def categorical_cross_entropy(y_true: float | None = None, y_pred: float | None = None, **kwargs):
    return build_result(
        fid="categorical_cross_entropy",
        name="Categorical Cross-Entropy",
        expression="-Sum(y_i*log(p_i))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "y_true": kwargs.get("y_true", y_true),
            "y_pred": kwargs.get("y_pred", y_pred),
        },
    )

@formula("hinge_loss", "Hinge Loss", "Mean(max(0, 1 - y*yhat))", DOMAIN_KEY, unit="")
def hinge_loss(y_true: float | None = None, y_pred: float | None = None, **kwargs):
    return build_result(
        fid="hinge_loss",
        name="Hinge Loss",
        expression="Mean(max(0, 1 - y*yhat))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "y_true": kwargs.get("y_true", y_true),
            "y_pred": kwargs.get("y_pred", y_pred),
        },
    )

@formula("kl_divergence", "KL Divergence", "Sum(p*log(p/q))", DOMAIN_KEY, unit="")
def kl_divergence(p_dist: float | None = None, q_dist: float | None = None, **kwargs):
    return build_result(
        fid="kl_divergence",
        name="KL Divergence",
        expression="Sum(p*log(p/q))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "p_dist": kwargs.get("p_dist", p_dist),
            "q_dist": kwargs.get("q_dist", q_dist),
        },
    )

@formula("focal_loss", "Focal Loss", "-alpha*(1-p)^gamma*log(p)", DOMAIN_KEY, unit="")
def focal_loss(y_true: float | None = None, y_pred: float | None = None, alpha: float | None = None, gamma: float | None = None, **kwargs):
    return build_result(
        fid="focal_loss",
        name="Focal Loss",
        expression="-alpha*(1-p)^gamma*log(p)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "y_true": kwargs.get("y_true", y_true),
            "y_pred": kwargs.get("y_pred", y_pred),
            "alpha": kwargs.get("alpha", alpha),
            "gamma": kwargs.get("gamma", gamma),
        },
    )

@formula("log_loss", "Log Loss", "-Mean(y*log(p)+(1-y)*log(1-p))", DOMAIN_KEY, unit="")
def log_loss(y_true: float | None = None, y_pred: float | None = None, **kwargs):
    return build_result(
        fid="log_loss",
        name="Log Loss",
        expression="-Mean(y*log(p)+(1-y)*log(1-p))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "y_true": kwargs.get("y_true", y_true),
            "y_pred": kwargs.get("y_pred", y_pred),
        },
    )

@formula("msle_loss", "Mean Squared Log Error", "Mean((log(1+y)-log(1+yhat))^2)", DOMAIN_KEY, unit="")
def msle_loss(y_true: float | None = None, y_pred: float | None = None, **kwargs):
    return build_result(
        fid="msle_loss",
        name="Mean Squared Log Error",
        expression="Mean((log(1+y)-log(1+yhat))^2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "y_true": kwargs.get("y_true", y_true),
            "y_pred": kwargs.get("y_pred", y_pred),
        },
    )

@formula("sigmoid", "Sigmoid", "1 / (1 + e^-x)", DOMAIN_KEY, unit="")
def sigmoid(x: float | None = None, **kwargs):
    return build_result(
        fid="sigmoid",
        name="Sigmoid",
        expression="1 / (1 + e^-x)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
        },
    )

@formula("relu", "ReLU", "max(0, x)", DOMAIN_KEY, unit="")
def relu(x: float | None = None, **kwargs):
    return build_result(
        fid="relu",
        name="ReLU",
        expression="max(0, x)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
        },
    )

@formula("leaky_relu", "Leaky ReLU", "x if x>0 else alpha*x", DOMAIN_KEY, unit="")
def leaky_relu(x: float | None = None, alpha: float | None = None, **kwargs):
    return build_result(
        fid="leaky_relu",
        name="Leaky ReLU",
        expression="x if x>0 else alpha*x",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
            "alpha": kwargs.get("alpha", alpha),
        },
    )

@formula("tanh_activation", "Tanh", "(e^x - e^-x)/(e^x + e^-x)", DOMAIN_KEY, unit="")
def tanh_activation(x: float | None = None, **kwargs):
    return build_result(
        fid="tanh_activation",
        name="Tanh",
        expression="(e^x - e^-x)/(e^x + e^-x)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
        },
    )

@formula("softmax", "Softmax", "e^xi / Sum(e^xj)", DOMAIN_KEY, unit="")
def softmax(x_vector: float | None = None, **kwargs):
    return build_result(
        fid="softmax",
        name="Softmax",
        expression="e^xi / Sum(e^xj)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x_vector": kwargs.get("x_vector", x_vector),
        },
    )

@formula("gelu", "GELU", "x * Phi(x)", DOMAIN_KEY, unit="")
def gelu(x: float | None = None, **kwargs):
    return build_result(
        fid="gelu",
        name="GELU",
        expression="x * Phi(x)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
        },
    )

@formula("elu", "ELU", "x if x>0 else alpha*(e^x - 1)", DOMAIN_KEY, unit="")
def elu(x: float | None = None, alpha: float | None = None, **kwargs):
    return build_result(
        fid="elu",
        name="ELU",
        expression="x if x>0 else alpha*(e^x - 1)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
            "alpha": kwargs.get("alpha", alpha),
        },
    )

@formula("swish", "Swish", "x * sigmoid(x)", DOMAIN_KEY, unit="")
def swish(x: float | None = None, **kwargs):
    return build_result(
        fid="swish",
        name="Swish",
        expression="x * sigmoid(x)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
        },
    )

@formula("softplus", "Softplus", "log(1 + e^x)", DOMAIN_KEY, unit="")
def softplus(x: float | None = None, **kwargs):
    return build_result(
        fid="softplus",
        name="Softplus",
        expression="log(1 + e^x)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
        },
    )

@formula("accuracy", "Accuracy", "(TP + TN) / (TP+TN+FP+FN)", DOMAIN_KEY, unit="")
def accuracy(tp: float | None = None, tn: float | None = None, fp: float | None = None, fn: float | None = None, **kwargs):
    return build_result(
        fid="accuracy",
        name="Accuracy",
        expression="(TP + TN) / (TP+TN+FP+FN)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "tp": kwargs.get("tp", tp),
            "tn": kwargs.get("tn", tn),
            "fp": kwargs.get("fp", fp),
            "fn": kwargs.get("fn", fn),
        },
    )

@formula("precision", "Precision", "TP / (TP + FP)", DOMAIN_KEY, unit="")
def precision(tp: float | None = None, fp: float | None = None, **kwargs):
    return build_result(
        fid="precision",
        name="Precision",
        expression="TP / (TP + FP)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "tp": kwargs.get("tp", tp),
            "fp": kwargs.get("fp", fp),
        },
    )

@formula("recall", "Recall (Sensitivity)", "TP / (TP + FN)", DOMAIN_KEY, unit="")
def recall(tp: float | None = None, fn: float | None = None, **kwargs):
    return build_result(
        fid="recall",
        name="Recall (Sensitivity)",
        expression="TP / (TP + FN)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "tp": kwargs.get("tp", tp),
            "fn": kwargs.get("fn", fn),
        },
    )

@formula("f1_score", "F1 Score", "2*P*R / (P + R)", DOMAIN_KEY, unit="")
def f1_score(precision: float | None = None, recall: float | None = None, **kwargs):
    return build_result(
        fid="f1_score",
        name="F1 Score",
        expression="2*P*R / (P + R)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "precision": kwargs.get("precision", precision),
            "recall": kwargs.get("recall", recall),
        },
    )

@formula("f_beta_score", "F-Beta Score", "(1+b^2)*P*R / (b^2*P + R)", DOMAIN_KEY, unit="")
def f_beta_score(precision: float | None = None, recall: float | None = None, beta: float | None = None, **kwargs):
    return build_result(
        fid="f_beta_score",
        name="F-Beta Score",
        expression="(1+b^2)*P*R / (b^2*P + R)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "precision": kwargs.get("precision", precision),
            "recall": kwargs.get("recall", recall),
            "beta": kwargs.get("beta", beta),
        },
    )

@formula("specificity", "Specificity", "TN / (TN + FP)", DOMAIN_KEY, unit="")
def specificity(tn: float | None = None, fp: float | None = None, **kwargs):
    return build_result(
        fid="specificity",
        name="Specificity",
        expression="TN / (TN + FP)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "tn": kwargs.get("tn", tn),
            "fp": kwargs.get("fp", fp),
        },
    )

@formula("roc_auc", "ROC AUC", "Integral of TPR over FPR", DOMAIN_KEY, unit="")
def roc_auc(y_true: float | None = None, y_scores: float | None = None, **kwargs):
    return build_result(
        fid="roc_auc",
        name="ROC AUC",
        expression="Integral of TPR over FPR",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "y_true": kwargs.get("y_true", y_true),
            "y_scores": kwargs.get("y_scores", y_scores),
        },
    )

@formula("pr_auc", "PR AUC", "Integral of precision over recall", DOMAIN_KEY, unit="")
def pr_auc(y_true: float | None = None, y_scores: float | None = None, **kwargs):
    return build_result(
        fid="pr_auc",
        name="PR AUC",
        expression="Integral of precision over recall",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "y_true": kwargs.get("y_true", y_true),
            "y_scores": kwargs.get("y_scores", y_scores),
        },
    )

@formula("matthews_corr", "Matthews Correlation Coefficient", "(TP*TN-FP*FN)/sqrt(...)", DOMAIN_KEY, unit="")
def matthews_corr(tp: float | None = None, tn: float | None = None, fp: float | None = None, fn: float | None = None, **kwargs):
    return build_result(
        fid="matthews_corr",
        name="Matthews Correlation Coefficient",
        expression="(TP*TN-FP*FN)/sqrt(...)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "tp": kwargs.get("tp", tp),
            "tn": kwargs.get("tn", tn),
            "fp": kwargs.get("fp", fp),
            "fn": kwargs.get("fn", fn),
        },
    )

@formula("cohen_kappa", "Cohen's Kappa", "(po - pe) / (1 - pe)", DOMAIN_KEY, unit="")
def cohen_kappa(observed_agreement: float | None = None, expected_agreement: float | None = None, **kwargs):
    return build_result(
        fid="cohen_kappa",
        name="Cohen's Kappa",
        expression="(po - pe) / (1 - pe)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "observed_agreement": kwargs.get("observed_agreement", observed_agreement),
            "expected_agreement": kwargs.get("expected_agreement", expected_agreement),
        },
    )

@formula("balanced_accuracy", "Balanced Accuracy", "(Sensitivity + Specificity) / 2", DOMAIN_KEY, unit="")
def balanced_accuracy(sensitivity: float | None = None, specificity: float | None = None, **kwargs):
    return build_result(
        fid="balanced_accuracy",
        name="Balanced Accuracy",
        expression="(Sensitivity + Specificity) / 2",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "sensitivity": kwargs.get("sensitivity", sensitivity),
            "specificity": kwargs.get("specificity", specificity),
        },
    )

@formula("false_positive_rate", "False Positive Rate", "FP / (FP + TN)", DOMAIN_KEY, unit="")
def false_positive_rate(fp: float | None = None, tn: float | None = None, **kwargs):
    return build_result(
        fid="false_positive_rate",
        name="False Positive Rate",
        expression="FP / (FP + TN)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "fp": kwargs.get("fp", fp),
            "tn": kwargs.get("tn", tn),
        },
    )

@formula("false_negative_rate", "False Negative Rate", "FN / (FN + TP)", DOMAIN_KEY, unit="")
def false_negative_rate(fn: float | None = None, tp: float | None = None, **kwargs):
    return build_result(
        fid="false_negative_rate",
        name="False Negative Rate",
        expression="FN / (FN + TP)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "fn": kwargs.get("fn", fn),
            "tp": kwargs.get("tp", tp),
        },
    )

@formula("r2_score", "R-Squared Score", "1 - SSres/SStot", DOMAIN_KEY, unit="")
def r2_score(y_true: float | None = None, y_pred: float | None = None, **kwargs):
    return build_result(
        fid="r2_score",
        name="R-Squared Score",
        expression="1 - SSres/SStot",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "y_true": kwargs.get("y_true", y_true),
            "y_pred": kwargs.get("y_pred", y_pred),
        },
    )

@formula("adjusted_r2_ml", "Adjusted R-Squared", "1 - (1-R2)(n-1)/(n-k-1)", DOMAIN_KEY, unit="")
def adjusted_r2_ml(r2: float | None = None, n: float | None = None, k: float | None = None, **kwargs):
    return build_result(
        fid="adjusted_r2_ml",
        name="Adjusted R-Squared",
        expression="1 - (1-R2)(n-1)/(n-k-1)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "r2": kwargs.get("r2", r2),
            "n": kwargs.get("n", n),
            "k": kwargs.get("k", k),
        },
    )

@formula("explained_variance", "Explained Variance Score", "1 - Var(y-yhat)/Var(y)", DOMAIN_KEY, unit="")
def explained_variance(y_true: float | None = None, y_pred: float | None = None, **kwargs):
    return build_result(
        fid="explained_variance",
        name="Explained Variance Score",
        expression="1 - Var(y-yhat)/Var(y)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "y_true": kwargs.get("y_true", y_true),
            "y_pred": kwargs.get("y_pred", y_pred),
        },
    )

@formula("mape_metric", "MAPE", "Mean(|y-yhat|/y)*100", DOMAIN_KEY, unit="")
def mape_metric(y_true: float | None = None, y_pred: float | None = None, **kwargs):
    return build_result(
        fid="mape_metric",
        name="MAPE",
        expression="Mean(|y-yhat|/y)*100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "y_true": kwargs.get("y_true", y_true),
            "y_pred": kwargs.get("y_pred", y_pred),
        },
    )

@formula("smape", "SMAPE", "Mean(2|y-yhat|/(|y|+|yhat|))*100", DOMAIN_KEY, unit="")
def smape(y_true: float | None = None, y_pred: float | None = None, **kwargs):
    return build_result(
        fid="smape",
        name="SMAPE",
        expression="Mean(2|y-yhat|/(|y|+|yhat|))*100",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "y_true": kwargs.get("y_true", y_true),
            "y_pred": kwargs.get("y_pred", y_pred),
        },
    )

@formula("median_absolute_error", "Median Absolute Error", "Median(|y - yhat|)", DOMAIN_KEY, unit="")
def median_absolute_error(y_true: float | None = None, y_pred: float | None = None, **kwargs):
    return build_result(
        fid="median_absolute_error",
        name="Median Absolute Error",
        expression="Median(|y - yhat|)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "y_true": kwargs.get("y_true", y_true),
            "y_pred": kwargs.get("y_pred", y_pred),
        },
    )

@formula("jaccard_similarity", "Jaccard Similarity", "|A and B| / |A or B|", DOMAIN_KEY, unit="")
def jaccard_similarity(set_a: float | None = None, set_b: float | None = None, **kwargs):
    return build_result(
        fid="jaccard_similarity",
        name="Jaccard Similarity",
        expression="|A and B| / |A or B|",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "set_a": kwargs.get("set_a", set_a),
            "set_b": kwargs.get("set_b", set_b),
        },
    )

@formula("dice_coefficient", "Dice Coefficient", "2|A and B| / (|A|+|B|)", DOMAIN_KEY, unit="")
def dice_coefficient(set_a: float | None = None, set_b: float | None = None, **kwargs):
    return build_result(
        fid="dice_coefficient",
        name="Dice Coefficient",
        expression="2|A and B| / (|A|+|B|)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "set_a": kwargs.get("set_a", set_a),
            "set_b": kwargs.get("set_b", set_b),
        },
    )

@formula("canberra_distance", "Canberra Distance", "Sum(|x-y|/(|x|+|y|))", DOMAIN_KEY, unit="")
def canberra_distance(vector_a: float | None = None, vector_b: float | None = None, **kwargs):
    return build_result(
        fid="canberra_distance",
        name="Canberra Distance",
        expression="Sum(|x-y|/(|x|+|y|))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "vector_a": kwargs.get("vector_a", vector_a),
            "vector_b": kwargs.get("vector_b", vector_b),
        },
    )

@formula("braycurtis_distance", "Bray-Curtis Distance", "Sum(|x-y|)/Sum(|x+y|)", DOMAIN_KEY, unit="")
def braycurtis_distance(vector_a: float | None = None, vector_b: float | None = None, **kwargs):
    return build_result(
        fid="braycurtis_distance",
        name="Bray-Curtis Distance",
        expression="Sum(|x-y|)/Sum(|x+y|)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "vector_a": kwargs.get("vector_a", vector_a),
            "vector_b": kwargs.get("vector_b", vector_b),
        },
    )

@formula("haversine_distance", "Haversine Distance", "2r*asin(sqrt(hav))", DOMAIN_KEY, unit="")
def haversine_distance(lat1: float | None = None, lon1: float | None = None, lat2: float | None = None, lon2: float | None = None, **kwargs):
    return build_result(
        fid="haversine_distance",
        name="Haversine Distance",
        expression="2r*asin(sqrt(hav))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "lat1": kwargs.get("lat1", lat1),
            "lon1": kwargs.get("lon1", lon1),
            "lat2": kwargs.get("lat2", lat2),
            "lon2": kwargs.get("lon2", lon2),
        },
    )

@formula("jaro_winkler", "Jaro-Winkler Similarity", "Jaro + prefix*scale*(1-Jaro)", DOMAIN_KEY, unit="")
def jaro_winkler(string_a: float | None = None, string_b: float | None = None, **kwargs):
    return build_result(
        fid="jaro_winkler",
        name="Jaro-Winkler Similarity",
        expression="Jaro + prefix*scale*(1-Jaro)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "string_a": kwargs.get("string_a", string_a),
            "string_b": kwargs.get("string_b", string_b),
        },
    )

@formula("silhouette_score", "Silhouette Score", "(b - a) / max(a, b)", DOMAIN_KEY, unit="")
def silhouette_score(intra_distance: float | None = None, nearest_cluster_distance: float | None = None, **kwargs):
    return build_result(
        fid="silhouette_score",
        name="Silhouette Score",
        expression="(b - a) / max(a, b)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "intra_distance": kwargs.get("intra_distance", intra_distance),
            "nearest_cluster_distance": kwargs.get("nearest_cluster_distance", nearest_cluster_distance),
        },
    )

@formula("davies_bouldin", "Davies-Bouldin Index", "Mean(max((si+sj)/dij))", DOMAIN_KEY, unit="")
def davies_bouldin(cluster_scatters: float | None = None, cluster_distances: float | None = None, **kwargs):
    return build_result(
        fid="davies_bouldin",
        name="Davies-Bouldin Index",
        expression="Mean(max((si+sj)/dij))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cluster_scatters": kwargs.get("cluster_scatters", cluster_scatters),
            "cluster_distances": kwargs.get("cluster_distances", cluster_distances),
        },
    )

@formula("calinski_harabasz", "Calinski-Harabasz Index", "(BGSS/WGSS)*((n-k)/(k-1))", DOMAIN_KEY, unit="")
def calinski_harabasz(between_ss: float | None = None, within_ss: float | None = None, n: float | None = None, k: float | None = None, **kwargs):
    return build_result(
        fid="calinski_harabasz",
        name="Calinski-Harabasz Index",
        expression="(BGSS/WGSS)*((n-k)/(k-1))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "between_ss": kwargs.get("between_ss", between_ss),
            "within_ss": kwargs.get("within_ss", within_ss),
            "n": kwargs.get("n", n),
            "k": kwargs.get("k", k),
        },
    )

@formula("inertia", "Inertia (WCSS)", "Sum(||x - centroid||^2)", DOMAIN_KEY, unit="")
def inertia(points: float | None = None, centroids: float | None = None, **kwargs):
    return build_result(
        fid="inertia",
        name="Inertia (WCSS)",
        expression="Sum(||x - centroid||^2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "points": kwargs.get("points", points),
            "centroids": kwargs.get("centroids", centroids),
        },
    )

@formula("dunn_index", "Dunn Index", "Min_Inter_Cluster / Max_Intra_Cluster", DOMAIN_KEY, unit="")
def dunn_index(inter_distances: float | None = None, intra_distances: float | None = None, **kwargs):
    return build_result(
        fid="dunn_index",
        name="Dunn Index",
        expression="Min_Inter_Cluster / Max_Intra_Cluster",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "inter_distances": kwargs.get("inter_distances", inter_distances),
            "intra_distances": kwargs.get("intra_distances", intra_distances),
        },
    )

@formula("rand_index", "Rand Index", "(a + b) / C(n,2)", DOMAIN_KEY, unit="")
def rand_index(agreements: float | None = None, n: float | None = None, **kwargs):
    return build_result(
        fid="rand_index",
        name="Rand Index",
        expression="(a + b) / C(n,2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "agreements": kwargs.get("agreements", agreements),
            "n": kwargs.get("n", n),
        },
    )

@formula("adjusted_rand_index", "Adjusted Rand Index", "(RI - Expected) / (Max - Expected)", DOMAIN_KEY, unit="")
def adjusted_rand_index(contingency_table: float | None = None, **kwargs):
    return build_result(
        fid="adjusted_rand_index",
        name="Adjusted Rand Index",
        expression="(RI - Expected) / (Max - Expected)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "contingency_table": kwargs.get("contingency_table", contingency_table),
        },
    )

@formula("normalized_mutual_info", "Normalized Mutual Information", "MI / sqrt(H(U)*H(V))", DOMAIN_KEY, unit="")
def normalized_mutual_info(labels_true: float | None = None, labels_pred: float | None = None, **kwargs):
    return build_result(
        fid="normalized_mutual_info",
        name="Normalized Mutual Information",
        expression="MI / sqrt(H(U)*H(V))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "labels_true": kwargs.get("labels_true", labels_true),
            "labels_pred": kwargs.get("labels_pred", labels_pred),
        },
    )

@formula("entropy", "Shannon Entropy", "-Sum(p*log2(p))", DOMAIN_KEY, unit="")
def entropy(probabilities: float | None = None, **kwargs):
    return build_result(
        fid="entropy",
        name="Shannon Entropy",
        expression="-Sum(p*log2(p))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "probabilities": kwargs.get("probabilities", probabilities),
        },
    )

@formula("conditional_entropy", "Conditional Entropy", "H(Y) - I(X;Y)", DOMAIN_KEY, unit="")
def conditional_entropy(joint_dist: float | None = None, marginal_dist: float | None = None, **kwargs):
    return build_result(
        fid="conditional_entropy",
        name="Conditional Entropy",
        expression="H(Y) - I(X;Y)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "joint_dist": kwargs.get("joint_dist", joint_dist),
            "marginal_dist": kwargs.get("marginal_dist", marginal_dist),
        },
    )

@formula("mutual_information", "Mutual Information", "Sum(p*log(p/(px*py)))", DOMAIN_KEY, unit="")
def mutual_information(joint_dist: float | None = None, marginal_x: float | None = None, marginal_y: float | None = None, **kwargs):
    return build_result(
        fid="mutual_information",
        name="Mutual Information",
        expression="Sum(p*log(p/(px*py)))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "joint_dist": kwargs.get("joint_dist", joint_dist),
            "marginal_x": kwargs.get("marginal_x", marginal_x),
            "marginal_y": kwargs.get("marginal_y", marginal_y),
        },
    )

@formula("information_gain", "Information Gain", "H(parent) - Weighted_H(children)", DOMAIN_KEY, unit="")
def information_gain(parent_entropy: float | None = None, child_entropies: float | None = None, weights: float | None = None, **kwargs):
    return build_result(
        fid="information_gain",
        name="Information Gain",
        expression="H(parent) - Weighted_H(children)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "parent_entropy": kwargs.get("parent_entropy", parent_entropy),
            "child_entropies": kwargs.get("child_entropies", child_entropies),
            "weights": kwargs.get("weights", weights),
        },
    )

@formula("gini_impurity", "Gini Impurity", "1 - Sum(p^2)", DOMAIN_KEY, unit="")
def gini_impurity(class_probabilities: float | None = None, **kwargs):
    return build_result(
        fid="gini_impurity",
        name="Gini Impurity",
        expression="1 - Sum(p^2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "class_probabilities": kwargs.get("class_probabilities", class_probabilities),
        },
    )

@formula("gain_ratio", "Gain Ratio", "Information_Gain / Split_Info", DOMAIN_KEY, unit="")
def gain_ratio(information_gain: float | None = None, split_info: float | None = None, **kwargs):
    return build_result(
        fid="gain_ratio",
        name="Gain Ratio",
        expression="Information_Gain / Split_Info",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "information_gain": kwargs.get("information_gain", information_gain),
            "split_info": kwargs.get("split_info", split_info),
        },
    )

@formula("gradient_descent_step", "Gradient Descent Step", "theta - lr*gradient", DOMAIN_KEY, unit="")
def gradient_descent_step(theta: float | None = None, learning_rate: float | None = None, gradient: float | None = None, **kwargs):
    return build_result(
        fid="gradient_descent_step",
        name="Gradient Descent Step",
        expression="theta - lr*gradient",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "theta": kwargs.get("theta", theta),
            "learning_rate": kwargs.get("learning_rate", learning_rate),
            "gradient": kwargs.get("gradient", gradient),
        },
    )

@formula("momentum_update", "Momentum Update", "beta*v + (1-beta)*gradient", DOMAIN_KEY, unit="")
def momentum_update(velocity: float | None = None, gradient: float | None = None, beta: float | None = None, **kwargs):
    return build_result(
        fid="momentum_update",
        name="Momentum Update",
        expression="beta*v + (1-beta)*gradient",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "velocity": kwargs.get("velocity", velocity),
            "gradient": kwargs.get("gradient", gradient),
            "beta": kwargs.get("beta", beta),
        },
    )

@formula("adam_update", "Adam Optimizer Step", "theta - lr*mhat/(sqrt(vhat)+eps)", DOMAIN_KEY, unit="")
def adam_update(theta: float | None = None, m_hat: float | None = None, v_hat: float | None = None, learning_rate: float | None = None, epsilon: float | None = None, **kwargs):
    return build_result(
        fid="adam_update",
        name="Adam Optimizer Step",
        expression="theta - lr*mhat/(sqrt(vhat)+eps)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "theta": kwargs.get("theta", theta),
            "m_hat": kwargs.get("m_hat", m_hat),
            "v_hat": kwargs.get("v_hat", v_hat),
            "learning_rate": kwargs.get("learning_rate", learning_rate),
            "epsilon": kwargs.get("epsilon", epsilon),
        },
    )

@formula("rmsprop_update", "RMSProp Update", "theta - lr*g/sqrt(E[g^2]+eps)", DOMAIN_KEY, unit="")
def rmsprop_update(theta: float | None = None, gradient: float | None = None, mean_sq_grad: float | None = None, learning_rate: float | None = None, epsilon: float | None = None, **kwargs):
    return build_result(
        fid="rmsprop_update",
        name="RMSProp Update",
        expression="theta - lr*g/sqrt(E[g^2]+eps)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "theta": kwargs.get("theta", theta),
            "gradient": kwargs.get("gradient", gradient),
            "mean_sq_grad": kwargs.get("mean_sq_grad", mean_sq_grad),
            "learning_rate": kwargs.get("learning_rate", learning_rate),
            "epsilon": kwargs.get("epsilon", epsilon),
        },
    )

@formula("learning_rate_decay", "Learning Rate Decay", "lr0 * decay^epoch", DOMAIN_KEY, unit="")
def learning_rate_decay(initial_lr: float | None = None, decay_rate: float | None = None, epoch: float | None = None, **kwargs):
    return build_result(
        fid="learning_rate_decay",
        name="Learning Rate Decay",
        expression="lr0 * decay^epoch",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "initial_lr": kwargs.get("initial_lr", initial_lr),
            "decay_rate": kwargs.get("decay_rate", decay_rate),
            "epoch": kwargs.get("epoch", epoch),
        },
    )

@formula("l1_regularization", "L1 Regularization (Lasso)", "lambda * Sum(|w|)", DOMAIN_KEY, unit="")
def l1_regularization(weights: float | None = None, lambda_: float | None = None, **kwargs):
    return build_result(
        fid="l1_regularization",
        name="L1 Regularization (Lasso)",
        expression="lambda * Sum(|w|)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "weights": kwargs.get("weights", weights),
            "lambda": kwargs.get("lambda", lambda_),
        },
    )

@formula("l2_regularization", "L2 Regularization (Ridge)", "lambda * Sum(w^2)", DOMAIN_KEY, unit="")
def l2_regularization(weights: float | None = None, lambda_: float | None = None, **kwargs):
    return build_result(
        fid="l2_regularization",
        name="L2 Regularization (Ridge)",
        expression="lambda * Sum(w^2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "weights": kwargs.get("weights", weights),
            "lambda": kwargs.get("lambda", lambda_),
        },
    )

@formula("elastic_net_penalty", "Elastic Net Penalty", "lambda*(alpha*L1 + (1-alpha)*L2)", DOMAIN_KEY, unit="")
def elastic_net_penalty(weights: float | None = None, lambda_: float | None = None, alpha: float | None = None, **kwargs):
    return build_result(
        fid="elastic_net_penalty",
        name="Elastic Net Penalty",
        expression="lambda*(alpha*L1 + (1-alpha)*L2)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "weights": kwargs.get("weights", weights),
            "lambda": kwargs.get("lambda", lambda_),
            "alpha": kwargs.get("alpha", alpha),
        },
    )

@formula("tf_idf", "TF-IDF", "TF * log(N / DF)", DOMAIN_KEY, unit="")
def tf_idf(term_freq: float | None = None, num_docs: float | None = None, doc_freq: float | None = None, **kwargs):
    return build_result(
        fid="tf_idf",
        name="TF-IDF",
        expression="TF * log(N / DF)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "term_freq": kwargs.get("term_freq", term_freq),
            "num_docs": kwargs.get("num_docs", num_docs),
            "doc_freq": kwargs.get("doc_freq", doc_freq),
        },
    )

@formula("cosine_sim_vectors", "Cosine Similarity (Vectors)", "A.B / (|A|*|B|)", DOMAIN_KEY, unit="")
def cosine_sim_vectors(vector_a: float | None = None, vector_b: float | None = None, **kwargs):
    return build_result(
        fid="cosine_sim_vectors",
        name="Cosine Similarity (Vectors)",
        expression="A.B / (|A|*|B|)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "vector_a": kwargs.get("vector_a", vector_a),
            "vector_b": kwargs.get("vector_b", vector_b),
        },
    )

@formula("levenshtein_distance", "Levenshtein Distance", "Min edits to transform", DOMAIN_KEY, unit="")
def levenshtein_distance(string_a: float | None = None, string_b: float | None = None, **kwargs):
    return build_result(
        fid="levenshtein_distance",
        name="Levenshtein Distance",
        expression="Min edits to transform",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "string_a": kwargs.get("string_a", string_a),
            "string_b": kwargs.get("string_b", string_b),
        },
    )

@formula("bleu_score", "BLEU Score", "BP * exp(Sum(wn*log(pn)))", DOMAIN_KEY, unit="")
def bleu_score(reference: float | None = None, candidate: float | None = None, max_n: float | None = None, **kwargs):
    return build_result(
        fid="bleu_score",
        name="BLEU Score",
        expression="BP * exp(Sum(wn*log(pn)))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "reference": kwargs.get("reference", reference),
            "candidate": kwargs.get("candidate", candidate),
            "max_n": kwargs.get("max_n", max_n),
        },
    )

@formula("perplexity", "Perplexity", "2^(-Mean(log2(p)))", DOMAIN_KEY, unit="")
def perplexity(probabilities: float | None = None, **kwargs):
    return build_result(
        fid="perplexity",
        name="Perplexity",
        expression="2^(-Mean(log2(p)))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "probabilities": kwargs.get("probabilities", probabilities),
        },
    )

@formula("bm25_score", "BM25 Score", "IDF * (tf*(k+1))/(tf + k*(1-b+b*dl/avgdl))", DOMAIN_KEY, unit="")
def bm25_score(term_freq: float | None = None, doc_len: float | None = None, avg_doc_len: float | None = None, idf: float | None = None, k: float | None = None, b: float | None = None, **kwargs):
    return build_result(
        fid="bm25_score",
        name="BM25 Score",
        expression="IDF * (tf*(k+1))/(tf + k*(1-b+b*dl/avgdl))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "term_freq": kwargs.get("term_freq", term_freq),
            "doc_len": kwargs.get("doc_len", doc_len),
            "avg_doc_len": kwargs.get("avg_doc_len", avg_doc_len),
            "idf": kwargs.get("idf", idf),
            "k": kwargs.get("k", k),
            "b": kwargs.get("b", b),
        },
    )

@formula("min_max_scaling", "Min-Max Scaling", "(x - min) / (max - min)", DOMAIN_KEY, unit="")
def min_max_scaling(x: float | None = None, min_val: float | None = None, max_val: float | None = None, **kwargs):
    return build_result(
        fid="min_max_scaling",
        name="Min-Max Scaling",
        expression="(x - min) / (max - min)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
            "min_val": kwargs.get("min_val", min_val),
            "max_val": kwargs.get("max_val", max_val),
        },
    )

@formula("standard_scaling", "Standard Scaling (Z)", "(x - mean) / std", DOMAIN_KEY, unit="")
def standard_scaling(x: float | None = None, mean: float | None = None, std: float | None = None, **kwargs):
    return build_result(
        fid="standard_scaling",
        name="Standard Scaling (Z)",
        expression="(x - mean) / std",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
            "mean": kwargs.get("mean", mean),
            "std": kwargs.get("std", std),
        },
    )

@formula("robust_scaling", "Robust Scaling", "(x - median) / IQR", DOMAIN_KEY, unit="")
def robust_scaling(x: float | None = None, median: float | None = None, iqr: float | None = None, **kwargs):
    return build_result(
        fid="robust_scaling",
        name="Robust Scaling",
        expression="(x - median) / IQR",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
            "median": kwargs.get("median", median),
            "iqr": kwargs.get("iqr", iqr),
        },
    )

@formula("pca_explained_variance", "PCA Explained Variance Ratio", "Eigenvalue_i / Sum(Eigenvalues)", DOMAIN_KEY, unit="")
def pca_explained_variance(eigenvalue: float | None = None, total_eigenvalue_sum: float | None = None, **kwargs):
    return build_result(
        fid="pca_explained_variance",
        name="PCA Explained Variance Ratio",
        expression="Eigenvalue_i / Sum(Eigenvalues)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "eigenvalue": kwargs.get("eigenvalue", eigenvalue),
            "total_eigenvalue_sum": kwargs.get("total_eigenvalue_sum", total_eigenvalue_sum),
        },
    )

@formula("sigmoid_derivative", "Sigmoid Derivative", "sigmoid(x) * (1 - sigmoid(x))", DOMAIN_KEY, unit="")
def sigmoid_derivative(x: float | None = None, **kwargs):
    return build_result(
        fid="sigmoid_derivative",
        name="Sigmoid Derivative",
        expression="sigmoid(x) * (1 - sigmoid(x))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
        },
    )

@formula("dropout_inverted", "Inverted Dropout Scale", "x / (1 - drop_rate)", DOMAIN_KEY, unit="")
def dropout_inverted(x: float | None = None, drop_rate: float | None = None, **kwargs):
    return build_result(
        fid="dropout_inverted",
        name="Inverted Dropout Scale",
        expression="x / (1 - drop_rate)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
            "drop_rate": kwargs.get("drop_rate", drop_rate),
        },
    )

@formula("batch_normalization", "Batch Normalization", "gamma * (x - mean)/sqrt(var+eps) + beta", DOMAIN_KEY, unit="")
def batch_normalization(x: float | None = None, mean: float | None = None, var: float | None = None, gamma: float | None = None, beta: float | None = None, eps: float | None = None, **kwargs):
    return build_result(
        fid="batch_normalization",
        name="Batch Normalization",
        expression="gamma * (x - mean)/sqrt(var+eps) + beta",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
            "mean": kwargs.get("mean", mean),
            "var": kwargs.get("var", var),
            "gamma": kwargs.get("gamma", gamma),
            "beta": kwargs.get("beta", beta),
            "eps": kwargs.get("eps", eps),
        },
    )

@formula("layer_normalization", "Layer Normalization", "gamma * (x - mean)/sqrt(var+eps) + beta", DOMAIN_KEY, unit="")
def layer_normalization(x: float | None = None, mean: float | None = None, var: float | None = None, gamma: float | None = None, beta: float | None = None, eps: float | None = None, **kwargs):
    return build_result(
        fid="layer_normalization",
        name="Layer Normalization",
        expression="gamma * (x - mean)/sqrt(var+eps) + beta",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "x": kwargs.get("x", x),
            "mean": kwargs.get("mean", mean),
            "var": kwargs.get("var", var),
            "gamma": kwargs.get("gamma", gamma),
            "beta": kwargs.get("beta", beta),
            "eps": kwargs.get("eps", eps),
        },
    )

@formula("cosine_annealing", "Cosine Annealing LR", "lr_min + 0.5*(lr_max-lr_min)*(1+cos(pi*t/T))", DOMAIN_KEY, unit="")
def cosine_annealing(lr_min: float | None = None, lr_max: float | None = None, t: float | None = None, total_steps: float | None = None, **kwargs):
    return build_result(
        fid="cosine_annealing",
        name="Cosine Annealing LR",
        expression="lr_min + 0.5*(lr_max-lr_min)*(1+cos(pi*t/T))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "lr_min": kwargs.get("lr_min", lr_min),
            "lr_max": kwargs.get("lr_max", lr_max),
            "t": kwargs.get("t", t),
            "total_steps": kwargs.get("total_steps", total_steps),
        },
    )

@formula("attention_score", "Scaled Dot-Product Attention", "softmax(QK^T / sqrt(d_k))", DOMAIN_KEY, unit="")
def attention_score(query_key_dot: float | None = None, d_k: float | None = None, **kwargs):
    return build_result(
        fid="attention_score",
        name="Scaled Dot-Product Attention",
        expression="softmax(QK^T / sqrt(d_k))",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "query_key_dot": kwargs.get("query_key_dot", query_key_dot),
            "d_k": kwargs.get("d_k", d_k),
        },
    )

@formula("nadam_update", "NAdam Update Step", "theta - lr*mhat/(sqrt(vhat)+eps)", DOMAIN_KEY, unit="")
def nadam_update(theta: float | None = None, lr: float | None = None, mhat: float | None = None, vhat: float | None = None, eps: float | None = None, **kwargs):
    return build_result(
        fid="nadam_update",
        name="NAdam Update Step",
        expression="theta - lr*mhat/(sqrt(vhat)+eps)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "theta": kwargs.get("theta", theta),
            "lr": kwargs.get("lr", lr),
            "mhat": kwargs.get("mhat", mhat),
            "vhat": kwargs.get("vhat", vhat),
            "eps": kwargs.get("eps", eps),
        },
    )

@formula("adagrad_update", "AdaGrad Update Step", "theta - lr*g/(sqrt(G)+eps)", DOMAIN_KEY, unit="")
def adagrad_update(theta: float | None = None, lr: float | None = None, gradient: float | None = None, accumulated_sq: float | None = None, eps: float | None = None, **kwargs):
    return build_result(
        fid="adagrad_update",
        name="AdaGrad Update Step",
        expression="theta - lr*g/(sqrt(G)+eps)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "theta": kwargs.get("theta", theta),
            "lr": kwargs.get("lr", lr),
            "gradient": kwargs.get("gradient", gradient),
            "accumulated_sq": kwargs.get("accumulated_sq", accumulated_sq),
            "eps": kwargs.get("eps", eps),
        },
    )

@formula("weight_init_xavier", "Xavier Init Variance", "2 / (fan_in + fan_out)", DOMAIN_KEY, unit="")
def weight_init_xavier(fan_in: float | None = None, fan_out: float | None = None, **kwargs):
    return build_result(
        fid="weight_init_xavier",
        name="Xavier Init Variance",
        expression="2 / (fan_in + fan_out)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "fan_in": kwargs.get("fan_in", fan_in),
            "fan_out": kwargs.get("fan_out", fan_out),
        },
    )

@formula("weight_init_he", "He Init Variance", "2 / fan_in", DOMAIN_KEY, unit="")
def weight_init_he(fan_in: float | None = None, **kwargs):
    return build_result(
        fid="weight_init_he",
        name="He Init Variance",
        expression="2 / fan_in",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "fan_in": kwargs.get("fan_in", fan_in),
        },
    )

@formula("top_k_accuracy", "Top-K Accuracy", "Correct_in_TopK / Total", DOMAIN_KEY, unit="")
def top_k_accuracy(correct_in_topk: float | None = None, total: float | None = None, **kwargs):
    return build_result(
        fid="top_k_accuracy",
        name="Top-K Accuracy",
        expression="Correct_in_TopK / Total",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "correct_in_topk": kwargs.get("correct_in_topk", correct_in_topk),
            "total": kwargs.get("total", total),
        },
    )

@formula("ndcg", "NDCG", "DCG / IDCG", DOMAIN_KEY, unit="")
def ndcg(dcg: float | None = None, idcg: float | None = None, **kwargs):
    return build_result(
        fid="ndcg",
        name="NDCG",
        expression="DCG / IDCG",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "dcg": kwargs.get("dcg", dcg),
            "idcg": kwargs.get("idcg", idcg),
        },
    )

@formula("map_at_k", "Mean Average Precision @K", "Mean(AP@k per query)", DOMAIN_KEY, unit="")
def map_at_k(average_precisions: float | None = None, **kwargs):
    return build_result(
        fid="map_at_k",
        name="Mean Average Precision @K",
        expression="Mean(AP@k per query)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "average_precisions": kwargs.get("average_precisions", average_precisions),
        },
    )

@formula("hamming_loss", "Hamming Loss", "Wrong_Labels / Total_Labels", DOMAIN_KEY, unit="")
def hamming_loss(wrong_labels: float | None = None, total_labels: float | None = None, **kwargs):
    return build_result(
        fid="hamming_loss",
        name="Hamming Loss",
        expression="Wrong_Labels / Total_Labels",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "wrong_labels": kwargs.get("wrong_labels", wrong_labels),
            "total_labels": kwargs.get("total_labels", total_labels),
        },
    )

@formula("wasserstein_distance_1d", "Wasserstein Distance (1D)", "Sum(|CDF1 - CDF2|)", DOMAIN_KEY, unit="")
def wasserstein_distance_1d(cdf1: float | None = None, cdf2: float | None = None, **kwargs):
    return build_result(
        fid="wasserstein_distance_1d",
        name="Wasserstein Distance (1D)",
        expression="Sum(|CDF1 - CDF2|)",
        domain=DOMAIN_KEY,
        unit="",
        inputs={
            "cdf1": kwargs.get("cdf1", cdf1),
            "cdf2": kwargs.get("cdf2", cdf2),
        },
    )
