from utility import *
from Exceptions import TokenNotDefineException


def tokenize(expression: str ) -> list:
    """
        Iterates through the mathematical expression Each element in the expression
        becomes a tuple in the returned list containing (Priority, ID, Type).

        Args:
            expression (str): The mathematical expression.

        Returns:
            list: A list of tuples containing (Priority, ID, Type).

        Raises:
            TokenNotDefineException: If the expression contains a character that is not defined.
    """

    lst = []
    number = ""
    operators = ['+', '-', '*', '/', '@', '^', '%', '$', '&']

    for token in expression:
        if is_number(token) or token == '.':
            number += token

        else:
            if number != "":
                lst.append((number,"Number"))
                number = ""

            try:
                lst.append(get_operator_config(token))

            except TokenNotDefineException:
                raise TokenNotDefineException(f"Invalid expression: {token} character is not defined in calculator")

    if number != "":
        lst.append((number, "Number"))

    return lst