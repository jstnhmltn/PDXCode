#created function that returns the a string in reverse
def reverse(string): 
    string = string[::-1] 
    return string 

s = input("Enter a string: \n")
  
print ("Original string: ",end="") 
print (s) 
  
print ("Reversed string: ",end="") 
print (reverse(s)) 

#compares original string and reverse function call of the string
if s != reverse(s):
    print("Not a palindrome")
elif s == reverse(s):
    print("Palindrome!")
else:
    print("Invalid")
