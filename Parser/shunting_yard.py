from utility import get_operator,get_right_annotation
from Exceptions import MismatchedParenthesesException


#NOTE: does not handle "!" or "~" need to handle it beforehand
def parser(tokenize_expression: list) -> str:
    output = ""
    operators = []

    for token in tokenize_expression:
        if token[-1] == "Number":
            output += token[0] + ","

        else:
            if token[-1] == "Operator":
                while (operators and operators[-1][-1] != "LParentheses" and
                    (operators[-1][0] > token[0] or (operators[-1][0] == token[0] and
                            get_operator(token[1]) not in get_right_annotation()))):
                    output += get_operator(operators.pop()[1]) + ","
                operators.append(token)

            elif token[-1] == "LParentheses" :
                operators.append(token)

            elif token[-1] == "RParentheses":
                while operators and operators[-1][-1] != "LParentheses":
                    output += get_operator(operators.pop()[1]) + ","
                if not operators:
                    raise MismatchedParenthesesException("Invalid parentheses, there are more ')' then there are '('")
                operators.pop()

    if operators:
        if operators[-1][-1] == "LParentheses":
            raise MismatchedParenthesesException("Invalid parentheses, there are more '(' then there are ')'")
        output += get_operator(operators.pop()[1]) + ","

    return output