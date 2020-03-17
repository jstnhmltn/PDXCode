from random import randint

#create a list of play choices
c = ["rock", "paper", "scissors"]

#assign random computer choice
comp = c[randint(0,2)]

play = True
#loop for continuous play
while play == True:

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
        print("YOU WIN \n")
    else:
        print("COMPUTER CHOICE IS " + comp)
        print("COMPUTER WIN \n")
        break
    restart = input("PLAY AGAIN? \n")
if restart == 'y' or 'Y': 
    play = True
elif restart == 'n' or 'N':
    play = False
