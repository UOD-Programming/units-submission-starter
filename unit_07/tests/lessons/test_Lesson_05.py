import json
import os
import sys
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]

# Add the repository root so the unit_07 package can be imported.
sys.path.insert(0, str(REPOSITORY_ROOT))

from unit_07.src.lessons.Lesson_05 import load  # Replace `your_module` with the actual module name where `load()` is implemented


def test_load(tmp_path):
    filename = tmp_path / "test_items.json"
    data = {"items": ["apple", "banana", "cherry"]}

    try:
        # Setup: Create a test JSON file
        with open(filename, "w") as f:
            json.dump(data, f)

        # Test: Verify that the load function reads the file correctly
        loaded_data = load(filename)
        assert loaded_data == data, f"Expected {data}, but got {loaded_data}"
    finally:
        # Teardown: Remove the test file
        if os.path.exists(filename):
            os.remove(filename)
