##  Justin Hamilton
##  Lab05ver2-Emoticon.py
##  

import random

def smiley():
    i = 0
    while i < 5:
        #welcome screen
        print()
        input("\033[1;32;40m Press enter to generate emoticon.. ")
        print()

        eyes = [":", ";", "$"]
        nose = ["-", "=", "+"]
        mouth = ["{", "}", "/"]
        eyes = random.choice(eyes)
        nose = random.choice(nose)
        mouth = random.choice(mouth)
        print(eyes + nose + mouth)
        print()
        i += 1
smiley()