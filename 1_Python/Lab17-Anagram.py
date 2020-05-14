#created function that converts to lowercase, removes spaces, sorts letters
def anagram(string): 
    string = string.lower()
    string = string.replace(" ", "") 
    string = str(sorted(string))
    return string 

#getting strings from user
first = input("Enter a first string: \n")
second = input("Enter second string \n")
  

#compares strings through anagram function call
if anagram(first) != anagram(second):
    print("Not an anagram")
elif anagram(first) == anagram(second):
    print("ANAGRAM!")
else:
    print("Invalid")
