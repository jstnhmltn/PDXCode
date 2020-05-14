#   Justin Hamilton
#   brokencode.py
#   2020-03-21

def convert_to_c(temp=0):
   print((temp * 9) / 5 + 32)

def convert_to_f(temp=0):
   print((temp - 32) * 5 / 9)

def main(a):
    a = temp
    temp = float(input('enter a temperature: '))
    unit = input('enter a unit: ')
    converted_temp = str(input('enter a unit to convert to: '))

    if unit in ('c', 'C'):
        converted_temp = convert_to_c(temp)
    elif unit in ('f', 'F'):
        converted_temp = convert_to_f(temp)
    else:
        print('no temp entered')  

main(a)