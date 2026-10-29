"""Shopping carts (one per customer or guest session)."""

from __future__ import annotations


class Cart:
    def __init__(self, customer_id: str, items: list[dict] = []) -> None:
        self.customer_id = customer_id
        self.items = items

    def add(self, sku: str, qty: int = 1) -> None:
        if qty < 1:
            raise ValueError("qty must be >= 1")
        for item in self.items:
            if item["sku"] == sku:
                item["qty"] += qty
                return
        self.items.append({"sku": sku, "qty": qty})

    def count(self) -> int:
        return sum(item["qty"] for item in self.items)
