from secret import secretNum
chocolate = 0
while chocolate<5:
    chocolate=chocolate+1
    guess=int(input("Guess the secret number bro"))
    if guess < secretNum:
        print("Too low!",5-chocolate,"guess(es) left")
    elif guess > secretNum:
        print("Too high!",5-chocolate,"guess(es) left")
    else:
        print("Correct! The guess is the same as the secret!")
        exit()
while True:
    print("Get Dunked Onnnnn!")
