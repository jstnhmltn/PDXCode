#Justin Hamilton
#Lab13-ROT13.py
# 
eng = "abcdefghijklmnopqrstuvwxyz"
rot = "nopqrstuvwxyzabcdefghijklm"

trans = str.maketrans(eng, rot)

str = input("Enter a string \n")

print (str.translate(trans))