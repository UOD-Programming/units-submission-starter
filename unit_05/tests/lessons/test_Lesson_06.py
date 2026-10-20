import sys
import os

# Add the path to the "Lesson_06.py" file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'lessons')))

# Import all functions from Lesson_06.py
from unit_05.src.lessons.Lesson_06 import *


def test_new_list_item_one():
    # Test case 1
    l = [1, 2, 3, 4]
    result = new_list_item_one(l, 0)
    assert result == [0, 2, 3, 4]
    assert l == [1, 2, 3, 4]  # Original list should remain unchanged

    # Test case 2
    l = [2, 3, 4]
    result = new_list_item_one(l, 4)
    assert result == [4, 3, 4]
    assert l == [2, 3, 4]  # Original list should remain unchanged


def test_update_list_item_one():
    # Test case 1
    l = [1, 2, 3, 4]
    update_list_item_one(l, 0)
    assert l == [0, 2, 3, 4]

    # Test case 2
    l = [2, 3, 4]
    update_list_item_one(l, 4)
    assert l == [4, 3, 4]

