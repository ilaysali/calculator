from Exceptions import NumbersInARowException


def is_number(token: str) -> bool:
    """
    Checks if the string token can be converted to a float.

    Args:
        token (str): The string to check.

    Returns:
        bool: True if the token is a valid number.
    """

    try:
        if (token[0] == '+' or token[0] == '-'):
            return False
        float(token)
        return True
    except ValueError:
        return False


def remove_whitespace(expression: str) -> str:
    """
    Removes whitespace from an expression after validating that it does not
    contain two consecutive numbers.

    Args:
        expression (str): The mathematical expression to validate.

    Returns:
        str: The expression with all whitespace removed.

    Raises:
        NumbersInARowException: If two numbers appear sequentially without an operator.
    """

    divided_by_whitespace = expression.split()
    is_previous_number = False
    for token in divided_by_whitespace:
        if is_number(token):
            if is_previous_number:
                raise NumbersInARowException("Invalid syntax: Two numbers in a row")
            is_previous_number = True
        else:
            is_previous_number = False

    return expression.replace(' ', '')





