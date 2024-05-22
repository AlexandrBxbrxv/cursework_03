from ..src.functions import censor
import unittest


def test_censor():
    assert censor('1111 1111 1111 1111', '123456') == '1111 11** **** 1111', '****56'


def divide(a, b):
    return a / b


def test_divide():
    assert divide(1, 2) == 0.5
    assert divide(2, 2) == 1
    assert divide(4.4, 2) == 2.2
    assert divide(10_000, 2) == 5000


class TestDivide(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(4, 2), 2)

