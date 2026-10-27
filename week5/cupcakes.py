# Recap Part 1 - Guess & Check with nested loops (cupcake problem)

TOTAL = 28
found = False

for david in range(0, TOTAL + 1):
    for emma in range(0, TOTAL + 1):
        for frank in range(0, TOTAL + 1):
            # CHECK all three conditions at the same time
            if emma == david + 3 and frank == 3 * david and david + emma + frank == TOTAL:
                print("David packed", david, "cupcakes!")
                print("Emma packed", emma, "cupcakes!")
                print("Frank packed", frank, "cupcakes!")
                found = True
                break           # leaves the frank loop
        if found:
            break               # leaves the emma loop
    if found:
        break                   # leaves the david loop

if not found:
    print("No solution found.")
