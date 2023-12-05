def main():
  calibration_data = []

  with open('input.txt') as file:
    for line in file:
      calibration_data.append(line.strip())
  file.close()

  sum = 0

  for item in calibration_data:
    num1 = find_first_digit(item)
    num2 = find_second_digit(item)
    number = int(num1 + num2)
    sum += number
  
  print("The sum of all the calibration values:", sum)


# Returns the first digit found in a string
def find_first_digit(s):
  for character in s:
    if character.isdigit():
      return character

# Returns the second digit found in a string
def find_second_digit(s):
  for character in reversed(s):
    if character.isdigit():
      return character

main()