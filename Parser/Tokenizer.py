from utility import is_number,get_operator_config
from validation import validate_input


def tokenize(expression: str ) -> list:
    """
    Iterates through the mathematical expression Each element in the expression
    becomes a tuple in the returned list containing (Priority, ID, Type).

    Args:
        expression (str): The mathematical expression.

    Returns:
        list: A list of tuples containing  if operator -(Priority, ID, Type) if number -(value,Number)  .
    """

    lst = []
    number = ""

    for token in expression:
        if is_number(token) or token == '.':
            number += token

        else:
            if number != "":
                whole_number = (number,"Number")
                validate_input(whole_number, lst[-1] if lst else None)
                lst.append(whole_number)
                number = ""

            token_tuple = get_operator_config(token)
            validate_input(token_tuple, lst[-1] if lst else None)
            lst.append(token_tuple)

    if number != "":
        whole_number = (number, "Number")
        validate_input(whole_number, lst[-1] if lst else None)
        lst.append((number, "Number"))
    return lst