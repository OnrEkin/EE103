# Lists: Enumerate

# 1) List comprehension
dummy_list = [x ** 2 for x in range(10)]
print("dummy_list =", dummy_list)

# 2) enumerate gives (index, value) pairs
for index, value in enumerate(dummy_list):
    print(index)
    print(value)
