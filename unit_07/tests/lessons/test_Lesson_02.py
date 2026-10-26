import os
import sys

# Add the path to the src/lessons file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'lessons')))

from unit_07.src.lessons import Lesson_02_hello as hello

def test_hello():
    # Test the hello() function
    assert hello.hi("Joe") == "Hello Joe", "hello() did not return the correct string"
    assert hello.hi("Alice") == "Hello Alice", "hello() did not return the correct string"

def test_goodbye():
    # Test the goodbye() function
    assert hello.goodbye("Joe") == "Goodbye Joe", "goodbye() did not return the correct string"
    assert hello.goodbye("Alice") == "Goodbye Alice", "goodbye() did not return the correct string"
