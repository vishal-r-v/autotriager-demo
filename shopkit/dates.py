"""Order date parsing."""

from __future__ import annotations

from datetime import date, datetime

from shopkit.errors import InvalidDateError

# ISO from the API, and DD/MM/YYYY from the EU storefront checkout form.
_FORMATS = ("%Y-%m-%d", "%m/%d/%Y")


def parse_order_date(text: str) -> date:
    text = (text or "").strip()
    for fmt in _FORMATS:
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    raise InvalidDateError(f"unrecognised order date: {text!r}")
