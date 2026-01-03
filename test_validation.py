import pytest
from main import calculate

valid_test_cases = [
    ("(3456 + 7890)*(234 - 56) / 12 - 987 + 6543", 173855),
    ("((1200 - 375) / 5 + 48)*(72 - 19) - 999", 10290),
    ("(3 ^ 7 + 5 ^ 6 - 7 ^ 4) / ((81)^0.5 + 2 ^ 5)", 375.8780487804878),
    ("(9 ^ (3 / 2) + (16)^0.5) ^ 2 - 4 ^ 5", -63.0),
    ("((5 / 8 + 7 / 12) / (3 / 4 - 1 / 6))*(9 / 5)", 3.728571428571429),
    ("((2 / 3 + 5 / 7) / (4 / 9 - 1 / 3))", 12.428571428571429),
    ("((8 + 3*(5 - 2)) ^ 2 - (6 + 4) ^ 2) / 7", 27),
    ("((15 - (3 ^ 2 + 4))*(18 / (2 + 1))) / 5", 2.4),
    ("((625 - 144)^0.5 + 3 ^ 4) / ((7 - 2) ^ 2)*(9 + 6 / 3)", 45.289953367762976),
    ("(2 ^ 5 + 3 ^ 4) * (81 / 9 - (16)^0.5) - 100", 465),
]

def get_invalid_inputs():
    """
    Generates a list of invalid inputs.
    """
    invalid_inputs = []

    invalid_inputs.extend(["", "   ", "\t", "  \t  ", "\n"])

    invalid_inputs.extend(["abc", "12a3", "2 + x", "hello world", "2 # 3", "2 ? 3", "2 ; 3"])

    invalid_inputs.extend(["[1+2]", "{3*4}", "2 * [3 + 4]", "(1 + 2}"])

    invalid_inputs.extend(["(1+2", "1+2)", "((5*2)", "()", ")3+2("])

    binary_ops = ['+', '-', '*', '/', '^', '%', '$', '&', '@', '#','!','~']
    for op1 in binary_ops:
        for op2 in binary_ops:
            invalid_inputs.append(f"5{op1}{op2}5")

    for op in ['*', '/', '^', '%', '$', '&', '@']:
        invalid_inputs.append(f"{op}5")
        invalid_inputs.append(f"5{op}")
    invalid_inputs.append("5+")
    invalid_inputs.append("5-")

    invalid_inputs.append("3~")
    invalid_inputs.append("5~2")
    invalid_inputs.append("!5")

    invalid_inputs.extend(["1..5", ".", "5.2.1", ".+5"])

    return invalid_inputs

def test_tokenize_basic():
    pass

def test_tokenize_complex():
    assert calculate("") == 45.289953367762976

def test_tokenize_decimals():
    assert calculate("2#3") == 45.289953367762976

@pytest.mark.parametrize("expression, expected", valid_test_cases)
def test_calculator_valid_inputs(expression, expected):
    assert calculate(expression) == pytest.approx(expected, rel=1e-5)

@pytest.mark.parametrize("invalid_input", get_invalid_inputs())
def test_invalid_inputs_generated(invalid_input):
    result = calculate(invalid_input)
    assert result is None, f"Expected None for invalid input '{invalid_input}', but got {result}"

def test_calculator_valid_input(expression, expected):
    assert calculate("2#3") == 5, f"Expected None for invalid input '{expression}', but got {calculate(expression)}"



