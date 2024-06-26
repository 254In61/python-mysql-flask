"""
This module provides basic unit testing of functions created.
"""
from mymodules.calculator import adding


VALUE_ONE = 50
VALUE_TWO = 2


# Test addition function
def test_addition():
    """
    Function to test adding() function
    """
    assert adding(VALUE_ONE,VALUE_TWO) == 52
