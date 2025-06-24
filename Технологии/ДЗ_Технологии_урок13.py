from functools import reduce


def get_cube(n):
    try:
        return int(n) ** 3
    except(ValueError, TypeError):
        pass


print(list(map(get_cube, ['1', 2, 3, 4, 5])))


def is_remainder(n):
    return n % 5 == 0


print(list(filter(is_remainder, [1, 2, 5, 6, 7, 10, 15, 16])))


def is_even(n):
    return n % 2 != 0


def multiply(x, y):
    return x * y


print(reduce(multiply, filter(is_even, [1, 2, 3, 5, 4, 6, 10])))

