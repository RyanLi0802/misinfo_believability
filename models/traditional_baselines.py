import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.model_selection import cross_validate, KFold
from sklearn.metrics import f1_score, precision_score, accuracy_score, recall_score, make_scorer
import data_utils
import xgboost as xgb

few_train, many_train = data_utils.get_train_set()
print(few_train.shape[0], many_train.shape[0])

train_data = pd.concat([few_train, many_train], axis=0)
train_targets = [0] * few_train.shape[0] + [1] * many_train.shape[0]

features = data_utils.extract_significant_features(train_data)
print(train_data.shape)
print(features.shape)

few_test, many_test = data_utils.get_test_set()
test_data = pd.concat([few_test, many_test], axis=0)

test_targets = [0] * few_test.shape[0] + [1] * many_test.shape[0]
test_features = data_utils.extract_significant_features(test_data)

classifiers = [
    LogisticRegression(max_iter=1000),
    KNeighborsClassifier(3),
    SVC(gamma=2, C=1),
    GaussianProcessClassifier(1.0 * RBF(1.0)),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(alpha=0.01, max_iter=10000),
    AdaBoostClassifier(),
    GaussianNB(),
]

for classifier in classifiers:
    result = []
    print("------------------------------------------")
    print(str(classifier))
    classifier.fit(features, train_targets)
    pred = classifier.predict(test_features)
    scoring = {'accuracy': make_scorer(accuracy_score),
               'precision': make_scorer(precision_score, average='macro'),
               'recall': make_scorer(recall_score),
               'f1': make_scorer(f1_score)
               }
    scores_dict = cross_validate(classifier, features, train_targets, cv=5, scoring=scoring,
                                 return_train_score=True)
    result.append([str(classifier), {metric: round(
        np.mean(scores), 5) for metric, scores in scores_dict.items()}])
    print("------------------------------------------")
    print(result)
    print()
    print()

# XGBoost
model = xgb.XGBClassifier()
scoring = {'accuracy': make_scorer(accuracy_score),
               'precision': make_scorer(precision_score, average='macro'),
               'recall': make_scorer(recall_score),
               'f1': make_scorer(f1_score)
               }
scores_dict = cross_validate(model, features, train_targets, cv=5, scoring=scoring, return_train_score=True)
result = []
result.append([str(model), {metric: round(
    np.mean(scores), 5) for metric, scores in scores_dict.items()}])
print("------------------------------------------")
print(result)