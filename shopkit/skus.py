"""SKU helpers shared by inventory and catalog."""

from __future__ import annotations


def normalize_sku(sku: str) -> str:
    """Canonical SKU form used as a dictionary key across the shop."""
    return sku.strip()
