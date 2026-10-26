import random
import os
import sys

# Add the path to the src/lessons file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'lessons')))

from unit_08.src.lessons.Lesson_01 import filter_palindromes, is_palindrome


def test_filter_palindromes():
    test_cases = [
        (["ABBA", "snake", "Peep", "this"], ["ABBA", "Peep"]),
        (["civic", "test", "peep", "emma"], ["civic", "peep"]),
        (["civic", "radar", "programming", "computing", "level", "rotor", "kayak", "madam", "and", "refer"],
         ["civic", "radar", "level", "rotor", "kayak", "madam", "refer"])
    ]

    for input_list, expected_output in test_cases:
        result = filter_palindromes(input_list)
        assert result == expected_output, f"For input {input_list}, expected {expected_output}, but got {result}"


def test_is_palindrome():
    test_cases = [
        ("ABBA", True),
        ("snake", False),
        ("Peep", True),
        ("this", False),
        ("rotor", True),
        ("madam", True),
        ("civic", True),
        ("programming", False),
        ("computing", False)
    ]

    for input_string, expected_output in test_cases:
        result = is_palindrome(input_string)
        assert result == expected_output, f"For input {input_string}, expected {expected_output}, but got {result}"

    # Test with random palindrome
    pal_len = random.randint(5, 10)
    pal_str = ''.join(str(i) for i in range(pal_len))
    assert not is_palindrome(pal_str), f"Random string {pal_str} incorrectly identified as a palindrome"
    assert is_palindrome(pal_str + pal_str[::-1]), f"Concatenated palindrome {pal_str + pal_str[::-1]} not identified"


if __name__ == "__main__":
    test_filter_palindromes()
    test_is_palindrome()
    print("All tests passed!")
