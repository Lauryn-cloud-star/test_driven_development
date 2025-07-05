import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from multiply import multiply_v2

def test_multiply_1_1():
    assert multiply_v2(1, 1) == 1


def test_multiply_2_2():
    assert multiply_v2(2, 2) == 4

def test_multiply_3_3():
    assert multiply_v2(3, 3) == 9

def test_multiply_4_4():
    assert multiply_v2(4, 4) == 16

def test_multiply_23_45():
    assert multiply_v2(23, 45) == 1035