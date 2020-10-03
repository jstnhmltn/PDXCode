# Justin Hamilton
# October 3, 2020

# Find square values of each number list

# BEST PRACTICE
# O(1) runtime solution using map() to allow a function
# to return iterables on demand

# Write a function that returns the square root of number
def square(number):
    return number ** 2

# List is given
numbers = [1, 2, 3, 4, 5]

# Use map() to apply square() to numbers
squared = map(square, numbers)

print(list(squared))


# BRUTE FORCE
# O(n) runtime solution using for loop.
# Longer runtime to use explicit loop.
# Less efficient to store each new value after every iteration

# List is given
# numbers = [1, 2, 3, 4, 5]

# squared = []

# Find square value for each iteration
# for num in numbers:
#     squared.append(num ** 2)
    
# print(squared)