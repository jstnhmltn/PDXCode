# 2020-03-20
# Lab02ver2-Madlib.py
# -added the use of function 
# -added a while loop to ask if user wants to continue play

def go():
    name = input("What is your name? \n")
    while True:
        adj1 = input("Give an adjective. ")
        noun1 = input("Now, give a noun. ")
        adj2 = input("Give another adjective: ")
        ant = input("Now, enter how you feel: ")
        car = input("Enter a type of transportation: ")
        print()
        print(f"This is an amber alert for " + name.upper() + ",")
        print(f" " + "whom has a very " + adj1.upper() + " and " + adj2.upper())
        print(f" " + noun1.upper() + ". " + name.upper() + " was last seen driving a " + car.upper() +", ")
        print(f"and now they are " + ant.upper() + ".")
        print()
        keep_going = input("PLAY AGAIN = [y]\n QUIT = [n] \n")
        if keep_going == 'n':
            print(f"GOODBYE, " + name.upper() + "!")
            break
        else:
            continue
go()