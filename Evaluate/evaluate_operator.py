from utility import get_operator
from Exceptions import TokenNotDefineException
import math


def solve_operator (token: tuple, number2: tuple, number1: tuple) -> float:
    """
    Manage the evaluation process for operators, decides what function need to handle each token.

    Args:
        token (tuple): operator.
        number1 (tuple): number
        number2 (tuple): number

    Returns:
        float: The result for calculating number as token operator.

    Raises:
        TokenNotDefineException: If token not defined as operator.
    """
    match get_operator(token[1]):
        case "+":
            return solve_plus(number1,number2)
        case "-":
            return solve_minus(number1, number2)
        case "*":
            return solve_multiply(number1, number2)
        case "/":
            return solve_divide(number1, number2)
        case "^":
            return solve_pow(number1, number2)
        case "%":
            return solve_modulo(number1, number2)
        case "$":
            return solve_max(number1, number2)
        case "&":
            return solve_min(number1, number2)
        case "@":
            return solve_avg(number1, number2)
        case _:
            raise TokenNotDefineException("did you forgot to add to here the new operator?")

def solve_plus (number1: tuple, number2: tuple) -> float:
    return  float(number1[0]) + float(number2[0])

def solve_minus (number1: tuple, number2: tuple) -> float:
    return  float(number1[0]) - float(number2[0])

def solve_multiply (number1: tuple, number2: tuple) -> float:
    return  float(number1[0]) * float(number2[0])

def solve_divide (number1: tuple, number2: tuple) -> float:
    return  float(number1[0]) / float(number2[0])

def solve_pow (number1: tuple, number2: tuple) -> float:
    return  math.pow(float(number1[0]), float(number2[0]))

def solve_modulo (number1: tuple, number2: tuple) -> float:
    return  float(number1[0]) % float(number2[0])

def solve_max (number1: tuple, number2: tuple) -> float:
    num1 = float(number1[0])
    num2 = float(number2[0])
    return num1 if num1 > num2 else num2

def solve_min (number1: tuple, number2: tuple) -> float:
    num1 = float(number1[0])
    num2 = float(number2[0])
    return num1 if num1 < num2 else num2

def solve_avg (number1: tuple, number2: tuple) -> float:
    return  (float(number1[0]) + float(number2[0])) / 2