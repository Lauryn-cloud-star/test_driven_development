import sys
import os
# Ensure the parent directory is in the path to import the fibonacci module
# This is necessary if the tests are run from a different directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fibonacci import fibonacci

def test_fibonacci_0():
    assert fibonacci(0) == 0

def test_fibonacci_1():
    assert fibonacci(1) == 1

def test_fibonacci_4():
    assert fibonacci(4) == 3
