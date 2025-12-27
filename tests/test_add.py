import pytest
from src.python_calculator.utils.add import add


@pytest.mark.parametrize(
    "x, y, result",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
        (10, 5, 15),
        (-3, -7, -10),
        (2.5, 2.6, 5.1),
        (1000000, 2000000, 3000000),
    ],
)
def test_add(x, y, result):
    assert add(x, y) == result
