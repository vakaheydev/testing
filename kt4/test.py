import pytest

from kt2.utils import calculate_grades_averages
from util import *

test_data = [(num, num % 2 == 0) for num in range(1, 11)]


@pytest.mark.parametrize('number, expected', test_data)
def test_is_even(number, expected):
    assert is_even(number) == expected


test_data = [(num, num + 1, num * (num + 1)) for num in range(1, 11)]


@pytest.mark.parametrize('a, b, expected', test_data)
def test_calculate_area(a, b, expected):
    assert calculate_area(a, b) == expected


test_data = [(1, 2, 2, 'isosceles'),
             (2, 1, 2, 'isosceles'),
             (2, 2, 1, 'isosceles'),

             (2, 2, 2, 'equilateral'),

             (1, 2, 3, 'various'),
             (3, 1, 2, 'various'),
             (1, 3, 2, 'various')]


@pytest.mark.parametrize('a, b, c, expected', test_data)
def test_classify_triangle(a, b, c, expected):
    assert classify_triangle(a, b, c) == expected


expected = [78.25, 48.0, 44.0, 47.0, 45.0, 46.0, 43.0, 50.0, 83.0, 97.0, 40.0, 45.0, 77.0, 90.0, 4.0, 40.0]
actual = calculate_grades_averages()
test_data = list(zip(actual, expected))


@pytest.mark.parametrize('actual, expected', test_data)
def test_calculate_grades_average(actual, expected):
    assert actual == expected
