#f(g,x) = g^2 - x we are looking for the root satisfying f(g,x) = 0
#nextguess = guess - f(guess)/f'(guess)

x = float(input("What x to find the square root of?"))
g = float(input("What guess to start with?"))

nextguess = g - (g**2 - x) / (2 * g)
print(nextguess)