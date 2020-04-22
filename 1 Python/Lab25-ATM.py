#Justin Hamilton
#Lab25-ATM.py
#2020-04-02
#Comments and code written during lecture on Classes 
#still working

class ATM: #defining a class named ATM. will need first function as __init__ with self as first argument for all functions
    def __init__(self):  #takes in addtl args. Always need (self)..  Will need to define each object 
        pass
    def check_balance(self): # Using args from __init__. will check the balance, which in this case will be set
        pass
    def deposit(self, amount):  #Using args from __init__. Will prepare and deposit an inputed amount.
        pass
    def check_withdrawal(self, amount):
        pass
    def withdrawal(self, amount): #using args from __init__ will allow user to conduct a withdrawal and return remaining balance
        pass
    def calc_interest(): 
        pass
    
my_atm =ATM() #args to ATM() should match  those passed into __init__. except ???

print(my_atm.check_balance()) #
print(my_atm.deposit(34.00)) #

