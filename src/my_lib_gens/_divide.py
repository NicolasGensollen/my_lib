"""Division module."""

__all__ = ["div"]


def div(a: float, b: float) -> float:
    """Perform division between provided arguments."""
    from ._errors import MyLibZeroDivisionError

    if b == 0:
        raise MyLibZeroDivisionError("Cannot divide by zero")
    return a / b
