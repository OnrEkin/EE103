# Tuples: Swap variables. Aim: x = 2 & y = 1

# 1) x = y then y = x
x = 1
y = 2
x = y   # x becomes 2, the old value 1 is lost
y = x   # y becomes x, which is already 2
print("1) x = y; y = x       ->  x =", x, " y =", y, " (does NOT work, both are 2)")

# 2) Use a temporary variable
x = 1
y = 2
temp = x   # save the old x
x = y
y = temp
print("2) with temp          ->  x =", x, " y =", y, " (works)")

# 3) Tuple swap: the right side (y, x) is built first, then unpacked into x and y
x = 1
y = 2
(x, y) = (y, x)
print("3) (x, y) = (y, x)    ->  x =", x, " y =", y, " (works)")
