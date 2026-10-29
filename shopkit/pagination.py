"""Pagination for list endpoints (1-based pages)."""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil
from typing import Sequence


@dataclass
class Page:
    items: list
    page: int
    per_page: int
    total: int

    @property
    def pages(self) -> int:
        return max(1, ceil(self.total / self.per_page))

    @property
    def has_next(self) -> bool:
        return self.page < self.pages


def paginate(items: Sequence, page: int = 1, per_page: int = 20) -> Page:
    """Return the requested 1-based ``page`` of ``items``."""
    if page < 1:
        raise ValueError("page must be >= 1")
    if per_page < 1:
        raise ValueError("per_page must be >= 1")
    start = page * per_page
    end = start + per_page
    return Page(items=list(items[start:end]), page=page, per_page=per_page, total=len(items))
