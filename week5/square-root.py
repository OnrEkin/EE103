# Task Part 1 - Approximate square root with guess & check (exhaustive enumeration)

x = float(input("Enter a number to find its square root: "))

epsilon = 0.01          # acceptable error
num_guesses = 0
guess = 0.0
increment = 0.0001      # try 0.00001 for inputs like 12345 / 54321 (slower but safer)

# Keep going while we are NOT close enough,
# but stop if guess^2 already passed x (we overshot -> avoid infinite loop)
while abs(guess**2 - x) >= epsilon and guess**2 <= x:
    guess = guess + increment
    num_guesses = num_guesses + 1
    # Debug print (every 1000 is too noisy for big inputs, so every 100000 here)
    if num_guesses % 100000 == 0:
        print("Current guess =", guess)

print("Number of guesses =", num_guesses)
if abs(guess**2 - x) >= epsilon:
    print("Failed to find the square root of", x, "(overshot it)")
else:
    print(guess, "is close to the square root of", x)
