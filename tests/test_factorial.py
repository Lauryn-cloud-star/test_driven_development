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

def test_factorial_for_3():
    assert factorial(3) == 6

def test_factorial_for_4():
    assert factorial(4) == 24

def test_factorial_for_10():
    assert factorial(10) == 3628800