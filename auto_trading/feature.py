import pandas as pd
from symbol_data import SymbolData
from raw_data import RawData
from datamart import Datamart

class Feature:
    """Feature class creates pd.DataFrame composed by explanatory variables.
    By putting datamarts of ETFs or index names listed on yahoo-finance, you can get a pd.DataFrame with explanatory variables.
    Args:
        datamarts: datamarts list you want to make explanatory variables   
    """    
    
    def __init__(self, datamarts: list):
        self._datamarts = datamarts
        
    def concat_datamarts(self) -> pd.DataFrame:
        self._datamarts = [pd.DataFrame(self._datamart).drop('target', axis=1) for self._datamart in self._datamarts]
        self.df = pd.concat([self._datamart for self._datamart in self._datamarts], axis=1)
        return self.df
