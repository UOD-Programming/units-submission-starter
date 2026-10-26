import os
import json
import copy
from pathlib import Path

UNIT_ROOT = Path(__file__).resolve().parents[2]

# Add the path to the src/exercises file to sys.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'exercises')))
from unit_07.src.exercises.Exercise_02 import save, load, add_item


def test_save_and_load(tmp_path):
    # Set up test data
    filename = tmp_path / "menu.json"
    test_menu = {"menu": {"1": {"Name": "Test Pizza", "Price": 11.99}}, "next_id": 2}

    try:
        # Save the menu to file
        save(filename, test_menu)
        assert os.path.exists(filename), f"File {filename} not saved successfully..."

        # Verify the saved content
        with open(filename) as f:
            menu_dict_test = json.load(f)
        assert menu_dict_test == test_menu, "Menu data not saved correctly"

        # Load the menu from file and verify
        loaded_menu = load(filename)
        assert loaded_menu == test_menu, "Loaded menu does not match saved menu"
    finally:
        # Cleanup after the test
        if os.path.exists(filename):
            os.remove(filename)


def test_add_item():
    # Set up test data
    test_menu = {"menu": {"1": {"Name": "Test Pizza", "Price": 11.99}}, "next_id": 2}

    # Create a copy of the test menu and add an item
    menu_copy = copy.deepcopy(test_menu)
    add_item(menu_copy, "Onion Soup", "3.99")

    # Define the expected menu after adding the item
    expected_menu = copy.deepcopy(test_menu)
    expected_menu["menu"]["2"] = {"Name": "Onion Soup", "Price": 3.99}
    expected_menu["next_id"] = 3

    assert menu_copy == expected_menu, "Item not added correctly"
