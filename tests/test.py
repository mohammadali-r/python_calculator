# import pytest

from operations.add import add
from operations.subtract import subtract
from operations.multiply import multiply
from operations.divide import divide

def test_add_1():
    assert add(2, 3) == 5