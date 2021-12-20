import pytest

from auto_trading.model import Model
from auto_trading.datamart import Datamart

datamart = Datamart.datamart


def test_model_class():
    assert Model(datamart)._datamart
