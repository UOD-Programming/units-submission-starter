import os
import sys
from pathlib import Path

UNIT_ROOT = Path(__file__).resolve().parents[2]

# Add the path to the src/exercises file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'exercises')))

from unit_07.src.exercises.Exercise_01 import count_words

def test_count_words():
    filename = UNIT_ROOT / "src/exercises/Exercise_01_example.txt"
    assert count_words(filename) == 15
