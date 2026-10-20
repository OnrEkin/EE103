total_tickets = 1000

for alyssa in range(total_tickets + 1):
    ben = alyssa - 20
    cindy = 2 * alyssa
    
    if alyssa + ben + cindy == total_tickets:
        print(f"Alyssa {alyssa} bilet satmıştır.")
        print(f"(Ben: {ben}, Cindy: {cindy})")
        break