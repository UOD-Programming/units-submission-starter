import os
import sys

# Add the path to the "Lesson_01.py" file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'lessons')))

from unit_06.src.lessons.Lesson_02 import change_list


def test_change_list_1():
    # Test case 1
    test_list = ["Pear", "Orange", "Peach", "Apple"]
    assert change_list(test_list) == ["Apple", "Banana", "Peach", "Pear"]

def test_change_list_2():
    # Test case 2
    test_list = ["Sam", "Bradley", "Wayne"]
    assert change_list(test_list) == ['Banana', 'Sam', 'Wayne']


def test_original_list_unchanged():
    # Test that the original list is not modified
    test_list = ["Pear", "Orange", "Peach", "Apple"]
    original_list = test_list.copy()
    change_list(test_list)
    assert test_list == original_list

    test_list = ["Sam", "Bradley", "Wayne"]
    original_list = test_list.copy()
    change_list(test_list)
    assert test_list == original_list