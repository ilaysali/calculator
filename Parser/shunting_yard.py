from utility import get_operator,get_right_annotation
from Exceptions import MismatchedParenthesesException,InvalidOperandException,IntegerExpectedException

# NOTE does not handle ~ yet
def parser(tokenize_expression: list) -> list:
    output = []
    operators = []

    for token in tokenize_expression:
        if token[-1] == "Number":
            output.append(token)

        elif token[-1] == "Operator":
            while (operators and operators[-1][-1] != "LParentheses" and
                (operators[-1][0] > token[0] or (operators[-1][0] == token[0] and
                    get_operator(token[1]) not in get_right_annotation()))):
                output.append(operators.pop())
            operators.append(token)

        elif token[-1] == "LParentheses" :
            operators.append(token)

        elif token[-1] == "RParentheses":
            while operators and operators[-1][-1] != "LParentheses":
                output.append(operators.pop())
            if not operators:
                raise MismatchedParenthesesException("Invalid parentheses, there are more ')' then there are '('")
            operators.pop()

        elif token[-1] == "Unary" and get_operator(token[1]) == "!":
            output.append(factorial(output.pop()))

    while operators:
        if operators[-1][-1] == "LParentheses":
            raise MismatchedParenthesesException("Invalid parentheses, there are more '(' then there are ')'")
        output.append(operators.pop())

    return output

def factorial (number: tuple) -> tuple:
    if number[-1] != "Number":
        raise InvalidOperandException(f"Factorial (!) can only be applied to numbers, not '{number[0]}'")
    if number[0].find(".") != -1:
        raise IntegerExpectedException(f"Factorial requires an integer cant get handle float")

    return str(solve_factorial(int(number[0]))), number[-1]

def solve_factorial(number: int) -> int:
    factorial_number = 1
    for i in range(2, number + 1):
        factorial_number *= i
    return factorial_number