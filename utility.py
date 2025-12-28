def is_number(token: str) -> bool:
    """
    Checks if the string token can be converted to a float.

    Args:
        token (str): The string to check.

    Returns:
        bool: True if the token is a valid number.
    """

    try:
        # casting str to float that begins with + or - returns true instead of false. (e.g. +5 => needs to return false)
        if token[0] == '+' or token[0] == '-':
            return False
        float(token)
        return True
    except ValueError:
        return False