#Justin Hamilton
#Lab20-CreditCardValidation.py
#Still working on this one

def main():
    i = 0
    #input for credit card number
    card_number = str(input("Enter credit card number: \n"))
    #converts each character in string to list
    list_nums = list(card_number)
    #removes last item in list
    list_nums.pop()
    #print current results
    print(list_nums)
    #reverses list
    list_nums.reverse()
    #print current results
    print(list_nums)
    #create for loop to add double each every other item in list
    for i in range(0, len(list_nums)):
        list_nums[i] * 2
        i += 2
    print(list_nums)

main()