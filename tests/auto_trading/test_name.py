import pytest

from auto_trading.name import Name


def test_name_class():
    assert Name("MSFT", "US")


@pytest.mark.parametrize(
    "company_ticker,nation,ticker_expected",
    [("MSFT", "US", "MSFT"), ("7203", "JP", "7203.T")],
    )
def test_name(company_ticker, nation, ticker_expected):
    ticker = Name(company_ticker, nation).ticker
    actual = ticker
    expected = ticker_expected
    assert actual == expected
