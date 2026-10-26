import os
import sys

# Add the path to the "Lesson_01.py" file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'lessons')))

from unit_06.src.lessons.Lesson_03 import tuple_search


def test_tuple_search_basic():
    spaghetti_soup = ("a", "b", "g", "c", "a", "z", "g", "a", "g", "y")
    assert tuple_search(spaghetti_soup, "g") == (3, 2)


def test_tuple_search_first_element():
    test_tuple = ("x", "y", "z", "x", "y")
    assert tuple_search(test_tuple, "x") == (2, 0)


def test_tuple_search_last_element():
    test_tuple = ("a", "b", "c", "d", "e")
    assert tuple_search(test_tuple, "e") == (1, 4)


def test_tuple_search_single_occurrence():
    test_tuple = ("apple", "banana", "cherry", "date")
    assert tuple_search(test_tuple, "cherry") == (1, 2)


def test_tuple_search_with_numbers():
    test_tuple = (1, 2, 3, 2, 1, 4, 5, 2)
    assert tuple_search(test_tuple, 2) == (3, 1)
