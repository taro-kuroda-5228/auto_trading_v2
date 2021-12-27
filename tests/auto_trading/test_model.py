import pytest
import pandas
import lightgbm as lgb
from pandas._testing import assert_frame_equal
from sklearn.model_selection import train_test_split

from auto_trading.model import Model
from auto_trading.name import Name
from auto_trading.symbol_data import SymbolData
from auto_trading.datamart import Datamart
from auto_trading.raw_data import RawData


class TestModelInstance:
    @pytest.fixture(autouse=True)
    def setup(self):
        ticker_msft = Name("MSFT", "US").ticker
        symbol_data_msft = SymbolData(ticker_msft).symbol_data
        raw_data_msft = RawData(symbol_data_msft).raw_data
        self.datamart = Datamart(raw_data_msft, "open", 5).datamart
        self.model = Model(self.datamart)

    def test_model_instance_datamart(self):
        assert_frame_equal(self.model._datamart, self.datamart)

    def test_model_instance_fit_clf(self):
        self.model.fit()
        assert self.model.clf
