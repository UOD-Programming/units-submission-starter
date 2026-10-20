import sys
import os

# Add the path to src/exercises (assuming exercise_4.py is located there)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'exercises')))

# Import the function from exercise_4.py
from unit_05.src.exercises.Exercise_04 import arithmetic_sum

def test_arithmetic_sum():
    """Test the arithmetic_sum function with various cases."""
    
    # Test case 1: a = 1, d = 1, n = 100
    assert arithmetic_sum(1, 1, 100) == 5050, "Failed case 1: arithmetic_sum(1, 1, 100)"
    
    # Test case 2: a = 2, d = 5, n = 45
    assert arithmetic_sum(2, 5, 45) == 5040, "Failed case 2: arithmetic_sum(2, 5, 45)"
    
    # Test case 3: a = 10, d = 4, n = 5
    assert arithmetic_sum(10, 4, 5) == 90, "Failed case 3: arithmetic_sum(10, 4, 5)"
    
    # Test case 4: a = 1, d = 2, n = 1000
    assert arithmetic_sum(1, 2, 1000) == 1000000, "Failed case 4: arithmetic_sum(1, 2, 1000)"
    
    # Test case 5: a = -5, d = -2, n = 20
    assert arithmetic_sum(-5, -2, 20) == -480, "Failed case 5: arithmetic_sum(-5, -2, 20)"
    
    # Test case 6: a = 3, d = 2, n = 15
    assert arithmetic_sum(3, 2, 15) == 255, "Failed case 6: arithmetic_sum(3, 2, 15)"

