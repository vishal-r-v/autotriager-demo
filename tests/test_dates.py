from datetime import date

import pytest

from shopkit.dates import parse_order_date
from shopkit.errors import InvalidDateError


def test_iso_dates():
    assert parse_order_date("2024-02-29") == date(2024, 2, 29)


def test_garbage_rejected():
    with pytest.raises(InvalidDateError):
        parse_order_date("yesterday")
