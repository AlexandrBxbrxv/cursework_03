from src.functions import *


def test_censor():
    assert (censor('Счет 38976430693692818358', 'Visa Classic 6831982476737658')
            == ('3897 64** **** **** 8358', '**7658'))
    assert (censor('Maestro 3928549031574026', 'Счет 84163357546688983493')
            == ('3928 54** **** 4026', '**3493'))


def test_censor__no_name():
    assert (censor(None, 'Счет 96231448929365202391')
            == ('Неизвестный', '**2391'))


def test_get_data():
    assert get_data()[0] == {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}
