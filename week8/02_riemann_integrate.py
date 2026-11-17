# Recap 2: Midpoint Riemann sum integrator for the integral of f(x) from 0 to 1


def integrate(func, steps=1000):
    """func is a single-variable function, steps is the number of sub-intervals.
    Returns the midpoint Riemann sum approximation of the integral of func over [0, 1]."""
    total_area = 0
    dx = 1 / steps
    for i in range(steps):
        x_i = (i + 0.5) * dx          # midpoint of the i-th sub-interval
        total_area += func(x_i) * dx  # f(0.5dx)dx + f(1.5dx)dx + ...
    return total_area


def take_square(x):
    return x ** 2


print("Integral of x^2 from 0 to 1:", integrate(take_square), "(exact: 1/3 =", 1 / 3, ")")
print("Integral of x   from 0 to 1:", integrate(lambda x: x), "(exact: 0.5)")
print("Integral of 1   from 0 to 1:", integrate(lambda x: 1), "(exact: 1)")
print("Integral of x^3 from 0 to 1:", integrate(lambda x: x ** 3), "(exact: 0.25)")

# More steps -> better approximation
for steps in [1, 10, 100, 1000]:
    print("steps =", steps, " integral of x^2 =", integrate(take_square, steps))
