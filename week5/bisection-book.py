# Task Part 2 - Bisection search: find the secret favorite page in a 148-page book

secret = int(input("Enter the secret favorite page (1-148): "))

low = 1
high = 148
num_guesses = 0

while low <= high:
    guess = (low + high) // 2           # always guess the middle of what's left
    num_guesses = num_guesses + 1
    print("Guess", num_guesses, ":", guess)

    if guess == secret:
        print("Found it! Page", guess, "in", num_guesses, "guesses.")
        break
    elif secret > guess:
        print("   hint: higher")
        low = guess + 1                 # throw away the lower half
    else:
        print("   hint: smaller")
        high = guess - 1                # throw away the upper half
