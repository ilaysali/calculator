"""
Main entry point for the calculator application.
Handles user input loop and orchestrates the calculation process.
"""

from Evaluate import evaluate_postfix
from Parser import parser, tokenize
from Reform import remove_whitespace, reform_sequence_of_priority1
from Exceptions import (
    InvalidInputException, InvalidOperandException, TokenNotDefineException,
    NumbersInARowException, MismatchedParenthesesException, IntegerExpectedException
)


def calculate(expression: str) -> float:
    # 1. Remove whitespace and reform special sequences
    expression = remove_whitespace(expression)
    expression = reform_sequence_of_priority1(expression)
    print(f"Reformed: {expression}")

    # 2. Tokenize
    token_list = tokenize(expression)
    print(f"Tokenized: {token_list}")

    # 3. Parse (Shunting Yard)
    postfix_list = parser(token_list)
    print(f"Parsed (Postfix): {postfix_list}")

    # 4. Evaluate
    result = evaluate_postfix(postfix_list)
    return result


def main():
    """
    Main application loop.
    Accepts input until the user types 'exit'.
    """

    print("Type 'exit' to quit.\n")
    while True:
        try:
            user_input = input("Enter an expression: \n")

            if user_input.strip().lower() == "exit":
                print("Exit calculator")
                break

            result = calculate(user_input)
            print(f"Result: {result}\n")

        except TokenNotDefineException as e:
            print(f"Input Error: {e}\n")

        except NumbersInARowException as e:
            print(f"Input Error: {e}\n")

        except MismatchedParenthesesException as e:
            print(f"Input Error: {e}\n")

        except InvalidOperandException as e:
            print(f"Input Error: {e}\n")

        except IntegerExpectedException as e:
            print(f"Input Error: {e}\n")

        except InvalidInputException as e:
            print(f"Input Error: {e}\n")

        except ZeroDivisionError:
            print("Math Error: Cannot divide by zero.\n")

        except OverflowError:
            print("Overflow Error: The result is too large.\n")

        except IndexError:
            print("Syntax Error: Incomplete expression.\n")

        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")


if __name__ == "__main__":
    main()