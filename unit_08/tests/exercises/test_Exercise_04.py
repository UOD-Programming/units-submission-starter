import os
import sys
import pytest

# Add the path to the src/exercises file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'exercises')))

from unit_08.src.exercises.Exercise_04 import base_10_convertor_rec


def test_basic_conversions():
    assert base_10_convertor_rec("1011", convert_from_base=2) == 11
    assert base_10_convertor_rec("00341", 5) == 96


def test_recursive_calls_with_trace(capsys):
    test_cases = [
        ("1011", 2, 11),
        ("00341", 5, 96),
    ]

    for num_string, base, expected_output in test_cases:
        # Call the function and capture output
        result = base_10_convertor_rec(num_string, convert_from_base=base)

        # Capture trace messages from `stdout`
        captured = capsys.readouterr()
        trace_output = captured.out

        assert result == expected_output
        assert "Entering recursive call 1" in trace_output
        assert "Exiting recursive call 1" in trace_output


def test_trace_logging_depth(capsys):
    test_cases = [
        ("1011", 2, 4),
        ("00341", 5, 5),
    ]

    for num_string, base, expected_depth in test_cases:
        # Call the function and capture output
        _ = base_10_convertor_rec(num_string, convert_from_base=base)

        # Capture trace messages from `stdout`
        captured = capsys.readouterr()
        trace_output = captured.out
        enter_calls = trace_output.count("Entering recursive call")
        exit_calls = trace_output.count("Exiting recursive call")

        # Check that the number of entering and exiting calls match
        assert enter_calls == exit_calls
        assert enter_calls == expected_depth
