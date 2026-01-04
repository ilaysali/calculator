from Exceptions import MismatchedParenthesesException


def parser(tokenize_expression: list) -> list:
    """
    Manage the postfix process, makes tokenized list as postfix.

    Args:
        tokenize_expression (list): expression as a list of tuples.

    Returns:
        list: expression as postfix.

    Raises:
        MismatchedParenthesesException: If not the same number of left and right parentheses.
    """

    output = []
    operators = []

    for token in tokenize_expression:
        if token[-1] == "Number":
            output.append(token)

        elif token[-1] == "Operator" or token[-1] == "Unary":
            while operators and operators[-1][-1] != "LParentheses" and operators[-1][0] >= token[0]:
                output.append(operators.pop())
            operators.append(token)

        elif token[-1] == "LParentheses":
            operators.append(token)

        elif token[-1] == "RParentheses":
            while operators and operators[-1][-1] != "LParentheses":
                output.append(operators.pop())
            if not operators:
                raise MismatchedParenthesesException("in parser: Invalid parentheses, there are more ')' then there are '('")
            operators.pop()

    while operators:
        if operators[-1][-1] == "LParentheses":
            raise MismatchedParenthesesException("in parser: Invalid parentheses, there are more '(' then there are ')'")
        output.append(operators.pop())

    return output

