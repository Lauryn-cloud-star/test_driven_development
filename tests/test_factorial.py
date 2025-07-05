import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from factorial import factorial

def test_factorial_for_0():
    assert factorial(0) == 1

def test_factorial_for_1():
    assert factorial(1) == 1

def test_factorial_for_2():
    assert factorial(2) == 2