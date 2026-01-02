from Evaluate import evaluate_postfix
from Parser import *
from Reform import *
from Exceptions import *


def calculate (string):
    try:
        #string = input("Enter a string: ")
        string = remove_whitespace(string)
        string = reform_sequence_of_priority1(string)
        print(f"Reformed: {string}")

        lst = tokenize(string)
        print(f"Tokenized: {lst}")

        lst = parser(lst)
        print(f"Parsed (Postfix): {lst}")

        result = evaluate_postfix(lst)
        print(f"Result: {result}")
        return result

    except TokenNotDefineException as e:
        print(f"Input Error: {e}")
        #calculate()
        return None

    except NumbersInARowException as e:
        print(f"Input Error: {e}")
        # calculate()
        return None

    except MismatchedParenthesesException as e:
        print(f"Input Error: {e}")
        # calculate()
        return None

    except InvalidOperandException as e:
        print(f"Input Error: {e}")
        # calculate()
        return None

    except IntegerExpectedException as e:
        print(f"Input Error: {e}")
        # calculate()
        return None

    except InvalidInputException as e:
        print(f"Input Error: {e}")
        #calculate()
        return None

    except ZeroDivisionError:
        print("Math Error: Cannot divide by zero.")
        #calculate()
        return None

    except IndexError:
        print("In evaluate_postfix pop from empty list.")
        # calculate()
        return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        #calculate()
        return None
