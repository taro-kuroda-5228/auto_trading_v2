import pytest

from auto_trading.raw_data import RawData

import pandas as pd
import datetime

from auto_trading.symbol_data import SymbolData

symbol_data = SymbolData("MSFT").symbol_data


def test_raw_data_class():
    assert RawData(symbol_data)


def test_raw_data_type():
    actual = type(RawData(symbol_data).raw_data)
    expected = pd.DataFrame
    assert actual == expected


def test_raw_data_data_n():
    actual = RawData(symbol_data).raw_data.size
    expected = 286 * 6
    assert actual <= expected


def adjust_date_of_week(date):
    date_of_week = datetime.date.today().strftime("%A")
    if date_of_week == "Sunday":
        date -= datetime.timedelta(days=2)
    elif date_of_week == "Monday":
        date -= datetime.timedelta(days=3)
    else:
        date -= datetime.timedelta(days=1)
    return date


def test_raw_data_index_0():
    date = datetime.date.today()
    date = adjust_date_of_week(date)
    expected = date.strftime("%Y-%m-%d")
    actual = RawData(symbol_data).raw_data.index[0]
    assert actual == expected
