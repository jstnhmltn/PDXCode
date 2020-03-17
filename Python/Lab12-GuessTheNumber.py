def guess():
    import random

    comp_choice = random.randint(1, 10)

    choice = int(input("WHAT NUBER DO YOU GUESS? \n"))

    if comp_choice == choice:
        print("CORRECT \n")
    else:
        print("INCORRECT \n")
guess()