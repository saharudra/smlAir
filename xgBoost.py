import xgboost as xgb
import pandas as pd
from xgboost.sklearn import XGBClassifier
import numpy as np
from sklearn import metrics
from sklearn.grid_search import GridSearchCV
import time


smallerDataset = pd.read_csv("smallerDataset.csv", sep = ',')
train = pd.DataFrame.as_matrix(smallerDataset)[1:7000, 3:-1]
train_labels = pd.DataFrame.as_matrix(smallerDataset)[1:7000, -1]
test = pd.DataFrame.as_matrix(smallerDataset)[7000:, 3:-1]
test_labels = pd.DataFrame.as_matrix(smallerDataset)[7000:, -1]
print(train_labels.shape)
dtrain = xgb.DMatrix(train, train_labels)
dtest = xgb.DMatrix(test, test_labels)
print("Train dataset contains {0} rows and {1} columns".format(dtrain.num_row(), dtrain.num_col()))

num_rounds = 10
'''
for i in range(3, 10, 2):
    for j in range(1, 7, 2):
        init_params = {
            'learning_rate': 0.1,
            'n_estimators': 1000,
            'max_depth': i,
            'min_child_weight': j,
            'silent': 1,
            'gamma': 0,
            'subsample': 0.8,
            'colsample_bytree': 0.8,
            'objective': 'multi:softprob',
            'nthread': 4,
            'scale_pos_weight': 1,
            'seed': 27,
            'num_class': 12
        }

        print("MAX DEPTH : ", i)
        print("MIN CHILD WEIGHT : ", j)
        watchlist = [(dtest, 'test'), (dtrain, 'train')]
        clf = xgb.train(init_params, dtrain, num_rounds, watchlist)
'''

seed = 342
np.random.seed(seed)


params_grid = {
    'max_depth':[1, 3, 5, 7, 9],
    'n_estimators':[10, 100, 1000],
    'learning_rate':np.linspace(1e-16, 1, 3),
    'min_child_weight':[1, 3, 5, 7],
    'gamma':[0, 0.1, 0.3, 0.5]
}

params_fixed = {
    'learning_rate': 0.1,
    'silent': 1,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    'objective': 'multi:softprob',
    'nthread': 4,
    'scale_pos_weight': 1,
}

bst_grid = GridSearchCV(
    estimator=XGBClassifier(**params_fixed, seed = seed),
    param_grid=params_grid,
    cv = 5,
    scoring='accuracy'
    )
train_labels = train_labels.astype(str)
bst_grid.fit(train, train_labels)

bst_grid.grid_scores_