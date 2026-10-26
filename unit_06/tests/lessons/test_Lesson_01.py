import os
import sys

# Add the path to the "Lesson_01.py" file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'lessons')))

from unit_06.src.lessons.Lesson_01 import longest_word, num_characters

def test_longest_word():
    sample_string_list = [
        ["Hello", "World"],
        ["You", "say", "you", "want", "a", "revolution"],
        ["It's", "fine", "to", "celebrate", "success", "but", "it", "is", "more", "important", "to", "heed", "the", "lessons", "of", "failure"]
    ]
    sample_string_list2 = [["Hello", "World"], ["Apple", "Pears"]]

    assert longest_word(sample_string_list) == "revolution"
    assert longest_word(sample_string_list2) == "Hello"

def test_num_characters():
    sample_string_list = [
        ["Hello", "World"],
        ["You", "say", "you", "want", "a", "revolution"],
        ["It's", "fine", "to", "celebrate", "success", "but", "it", "is", "more", "important", "to", "heed", "the", "lessons", "of", "failure"]
    ]
    sample_string_list2 = [["Hello", "World"], ["Apple", "Pears"]]

    assert num_characters(sample_string_list) == 105
    assert num_characters(sample_string_list2) == 20

def test_longest_word_empty_list():
    assert longest_word([]) is None

def test_num_characters_empty_list():
    assert num_characters([]) == 0

def test_longest_word_multiple_longest():
    test_list = [["abc", "def"], ["ghi", "jkl"]]
    assert longest_word(test_list) == "abc"  # Should return the first longest word encountered

def test_num_characters_single_character():
    test_list = [["a"], ["b", "c"]]
    assert num_characters(test_list) == 3
