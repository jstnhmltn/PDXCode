#create list of 26 entries
alphabet = 'abcdefghijklmnopqrstuvwxyz'

#user prompt for string and key as an integer
string_input = input('Enter your string: \n')
key = int(input('Enter key length: \n'))

#this is variable represents the length of the string
n = len(string_input)

#defining variable for output string that has no current value
string_output =  " "

#loops through each letter, returns starting and finishing loation
for i in range(n):
    character = string_input[i]
    location = alphabet.find(character)

    new_location = (location + key) % 26 
    print(character, location, new_location)
    string_output += alphabet[new_location]
print(string_output)
