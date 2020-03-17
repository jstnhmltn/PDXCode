##cards = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

lib = ['A':1, 'J':10, 'Q':10, 'K':10]
a = input("What is your first card? \n")
b = input("What is your second card? \n")
c = input("What is your third card? \n")
sum = a+b+c

if sum < 17: 
    print(f'HIT \n')
elif 21 > sum >= 17: 
    print(f'STAY \n')
elif sum == 21: 
    print(f'BLACKJACK \n')
elif sum > 21: 
    print(f'BUST \n')
