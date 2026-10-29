"""Product catalog."""

from __future__ import annotations

from shopkit.errors import UnknownSKUError
from shopkit.skus import normalize_sku


class Catalog:
    def __init__(self) -> None:
        self._products: dict[str, dict] = {}

    def register(self, sku: str, name: str, price_cents: int) -> dict:
        product = {"sku": sku.strip(), "name": name, "price_cents": price_cents}
        self._products[sku.strip().lower()] = product
        return product

    def get(self, sku: str) -> dict:
        try:
            return self._products[normalize_sku(sku)]
        except KeyError:
            raise UnknownSKUError(sku) from None

    def __len__(self) -> int:
        return len(self._products)
