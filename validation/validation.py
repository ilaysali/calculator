from Exceptions import InvalidInputException
from utility import is_number, get_operator

START_TOKENS = ["Number", "(", "M", "~"]  # Tokens that start an operand
END_TOKENS = ["Number", ")", "!", "#"]    # Tokens that end an operand

def validate_input(current: tuple, previous: tuple = None) -> None:
    """
    Validates the placement of the current token based on the previous token.

    Args:
        current (tuple): The current token to validate .
        previous (tuple, optional): The previous token processed. Defaults to None.

    Raises:
        InvalidInputException: If the token placement violates input rules.
    """

    current_token = current[-1] if is_number(current[0]) else get_operator(current[1])
    previous_token = (previous[-1] if is_number(previous[0]) else get_operator(previous[1])) if previous else None

    if current_token in START_TOKENS:
        _validate_operand_context(previous_token, current_token)

    else:
        _validate_operator_context(previous_token, current_token)

def _validate_operand_context(previous_token: str, current_token: str) -> None:
    """
    Validates tokens that act as operands or start of expressions
    (Numbers, Left Parentheses, Left Unary Operators).

    Args:
        previous_token (str): The previous token the current one.
        current_token (str): The current token being validated.

    Raises:
        InvalidInputException: If input rules are violated.
    """

    if previous_token and previous_token in END_TOKENS:
        raise InvalidInputException(f"Invalid input in validate_operand_context: {current_token} cant come after {previous_token}")
    if current_token != '(' and current_token == previous_token:
        raise InvalidInputException(f"Invalid input in validate_operand_context: {current_token} cant come after itself")

def _validate_operator_context(previous_token: str, current_token: str) -> None:
    """
    Validates binary operators, right parentheses, and right unary operators.

    Args:
        previous_token (str): The previous token the current one.
        current_token (str): The current token being validated.

    Raises:
         InvalidInputException: If input rules are violated.
    """

    if not previous_token:
        raise InvalidInputException(f"Invalid input in validate_operator_context:{current_token} cant be at the start of input")
    if previous_token not in END_TOKENS:
        raise InvalidInputException(f"Invalid input in validate_operator_context: {current_token} cant come after {previous_token}")