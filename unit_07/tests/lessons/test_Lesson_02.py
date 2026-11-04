import sys
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]

# Add the repository root so the unit_07 package can be imported.
sys.path.insert(0, str(REPOSITORY_ROOT))

from unit_07.src.lessons import Lesson_02_hello as hello

def test_hello():
    # Test the hello() function
    assert hello.hi("Joe") == "Hello Joe", "hello() did not return the correct string"
    assert hello.hi("Alice") == "Hello Alice", "hello() did not return the correct string"

def test_goodbye():
    # Test the goodbye() function
    assert hello.goodbye("Joe") == "Goodbye Joe", "goodbye() did not return the correct string"
    assert hello.goodbye("Alice") == "Goodbye Alice", "goodbye() did not return the correct string"
