from Exceptions import InvalidInputException
from utility import is_number, get_operator


def validate_input ( current:tuple, previous: tuple = None) -> None:
    current_token = current[-1] if is_number(current[0]) else get_operator(current[1])
    previous_token = (previous[-1] if is_number(previous[0]) else get_operator(previous[1])) if previous else None

    if current_token in ["Number", '(', 'M', '~']:
        validate_numbers_LParentheses_Lunary(previous_token, current_token)

    else:
        validate_operators_RParentheses_Runary(previous_token, current_token)




def validate_numbers_LParentheses_Lunary (previous_token: str, current_token: str) -> None:
    if previous_token and previous_token in ["Number", ')', '!', '#']:
        raise InvalidInputException(f"Invalid input in validate_numbers_LParentheses_Lunary: {current_token} cant come after {previous_token}")
    if current_token != '(' and current_token == previous_token :
        raise InvalidInputException(f"Invalid input in validate_numbers_LParentheses_Lunary: {current_token} cant come after itself")

def validate_operators_RParentheses_Runary (previous_token: str, current_token: str) -> None:
    if not previous_token:
        raise InvalidInputException(f"Invalid input in validate_operators_RParentheses_Runary:{current_token} cant be at the start of input")
    if not previous_token in ["Number", ')', '!', '#']:
        raise InvalidInputException(f"Invalid input in validate_operators_RParentheses_Runary: {current_token} cant come after {previous_token}")