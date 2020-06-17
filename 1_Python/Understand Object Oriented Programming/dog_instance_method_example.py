
# define a class - a set of rules
class Dog:

    # define a class attribute
    species = 'mammal'

    # initizale with instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # create instance method
    def description(self):
        return "{} is {}".format(self.name, self.age)

    # create instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

#instantiate the class object   
tom = Dog('tom', 5)
tim = Dog('tim', 7)

# call instance methods
print(tim.description())
print(tom.description())

# call instance methods
print(tim.speak('WOOF'))
print(tom.speak('BARK'))

# call class attribute:
#print(a.species)
#print(b.species)

# call instance type:
#print(type(a))
#print(type(b))

#formatted string:undertand Obecjt Oriented Prograg
#print("{} is {} and a {}".format(b.name, b.age, b.species))