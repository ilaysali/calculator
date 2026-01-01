from evaluate_operator import solve_operator
from evaluate_unary import solve_unary
from Exceptions import IntegerExpectedException


def evaluate_postfix(expression_after_postfix: list) -> float:
    """
    Manage the final evaluation process, decides what function need to handle each token.

    Args:
        expression_after_postfix (list): The expression as a postfix list of tuple.

    Returns:
        float: The result for calculating the expression.

    Raises:
        IntegerExpectedException: If expression is empty.
    """

    numbers_to_calculate = []

    for token in expression_after_postfix:
        if token[-1] == "Number":
            numbers_to_calculate.append(token)

        elif token[-1] == "Unary":
            numbers_to_calculate.append((solve_unary(token, numbers_to_calculate.pop()), "Number"))

        else:
            numbers_to_calculate.append((solve_operator(token,numbers_to_calculate.pop(),numbers_to_calculate.pop()), "Number"))

    if numbers_to_calculate:
        return  float(numbers_to_calculate.pop()[0])
    raise IntegerExpectedException("Empty input")