from utility import get_operator
from Exceptions import TokenNotDefineException
import math


def solve_operator(token: tuple, operand_b: tuple, operand_a: tuple) -> float:
    """
    Manages the evaluation process for binary operators.
    (operand_b is popped first from list, so it is the first operand).

    Args:
        token (tuple): The operator token.
        operand_b (tuple): The second number (right side).
        operand_a (tuple): The first number (left side).

    Returns:
        float: The result of (operand_a OP operand_b).

    Raises:
        TokenNotDefineException: If the operator is unknown.
    """

    val_a = float(operand_a[0])
    val_b = float(operand_b[0])

    match get_operator(token[1]):
        case "+":
            return _solve_plus(val_a, val_b)
        case "-":
            return _solve_minus(val_a, val_b)
        case "*":
            return _solve_multiply(val_a, val_b)
        case "/":
            return _solve_divide(val_a, val_b)
        case "^":
            return _solve_pow(val_a, val_b)
        case "%":
            return _solve_modulo(val_a, val_b)
        case "$":
            return _solve_max(val_a, val_b)
        case "&":
            return _solve_min(val_a, val_b)
        case "@":
            return _solve_avg(val_a, val_b)
        case _:
            raise TokenNotDefineException("in solve_operator: did you forgot to add to here the new operator?")

def _solve_plus(val_a: float, val_b: float) -> float:
    return _check_too_big(val_a + val_b)

def _solve_minus(val_a: float, val_b: float) -> float:
    return _check_too_big(val_a - val_b)

def _solve_multiply(val_a: float, val_b: float) -> float:
    return _check_too_big(val_a * val_b)

def _solve_divide(val_a: float, val_b: float) -> float:
    return _check_too_big(val_a / val_b)

def _solve_pow(val_a: float, val_b: float) -> float:
    return math.pow(val_a, val_b)

def _solve_modulo(val_a: float, val_b: float) -> float:
    return val_a % val_b

def _solve_max(val_a: float, val_b: float) -> float:
    return val_a if val_a > val_b else val_b

def _solve_min(val_a: float, val_b: float) -> float:
    return val_a if val_a < val_b else val_b

def _solve_avg(val_a: float, val_b: float) -> float:
    return _check_too_big((val_a + val_b) / 2)

def _check_too_big(result: float) -> float:
    if result == float('inf') or result == float('-inf'):
        raise OverflowError("Result too large")
    return result