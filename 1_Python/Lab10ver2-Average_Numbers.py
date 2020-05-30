#   Justin Hamilton
#   Lab10ver2-Average_Numbers.py
#   2020-03-21

def avg_list():
    list = []
    i = 0
    avg = 0
    length = int(input("How many numbers in list: \n"))
    while i < length:
        x = int(input("Enter number for list: \n"))
        list.append(x)
        i += 1
    else:
        avg = sum(list)/len(list)
        print(f'Average is =', avg)
avg_list()