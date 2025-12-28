from utility import is_number
from Exceptions import TokenNotDefineException


def tokenize(expression: str ) -> list:
    """
        Iterates through the mathematical expression Each element in the expression
        becomes a tuple in the returned list containing (token value, its type).

        Args:
            expression (str): The mathematical expression.

        Returns:
            list: A list of tuples where each tuple is formatted as (value, type).

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

            if token in operators:
                lst.append((token, "Operator"))

            elif token == '!':
                lst.append((token, "ROperator"))

            elif token == '~':
                lst.append((token, "LOperator"))

            elif token == '(':
                lst.append((token, "RParentheses "))

            elif token == ')':
                lst.append((token, "LParentheses "))

            else:
                raise TokenNotDefineException(f"Invalid expression: {token} character is not define in calculator")

    if number != "":
        lst.append((number, "Number"))

    return lst