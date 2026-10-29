import pytest

from shopkit import pricing


@pytest.fixture(autouse=True)
def _clear():
    pricing.clear_cache()
    yield
    pricing.clear_cache()


def test_us_tax():
    assert pricing.price_with_tax({"sku": "MUG-01", "price_cents": 1000}, "US") == 1070


def test_cache_expires():
    p = {"sku": "MUG-01", "price_cents": 1000}
    assert pricing.price_with_tax(p, "UK", now=0.0) == 1200
    assert pricing.price_with_tax(p, "UK", now=pricing.CACHE_TTL_S + 1) == 1200
