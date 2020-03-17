def add(a, b):
    return a + b
def substract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

while True:
    choice = input("What is the operation you'd like to perform? \n")

    num1 = int(input("What is the first number? \n"))
    num2 = int(input("What is the second number? \n"))

    if choice == '+':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '-':
        print(num1, "-", num2, "=", substract(num1, num2))
    elif choice == '*':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '/':
        print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == 'done':
        print("goodbye!")
        break
    else:
        print("INVALID")
    