##  Justin Hamilton
##  Lab02-Madlib.py
##  2020-03-20
##  - uses function

def main():
    adj1 = input("Give an adjective. ")

    noun1 = input("Now, give a noun. ")

    adj2 = input("Give another adjective. ")

    ant = input("Now, give an antonym for alive. ")

    car = input("Give a model of car. ")

    noun2 = input("Now, give a noun. ")

    print()
    print(f"This is an amber alert for a " + noun1 + ",")
    print(f" " + "whom is a very " + adj1 + " and " + adj2)
    print(f" " + noun2 + ". Last seen driving a " + car +", ")
    print(f"and now they are " + ant + ".")
    print()
main()