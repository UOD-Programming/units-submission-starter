import pytest
import os
import sys

# Add the path to the "Lesson_01.py" file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'lessons')))
from unit_06.src.lessons.Lesson_06 import sum_div_3

def test_sum_div_3_basic():
    assert sum_div_3(10) == 18
    assert sum_div_3(12) == 30
    assert sum_div_3(100) == 1683

def test_sum_div_3_edge_cases():
    assert sum_div_3(0) == 0
    assert sum_div_3(1) == 0
    assert sum_div_3(2) == 0
    assert sum_div_3(3) == 3

def test_sum_div_3_large_number():
    assert sum_div_3(1000) == 166833

def test_sum_div_3_float():
    with pytest.raises(TypeError):
        sum_div_3(10.5)

def test_sum_div_3_string():
    with pytest.raises(TypeError):
        sum_div_3("10")

def test_sum_div_3_prime():
    assert sum_div_3(17) == 45  # 3 + 6 + 9 + 12 + 15

def test_sum_div_3_multiple_of_three():
    assert sum_div_3(9) == 18  # 3 + 6 + 9