# Mutability: Lists vs. Tuples

my_list = [1, 3, 5]
my_tuple = (1, 3, 5)

my_list[1] = 5
print("my_list after my_list[1] = 5:", my_list)   # [1, 5, 5]

try:
    my_tuple[1] = 5
except TypeError as error:
    print("my_tuple[1] = 5 -> TypeError:", error)
print("my_tuple is unchanged:", my_tuple)          # (1, 3, 5)

# Why: lists are MUTABLE, their elements can be changed after they are created.
# Tuples are IMMUTABLE, once created their elements cannot be changed.
# To "change" a tuple you have to create a new one:
my_tuple = my_tuple[:1] + (5,) + my_tuple[2:]
print("new tuple:", my_tuple)                      # (1, 5, 5)
