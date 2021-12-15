import pytest
import pandas as pd

from auto_trading.name import Name
from auto_trading.symbol_data import SymbolData
from auto_trading.datamart import Datamart
from auto_trading.raw_data import RawData

ticker_msft = Name("MSFT", "US").ticker
symbol_data_msft = SymbolData(ticker_msft).symbol_data
raw_data_msft = RawData(symbol_data_msft).raw_data

ticker_toyota = Name("7203", "JP").ticker
symbol_data_toyota = SymbolData(ticker_toyota).symbol_data
raw_data_toyota = RawData(symbol_data_toyota).raw_data


def test_datamart_class():
    assert Datamart(raw_data_msft, "open", 5)


def test_datamart_type():
    actual = type(Datamart(raw_data_msft, "open", 5).datamart)
    expected = pd.DataFrame
    assert actual == expected


def test_datamart_us():
    actual = Datamart(raw_data_msft, "open", 5).datamart
    expected = [333.22, 340.68, 334.98, 334.98, 334.98, 334.41, 335.31]
    assert all(actual == expected)


def test_datamart_jp():
    actual = Datamart(raw_data_toyota, "close", 3).datamart
    expected = [2118.50, 2045.00, 2002.00, 2052.00, 2052.00]
    assert all(actual == expected)
