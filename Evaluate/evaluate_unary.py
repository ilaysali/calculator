from Exceptions import TokenNotDefineException, InvalidOperandException, IntegerExpectedException
from utility import get_operator, is_number


MAX_FACTORIAL_INPUT = 160

def solve_unary(token: tuple, operand: tuple) -> float:
    """
    Manages the evaluation process for unary operators.
    Decides which function should handle the token based on its associativity (left/right).

    Args:
        token (tuple): The unary operator token (Priority, ID, Type, Direction).
        operand (tuple): The number token to apply the operator on.

    Returns:
        float: The calculation result.

    Raises:
        InvalidOperandException: If the operand is not a number.
     """
    if operand[-1] != "Number":
        raise InvalidOperandException(f"in solve_unary: can only be applied to numbers, not '{operand[0]}'")

    if token[2] == "left":
        return _handle_left_unary(token, operand)
    return _handle_right_unary(token, operand)

def _handle_left_unary(token: tuple, operand: tuple) -> float:
    """ Handles left-associative unary operators. """

    operator_symbol = get_operator(token[1])
    if operator_symbol == "M":
        return _solve_negation(operand)

    if operator_symbol == "~":
        return _solve_tilda(operand)

    raise TokenNotDefineException("in left_unary: did you forgot to add to here the new left unary?")

def _handle_right_unary(token: tuple, operand: tuple) -> float:
    """ Handles right-associative unary operators. """

    if not is_number(operand[0]):
        raise IntegerExpectedException("in right_unary: can only be applied to positive numbers")
    operator_symbol = get_operator(token[1])

    if operator_symbol == "!":
        return _calculate_factorial_wrapper(operand)

    if operator_symbol == "#":
        return _sum_digits(operand)
    raise TokenNotDefineException("in right_unary: did you forgot to add to here the new right unary?")

def _solve_negation(operand: tuple) -> float:
    return float(operand[0]) * -1

def _solve_tilda(operand: tuple) -> float:
    return float(operand[0]) * -1

def _calculate_factorial_wrapper(operand: tuple) -> float:
    value = float(operand[0])
    if value % 1 != 0:
        raise IntegerExpectedException(f"in factorial: Factorial requires an integer cant get handle float")
    if value > MAX_FACTORIAL_INPUT:
        raise OverflowError("Result too large can only calculate up to 160!")
    return _solve_factorial(int(value))

def _solve_factorial(operand: int) -> int:
    factorial_number = 1
    for i in range(2, operand + 1):
        factorial_number *= i
    return factorial_number

def _sum_digits(operand: tuple) -> int:
    sum_of_digits = 0
    for digit in operand[0]:
        if digit != ".":
            sum_of_digits += int(digit)
    return sum_of_digits