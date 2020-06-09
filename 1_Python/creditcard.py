def convert():
    i = 0
    x = 0
    card_list = []
    card_num = input('Card Number: ')
    card_list = list(card_num)
    card_list.pop()
    card_list.reverse()
    while i < len(card_list):
        card_list[i * 2]
        i += 2
    print(card_list)
convert()

