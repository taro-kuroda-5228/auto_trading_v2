import lightgbm as lgb
import pandas as pd
from sklearn.model_selection import train_test_split

clf = lgb.LGBMClassifier()


class Model:
    def __init__(self, datamart):
        self._datamart = datamart

    def fit(self, clf):
        self.clf = clf
        return self.clf
