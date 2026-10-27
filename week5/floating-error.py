# Recap Part 3 - Demonstrate floating point error

x = 0
for i in range(10):
    x = x + 0.1
    print("Step", i + 1, ": x =", x)

print()
print("Final x =", x)
print("x == 1.0 ?", x == 1.0)

# The safe way to compare floats: check if they are "close enough"
print("abs(x - 1.0) < 1e-9 ?", abs(x - 1.0) < 1e-9)
