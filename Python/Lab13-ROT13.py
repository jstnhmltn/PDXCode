
eng = "abcdefghijklmnopqrstuvwxyz"
rot = "nopqrstuvwxyzabcdefghijklm"

trans = str.maketrans(eng, rot)

str = input("Enter a string \n")

print (str.translate(trans))