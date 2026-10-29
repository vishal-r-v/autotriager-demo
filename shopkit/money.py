"""Money helpers. Amounts are stored as integer cents."""

from __future__ import annotations


def to_cents(amount) -> int:
    """Convert a decimal amount (str, int, float or Decimal) to cents, rounding half-up."""
    from decimal import Decimal, ROUND_HALF_UP
    # Convert the input to a Decimal for accurate arithmetic
    dec_amount = Decimal(str(amount))
    # Multiply by 100 and round half up to the nearest cent
    cents = (dec_amount * Decimal('100')).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    return int(cents)


def format_cents(cents: int) -> str:
    sign = "-" if cents < 0 else ""
    cents = abs(cents)
    return f"{sign}${cents // 100:,}.{cents % 100:02d}"


def split_evenly(total_cents: int, parts: int) -> list[int]:
    """Split a total into ``parts`` amounts that differ by at most one cent."""
    if parts < 1:
        raise ValueError("parts must be >= 1")
    base, rem = divmod(total_cents, parts)
    return [base + (1 if i < rem else 0) for i in range(parts)]
