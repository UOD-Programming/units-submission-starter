import os
import sys
from unittest.mock import patch

# Add the path to the src/exercises file to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'exercises')))

from unit_07.src.exercises.Exercise_03 import coin_tosses, count, percentage, main


def test_coin_toss_simulation_case1():
    tosses = [1, 0, 0, 0, 1]
    expected_output = [
        'How many coin tosses would you like to simulate?',
        'No. of Heads: 2',
        'No. of Tails: 3',
        '%   of Heads: 40.0',
        '%   of Tails: 60.0'
    ]

    inputs = iter([str(len(tosses))])
    output = []

    def mock_input(prompt):
        output.append(prompt)
        return next(inputs)

    def mock_print(*args, **kwargs):
        end = kwargs.get('end', '\n')
        output.append(''.join(map(str, args)) + end)

    with patch('builtins.input', side_effect=mock_input), \
         patch('builtins.print', side_effect=mock_print), \
         patch('unit_07.src.exercises.Exercise_03.coin_tosses', return_value=tosses):
        main()
    expected_output = "".join(expected_output)
    output = "".join([s.strip() for s in output])
    assert output == expected_output


def test_coin_toss_simulation_case2():
    tosses = [
        0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1,
        0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0,
        0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0,
        0
    ]
    expected_output = [
        'How many coin tosses would you like to simulate?',
        'No. of Heads: 47',
        'No. of Tails: 56',
        '%   of Heads: 45.63',
        '%   of Tails: 54.37'
    ]

    inputs = iter([str(len(tosses))])
    output = []

    def mock_input(prompt):
        output.append(prompt)
        return next(inputs)

    def mock_print(*args, **kwargs):
        end = kwargs.get('end', '\n')
        output.append(''.join(map(str, args)) + end)

    with patch('builtins.input', side_effect=mock_input), \
         patch('builtins.print', side_effect=mock_print), \
         patch('unit_07.src.exercises.Exercise_03.coin_tosses', return_value=tosses):
        main()
    expected_output = "".join(expected_output)
    output = "".join([s.strip() for s in output])
    assert output == expected_output


def test_percentage_calculation():
    count_tosses = (5, 3)
    expected_percentage = (62.5, 37.5)
    assert percentage(count_tosses) == expected_percentage


def test_count_function():
    tosses = [1, 0, 1, 1, 0]
    expected_count = (3, 2)
    assert count(tosses) == expected_count


def test_coin_tosses_function():
    with patch('random.choices', side_effect=lambda population, k: [1 if i % 2 == 0 else 0 for i in range(k)]):
        tosses = coin_tosses(1000)
        assert len(tosses) == 1000
        assert min(tosses) == 0 and max(tosses) == 1

        tosses_2 = coin_tosses(1000)
        assert tosses != tosses_2  # Random output should differ
