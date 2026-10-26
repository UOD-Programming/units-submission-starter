import inspect
import os
import sys

# Add the path to the src/lessons file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'lessons')))

from unit_08.src.lessons.Lesson_02 import initials


def count_args(func):
    """Counts positional and keyword arguments of a function."""
    signature = inspect.signature(func)
    parameters = signature.parameters

    positional_count = 0
    keyword_count = 0

    for param in parameters.values():
        if param.default == inspect.Parameter.empty and param.kind != inspect.Parameter.VAR_POSITIONAL:
            positional_count += 1
        elif param.default != inspect.Parameter.empty and param.kind != inspect.Parameter.VAR_KEYWORD:
            keyword_count += 1

    return positional_count, keyword_count


def test_initials_functionality():
    """Test the functionality of the initials function."""
    test_cases = [
        (("James", "Marshall", "Hendrix"), "J.M.H"),
        (("John", "Ronald", "Reuel", "Tolkien"), "J.R.R.T"),
        (("Scooby", "Doo"), "S.D"),
        (("Lionel", "Andrés", "Messi"), "L.A.M")
    ]

    for input_names, expected_output in test_cases:
        result = initials(*input_names)
        assert result == expected_output, f"For input {input_names}, expected {expected_output}, but got {result}"


if __name__ == "__main__":
    test_initials_signature()
    test_initials_functionality()
    print("All tests passed!")
