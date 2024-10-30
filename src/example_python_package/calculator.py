"""Functions for basic arithmetic operations."""


def add(x: int | float, y: int | float) -> int | float:
    """Add two numbers together.

    Args:
        x (int | float): The first number.
        y (int | float): The second number.

    Returns:
        int | float: The sum of the two numbers.
    """
    return x + y


def subtract(x: int | float, y: int | float) -> int | float:
    """Subtract one number from another.

    Args:
        x (int | float): The number to subtract from.
        y (int | float): The number to subtract.

    Returns:
        int | float: The result of the subtraction.
    """
    return x - y


def multiply(x: int | float, y: int | float) -> int | float:
    """Multiply two numbers together.

    Args:
        x (int | float): The first number.
        y (int | float): The second number.

    Returns:
        int | float: The product of the two numbers.
    """
    return x * y


def divide(x: int | float, y: int | float) -> int | float:
    """Divide one number by another.

    Args:
        x (int | float): The dividend.
        y (int | float): The divisor.

    Returns:
        int | float: The result of the division.
    """
    return x / y
