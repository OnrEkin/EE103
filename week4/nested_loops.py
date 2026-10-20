total_tickets = 10

found = False
for alyssa in range(total_tickets + 1):
    for ben in range(total_tickets + 1):
        for cindy in range(total_tickets + 1):
            if (alyssa + ben + cindy == total_tickets) and (ben == alyssa - 2) and (cindy == 2 * alyssa):
                print(f"Alyssa {alyssa} bilet satmıştır.")
                print(f"(Ben: {ben}, Cindy: {cindy})")
                found = True
                break
        if found:
            break
    if found:
        break