# Recap 3: Do-twice function, applies f_x two times: f_x(f_x(x))

from math import sqrt


def f_x_twice(x, f_x):
    """x is a number, f_x is a single-variable function.
    Returns f_x(f_x(x))"""
    return f_x(f_x(x))


# sqrt(sqrt(16)) = sqrt(4) = 2.0
print("f_x_twice(16, sqrt) =", f_x_twice(16, sqrt))

# (2**2)**2 = 4**2 = 16
print("f_x_twice(2, lambda x: x**2) =", f_x_twice(2, lambda x: x ** 2))
