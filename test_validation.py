from Tokenizer import tokenize
from Parser import parser
from Reform import reform_sequence_of_intensity1, remove_whitespace


def test_tokenize_basic():
    lst = tokenize("3.14+34*(5^3)-9")
    assert parser(lst) == "3.14,34,5,3,^,*,+,9,-,"

def test_tokenize_complex():
    lst = tokenize("~3.14+34*(~5!^3)-~9")
    assert parser(lst) == "3.14,34,5,3,^,*,+,9,-,"

def test_tokenize_decimals():
    lst = tokenize("~+-3")
    assert parser(lst) == "3.14,34,5,3,^,*,+,9,-,"

def test_tokenize_parentheses():
    s = remove_whitespace("6----8*9")
    print(s)
    s = reform_sequence_of_intensity1(s)

    assert s == "6-+8*9/12!"


