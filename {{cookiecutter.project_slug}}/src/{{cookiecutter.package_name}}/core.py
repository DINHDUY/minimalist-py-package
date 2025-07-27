"""Core functionality for the {{ cookiecutter.package_name }}.

This module contains the main classes and functions that demonstrate
the package structure and documentation standards.
"""

from typing import Union


def greet(name: str, enthusiastic: bool = False) -> str:
    """Generate a greeting message.

    Args:
        name: The name of the person to greet.
        enthusiastic: Whether to make the greeting enthusiastic with exclamation marks.

    Returns:
        A formatted greeting string.

    Examples:
        >>> greet("Alice")
        'Hello, Alice!'
        >>> greet("Bob", enthusiastic=True)
        'Hello, Bob!!!'
    """
    if enthusiastic:
        return f"Hello, {name}!!!"
    return f"Hello, {name}!"


class Calculator:
    """A simple calculator class demonstrating basic arithmetic operations.

    This class provides basic mathematical operations and maintains a history
    of calculations performed.

    Attributes:
        history: A list of tuples containing operation history in the format
            (operation, operand1, operand2, result).
    """

    def __init__(self) -> None:
        """Initialize the calculator with empty history."""
        self.history: list[tuple[str, float, float, float]] = []

    def add(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Add two numbers.

        Args:
            a: The first number.
            b: The second number.

        Returns:
            The sum of a and b.

        Examples:
            >>> calc = Calculator()
            >>> calc.add(2, 3)
            5.0
            >>> calc.add(1.5, 2.5)
            4.0
        """
        result = float(a + b)
        self.history.append(("add", float(a), float(b), result))
        return result

    def subtract(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Subtract the second number from the first.

        Args:
            a: The number to subtract from.
            b: The number to subtract.

        Returns:
            The difference of a and b.

        Examples:
            >>> calc = Calculator()
            >>> calc.subtract(5, 3)
            2.0
            >>> calc.subtract(10.5, 4.2)
            6.3
        """
        result = float(a - b)
        self.history.append(("subtract", float(a), float(b), result))
        return result

    def multiply(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Multiply two numbers.

        Args:
            a: The first number.
            b: The second number.

        Returns:
            The product of a and b.

        Examples:
            >>> calc = Calculator()
            >>> calc.multiply(4, 5)
            20.0
            >>> calc.multiply(2.5, 4)
            10.0
        """
        result = float(a * b)
        self.history.append(("multiply", float(a), float(b), result))
        return result

    def divide(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Divide the first number by the second.

        Args:
            a: The dividend.
            b: The divisor.

        Returns:
            The quotient of a and b.

        Raises:
            ValueError: If b is zero.

        Examples:
            >>> calc = Calculator()
            >>> calc.divide(10, 2)
            5.0
            >>> calc.divide(7, 2)
            3.5
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = float(a / b)
        self.history.append(("divide", float(a), float(b), result))
        return result

    def get_history(self) -> list[tuple[str, float, float, float]]:
        """Get the calculation history.

        Returns:
            A list of tuples containing the operation history.
            Each tuple contains (operation, operand1, operand2, result).

        Examples:
            >>> calc = Calculator()
            >>> calc.add(2, 3)
            5.0
            >>> calc.multiply(4, 5)
            20.0
            >>> calc.get_history()
            [('add', 2.0, 3.0, 5.0), ('multiply', 4.0, 5.0, 20.0)]
        """
        return self.history.copy()

    def clear_history(self) -> None:
        """Clear the calculation history.

        Examples:
            >>> calc = Calculator()
            >>> calc.add(1, 2)
            3.0
            >>> calc.clear_history()
            >>> calc.get_history()
            []
        """
        self.history.clear()
