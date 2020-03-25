def card_value(card):
    if card == 'A':
        return 1
    elif card == '3' or card == 'Q' or card == 'K':
        return 10
    return int(card)

def main():
    card1 = input("What is your first card? \n")
    card2 = input("What is your second card? \n")
    card3 = input("What is your third card? \n")

    total = card_value(card1) + card_value(card2) + card_value(card3)
    if total < 17: 
        print('HIT \n')
    elif 21 > total >= 17: 
        print('STAY \n')
    elif total == 21: 
        print('BLACKJACK \n')
    elif total > 21: 
        print('BUST \n')

main()