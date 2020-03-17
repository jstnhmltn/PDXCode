##Random Emoticon Generator

import random

#welcome screen
print()
input("Press enter to generate emoticon.. ")
print()

eyes = [":", ";", "$"]
nose = ["-", "=", "+"]
mouth = ["{", "}", "/"]
eyes = random.choice(eyes)
nose = random.choice(nose)
mouth = random.choice(mouth)
print(eyes + nose + mouth)
