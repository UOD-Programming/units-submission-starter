import os
import sys
import random
from pathlib import Path

UNIT_ROOT = Path(__file__).resolve().parents[2]

# Add the path to the src/lessons file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'lessons')))

from unit_07.src.lessons.Lesson_04 import write_nums


def test_write_nums_fixed(monkeypatch):
    n = 10
    filename = UNIT_ROOT / "src/lessons/Lesson_04_nums.txt"
    monkeypatch.chdir(UNIT_ROOT)

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
    filename = UNIT_ROOT / "src/lessons/Lesson_04_nums.txt"
    monkeypatch.chdir(UNIT_ROOT)

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
