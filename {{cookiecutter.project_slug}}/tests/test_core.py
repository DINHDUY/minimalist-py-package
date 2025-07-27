"""Tests for the core module."""

import pytest

from {{ cookiecutter.package_name }}.core import Calculator, greet


class TestGreet:
    """Test cases for the greet function."""

    def test_greet_basic(self):
        """Test basic greeting functionality."""
        result = greet("Alice")
        assert result == "Hello, Alice!"

    def test_greet_enthusiastic(self):
        """Test enthusiastic greeting."""
        result = greet("Bob", enthusiastic=True)
        assert result == "Hello, Bob!!!"

    def test_greet_empty_name(self):
        """Test greeting with empty name."""
        result = greet("")
        assert result == "Hello, !"

    def test_greet_enthusiastic_false(self):
        """Test explicit non-enthusiastic greeting."""
        result = greet("Charlie", enthusiastic=False)
        assert result == "Hello, Charlie!"


class TestCalculator:
    """Test cases for the Calculator class."""

    def test_calculator_init(self):
        """Test calculator initialization."""
        calc = Calculator()
        assert calc.history == []

    def test_add(self):
        """Test addition operation."""
        calc = Calculator()
        result = calc.add(2, 3)
        assert result == 5.0
        assert len(calc.history) == 1
        assert calc.history[0] == ("add", 2.0, 3.0, 5.0)

    def test_add_floats(self):
        """Test addition with float numbers."""
        calc = Calculator()
        result = calc.add(1.5, 2.7)
        assert result == pytest.approx(4.2)

    def test_subtract(self):
        """Test subtraction operation."""
        calc = Calculator()
        result = calc.subtract(10, 3)
        assert result == 7.0
        assert len(calc.history) == 1
        assert calc.history[0] == ("subtract", 10.0, 3.0, 7.0)

    def test_multiply(self):
        """Test multiplication operation."""
        calc = Calculator()
        result = calc.multiply(4, 5)
        assert result == 20.0
        assert len(calc.history) == 1
        assert calc.history[0] == ("multiply", 4.0, 5.0, 20.0)

    def test_divide(self):
        """Test division operation."""
        calc = Calculator()
        result = calc.divide(10, 2)
        assert result == 5.0
        assert len(calc.history) == 1
        assert calc.history[0] == ("divide", 10.0, 2.0, 5.0)

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        calc = Calculator()
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)

    def test_multiple_operations(self):
        """Test multiple operations and history tracking."""
        calc = Calculator()
        calc.add(1, 2)
        calc.subtract(5, 3)
        calc.multiply(4, 2)

        history = calc.get_history()
        assert len(history) == 3
        assert history[0] == ("add", 1.0, 2.0, 3.0)
        assert history[1] == ("subtract", 5.0, 3.0, 2.0)
        assert history[2] == ("multiply", 4.0, 2.0, 8.0)

    def test_get_history_returns_copy(self):
        """Test that get_history returns a copy, not reference."""
        calc = Calculator()
        calc.add(1, 1)

        history1 = calc.get_history()
        history2 = calc.get_history()

        # Modify one copy
        history1.append(("test", 0.0, 0.0, 0.0))

        # Original and second copy should be unaffected
        assert len(calc.history) == 1
        assert len(history2) == 1

    def test_clear_history(self):
        """Test clearing calculation history."""
        calc = Calculator()
        calc.add(1, 2)
        calc.multiply(3, 4)
        assert len(calc.history) == 2

        calc.clear_history()
        assert calc.history == []
        assert calc.get_history() == []

    def test_operations_with_mixed_types(self):
        """Test operations with mixed int and float types."""
        calc = Calculator()

        # int + float
        result1 = calc.add(5, 2.5)
        assert result1 == 7.5

        # float - int
        result2 = calc.subtract(10.0, 3)
        assert result2 == 7.0

        # Verify history stores as floats
        history = calc.get_history()
        assert history[0] == ("add", 5.0, 2.5, 7.5)
        assert history[1] == ("subtract", 10.0, 3.0, 7.0)
