
import sys
import os

# Add the path to the "Lesson_02.py" file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'lessons')))

# Import all functions from Lesson_02.py
from unit_05.src.lessons.Lesson_02 import *

def get_random_string(length):
    import random
    import string
    return ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=length))

def test_reverse_and_get_character():
    assert reverse("This is a string") == "gnirts a si sihT"
    assert reverse("Hello World") == "dlroW olleH"
    string_one = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    assert reverse(string_one) == string_one[::-1]
    string_two = get_random_string(10)
    assert reverse(string_two) == string_two[::-1]
    assert get_character("This is a string", 3) == "i"
    assert get_character("Hello World", 5) == "o"
    assert get_character(string_one, 10) == string_one[9]
    assert get_character(string_two, 2) == string_two[1]