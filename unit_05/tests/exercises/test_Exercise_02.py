import sys
import os
import pytest

# Add the path to src/exercises
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'exercises')))

# Import the function from Exercise_02.py
from unit_05.src.exercises.Exercise_02 import convert_temp

def test_celsius_to_fahrenheit_case_1():
    """Test Celsius to Fahrenheit conversion for case 1."""
    temp_c = 4
    expected_f = 39.2
    result = convert_temp(temp_c)
    assert result is not None
    result = round(result, 2)
    assert result == expected_f, f"C to F: Expected {expected_f} for {temp_c}°C, but got {result}"

def test_celsius_to_fahrenheit_case_2():
    """Test Celsius to Fahrenheit conversion for case 2."""
    temp_c = 53
    expected_f = 127.4
    result = convert_temp(temp_c)
    assert result is not None
    result = round(result, 2)
    assert result == expected_f, f"C to F: Expected {expected_f} for {temp_c}°C, but got {result}"

def test_fahrenheit_to_celsius_case_1():
    """Test Fahrenheit to Celsius conversion for case 1."""
    temp_f = 44
    expected_c = 6.67
    result = convert_temp(temp_f, Fahrenheit=True)
    assert result is not None
    result = round(result, 2)
    assert result == expected_c, f"F to C: Expected {expected_c} for {temp_f}°F, but got {result}"

def test_fahrenheit_to_celsius_case_2():
    """Test Fahrenheit to Celsius conversion for case 2."""
    temp_f = 130
    expected_c = 54.44
    result = convert_temp(temp_f, Fahrenheit=True)
    assert result is not None
    result = round(result, 2)
    assert result == expected_c, f"F to C: Expected {expected_c} for {temp_f}°F, but got {result}"

def test_invalid():
    """Test invalid input for both Celsius and Fahrenheit conversions, expecting ValueErrors."""

    temp_c = -300
    with pytest.raises(ValueError, match="Temperature below absolute zero is invalid for Celsius."):
        convert_temp(temp_c)

    temp_f = -500
    with pytest.raises(ValueError, match="Temperature below absolute zero is invalid for Fahrenheit."):
        convert_temp(temp_f, Fahrenheit=True)
