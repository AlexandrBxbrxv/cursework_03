from ..src.functions import censor
# import unittest


def test_censor():
    assert (censor('Счет 38976430693692818358', 'Visa Classic 6831982476737658')
            == ('3897 64** **** **** 8358', '**7658'))
    assert (censor('Maestro 3928549031574026', 'Счет 84163357546688983493')
            == ('3928 54** **** 4026', '**3493'))


def test_censor_noname():
    assert (censor(None, 'Счет 96231448929365202391')
            == ('Неизвестный', '**2391'))


# def divide(a, b):
#     return a / b
#
#
# def test_divide():
#     assert divide(1, 2) == 0.5
#     assert divide(2, 2) == 1
#     assert divide(4.4, 2) == 2.2
#     assert divide(10_000, 2) == 5000


# class TestDivide(unittest.TestCase):
#     def test_divide(self):
#         self.assertEqual(divide(4, 2), 2)

