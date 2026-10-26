import os
import sys
import pytest

# Add the path to the src/lessons file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'lessons')))

from unit_08.src.lessons.Lesson_04 import string_list_concat, string_list_concat_with_space

def test_string_list_concat():
    test_cases = [
        (["This", "is", "a", "list", "of", "strings"], "Thisisalistofstrings"),
        (["monkeys", "like", "bananas"], "monkeyslikebananas"),
        (["Programming", "in", "Python"], "ProgramminginPython"),
    ]

    for input_list, expected_output in test_cases:
        assert string_list_concat(input_list.copy()) == expected_output


def test_string_list_concat_with_space():
    test_cases = [
        (["This", "is", "a", "list", "of", "strings"], "This is a list of strings"),
        (["monkeys", "like", "bananas"], "monkeys like bananas"),
        (["Programming", "in", "Python"], "Programming in Python"),
    ]

    for input_list, expected_output in test_cases:
        assert string_list_concat_with_space(input_list.copy()) == expected_output


def test_trace_string_list_concat(capsys):
    input_list = ["This", "is", "a", "list", "of", "strings"]

    result = string_list_concat(input_list.copy())

    # Capture trace messages from stdout
    captured = capsys.readouterr()
    trace_output = captured.out

    assert result == "Thisisalistofstrings"
    assert trace_output.count("Entering recursive call") == len(input_list)
    assert trace_output.count("Exiting recursive call") == len(input_list)


def test_trace_string_list_concat_with_space(capsys):
    input_list = ["This", "is", "a", "list", "of", "strings"]

    result = string_list_concat_with_space(input_list.copy())

    # Capture trace messages from stdout
    captured = capsys.readouterr()
    trace_output = captured.out

    assert result == "This is a list of strings"
    assert trace_output.count("Entering recursive call") == len(input_list)
    assert trace_output.count("Exiting recursive call") == len(input_list)
