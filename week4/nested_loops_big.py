total_tickets = 1000

for alyssa in range(total_tickets + 1):
    for ben in range(total_tickets + 1):
        for cindy in range(total_tickets + 1):
            if (alyssa + ben + cindy == total_tickets) and (ben == alyssa - 20) and (cindy == 2 * alyssa):
                print(f"Alyssa: {alyssa}")