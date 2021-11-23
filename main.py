# main.py
from auto_trading.datamart import Datamart
from auto_trading.name import Name
from auto_trading.raw_data import RawData
from auto_trading.symbol_data import SymbolData


def main():
  ticker = Name("MSFT", "US").ticker
  symbol_data = SymbolData(ticker).symbol_data
  raw_data = RawData(symbol_data).raw_data
  datamart = Datamart(raw_data, "close", 5)
  print(datamart.datamart.head())


if __name__ == "__main__":
  main()