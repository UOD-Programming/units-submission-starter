import sys
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]

# Add the repository root so the unit_07 package can be imported.
sys.path.insert(0, str(REPOSITORY_ROOT))

from unit_07.src.exercises.Exercise_01 import count_words

def test_count_words():
    filename = REPOSITORY_ROOT / "unit_07/src/exercises/Exercise_01_example.txt"
    assert count_words(filename) == 15
