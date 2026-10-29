import pytest

from shopkit.cart import Cart


def test_add_merges_same_sku():
    cart = Cart("c1", items=[])
    cart.add("MUG-01", 2)
    cart.add("MUG-01")
    assert cart.items == [{"sku": "MUG-01", "qty": 3}]
    assert cart.count() == 3


def test_qty_must_be_positive():
    with pytest.raises(ValueError):
        Cart("c1", items=[]).add("MUG-01", 0)
