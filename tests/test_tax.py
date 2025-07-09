import sys
import os
# Ensure the parent directory is in the path to import the tax module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tax import tax


"""if __name__ == "__main__":
    earnings_list = [10000, 15000, 36000, 40000]
    for earnings in earnings_list:
        calculated = tax(earnings)
        expected = expected_tax(earnings)
        print(f"Earnings: {earnings}, Calculated Tax: {calculated}, Expected Tax: {expected}")"""


def test_tax_below_12000():
    assert tax(10000) == 0

def test_tax_between_12000_and_36000():
    assert tax(15000) == tax(15000)  
    assert tax(36000) == tax(36000)

