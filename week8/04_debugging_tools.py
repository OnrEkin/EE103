# Recap 4: Using the 3 debugging tools on the functions above
#   Tool 1: print statements   -> see the values while the code runs
#   Tool 2: pdb (import pdb; pdb.set_trace()) -> stop the program and inspect in the terminal
#   Tool 3: VS Code breakpoints -> click left of a line number (red dot), then Run > Start Debugging (F5)
#           and inspect the variables in the VARIABLES panel / DEBUG CONSOLE
#
# Set USE_PDB = True to stop inside the functions with pdb.
# pdb commands: n (next line), s (step into), c (continue), p var (print var), l (list code), q (quit)

from math import sqrt

DEBUG_PRINT = True   # Tool 1
USE_PDB = False      # Tool 2


def estimate_derivative(func, x, h=1e-5):
    f_plus = func(x + h)
    f_minus = func(x - h)
    if DEBUG_PRINT:
        print("[debug] estimate_derivative: x =", x, "f(x+h) =", f_plus, "f(x-h) =", f_minus)
    if USE_PDB:
        import pdb; pdb.set_trace()
    return (f_plus - f_minus) / (2 * h)   # Tool 3: put a breakpoint on this line


def integrate(func, steps=1000):
    total_area = 0
    dx = 1 / steps
    for i in range(steps):
        x_i = (i + 0.5) * dx
        total_area += func(x_i) * dx
        if DEBUG_PRINT and i < 3:   # print only the first few steps, not all 1000
            print("[debug] integrate: i =", i, "x_i =", x_i, "total_area =", total_area)
    if USE_PDB:
        import pdb; pdb.set_trace()
    return total_area   # Tool 3: put a breakpoint on this line


def f_x_twice(x, f_x):
    first = f_x(x)
    second = f_x(first)
    if DEBUG_PRINT:
        print("[debug] f_x_twice: x =", x, "f_x(x) =", first, "f_x(f_x(x)) =", second)
    if USE_PDB:
        import pdb; pdb.set_trace()
    return second   # Tool 3: put a breakpoint on this line


def take_square(x):
    return x ** 2


print("derivative of x^2 at 3:", estimate_derivative(take_square, 3))
print("integral of x^2 on [0,1]:", integrate(take_square))
print("f_x_twice(16, sqrt):", f_x_twice(16, sqrt))
print("f_x_twice(2, lambda x: x**2):", f_x_twice(2, lambda x: x ** 2))
