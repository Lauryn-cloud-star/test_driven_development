import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fibonacci import fibonacci

def test_fibonacci_0():
    assert fibonacci(0) == 0
