"""
Author: dizhong zhu
Date: 23/02/2022
"""

from utils.simple_math import (
    add,
    multiply
)


def test_add():
    assert add(4, 5) == 9


def test_multiply():
    assert multiply(4, 5) == 20
