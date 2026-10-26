import os
import sys

# Add the path to the src/exercises file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'lessons')))

from unit_08.src.lessons.Lesson_03 import task_answer

def test_task_answer_case1():
    str_list = ["this", "IS", "a", "list", "of", "a", "few", "strings"]
    expected_output = ['a', 'a', 'wef', 'sgnirts']
    assert task_answer(str_list) == expected_output


def test_task_answer_case2():
    str_list = ["this", "IS", "another", "list", "of", "strings"]
    expected_output = ['rehtona', 'sgnirts']
    assert task_answer(str_list) == expected_output


def test_task_answer_case3():
    str_list = ["one", "two", "three", "four", "five", "six"]
    expected_output = ['eno', 'owt', 'eerht', 'xis']
    assert task_answer(str_list) == expected_output
