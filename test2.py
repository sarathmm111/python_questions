from postfix import evaluate

def test_single_operand():
    assert 5==5
    
def test_operand_addition():
    assert evaluate("2+4") == 6
