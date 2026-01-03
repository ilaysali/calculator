from Exceptions import TokenNotDefineException, InvalidInputException


def is_number(token: str) -> bool:
    """
    Checks if the string token can be converted to a float.

    Args:
        token (str): The string to check.

    Returns:
        bool: True if the token is a valid number.

    raise InvalidInputException: If the token is not defined in calculator.
    """

    # Handle empty strings to prevent IndexError
    if not token:
        return False

    if not isinstance(token, str):
        return False

    # This logic forces "-5" to be read as Operator(-) then Number(5)
    if token[0] in ('+', '-'):
        return False

    if token.count('.') > 1:
        raise InvalidInputException(f"Invalid expression in is_number: {token} character is not defined in calculator")

    try:
        float(token)
        return True
    except ValueError:
        return False

""" Mapping operators to their priority, Giving them unique ID. """
OPERATOR_CONFIG = {
    "(": (0, 12, "LParentheses"),
    ")": (0, 13, "RParentheses"),
    "+": (1, 1, "Operator"),
    "-": (1, 2, "Operator"),
    "*": (2, 3, "Operator"),
    "/": (2, 4, "Operator"),
    "^": (3, 5, "Operator"),
    "%": (4, 6, "Operator"),
    "$": (5, 7, "Operator"),
    "&": (5, 8, "Operator"),
    "@": (5, 9, "Operator"),
    "M": (7, 14, "left", "Unary"),
    "~": (6, 11, "left", "Unary"),
    "!": (6, 10, "right", "Unary"),
    "#": (6, 15, "right", "Unary"),
}

# Automatically generate the reverse map with only (unique ID:operator)
ID_TO_OPERATORS = {value[1]: key for key, value in OPERATOR_CONFIG.items()}

# A tuple containing ALL operators that are functioning by right to left logic
RIGHT_ANNOTATION = ("^",)

def get_operator_config(operator: str) -> tuple:
    """
    Retrieves the full configuration tuple (Priority, ID, Type) for a given operator.

    Args:
        operator (str): The operator symbol.

    Returns:
        tuple: A tuple containing (Priority, ID, Type).

    Raises:
        TokenNotDefineException: If the operator is not defined.
    """
    try:
        return OPERATOR_CONFIG[operator]
    except KeyError:
        raise TokenNotDefineException(f"Invalid expression in get_operator_config: '{operator}' is not defined in calculator")

def _get_id(operator: str) -> int:
    """
    Gets the unique id of a given operator from the OPERATOR_CONFIG map.

    Args:
        operator (str): The operator symbol.

    Return:
        int: The unique id value.

    Raises:
        TokenNotDefineException: If the operator is not defined.
    """

    try:
        return OPERATOR_CONFIG[operator][1]
    except KeyError:
        raise TokenNotDefineException(f"Invalid expression in get_id: {operator} character is not defined in calculator")

def get_operator(operator_id: int) -> str:
    """
    Gets the operator from the ID_TO_OPERATORS map.

    Args:
        operator_id (int): The operator id.

    Return:
        str: The operator as a string.

    Raises:
        TokenNotDefineException: If the operator is not defined in the ID_TO_OPERATORS map.
    """

    try:
        return ID_TO_OPERATORS[operator_id]
    except KeyError:
        raise TokenNotDefineException(f"Invalid expression in get_operator: {operator_id} character is not defined in calculator")

def get_right_annotation() -> tuple:
    """ returns a tuple containing all operators that function from right to left. (ex: ^)"""
    return RIGHT_ANNOTATION

def is_operator(operator: str) -> bool:
    """ checks if string is an operator, '(' , ')' is not included as operators """
    try:
        if operator == "(" or operator == ")":
            return False
        _get_id(operator)
        return True
    except TokenNotDefineException:
        return False