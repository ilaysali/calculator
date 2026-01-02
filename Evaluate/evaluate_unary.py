from Exceptions import *
from utility import get_operator,is_number


def solve_unary (token: tuple, number: tuple) -> float:
    """
    Manage the evaluation process for unary operators, decides what function need to handle each token.

    Args:
        token (tuple): unary operator.
        number (tuple): number

    Returns:
        float: The result for calculating number per unary operator.

    Raises:
        TokenNotDefineException: If token not defined as unary.
    """
    if number[-1] != "Number":
        raise InvalidOperandException(f"can only be applied to numbers, not '{number[0]}'")

    if get_operator(token[2]) == "left":
        return left_unary(token, number)
    return right_unary(token, number)

def left_unary (token: tuple, number: tuple) -> float:
    if get_operator(token[1]) == "M":
        return solve_M(number)

    if get_operator(token[1]) == "~":
        return solve_tilda(number)
    raise TokenNotDefineException("did you forgot to add to here the new left unary?")

def right_unary (token: tuple, number: tuple) -> float:
    if not is_number(number[0]):
        raise IntegerExpectedException("can only be applied to positive numbers")

    if get_operator(token[1]) == "!":
        return factorial(number)

    if get_operator(token[1]) == "#":
        return sum_digits(number)
    raise TokenNotDefineException("did you forgot to add to here the new right unary?")

def solve_M (number: tuple) -> float:
    return  float(number[0]) * -1

def solve_tilda (number: tuple) -> float:
    return  float(number[0]) * -1

def factorial (number: tuple) -> float:
    f_number = float(number[0])
    if  f_number % 1 != 0:
        raise IntegerExpectedException(f"Factorial requires an integer cant get handle float")
    return solve_factorial(int(f_number))

def solve_factorial(number: int) -> int:
    factorial_number = 1
    for i in range(2, number + 1):
        factorial_number *= i
    return factorial_number

def sum_digits (number: tuple) -> int:
    sum_of_digits = 0
    for digit in number[0]:
        if digit != ".":
            sum_of_digits += int(digit)
    return sum_of_digits