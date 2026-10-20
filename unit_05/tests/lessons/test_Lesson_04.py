import inspect
import sys
import os
from unittest.mock import patch
import io

# Add the path to the "Lesson_04.py" file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'lessons')))

# Import all functions from Lesson_04.py
from unit_05.src.lessons.Lesson_04 import *

def test_function_exists_and_arguments():
    """Test the function signature of print_list."""

    function_name = "print_list"
    assert function_name in globals(), f"{function_name} is not defined"

    argspec = inspect.getfullargspec(print_list)
    
    # Ensure the function accepts exactly one positional argument
    arguments = argspec.args[:len(argspec.args) - len(argspec.defaults)] if argspec.defaults else argspec.args
    assert len(arguments) == 1, "Function does not take in a single positional argument"
    
    # Ensure the function has a keyword argument 'multiple'
    keyword_arguments = argspec.args[-len(argspec.defaults):] if argspec.defaults else []
    assert "multiple" in keyword_arguments, "Function does not have a keyword argument called multiple"
    
    # Check if the default value for 'multiple' is 1
    assert argspec.defaults[-1] == 1, "Default value for 'multiple' should be 1"

def test_print_list_output_case1():
    """Test print_list with input_list=[4, 3, 2, 1] and default multiple."""
    input_list = [4, 3, 2, 1]
    expected_output = "4\n3\n2\n1\n"
    
    with patch('sys.stdout', new=io.StringIO()) as fake_out:
        print_list(input_list)
        assert fake_out.getvalue() == expected_output, f"Failed with input_list={input_list}"

def test_print_list_output_case2():
    """Test print_list with input_list=[2, 3, 6, 4] and multiple=2."""
    input_list = [2, 3, 6, 4]
    expected_output = "4\n6\n12\n8\n"
    
    with patch('sys.stdout', new=io.StringIO()) as fake_out:
        print_list(input_list, multiple=2)
        assert fake_out.getvalue() == expected_output, f"Failed with input_list={input_list} and multiple=2"

def test_print_list_output_case3():
    """Test print_list with input_list=[2, 3, 6, 4] and multiple=3."""
    input_list = [2, 3, 6, 4]
    expected_output = "6\n9\n18\n12\n"
    
    with patch('sys.stdout', new=io.StringIO()) as fake_out:
        print_list(input_list, multiple=3)
        assert fake_out.getvalue() == expected_output, f"Failed with input_list={input_list} and multiple=3"

def test_print_list_output_case4():
    """Test print_list with input_list=[2, 3, 6, 4] and multiple=5."""
    input_list = [2, 3, 6, 4]
    expected_output = "10\n15\n30\n20\n"
    
    with patch('sys.stdout', new=io.StringIO()) as fake_out:
        print_list(input_list, multiple=5)
        assert fake_out.getvalue() == expected_output, f"Failed with input_list={input_list} and multiple=5"

def test_print_list_default_behavior():
    """Test print_list with default multiple value."""
    input_list = [4, 1, 6, 7]
    expected_output = "4\n1\n6\n7\n"
    
    with patch('sys.stdout', new=io.StringIO()) as fake_out:
        print_list(input_list)
        assert fake_out.getvalue() == expected_output, "Failed with default multiple value"
