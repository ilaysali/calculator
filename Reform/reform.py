from Exceptions import NumbersInARowException, TokenNotDefineException, InvalidInputException
from utility import is_number, is_operator


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
                raise NumbersInARowException("in remove_whitespace: Invalid syntax: Two numbers in a row")
            is_previous_number = True

        else:
            is_previous_number = False
    expression = expression.replace(' ', '')
    return expression.replace('\t', '')

def reform_sequence_of_priority1(expression: str) -> str:
    """
    Replaces sequence of -,+:
        if at the start of the sequence there is operator:
            then sequence becomes part of number(max priority)
        else:
            reduce sequence of -,+ via mathematical logic.

    Args:
        expression (str): The mathematical expression.

    Returns:
        str: The expression with replaced sequence of -,+.

    Raises:
        TokenNotDefineException if there is character 'M' in expression.
        InvalidInputException sequence of '-' and '+' must come before a number.
    """

    # This function can add valid 'M' characters so check in advanced for invalid 'M' character
    if 'M' in expression:
        raise TokenNotDefineException("in reform_sequence_of_priority1: Invalid expression: 'M' character is not defined in calculator")

    reformed_expression = []
    minus_count = 0
    sequence = False
    operator_at_start_of_sequence = False

    if expression[0] == '-':
        expression = "0" + expression

    for token in expression:
        if (token == '-' or token == '+') and operator_at_start_of_sequence:
            if token == '-':
                minus_count += 1
            sequence = True

        else:
            operator_at_start_of_sequence = False
            if sequence:
                if not is_number(token):
                    raise InvalidInputException("Invalid input in reform_sequence_of_priority1: sequence ('-','+') must come before a number")

                if minus_count % 2 != 0:
                    reformed_expression.append("M")

                sequence = False
                minus_count = 0

            if is_operator(token):
                operator_at_start_of_sequence = True

            reformed_expression.append(token)

    return ''.join(reformed_expression)

