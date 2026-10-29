"""Sales reports for the admin dashboard."""

from __future__ import annotations


def customer_totals(orders: list[dict]) -> dict[str, int]:
    """Total spend in cents per customer id."""
    totals: dict[str, int] = {}
    for order in orders:
        cid = order["customer_id"]
        totals[cid] = totals.get(cid, 0) + order["total_cents"]
    return totals


def top_customers(orders: list[dict], n: int = 3) -> list[tuple[str, int]]:
    """The ``n`` customers with the highest total spend, highest first."""
    ranked = sorted(customer_totals(orders).items(), key=lambda kv: -kv[1])
    return ranked[:n]
