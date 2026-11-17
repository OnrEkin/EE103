# Tuples: Functions with variable number of arguments


# 1) First version
def mean_v1(*args):
    tot = 0
    for arg in args:
        tot += arg
    return tot / len(args)


print("mean_v1(4, 6, 8) =", mean_v1(4, 6, 8))            # 6.0
print("mean_v1(1, 2, 3, 4, 5) =", mean_v1(1, 2, 3, 4, 5))  # 3.0

# 2) mean_v1(1, 2, '3', 4, 5) gives:
#    TypeError: unsupported operand type(s) for +=: 'int' and 'str'
# Debugging: put a breakpoint on the 'tot += arg' line (or import pdb; pdb.set_trace())
# and check:  type(args) -> <class 'tuple'>,  args -> (1, 2, '3', 4, 5),  type(args[2]) -> <class 'str'>
# So *args collects all inputs into a tuple, and one element is a string.
try:
    mean_v1(1, 2, '3', 4, 5)
except TypeError as error:
    print("mean_v1(1, 2, '3', 4, 5) -> TypeError:", error)


# Fixed version: convert every argument to a number before adding
def mean(*args):
    print("[debug] type(args) =", type(args), " args =", args)
    tot = 0
    for arg in args:
        tot += float(arg)   # works for int, float and numeric strings like '3'
    return tot / len(args)


print("mean(4, 6, 8) =", mean(4, 6, 8))
print("mean(1, 2, 3, 4, 5) =", mean(1, 2, 3, 4, 5))
print("mean(1, 2, '3', 4, 5) =", mean(1, 2, '3', 4, 5))

# 3) One-element tuples need a comma
dummy1 = (3)    # just the integer 3 in parentheses
dummy2 = (3,)   # a tuple with one element
print("dummy1 =", dummy1, " type:", type(dummy1))   # <class 'int'>
print("dummy2 =", dummy2, " type:", type(dummy2))   # <class 'tuple'>
