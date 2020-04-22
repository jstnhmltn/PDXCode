##  Justin Hamilton
##  Lab04-Magic8.py
##  2020-03-21
##  - added function

import random
def magic():
    ##Print a welcome screen to the user.
    print("Welcome to the MAGIC 8 BALL GAME")

    ##Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
    input("Enter a 'yes' or 'no' question \n")

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
        "Very doubtful"
        ]

    choice = answers[random.randint(0,19)]
    ##Display the result of the 8-ball.
    print(choice)
mad_lib()


