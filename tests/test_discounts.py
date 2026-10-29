from decimal import Decimal

import pytest

from shopkit.discounts import apply_discount


def test_save10_on_large_order():
    assert apply_discount(Decimal("100.00"), "save10") == Decimal("90.00")


def test_save10_below_threshold():
    assert apply_discount(Decimal("49.99"), "SAVE10") == Decimal("49.99")


def test_no_code_and_unknown_code():
    assert apply_discount(Decimal("10.00"), None) == Decimal("10.00")
    with pytest.raises(ValueError):
        apply_discount(Decimal("10.00"), "BOGUS")
