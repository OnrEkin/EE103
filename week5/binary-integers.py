# Recap Part 2 - Binary representation of a non-negative integer

number = int(input("Enter a non-negative integer: "))

if number == 0:
    binary = "0"
else:
    binary = ""
    n = number
    while n > 0:
        remainder = n % 2               # remainder of division by 2 -> next bit
        binary = str(remainder) + binary  # put it on the LEFT (first remainder is the last bit)
        n = n // 2                      # integer division

print("Binary representation of", number, "is", binary)
