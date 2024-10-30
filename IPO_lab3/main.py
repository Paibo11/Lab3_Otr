#  Функция для определения n чисел Фибоначчи
def fibonacci(n: int):
    if n <= 0:
        raise ValueError("Количество чисел должно быть положительным.")

    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence[:n]


# Сортировка пузырьком
def bubble_sort(arr):
    n = len(arr)
    sorted_arr = arr[:]

    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]

    return sorted_arr

# Калькулятор
def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно.")
        return a / b
    else:
        raise ValueError("Некорректная операция.")
