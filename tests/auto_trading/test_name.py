from auto_trading.name import Name

def test_name():
    actual = Name("MSFT", "US").ticker
    expected = "MSFT"
    assert actual == expected
