#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#
from .estimator_base import H2OEstimator


class H2ODeepLearningEstimator(H2OEstimator):
    """
    Deep Learning
    -------------
    Build a supervised Deep Neural Network model
    Builds a feed-forward multilayer artificial neural network on an H2OFrame

    Parameters (optional, unless specified otherwise)
    ----------
      model_id : str
        Destination id for this model; auto-generated if not specified.

      training_frame : str
        Id of the training data frame (Not required, to allow initial validation of model parameters).

      validation_frame : str
        Id of the validation data frame.

      nfolds : int
        Number of folds for N-fold cross-validation (0 to disable or ≥ 2).
        Default: 0

      keep_cross_validation_predictions : bool
        Whether to keep the predictions of the cross-validation models.
        Default: False

      keep_cross_validation_fold_assignment : bool
        Whether to keep the cross-validation fold assignment.
        Default: False

      fold_assignment : "AUTO" | "Random" | "Modulo" | "Stratified"
        Cross-validation fold assignment scheme, if fold_column is not specified. The 'Stratified' option will stratify
        the folds based on the response variable, for classification problems.
        Default: "AUTO"

      fold_column : VecSpecifier
        Column with cross-validation fold index assignment per observation.

      response_column : VecSpecifier
        Response variable column.

      ignored_columns : list(str)
        Names of columns to ignore for training.

      ignore_const_cols : bool
        Ignore constant columns.
        Default: True

      score_each_iteration : bool
        Whether to score during each iteration of model training.
        Default: False

      weights_column : VecSpecifier
        Column with observation weights. Giving some observation a weight of zero is equivalent to excluding it from the
        dataset; giving an observation a relative weight of 2 is equivalent to repeating that row twice. Negative
        weights are not allowed.

      offset_column : VecSpecifier
        Offset column. This will be added to the combination of columns before applying the link function.

      balance_classes : bool
        Balance training data class counts via over/under-sampling (for imbalanced data).
        Default: False

      class_sampling_factors : list(float)
        Desired over/under-sampling ratios per class (in lexicographic order). If not specified, sampling factors will
        be automatically computed to obtain class balance during training. Requires balance_classes.

      max_after_balance_size : float
        Maximum relative size of the training data after balancing class counts (can be less than 1.0). Requires
        balance_classes.
        Default: 5.0

      max_confusion_matrix_size : int
        Maximum size (# classes) for confusion matrices to be printed in the Logs.
        Default: 20

      max_hit_ratio_k : int
        Max. number (top K) of predictions to use for hit ratio computation (for multi-class only, 0 to disable).
        Default: 0

      checkpoint : str
        Model checkpoint to resume training with.

      pretrained_autoencoder : str
        Pretrained autoencoder model to initialize this model with.

      overwrite_with_best_model : bool
        If enabled, override the final model with the best model found during training.
        Default: True

      use_all_factor_levels : bool
        Use all factor levels of categorical variables. Otherwise, the first factor level is omitted (without loss of
        accuracy). Useful for variable importances and auto-enabled for autoencoder.
        Default: True

      standardize : bool
        If enabled, automatically standardize the data. If disabled, the user must provide properly scaled input data.
        Default: True

      activation : "Tanh" | "TanhWithDropout" | "Rectifier" | "RectifierWithDropout" | "Maxout" | "MaxoutWithDropout"
        Activation function.
        Default: "Rectifier"

      hidden : list(int)
        Hidden layer sizes (e.g. [100, 100]).
        Default: [200, 200]

      epochs : float
        How many times the dataset should be iterated (streamed), can be fractional.
        Default: 10.0

      train_samples_per_iteration : int
        Number of training samples (globally) per MapReduce iteration. Special values are 0: one epoch, -1: all
        available data (e.g., replicated training data), -2: automatic.
        Default: -2

      target_ratio_comm_to_comp : float
        Target ratio of communication overhead to computation. Only for multi-node operation and
        train_samples_per_iteration = -2 (auto-tuning).
        Default: 0.05

      seed : int
        Seed for random numbers (affects sampling) - Note: only reproducible when running single threaded.
        Default: -1

      adaptive_rate : bool
        Adaptive learning rate.
        Default: True

      rho : float
        Adaptive learning rate time decay factor (similarity to prior updates).
        Default: 0.99

      epsilon : float
        Adaptive learning rate smoothing factor (to avoid divisions by zero and allow progress).
        Default: 1e-08

      rate : float
        Learning rate (higher => less stable, lower => slower convergence).
        Default: 0.005

      rate_annealing : float
        Learning rate annealing: rate / (1 + rate_annealing * samples).
        Default: 1e-06

      rate_decay : float
        Learning rate decay factor between layers (N-th layer: rate·rate_decayᴺ⁻¹).
        Default: 1.0

      momentum_start : float
        Initial momentum at the beginning of training (try 0.5).
        Default: 0.0

      momentum_ramp : float
        Number of training samples for which momentum increases.
        Default: 1000000.0

      momentum_stable : float
        Final momentum after the ramp is over (try 0.99).
        Default: 0.0

      nesterov_accelerated_gradient : bool
        Use Nesterov accelerated gradient (recommended).
        Default: True

      input_dropout_ratio : float
        Input layer dropout ratio (can improve generalization, try 0.1 or 0.2).
        Default: 0.0

      hidden_dropout_ratios : list(float)
        Hidden layer dropout ratios (can improve generalization), specify one value per hidden layer, defaults to 0.5.

      l1 : float
        L1 regularization (can add stability and improve generalization, causes many weights to become 0).
        Default: 0.0

      l2 : float
        L2 regularization (can add stability and improve generalization, causes many weights to be small.
        Default: 0.0

      max_w2 : float
        Constraint for squared sum of incoming weights per unit (e.g. for Rectifier).
        Default: ∞

      initial_weight_distribution : "UniformAdaptive" | "Uniform" | "Normal"
        Initial weight distribution.
        Default: "UniformAdaptive"

      initial_weight_scale : float
        Uniform: -value...value, Normal: stddev.
        Default: 1.0

      initial_weights : list(str)
        A list of H2OFrame ids to initialize the weight matrices of this model with.

      initial_biases : list(str)
        A list of H2OFrame ids to initialize the bias vectors of this model with.

      loss : "Automatic" | "CrossEntropy" | "Quadratic" | "Huber" | "Absolute" | "Quantile"
        Loss function.
        Default: "Automatic"

      distribution : "AUTO" | "bernoulli" | "multinomial" | "gaussian" | "poisson" | "gamma" | "tweedie" | "laplace" |
                     "huber" | "quantile"
        Distribution function.
        Default: "AUTO"

      quantile_alpha : float
        Desired quantile for quantile regression (from 0.0 to 1.0).
        Default: 0.5

      tweedie_power : float
        Tweedie power.
        Default: 1.5

      score_interval : float
        Shortest time interval (in seconds) between model scoring.
        Default: 5.0

      score_training_samples : int
        Number of training set samples for scoring (0 for all).
        Default: 10000

      score_validation_samples : int
        Number of validation set samples for scoring (0 for all).
        Default: 0

      score_duty_cycle : float
        Maximum duty cycle fraction for scoring (lower: more training, higher: more scoring).
        Default: 0.1

      classification_stop : float
        Stopping criterion for classification error fraction on training data (-1 to disable).
        Default: 0.0

      regression_stop : float
        Stopping criterion for regression error (MSE) on training data (-1 to disable).
        Default: 1e-06

      stopping_rounds : int
        Early stopping based on convergence of stopping_metric. Stop if simple moving average of length k of the
        stopping_metric does not improve for k:=stopping_rounds scoring events (0 to disable)
        Default: 5

      stopping_metric : "AUTO" | "deviance" | "logloss" | "MSE" | "AUC" | "lift_top_group" | "r2" | "misclassification"
                        | "mean_per_class_error"
        Metric to use for early stopping (AUTO: logloss for classification, deviance for regression)
        Default: "AUTO"

      stopping_tolerance : float
        Relative tolerance for metric-based stopping criterion (stop if relative improvement is not at least this much)
        Default: 0.0

      max_runtime_secs : float
        Maximum allowed runtime in seconds for model training. Use 0 to disable.
        Default: 0.0

      score_validation_sampling : "Uniform" | "Stratified"
        Method used to sample validation dataset for scoring.
        Default: "Uniform"

      diagnostics : bool
        Enable diagnostics for hidden layers.
        Default: True

      fast_mode : bool
        Enable fast mode (minor approximation in back-propagation).
        Default: True

      force_load_balance : bool
        Force extra load balancing to increase training speed for small datasets (to keep all cores busy).
        Default: True

      variable_importances : bool
        Compute variable importances for input features (Gedeon method) - can be slow for large networks.
        Default: False

      replicate_training_data : bool
        Replicate the entire training dataset onto every node for faster training on small datasets.
        Default: True

      single_node_mode : bool
        Run on a single node for fine-tuning of model parameters.
        Default: False

      shuffle_training_data : bool
        Enable shuffling of training data (recommended if training data is replicated and train_samples_per_iteration is
        close to #nodes x #rows, of if using balance_classes).
        Default: False

      missing_values_handling : "Skip" | "MeanImputation"
        Handling of missing values. Either Skip or MeanImputation.
        Default: "MeanImputation"

      quiet_mode : bool
        Enable quiet mode for less output to standard output.
        Default: False

      autoencoder : bool
        Auto-Encoder.
        Default: False

      sparse : bool
        Sparse data handling (more efficient for data with lots of 0 values).
        Default: False

      col_major : bool
        #DEPRECATED Use a column major weight matrix for input layer. Can speed up forward propagation, but might slow
        down backpropagation.
        Default: False

      average_activation : float
        Average activation for sparse auto-encoder. #Experimental
        Default: 0.0

      sparsity_beta : float
        Sparsity regularization. #Experimental
        Default: 0.0

      max_categorical_features : int
        Max. number of categorical features, enforced via hashing. #Experimental
        Default: 2147483647

      reproducible : bool
        Force reproducibility on small data (will be slow - only uses 1 thread).
        Default: False

      export_weights_and_biases : bool
        Whether to export Neural Network weights and biases to H₂O Frames.
        Default: False

      mini_batch_size : int
        Mini-batch size (smaller leads to better fit, larger can speed up and generalize better).
        Default: 1

      elastic_averaging : bool
        Elastic averaging between compute nodes can improve distributed model convergence. #Experimental
        Default: False

      elastic_averaging_moving_rate : float
        Elastic averaging moving rate (only if elastic averaging is enabled).
        Default: 0.9

      elastic_averaging_regularization : float
        Elastic averaging regularization strength (only if elastic averaging is enabled).
        Default: 0.001

    Examples
    --------
      >>> import h2o as ml
      >>> from h2o.estimators.deeplearning import H2ODeepLearningEstimator
      >>> ml.init()
      >>> rows = [[1,2,3,4,0], [2,1,2,4,1], [2,1,4,2,1], [0,1,2,34,1], [2,3,4,1,0]] * 50
      >>> fr = ml.H2OFrame(rows)
      >>> fr[4] = fr[4].asfactor()
      >>> model = H2ODeepLearningEstimator()
      >>> model.train(x=range(4), y=4, training_frame=fr)
    """
    def __init__(self, **kwargs):
        super(H2ODeepLearningEstimator, self).__init__()
        self._parms = {}
        for name in ["model_id", "training_frame", "validation_frame", "nfolds", "keep_cross_validation_predictions",
                     "keep_cross_validation_fold_assignment", "fold_assignment", "fold_column", "response_column",
                     "ignored_columns", "ignore_const_cols", "score_each_iteration", "weights_column", "offset_column",
                     "balance_classes", "class_sampling_factors", "max_after_balance_size", "max_confusion_matrix_size",
                     "max_hit_ratio_k", "checkpoint", "pretrained_autoencoder", "overwrite_with_best_model",
                     "use_all_factor_levels", "standardize", "activation", "hidden", "epochs",
                     "train_samples_per_iteration", "target_ratio_comm_to_comp", "seed", "adaptive_rate", "rho",
                     "epsilon", "rate", "rate_annealing", "rate_decay", "momentum_start", "momentum_ramp",
                     "momentum_stable", "nesterov_accelerated_gradient", "input_dropout_ratio", "hidden_dropout_ratios",
                     "l1", "l2", "max_w2", "initial_weight_distribution", "initial_weight_scale", "initial_weights",
                     "initial_biases", "loss", "distribution", "quantile_alpha", "tweedie_power", "score_interval",
                     "score_training_samples", "score_validation_samples", "score_duty_cycle", "classification_stop",
                     "regression_stop", "stopping_rounds", "stopping_metric", "stopping_tolerance", "max_runtime_secs",
                     "score_validation_sampling", "diagnostics", "fast_mode", "force_load_balance",
                     "variable_importances", "replicate_training_data", "single_node_mode", "shuffle_training_data",
                     "missing_values_handling", "quiet_mode", "autoencoder", "sparse", "col_major",
                     "average_activation", "sparsity_beta", "max_categorical_features", "reproducible",
                     "export_weights_and_biases", "mini_batch_size", "elastic_averaging",
                     "elastic_averaging_moving_rate", "elastic_averaging_regularization"]:
            pname = name[:-1] if name[-1] == '_' else name
            self._parms[pname] = kwargs[name] if name in kwargs else None
        if isinstance(self, H2OAutoEncoderEstimator): self._parms['autoencoder'] = True

    @property
    def training_frame(self):
        return self._parms["training_frame"]

    @training_frame.setter
    def training_frame(self, value):
        self._parms["training_frame"] = value

    @property
    def validation_frame(self):
        return self._parms["validation_frame"]

    @validation_frame.setter
    def validation_frame(self, value):
        self._parms["validation_frame"] = value

    @property
    def nfolds(self):
        return self._parms["nfolds"]

    @nfolds.setter
    def nfolds(self, value):
        self._parms["nfolds"] = value

    @property
    def keep_cross_validation_predictions(self):
        return self._parms["keep_cross_validation_predictions"]

    @keep_cross_validation_predictions.setter
    def keep_cross_validation_predictions(self, value):
        self._parms["keep_cross_validation_predictions"] = value

    @property
    def keep_cross_validation_fold_assignment(self):
        return self._parms["keep_cross_validation_fold_assignment"]

    @keep_cross_validation_fold_assignment.setter
    def keep_cross_validation_fold_assignment(self, value):
        self._parms["keep_cross_validation_fold_assignment"] = value

    @property
    def fold_assignment(self):
        return self._parms["fold_assignment"]

    @fold_assignment.setter
    def fold_assignment(self, value):
        self._parms["fold_assignment"] = value

    @property
    def fold_column(self):
        return self._parms["fold_column"]

    @fold_column.setter
    def fold_column(self, value):
        self._parms["fold_column"] = value

    @property
    def response_column(self):
        return self._parms["response_column"]

    @response_column.setter
    def response_column(self, value):
        self._parms["response_column"] = value

    @property
    def ignored_columns(self):
        return self._parms["ignored_columns"]

    @ignored_columns.setter
    def ignored_columns(self, value):
        self._parms["ignored_columns"] = value

    @property
    def ignore_const_cols(self):
        return self._parms["ignore_const_cols"]

    @ignore_const_cols.setter
    def ignore_const_cols(self, value):
        self._parms["ignore_const_cols"] = value

    @property
    def score_each_iteration(self):
        return self._parms["score_each_iteration"]

    @score_each_iteration.setter
    def score_each_iteration(self, value):
        self._parms["score_each_iteration"] = value

    @property
    def weights_column(self):
        return self._parms["weights_column"]

    @weights_column.setter
    def weights_column(self, value):
        self._parms["weights_column"] = value

    @property
    def offset_column(self):
        return self._parms["offset_column"]

    @offset_column.setter
    def offset_column(self, value):
        self._parms["offset_column"] = value

    @property
    def balance_classes(self):
        return self._parms["balance_classes"]

    @balance_classes.setter
    def balance_classes(self, value):
        self._parms["balance_classes"] = value

    @property
    def class_sampling_factors(self):
        return self._parms["class_sampling_factors"]

    @class_sampling_factors.setter
    def class_sampling_factors(self, value):
        self._parms["class_sampling_factors"] = value

    @property
    def max_after_balance_size(self):
        return self._parms["max_after_balance_size"]

    @max_after_balance_size.setter
    def max_after_balance_size(self, value):
        self._parms["max_after_balance_size"] = value

    @property
    def max_confusion_matrix_size(self):
        return self._parms["max_confusion_matrix_size"]

    @max_confusion_matrix_size.setter
    def max_confusion_matrix_size(self, value):
        self._parms["max_confusion_matrix_size"] = value

    @property
    def max_hit_ratio_k(self):
        return self._parms["max_hit_ratio_k"]

    @max_hit_ratio_k.setter
    def max_hit_ratio_k(self, value):
        self._parms["max_hit_ratio_k"] = value

    @property
    def checkpoint(self):
        return self._parms["checkpoint"]

    @checkpoint.setter
    def checkpoint(self, value):
        self._parms["checkpoint"] = value

    @property
    def pretrained_autoencoder(self):
        return self._parms["pretrained_autoencoder"]

    @pretrained_autoencoder.setter
    def pretrained_autoencoder(self, value):
        self._parms["pretrained_autoencoder"] = value

    @property
    def overwrite_with_best_model(self):
        return self._parms["overwrite_with_best_model"]

    @overwrite_with_best_model.setter
    def overwrite_with_best_model(self, value):
        self._parms["overwrite_with_best_model"] = value

    @property
    def use_all_factor_levels(self):
        return self._parms["use_all_factor_levels"]

    @use_all_factor_levels.setter
    def use_all_factor_levels(self, value):
        self._parms["use_all_factor_levels"] = value

    @property
    def standardize(self):
        return self._parms["standardize"]

    @standardize.setter
    def standardize(self, value):
        self._parms["standardize"] = value

    @property
    def activation(self):
        return self._parms["activation"]

    @activation.setter
    def activation(self, value):
        self._parms["activation"] = value

    @property
    def hidden(self):
        return self._parms["hidden"]

    @hidden.setter
    def hidden(self, value):
        self._parms["hidden"] = value

    @property
    def epochs(self):
        return self._parms["epochs"]

    @epochs.setter
    def epochs(self, value):
        self._parms["epochs"] = value

    @property
    def train_samples_per_iteration(self):
        return self._parms["train_samples_per_iteration"]

    @train_samples_per_iteration.setter
    def train_samples_per_iteration(self, value):
        self._parms["train_samples_per_iteration"] = value

    @property
    def target_ratio_comm_to_comp(self):
        return self._parms["target_ratio_comm_to_comp"]

    @target_ratio_comm_to_comp.setter
    def target_ratio_comm_to_comp(self, value):
        self._parms["target_ratio_comm_to_comp"] = value

    @property
    def seed(self):
        return self._parms["seed"]

    @seed.setter
    def seed(self, value):
        self._parms["seed"] = value

    @property
    def adaptive_rate(self):
        return self._parms["adaptive_rate"]

    @adaptive_rate.setter
    def adaptive_rate(self, value):
        self._parms["adaptive_rate"] = value

    @property
    def rho(self):
        return self._parms["rho"]

    @rho.setter
    def rho(self, value):
        self._parms["rho"] = value

    @property
    def epsilon(self):
        return self._parms["epsilon"]

    @epsilon.setter
    def epsilon(self, value):
        self._parms["epsilon"] = value

    @property
    def rate(self):
        return self._parms["rate"]

    @rate.setter
    def rate(self, value):
        self._parms["rate"] = value

    @property
    def rate_annealing(self):
        return self._parms["rate_annealing"]

    @rate_annealing.setter
    def rate_annealing(self, value):
        self._parms["rate_annealing"] = value

    @property
    def rate_decay(self):
        return self._parms["rate_decay"]

    @rate_decay.setter
    def rate_decay(self, value):
        self._parms["rate_decay"] = value

    @property
    def momentum_start(self):
        return self._parms["momentum_start"]

    @momentum_start.setter
    def momentum_start(self, value):
        self._parms["momentum_start"] = value

    @property
    def momentum_ramp(self):
        return self._parms["momentum_ramp"]

    @momentum_ramp.setter
    def momentum_ramp(self, value):
        self._parms["momentum_ramp"] = value

    @property
    def momentum_stable(self):
        return self._parms["momentum_stable"]

    @momentum_stable.setter
    def momentum_stable(self, value):
        self._parms["momentum_stable"] = value

    @property
    def nesterov_accelerated_gradient(self):
        return self._parms["nesterov_accelerated_gradient"]

    @nesterov_accelerated_gradient.setter
    def nesterov_accelerated_gradient(self, value):
        self._parms["nesterov_accelerated_gradient"] = value

    @property
    def input_dropout_ratio(self):
        return self._parms["input_dropout_ratio"]

    @input_dropout_ratio.setter
    def input_dropout_ratio(self, value):
        self._parms["input_dropout_ratio"] = value

    @property
    def hidden_dropout_ratios(self):
        return self._parms["hidden_dropout_ratios"]

    @hidden_dropout_ratios.setter
    def hidden_dropout_ratios(self, value):
        self._parms["hidden_dropout_ratios"] = value

    @property
    def l1(self):
        return self._parms["l1"]

    @l1.setter
    def l1(self, value):
        self._parms["l1"] = value

    @property
    def l2(self):
        return self._parms["l2"]

    @l2.setter
    def l2(self, value):
        self._parms["l2"] = value

    @property
    def max_w2(self):
        return self._parms["max_w2"]

    @max_w2.setter
    def max_w2(self, value):
        self._parms["max_w2"] = value

    @property
    def initial_weight_distribution(self):
        return self._parms["initial_weight_distribution"]

    @initial_weight_distribution.setter
    def initial_weight_distribution(self, value):
        self._parms["initial_weight_distribution"] = value

    @property
    def initial_weight_scale(self):
        return self._parms["initial_weight_scale"]

    @initial_weight_scale.setter
    def initial_weight_scale(self, value):
        self._parms["initial_weight_scale"] = value

    @property
    def initial_weights(self):
        return self._parms["initial_weights"]

    @initial_weights.setter
    def initial_weights(self, value):
        self._parms["initial_weights"] = value

    @property
    def initial_biases(self):
        return self._parms["initial_biases"]

    @initial_biases.setter
    def initial_biases(self, value):
        self._parms["initial_biases"] = value

    @property
    def loss(self):
        return self._parms["loss"]

    @loss.setter
    def loss(self, value):
        self._parms["loss"] = value

    @property
    def distribution(self):
        return self._parms["distribution"]

    @distribution.setter
    def distribution(self, value):
        self._parms["distribution"] = value

    @property
    def quantile_alpha(self):
        return self._parms["quantile_alpha"]

    @quantile_alpha.setter
    def quantile_alpha(self, value):
        self._parms["quantile_alpha"] = value

    @property
    def tweedie_power(self):
        return self._parms["tweedie_power"]

    @tweedie_power.setter
    def tweedie_power(self, value):
        self._parms["tweedie_power"] = value

    @property
    def score_interval(self):
        return self._parms["score_interval"]

    @score_interval.setter
    def score_interval(self, value):
        self._parms["score_interval"] = value

    @property
    def score_training_samples(self):
        return self._parms["score_training_samples"]

    @score_training_samples.setter
    def score_training_samples(self, value):
        self._parms["score_training_samples"] = value

    @property
    def score_validation_samples(self):
        return self._parms["score_validation_samples"]

    @score_validation_samples.setter
    def score_validation_samples(self, value):
        self._parms["score_validation_samples"] = value

    @property
    def score_duty_cycle(self):
        return self._parms["score_duty_cycle"]

    @score_duty_cycle.setter
    def score_duty_cycle(self, value):
        self._parms["score_duty_cycle"] = value

    @property
    def classification_stop(self):
        return self._parms["classification_stop"]

    @classification_stop.setter
    def classification_stop(self, value):
        self._parms["classification_stop"] = value

    @property
    def regression_stop(self):
        return self._parms["regression_stop"]

    @regression_stop.setter
    def regression_stop(self, value):
        self._parms["regression_stop"] = value

    @property
    def stopping_rounds(self):
        return self._parms["stopping_rounds"]

    @stopping_rounds.setter
    def stopping_rounds(self, value):
        self._parms["stopping_rounds"] = value

    @property
    def stopping_metric(self):
        return self._parms["stopping_metric"]

    @stopping_metric.setter
    def stopping_metric(self, value):
        self._parms["stopping_metric"] = value

    @property
    def stopping_tolerance(self):
        return self._parms["stopping_tolerance"]

    @stopping_tolerance.setter
    def stopping_tolerance(self, value):
        self._parms["stopping_tolerance"] = value

    @property
    def max_runtime_secs(self):
        return self._parms["max_runtime_secs"]

    @max_runtime_secs.setter
    def max_runtime_secs(self, value):
        self._parms["max_runtime_secs"] = value

    @property
    def score_validation_sampling(self):
        return self._parms["score_validation_sampling"]

    @score_validation_sampling.setter
    def score_validation_sampling(self, value):
        self._parms["score_validation_sampling"] = value

    @property
    def diagnostics(self):
        return self._parms["diagnostics"]

    @diagnostics.setter
    def diagnostics(self, value):
        self._parms["diagnostics"] = value

    @property
    def fast_mode(self):
        return self._parms["fast_mode"]

    @fast_mode.setter
    def fast_mode(self, value):
        self._parms["fast_mode"] = value

    @property
    def force_load_balance(self):
        return self._parms["force_load_balance"]

    @force_load_balance.setter
    def force_load_balance(self, value):
        self._parms["force_load_balance"] = value

    @property
    def variable_importances(self):
        return self._parms["variable_importances"]

    @variable_importances.setter
    def variable_importances(self, value):
        self._parms["variable_importances"] = value

    @property
    def replicate_training_data(self):
        return self._parms["replicate_training_data"]

    @replicate_training_data.setter
    def replicate_training_data(self, value):
        self._parms["replicate_training_data"] = value

    @property
    def single_node_mode(self):
        return self._parms["single_node_mode"]

    @single_node_mode.setter
    def single_node_mode(self, value):
        self._parms["single_node_mode"] = value

    @property
    def shuffle_training_data(self):
        return self._parms["shuffle_training_data"]

    @shuffle_training_data.setter
    def shuffle_training_data(self, value):
        self._parms["shuffle_training_data"] = value

    @property
    def missing_values_handling(self):
        return self._parms["missing_values_handling"]

    @missing_values_handling.setter
    def missing_values_handling(self, value):
        self._parms["missing_values_handling"] = value

    @property
    def quiet_mode(self):
        return self._parms["quiet_mode"]

    @quiet_mode.setter
    def quiet_mode(self, value):
        self._parms["quiet_mode"] = value

    @property
    def autoencoder(self):
        return self._parms["autoencoder"]

    @autoencoder.setter
    def autoencoder(self, value):
        self._parms["autoencoder"] = value

    @property
    def sparse(self):
        return self._parms["sparse"]

    @sparse.setter
    def sparse(self, value):
        self._parms["sparse"] = value

    @property
    def col_major(self):
        return self._parms["col_major"]

    @col_major.setter
    def col_major(self, value):
        self._parms["col_major"] = value

    @property
    def average_activation(self):
        return self._parms["average_activation"]

    @average_activation.setter
    def average_activation(self, value):
        self._parms["average_activation"] = value

    @property
    def sparsity_beta(self):
        return self._parms["sparsity_beta"]

    @sparsity_beta.setter
    def sparsity_beta(self, value):
        self._parms["sparsity_beta"] = value

    @property
    def max_categorical_features(self):
        return self._parms["max_categorical_features"]

    @max_categorical_features.setter
    def max_categorical_features(self, value):
        self._parms["max_categorical_features"] = value

    @property
    def reproducible(self):
        return self._parms["reproducible"]

    @reproducible.setter
    def reproducible(self, value):
        self._parms["reproducible"] = value

    @property
    def export_weights_and_biases(self):
        return self._parms["export_weights_and_biases"]

    @export_weights_and_biases.setter
    def export_weights_and_biases(self, value):
        self._parms["export_weights_and_biases"] = value

    @property
    def mini_batch_size(self):
        return self._parms["mini_batch_size"]

    @mini_batch_size.setter
    def mini_batch_size(self, value):
        self._parms["mini_batch_size"] = value

    @property
    def elastic_averaging(self):
        return self._parms["elastic_averaging"]

    @elastic_averaging.setter
    def elastic_averaging(self, value):
        self._parms["elastic_averaging"] = value

    @property
    def elastic_averaging_moving_rate(self):
        return self._parms["elastic_averaging_moving_rate"]

    @elastic_averaging_moving_rate.setter
    def elastic_averaging_moving_rate(self, value):
        self._parms["elastic_averaging_moving_rate"] = value

    @property
    def elastic_averaging_regularization(self):
        return self._parms["elastic_averaging_regularization"]

    @elastic_averaging_regularization.setter
    def elastic_averaging_regularization(self, value):
        self._parms["elastic_averaging_regularization"] = value

class H2OAutoEncoderEstimator(H2ODeepLearningEstimator):
    """
    Examples
    --------
      >>> import h2o as ml
      >>> from h2o.estimators.deeplearning import H2OAutoEncoderEstimator
      >>> ml.init()
      >>> rows = [[1,2,3,4,0]*50, [2,1,2,4,1]*50, [2,1,4,2,1]*50, [0,1,2,34,1]*50, [2,3,4,1,0]*50]
      >>> fr = ml.H2OFrame(rows)
      >>> fr[4] = fr[4].asfactor()
      >>> model = H2OAutoEncoderEstimator()
      >>> model.train(x=range(4), training_frame=fr)
    """
    pass

