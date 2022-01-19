
# coding: utf-8

import pandas as pd, numpy as np
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import roc_auc_score

param_grid = {
    "max_depth"        : [3, None],
    "max_features"     : [1, 3, 5],
    "min_samples_split": [2, 3, 10],
    "min_samples_leaf" : [1, 3, 10],
    "bootstrap"        : [True, False],
    "criterion"        : ["gini", "entropy"],
    "n_estimators"     : [5, 10]
}

clf = RandomForestClassifier()
