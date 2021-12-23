import pytest
import pandas
from pandas._testing import assert_frame_equal

from auto_trading.model import Model
from auto_trading.name import Name
from auto_trading.symbol_data import SymbolData
from auto_trading.datamart import Datamart
from auto_trading.raw_data import RawData


ticker_msft = Name("MSFT", "US").ticker
symbol_data_msft = SymbolData(ticker_msft).symbol_data
raw_data_msft = RawData(symbol_data_msft).raw_data
datamart = Datamart(raw_data_msft, "open", 5).datamart

model = Model(datamart)


def test_model_instance_datamart():
    assert_frame_equal(model._datamart, datamart)
