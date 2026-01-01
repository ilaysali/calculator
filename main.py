from Evaluate import evaluate_postfix
from Parser import parser
from Reform import *
from Tokenizer import tokenize


def calc (string: str):
    string = remove_whitespace(string)
    string = reform_sequence_of_priority1(string)
    print(string)
    lst = tokenize(string)
    print(lst)
    lst = parser(lst)
    print(lst)
    result = evaluate_postfix(lst)
    print(result)
    return result
