import io
import re
import os
import sys
from unittest.mock import patch

# Add the path to the "Exercise_02.py" file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'exercises')))
from unit_06.src.exercises.Exercise_02 import main, advanced_main, rand_num_list_gen

def test_main():
    """Test the output of main function."""
    with patch('sys.stdout', new=io.StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()

    # Check if all ranges are present
    ranges = ["1..10", "11..20", "21..30", "31..40", "41..50"]
    for range_str in ranges:
        assert range_str in output, f"Range {range_str} not found in output."

    # Check if the sum of all counts is 100
    counts = [int(line.split(": ")[1]) for line in output.split("\n") if ".." in line]
    assert sum(counts) == 100, f"Sum of counts is not 100. Got {sum(counts)}."

def test_advanced_main_case1():
    """Test advanced_main with num_input=100 and custom ranges."""
    num_input = "100"
    ranges_input = "1..20,21..30,31..45,46..50"
    with patch('builtins.input', side_effect=[num_input, ranges_input]), \
         patch('sys.stdout', new=io.StringIO()) as fake_out:
        advanced_main()
        output = fake_out.getvalue()

    # Check if all input ranges are present in the output
    for range_str in ranges_input.split(','):
        assert range_str in output, f"Range {range_str} not found in output."

    # Extract counts and check if their sum matches the input number
    counts = [int(re.search(r': (\d+)', line).group(1)) for line in output.split('\n') if '..' in line]
    assert sum(counts) >= int(num_input), f"Sum of counts is not >= {num_input}. Got {sum(counts)}."

def test_advanced_main_case2():
    """Test advanced_main with num_input=200 and overlapping ranges."""
    num_input = "200"
    ranges_input = "1..30,1..50"
    with patch('builtins.input', side_effect=[num_input, ranges_input]), \
         patch('sys.stdout', new=io.StringIO()) as fake_out:
        advanced_main()
        output = fake_out.getvalue()

    # Check if all input ranges are present in the output
    for range_str in ranges_input.split(','):
        assert range_str in output, f"Range {range_str} not found in output."

    # Extract counts and check if their sum matches or exceeds the input number
    counts = [int(re.search(r': (\d+)', line).group(1)) for line in output.split('\n') if '..' in line]
    assert sum(counts) >= int(num_input), f"Sum of counts is not >= {num_input}. Got {sum(counts)}."
