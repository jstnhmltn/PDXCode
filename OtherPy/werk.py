def convert_to_c(temp_input):
  return ((9 / 5) * temp_input) + 32

def convert_to_f(temp_input):
  return (5 / 9) * (temp_input - 32)

def main():
  
  temp_input = float(input('enter a temperature: '))
  convert_from_unit = input('enter a unit: ')
  convert_to_unit = input('enter a unit to convert to: ')
  converted_temp = ''

  if convert_to_unit in ('c', 'C'):
    converted_temp = convert_to_f(temp_input)
  elif convert_to_unit in ('f', 'F'):
    converted_temp = convert_to_c(temp_input)
  else:
    print('no temp entered')
  
  print(converted_temp)

main()