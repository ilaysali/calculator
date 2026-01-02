import pytest
from main import calculate


valid_test_cases = [
    ("(3456 + 7890)*(234 - 56) / 12 - 987 + 6543",173855),
    ("((1200 - 375) / 5 + 48)*(72 - 19) - 999",10290),
    ("(3 ^ 7 + 5 ^ 6 - 7 ^ 4) / ((81)^0.5 + 2 ^ 5)",375.8780487804878),
    ("(9 ^ (3 / 2) + (16)^0.5) ^ 2 - 4 ^ 5",-63.0),
    ("((5 / 8 + 7 / 12) / (3 / 4 - 1 / 6))*(9 / 5)",3.728571428571429),
    ("((2 / 3 + 5 / 7) / (4 / 9 - 1 / 3))",12.428571428571429),
    ("((8 + 3*(5 - 2)) ^ 2 - (6 + 4) ^ 2) / 7",27),
    ("((15 - (3 ^ 2 + 4))*(18 / (2 + 1))) / 5",2.4),
    ("((625 - 144)^0.5 + 3 ^ 4) / ((7 - 2) ^ 2)*(9 + 6 / 3)",45.289953367762976),
    ("(2 ^ 5 + 3 ^ 4) * (81 / 9 - (16)^0.5) - 100",465),
]

def test_tokenize_basic():
    pass

def test_tokenize_complex():
    assert calculate("4~@3") == 45.289953367762976

def test_tokenize_decimals():
    assert calculate("((625 - 144)^0.5 + 3 ^ 4) / ((7 - 2) ^ 2)*(9 + 6 / 3)") == 45.289953367762976

@pytest.mark.parametrize("expression, expected", valid_test_cases)
def test_calculator_valid_inputs(expression, expected):
    assert calculate(expression) == expected


