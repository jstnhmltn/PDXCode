##  Justin Hamilton
##  Lab04ver2-Magic8.py
##  2020-03-21
##  Uses random module and function to print random 
#   ansewrs to a yes or no question

import random
def magic():
    again = "yes"
    while again == "yes":
        ##Print a welcome screen to the user.
        print("\033[1;32;40mMAGIC 8 BALL GAME")

        ##Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
        input("Enter a YES or NO question: \n")

        ##Use the random module's random.choice() to choose a prediction.
        answers = ["It is certain", "Without a doubt", "It is decidedly so", "Yes definitely",
        "You may rely on it",
        "As I see it, yes",
        "Most likely",
        "Outlook good",
        "Yes",
        "Signs point to yes",
        "Reply hazy try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful"]

        choice = answers[random.randint(0,19)]

        ##Display the result of the 8-ball.
        print(choice)
        again = input("[y = play again] \n")
        if again == "":
            break
        else:
            again == "y"
magic()

