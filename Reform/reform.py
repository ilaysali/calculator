from Exceptions import NumbersInARowException
from utility import is_number


def remove_whitespace(expression: str) -> str:
    """
    Removes whitespace from an expression after validating that it does not
    contain two consecutive numbers.

    Args:
        expression (str): The mathematical expression.

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

def reform_sequence_of_priority1 (expression: str) -> str:
    """
    Replaces sequence of -,+:
        if at the start of the sequence there is '~':
            then sequence priority becomes '~' priority (ignores '+' operator)
        else:
            reduce sequence of -,+ via mathematical logic.

    Args:
        expression (str): The mathematical expression.

    Returns:
        str: The expression with replaced sequence of -,+.
    """

    reformed_expression = []
    minus_count = 0
    sequence = False
    tilda_at_start_of_sequence = False

    for token in expression:
        if token == '-' or token == '+':
            if token == '-':
                if tilda_at_start_of_sequence:
                    reformed_expression.append("~")

                else:
                    minus_count += 1
                    sequence = True
            elif not tilda_at_start_of_sequence:
                sequence = True

        else:
            tilda_at_start_of_sequence = False
            if sequence:
                if minus_count % 2 == 0:
                    reformed_expression.append("+")

                else:
                    reformed_expression.append("-")

                sequence = False
                minus_count = 0

            elif token == '~':
                tilda_at_start_of_sequence = True

            reformed_expression.append(token)

    return ''.join(reformed_expression)

