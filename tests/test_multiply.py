import pytest
from src.python_calculator.utils.multiply import multiply


@pytest.mark.parametrize(
    "x, y, result",
    [
        (2, 3, 6),
        (0, 0, 0),
        (1, 1, 1),
        (10, 5, 50),
        (-3, -7, 21),
        (2.5, 2.6, 6.5),
        (1000000, 2000000, 2000000000000),
    ],
)
def test_multiply(x, y, result):
    assert multiply(x, y) == result
