import lightgbm as lgb
import pandas as pd
from sklearn.model_selection import train_test_split


class Model:
    def __init__(self, datamart):
        self._datamart = datamart

    def fit(self):
        self.clf = lgb.LGBMClassifier()
        self.df = pd.DataFrame(self._datamart)
        self.X = self.df[
            ["open_N-0", "open_N-1", "open_N-2", "open_N-3", "open_N-4", "open_N-5"]
        ]
        self.y = self.df["target"]
        self.clf.fit(self.X, self.y)
