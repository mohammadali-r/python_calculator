import pytest
from src.python_calculator.utils.subtract import subtract


@pytest.mark.parametrize(
    "x, y, result",
    [
        (5, 2, 3),
        (0, 0, 0),
        (1, 1, 0),
        (10, 5, 5),
        (-3, -7, 4),
        (2.5, 1.5, 1.0),
        (2000000, 1000000, 1000000),
    ],
)
def test_subtract(x, y, result):
    assert subtract(x, y) == result
