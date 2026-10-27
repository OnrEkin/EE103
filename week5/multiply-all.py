# Recap Part 1 - Multiply all numbers in a range (for loop, while loop, sanity check)

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

# ---- Multiply-all-1: for loop ----
result_for = 1                      # start at 1, because 1 is neutral for multiplication
for i in range(start, end + 1):     # end + 1 so that 'end' itself is included
    result_for = result_for * i
print("Result with for loop:  ", result_for)

# ---- Multiply-all-2: while loop ----
result_while = 1
i = start                           # we manage the counter ourselves
while i <= end:
    result_while = result_while * i
    i = i + 1                       # forgetting this line = infinite loop
print("Result with while loop:", result_while)

# ---- Sanity check ----
if result_for == result_while:
    print("results are same")
else:
    print("results are different")
