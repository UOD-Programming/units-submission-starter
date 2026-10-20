import sys
import os

# Add the path to the "Lesson_01.py" file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'lessons')))

# Import all functions from Lesson_01.py
from unit_05.src.lessons.Lesson_01 import odd_test

def test_odd():
    """Tests the odd_test function for odd numbers."""
    assert odd_test(3) == True
    assert odd_test(9) == True
    assert odd_test(47) == True

def test_even():
    """Tests the odd_test function for even numbers."""
    assert odd_test(2) == False
    assert odd_test(20) == False
    assert odd_test(32) == False
