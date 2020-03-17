list1 = []
i = 0
avg = 0
length = int(input("How many numbers in list: \n"))
while i < length:
    x = int(input("Enter number for list: \n"))
    list1.append(x)
    i += 1
else:
    avg = sum(list1)/len(list1)
    print(f'Average is =', avg)