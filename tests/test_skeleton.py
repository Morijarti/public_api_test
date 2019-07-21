# -*- coding: utf-8 -*-

import pytest
from opt_out.public_api.skeleton import fib

__author__ = "Bojan Miletic"
__copyright__ = "Bojan Miletic"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
