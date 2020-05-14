##  Justin Hamilton
##  Lab03-Grading.py
##  2020-03-21
##  -added function

def grader():
    #welcome screen
    print("Welcome, What is your name? ")
    name = input()
    print()

    #user prompt
    num = int(input("What is your numeric grade, " + name + "? "))

    if num > 100:
        print("A+")
    elif num > 89:
        print("A")
    elif num > 79:
        print("B")
    elif num > 69:
        print("C")
    elif num > 59:
        print("D")
    elif num > 0:
        print("F")
    else:
        print("TRY AGAIN")
grader()