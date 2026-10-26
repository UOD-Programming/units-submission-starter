import pytest
import os
import sys

# Add the path to the src/exercises file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'exercises')))

from unit_08.src.exercises.Exercise_02 import and_many, or_many


def test_and_many():
    assert and_many(True) is True
    assert and_many(True, True) is True
    assert and_many(True, True, True) is True
    assert and_many(True, True, True, True) is True
    assert and_many(False, True) is False
    assert and_many(True, False, True) is False
    assert and_many(True, True, True, False) is False
    assert and_many(False) is False
    assert and_many(False, False) is False


def test_or_many():
    assert or_many(True) is True
    assert or_many(False, True) is True
    assert or_many(True, False, True) is True
    assert or_many(True, True, True, False) is True
    assert or_many(False) is False
    assert or_many(False, False) is False
    assert or_many(False, False, False) is False
    assert or_many(False, False, False, False) is False
