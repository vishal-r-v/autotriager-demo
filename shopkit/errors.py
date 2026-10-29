"""Exception types raised by shopkit."""


class ShopError(Exception):
    """Base class for shopkit errors."""


class OutOfStockError(ShopError):
    """Not enough units on hand for a reservation."""


class UnknownSKUError(ShopError, LookupError):
    """The SKU has never been registered or stocked."""


class InvalidDateError(ShopError, ValueError):
    """An order date string could not be parsed."""
