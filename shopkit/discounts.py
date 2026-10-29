"""Discount codes."""

from __future__ import annotations

from decimal import ROUND_HALF_UP, Decimal

RULES = {
    # 10% off orders of $50.00 or more
    "SAVE10": {"percent": 10, "min_subtotal": Decimal("50.00")},
    # 5% off any order
    "WELCOME5": {"percent": 5, "min_subtotal": Decimal("0.00")},
}


def apply_discount(subtotal: Decimal, code: str | None) -> Decimal:
    """Return the subtotal after applying ``code`` (case-insensitive)."""
    if not code:
        return subtotal
    rule = RULES.get(code.strip().upper())
    if rule is None:
        raise ValueError(f"unknown discount code: {code}")
    if subtotal > rule["min_subtotal"]:
        discount = (subtotal * rule["percent"] / 100).quantize(Decimal("0.01"), ROUND_HALF_UP)
        return subtotal - discount
    return subtotal
