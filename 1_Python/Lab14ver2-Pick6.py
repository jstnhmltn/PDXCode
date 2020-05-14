import random
import time

def pick6():
    ticket = []
    for i in range(6):
        ticket.append(random.randint(1, 99))
    return ticket

def num_matches(winning, ticket):
    payout = [0, 4, 7, 100, 50000, 1000000, 25000000]
    matches = 0
    for i in range(len(ticket)):
        if winning[i] == ticket [i]:
            matches += 1

    if matches > 3:
        print(winning)
        print(ticket)
        print(f'WIN ${payout[matches]}')
    
    return payout[matches]

def play100k():
    winning = pick6()
    bal = 0
    roi = (bal - 2) / 2
    return roi

    for i in range(100000):
        ticket = pick6()
        payout = num_matches(winning, ticket)
        bal += payout
    print('Balance: $', bal)
    

def main():
    roi = (bal - 2) / 2
    start = time.time()
    for i in range(100):
        play100k()
    print(f'Return on Investment: {roi}')
    print(f'Finished 10,000,000 lotto calculations. '
        + f'Runtime {time.time() - start} seconds')
main()