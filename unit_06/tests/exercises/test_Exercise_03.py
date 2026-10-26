import io
import os
import sys
from unittest.mock import patch

# Add the path to the "Exercise_03.py" file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'exercises')))
from unit_06.src.exercises.Exercise_03 import main


def test_main_case1():
    inputs = ["1", "5", "6", "10", "q"]
    expected_output = "The reverse of the numbers entered is:\n10\n6\n5\n1\n"
    with patch('builtins.input', side_effect=inputs), \
         patch('sys.stdout', new=io.StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()
    assert output.strip() == expected_output.strip()


def test_main_case2():
    inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    expected_output = "The reverse of the numbers entered is:\n10\n9\n8\n7\n6\n5\n4\n3\n2\n1\n"
    with patch('builtins.input', side_effect=inputs), \
         patch('sys.stdout', new=io.StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()
    assert output.strip() == expected_output.strip()


def test_main_case3():
    inputs = ["q"]
    expected_output = "No numbers entered.\n"
    with patch('builtins.input', side_effect=inputs), \
         patch('sys.stdout', new=io.StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()
    assert output.strip() == expected_output.strip()


def test_main_case4():
    inputs = ["1", "2", "q"]
    expected_output = "The reverse of the numbers entered is:\n2\n1\n"
    with patch('builtins.input', side_effect=inputs), \
         patch('sys.stdout', new=io.StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()
    assert output.strip() == expected_output.strip()


def test_main_case5():
    inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
    expected_output = "The reverse of the numbers entered is:\n10\n9\n8\n7\n6\n5\n4\n3\n2\n1\n"
    with patch('builtins.input', side_effect=inputs), \
         patch('sys.stdout', new=io.StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()
    assert output.strip() == expected_output.strip()

