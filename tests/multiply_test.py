import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from multiply import multiply

def test_multiply_firstcycle():
    assert multiply(1, 1) == 1

def text_multiply_secondcycle():
    assert multiply(2, 2) == 4

def test_multiply_thirdcycle():
    assert multiply(3, 3) == 16
