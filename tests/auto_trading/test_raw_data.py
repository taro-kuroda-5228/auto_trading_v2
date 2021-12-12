import pytest

from auto_trading.raw_data import RawData

import pandas as pd
import datetime

from auto_trading.symbol_data import SymbolData

symbol_data = SymbolData("MSFT").symbol_data


def test_raw_data_class():
    assert RawData(symbol_data)


def test_raw_data_type():
    raw_data_type = type(RawData(symbol_data).raw_data)
    actual = raw_data_type
    expected = pd.DataFrame
    assert actual == expected


def test_raw_data_data_n():
    data_n = RawData(symbol_data).raw_data.size
    actual = data_n
    expected = 286 * 6
    assert actual <= expected


def test_raw_data_index_0():
    # today = datetime.date.today()
    # today = today.strftime("%Y-%m-%d")
    today = "2021-12-10"
    actual = RawData(symbol_data).raw_data.loc[today]
    expected = pd.DataFrame([symbol_data]).tail(1)[1:6]
    assert all(actual == expected)
