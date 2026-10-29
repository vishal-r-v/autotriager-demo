import pytest

from shopkit.errors import OutOfStockError
from shopkit.inventory import Inventory


def test_add_and_reserve():
    inv = Inventory()
    inv.add_stock("AB-1", 5)
    assert inv.reserve("AB-1", 2) == 3
    assert inv.stock_for("AB-1") == 3


def test_out_of_stock():
    inv = Inventory()
    inv.add_stock("AB-1", 1)
    with pytest.raises(OutOfStockError):
        inv.reserve("AB-1", 2)
