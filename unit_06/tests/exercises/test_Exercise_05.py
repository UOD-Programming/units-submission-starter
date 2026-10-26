from io import StringIO
from unittest.mock import patch
import os
import sys

# Add the path to the "Exercise_05.py" file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'exercises')))
from unit_06.src.exercises.Exercise_05 import look_up, add, edit, delete, list_all


def test_look_up():
    address_book = {
        "Sam": "MS308, Markeaton St, Derby",
        "Sherlock": "221B Baker Street, London"
    }
    assert look_up(address_book, "Sam") == "MS308, Markeaton St, Derby"
    assert look_up(address_book, "Sherlock") == "221B Baker Street, London"


def test_add():
    address_book = {
        "Sam": "MS308, Markeaton St, Derby",
        "Sherlock": "221B Baker Street, London"
    }
    add(address_book, "John", "742 Evergreen Terrace, Springfield")
    assert "John" in address_book
    assert address_book["John"] == "742 Evergreen Terrace, Springfield"


def test_edit():
    address_book = {
        "Sam": "MS308, Markeaton St, Derby",
        "Sherlock": "221B Baker Street, London"
    }
    edit(address_book, "Sam", "New Address, New City")
    assert address_book["Sam"] == "New Address, New City"


def test_delete():
    address_book = {
        "Sam": "MS308, Markeaton St, Derby",
        "Sherlock": "221B Baker Street, London"
    }
    delete(address_book, "Sherlock")
    assert "Sherlock" not in address_book


def test_list_all():
    address_book = {
        "Sam": "MS308, Markeaton St, Derby",
        "Sherlock": "221B Baker Street, London"
    }
    expected_output = (
        "Name: Sam\n"
        "Address: MS308, Markeaton St, Derby\n"
        "\n"
        "Name: Sherlock\n"
        "Address: 221B Baker Street, London\n"
        "\n"
    )

    with patch('sys.stdout', new=StringIO()) as fake_out:
        list_all(address_book)
        assert fake_out.getvalue() == expected_output