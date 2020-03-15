# The following code is broken in at least six ways. It is your job to fix it. 
# The program is supposed to take a user entered temperature value, a user entered 
# temperature unit, and a unit to convert to, then output the appropriate 
# conversion. The conversions should be correct, I checked them quickly, but 
# I'm fairly sure they're right. At any rate, the main point is to figure out 
# how the code is broken, and fix it.

# We'll use this code in another exercise.
temp = 0
def convert_to_c(temp):
   print((9 / 5) * (temp + 32))

def convert_to_f(temp):
   print((5 / 9) * (temp - 32))

def main(temp):
    temp = float(input('enter a temperature: '))
    unit = input('enter a unit: ')
    converted_temp = str(input('enter a unit to convert to: '))

    if unit in ('c', 'C'):
        converted_temp = convert_to_f(temp)
    elif unit in ('f', 'F'):
        converted_temp == convert_to_c(temp)
    else:
        print('no temp entered')

main(temp)