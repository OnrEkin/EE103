# Recap Part 5 - Binary conversion of 0.1 with an acceptable error

x = 0.1
epsilon = 0.00001

f = x
binary = "0."
result = 0.0        # decimal value of the bits we have found so far
place = 0.5         # value of the current bit position: 1/2, 1/4, 1/8, ...

while abs(result - x) >= epsilon:
    f = f * 2
    bit = int(f)
    f = f - bit
    binary = binary + str(bit)
    result = result + bit * place   # add this bit's value to the result
    place = place / 2               # next position is worth half as much

print("Approximate binary of", x, ":", binary)
print("Its decimal value         :", result)
print("Error                     :", abs(result - x))
