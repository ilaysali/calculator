from Tokenizer import tokenize
from Parser import parser

def test_tokenize_basic():
    lst = tokenize("3.14+34*(5^3)-9")
    assert parser(lst) == "3.14,34,5,3,^,*,+,9,-,"

def test_tokenize_complex():
    assert tokenize("12+34*5") == ["12", "+", "34", "*", "5"]

def test_tokenize_decimals():
    assert tokenize("3.14+2") == ["3.14", "+", "2"]

def test_tokenize_parentheses():
    assert tokenize("(5+5)*2") == ["(", "5", "+", "5", ")", "*", "2"]


