"""
Author: dizhong zhu
Date: 23/02/2022
"""

from utils.simple_math import (
    add,
    multiply,
    sub,
    div
)


def test_add():
    assert add(4, 5) == 9


def test_multiply():
    assert multiply(4, 5) == 20


def test_sub():
    assert sub(4, 5) == -1


def test_div():
    assert div(4, 5) == 4/5
