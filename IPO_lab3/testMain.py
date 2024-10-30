import pytest
from main import fibonacci, bubble_sort, calculator

# Тесты для функции fibonacci
def test_fibonacci_valid():
    assert fibonacci(5) == [0, 1, 1, 2, 3]

def test_fibonacci_invalid():
    with pytest.raises(ValueError):
        fibonacci(0)

# Тесты для функции bubble_sort
def test_bubble_sort_valid():
    assert bubble_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]

def test_bubble_sort_invalid():
    with pytest.raises(TypeError):
        bubble_sort(None)


# Тесты для функции calculator
def test_calculator_valid():
    assert calculator(1, 1, '+') == 2
    assert calculator(5, 3, '-') == 2
    assert calculator(2, 3, '*') == 6
    assert calculator(6, 2, '/') == 3

def test_calculator_invalid_operation():
    with pytest.raises(ValueError):
        calculator(1, 1, '%')

def test_calculator_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator(1, 0, '/')
