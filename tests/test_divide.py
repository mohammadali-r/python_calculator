import pytest
from src.python_calculator.utils.divide import divide


@pytest.mark.parametrize(
    "x, y, result",
    [
        (10, 2, 5),
        (0, 1, 0),
        (1, 1, 1),
        (15, 3, 5),
        (-6, -2, 3),
        (2.5, 2.5, 1.0),
        (2000000, 1000000, 2),
        (10, 0, "Division by zero error"),  # Test case for division by zero
    ],
)
def test_divide(x, y, result):
    assert divide(x, y) == result
