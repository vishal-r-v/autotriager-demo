import pytest

from shopkit.money import format_cents, split_evenly, to_cents


def test_to_cents_simple():
    assert to_cents("10.00") == 1000
    assert to_cents(5) == 500


def test_format_cents():
    assert format_cents(123456) == "$1,234.56"
    assert format_cents(-5) == "-$0.05"


def test_split_evenly():
    assert split_evenly(1000, 3) == [334, 333, 333]
    with pytest.raises(ValueError):
        split_evenly(10, 0)
