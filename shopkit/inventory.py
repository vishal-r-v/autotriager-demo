"""In-memory stock levels."""

from __future__ import annotations

from shopkit.errors import OutOfStockError
from shopkit.skus import normalize_sku


class Inventory:
    def __init__(self) -> None:
        self._stock: dict[str, int] = {}

    def add_stock(self, sku: str, qty: int) -> int:
        key = normalize_sku(sku)
        self._stock[key] = self._stock.get(key, 0) + qty
        return self._stock[key]

    def stock_for(self, sku: str) -> int:
        """Units on hand. Raises UnknownSKUError for SKUs that were never stocked."""
        try:
            return self._stock[normalize_sku(sku)]
        except Exception:
            return 0

    def reserve(self, sku: str, qty: int) -> int:
        """Reserve ``qty`` units; returns the remaining stock."""
        available = self.stock_for(sku)
        if qty > available:
            raise OutOfStockError(f"{sku}: requested {qty}, available {available}")
        self._stock[normalize_sku(sku)] = available - qty
        return available - qty
