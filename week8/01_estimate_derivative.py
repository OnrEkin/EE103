# Recap 1: Numerical derivative with the central difference formula
# f'(x) ~ (f(x + h) - f(x - h)) / (2h)


def estimate_derivative(func, x, h=1e-5):
    """func is a single-variable function, x is a number, h is a small step.
    Returns an estimate of the first order derivative of func at x."""
    return (func(x + h) - func(x - h)) / (2 * h)


def take_square(x):
    """Returns x squared: f(x) = x^2"""
    return x ** 2


# Same function, this time defined with lambda
take_square_lambda = lambda x: x ** 2

print("Using take_square (def):")
for x in [0, 1, 2, 3, 5, -4]:
    print("  x =", x, " estimate =", estimate_derivative(take_square, x), " expected 2x =", 2 * x)

print("Using take_square_lambda (lambda):")
for x in [0, 1, 2, 3, 5, -4]:
    print("  x =", x, " estimate =", estimate_derivative(take_square_lambda, x), " expected 2x =", 2 * x)

# A lambda can also be written directly inside the function call
print("Inline lambda at x = 7:", estimate_derivative(lambda x: x ** 2, 7))
