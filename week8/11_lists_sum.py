# Lists: Compute the sum of elements in a list

# 1)
total = 0
dummy_range = range(10)

# 2) Convert the range to a list
dummy_list_1 = list(dummy_range)

# 3) Build the same list by appending
dummy_list_2 = []
for i in range(10):
    dummy_list_2.append(i)

# 4) Show they are equal
print("dummy_list_1 =", dummy_list_1)
print("dummy_list_2 =", dummy_list_2)
print("dummy_list_1 == dummy_list_2:", dummy_list_1 == dummy_list_2)   # True

# 5) Sum the elements
for element in dummy_list_1:
    total += element
print("total =", total)               # 45
print("check with sum():", sum(dummy_list_1))
