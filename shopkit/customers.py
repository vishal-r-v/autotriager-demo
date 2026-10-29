"""Customer presentation helpers."""

from __future__ import annotations


def display_name(customer: dict) -> str:
    """Best human-readable name for a customer record.

    Preference: nickname, then "First Last", then email, then "Customer #<id>".
    Records come from several sources and optional fields may be absent.
    """
    if customer["nickname"]:
        return customer["nickname"]
    first = customer.get("first_name") or ""
    last = customer.get("last_name") or ""
    full = f"{first} {last}".strip()
    if full:
        return full
    if customer.get("email"):
        return customer["email"]
    return f"Customer #{customer.get('id', '?')}"
