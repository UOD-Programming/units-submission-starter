import os
import sys
import random
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]

# Add the repository root so the unit_07 package can be imported.
sys.path.insert(0, str(REPOSITORY_ROOT))

from unit_07.src.lessons.Lesson_04 import write_nums


def test_write_nums_fixed(monkeypatch):
    n = 10
    filename = REPOSITORY_ROOT / "unit_07/src/lessons/Lesson_04_nums.txt"
    monkeypatch.chdir(REPOSITORY_ROOT)

    try:
        # Call the function to write numbers to the file
        write_nums(n)

        # Check if the file was created
        assert os.path.isfile(filename), f"File {filename} does not exist..."

        # Verify the contents of the file
        with open(filename, "r") as f:
            lines = f.readlines()

        expected_output = [f"{x}\n" for x in range(1, n + 1)]
        assert lines == expected_output, f"Output in {filename} is not correct"
    finally:
        # Cleanup: Remove the file to avoid clutter
        if os.path.exists(filename):
            os.remove(filename)


def test_write_nums_random(monkeypatch):
    # Generate a random number for n
    n = random.randint(1, 1000)
    filename = REPOSITORY_ROOT / "unit_07/src/lessons/Lesson_04_nums.txt"
    monkeypatch.chdir(REPOSITORY_ROOT)

    try:
        # Call the function to write numbers to the file
        write_nums(n)

        # Check if the file was created
        assert os.path.isfile(filename), f"File {filename} does not exist..."

        # Verify the contents of the file
        with open(filename, "r") as f:
            lines = f.readlines()

        expected_output = [f"{x}\n" for x in range(1, n + 1)]
        assert lines == expected_output, f"Output in {filename} is not correct."
    finally:
        # Cleanup: Remove the file to avoid clutter
        if os.path.exists(filename):
            os.remove(filename)
