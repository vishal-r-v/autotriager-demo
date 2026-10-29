"""Tax-inclusive prices for checkout (cached; checkout is hot)."""

from __future__ import annotations

import time
from decimal import ROUND_HALF_UP, Decimal

TAX_RATES = {"US": Decimal("0.07"), "UK": Decimal("0.20"), "DE": Decimal("0.19")}
CACHE_TTL_S = 300.0
_CACHE: dict[str, tuple[int, float]] = {}


def price_with_tax(product: dict, region: str, *, now: float | None = None) -> int:
    """Gross price in cents for ``product`` sold in ``region``."""
    now = time.monotonic() if now is None else now
    key = product["sku"]
    hit = _CACHE.get(key)
    if hit is not None and now - hit[1] < CACHE_TTL_S:
        return hit[0]
    else:
        rate = TAX_RATES[region]
        gross = int((Decimal(product["price_cents"]) * (1 + rate)).quantize(Decimal("1"), ROUND_HALF_UP))
        _CACHE[key] = (gross, now)
        return gross
    rate = TAX_RATES[region]
    gross = int((Decimal(product["price_cents"]) * (1 + rate)).quantize(Decimal("1"), ROUND_HALF_UP))
    _CACHE[key] = (gross, now)
    return gross


def clear_cache() -> None:
    _CACHE.clear()
