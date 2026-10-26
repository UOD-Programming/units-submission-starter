import os
import sys

# Add the path to the "Lesson_01.py" file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'lessons')))
from unit_06.src.lessons.Lesson_05 import add_from_list

def test_add_from_list_basic():
    test_dict = {"a": 1, "b": 2}
    items_to_add = [("e", 5), ("z", 26)]
    add_from_list(test_dict, items_to_add)
    assert test_dict == {"a": 1, "b": 2, "e": 5, "z": 26}

def test_add_from_list_overwrite():
    test_dict = {"a": 1, "b": 2}
    items_to_add = [("b", 3), ("c", 4)]
    add_from_list(test_dict, items_to_add)
    assert test_dict == {"a": 1, "b": 3, "c": 4}

def test_add_from_list_different_types():
    test_dict = {}
    items_to_add = [(3, "three"), (True, False)]
    add_from_list(test_dict, items_to_add)
    assert test_dict == {3: "three", True: False}

def test_add_from_list_large_input():
    test_dict = {str(i): i for i in range(1000)}
    items_to_add = [(str(i), i) for i in range(1000, 2000)]
    add_from_list(test_dict, items_to_add)
    assert len(test_dict) == 2000
    assert test_dict["1500"] == 1500
