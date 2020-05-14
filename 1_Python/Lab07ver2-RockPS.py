#   Justin Hamilton
#   Lab07ver2-RockPS.py
#   2020-03-21
from random import randint
def game():
    play = True
    #loop for continuous play
    while play == True:
        #create a list of play choices
        c = ["rock", "paper", "scissors"]

        #assign random computer choice
        comp = c[randint(0,2)]


        #input for player choice
        pl_c = input("rock, paper, or scissors? \n")

        if pl_c == comp:
            print("COMPUTER CHOICE IS " + comp)
            print("TIE \n")
        elif (pl_c == "rock") and (comp == "paper"):
            print("COMPUTER CHOICE IS " + comp)
            print("COMPUTER WIN \n")
        elif (pl_c == "rock") and (comp == "scissors"):
            print("COMPUTER CHOICE IS " + comp)
            print("YOU WIN \n")
        elif (pl_c == "paper") and (comp == "rock"):
            print("COMPUTER CHOICE IS " + comp)
        elif (pl_c == "scissors") and (comp == "paper"):
            print("COMPUTER CHOICE IS " + comp)
            print("YOU WIN \n")
        elif (pl_c == "scissors") and (comp == "rock"):
            print("COMPUTER CHOICE IS " + comp)
            print("COMPUTER WIN")
        else:
            print("COMPUTER CHOICE IS " + comp)
            print("COMPUTER WIN \n")
            break
        restart = input("Enter 'y' to restart game: \n")

    if restart == 'y' : 
        play = True
    else:
        play = False
game()