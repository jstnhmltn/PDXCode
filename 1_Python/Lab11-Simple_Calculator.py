def add(a, b):
    return a + b
def substract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
def quit():
    return exit()
num1 = int(input("What is the first number? \n"))
num2 = int(input("What is the second number? \n"))

while True:
    choice = input("What is the operation you'd like to perform? \n"
        "[Add: +]\n"
        "[Subtract: -]\n"
        "[Multiply: *]\n"
        "[Divide: /]\n")


    if choice == '+':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '-':
        print(num1, "-", num2, "=", substract(num1, num2))
    elif choice == '*':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '/':
        print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == ' ':
        print("INVALID")
        break
    else:
        print("goodbye!")
        break
    