from postfix import *

def test_single_operand():
    assert evaluate("5") == 5

def test_operand_addition():
    assert evaluate("24+") == 6
    
def test_operand_sub():
    assert evaluate("42-") == 2
    
def test_operand_sub1():
    assert evaluate("42-") == -3
