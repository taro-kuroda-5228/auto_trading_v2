import pytest

from auto_trading.symbol_data import SymbolData


def test_symbol_data_class():
  assert SymbolData('MSFT')

def symbol_data_type():
  type = type(SymbolData.symbol_data)
  actual = type
  type_expected = dict
  assert actual == type_expected

def symbol_data_keys():
  keys = list(SymbolData.symbol_data.keys())
  actual = keys
  keys_expected = ["timestamp", "open", "high", "low", "close", "volume"]
  assert actual == keys_expected

def symbol_data_data_n():
  data_n = len(SymbolData.symbol_data["timestamp"])
  actual = data_n
  data_n_expected = 286
  assert actual <= data_n_expected
