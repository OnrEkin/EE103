# Recap Part 4 - Binary representation of a number with a fractional part (e.g. 13.375)

number = float(input("Enter a positive number (e.g. 13.375): "))

int_part = int(number)          # 13
frac_part = number - int_part   # 0.375

# ---- Integer part: repeated division by 2 (same as binary-integers.py) ----
if int_part == 0:
    int_binary = "0"
else:
    int_binary = ""
    n = int_part
    while n > 0:
        int_binary = str(n % 2) + int_binary
        n = n // 2

# ---- Fraction part: repeated multiplication by 2 ----
frac_binary = ""
f = frac_part
max_digits = 32                 # safety limit, some fractions never end (see Part 5)
while f > 0 and len(frac_binary) < max_digits:
    f = f * 2
    bit = int(f)                # integer part (0 or 1) is the next bit
    frac_binary = frac_binary + str(bit)   # bits are added to the RIGHT this time
    f = f - bit                 # keep only the fractional part

if frac_binary == "":
    frac_binary = "0"

print("Binary representation of", number, "is", int_binary + "." + frac_binary)
