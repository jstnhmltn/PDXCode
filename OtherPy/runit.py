is_male = True 
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif is_tall and not(is_tall):
    print("You are a short male")
else:
    print("You are neither male nor tall or both")