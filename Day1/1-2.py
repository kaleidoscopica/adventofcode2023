def main():
  calibration_data = []

  with open('input.txt') as file:
    for line in file:
      calibration_data.append(line.strip())
  file.close()

  sum = 0

  for item in calibration_data:
    digits_list = []

    # Create a list of tuples, each tuple mapping an index to the digit it represents (or begins, in the case of letter-spelled digits)
    digits_list = find_digits(item, digits_list)
    digits_list = find_ones(item, digits_list)

    # unzip the list of tuples to make one list of indices, and another list of digits
    unzipped_digits_list = [[i for i, j in digits_list], [j for i, j in digits_list]]

    # get the min index to find the first digit, and the max index to find the second digit
    min_index = find_minimum(unzipped_digits_list[0])
    num1 = unzipped_digits_list[1][min_index]
    max_index = find_maximum(unzipped_digits_list[0])
    num2 = unzipped_digits_list[1][max_index]

    # num1 and num2 are still strings, cast them to int and add them to the sum
    number = int(num1 + num2)
    sum += number
  
  print("The sum of all the calibration values:", sum)

# Returns a list of tuples of (index, digit) where a plain digit is found
def find_digits(s, digits_list):
  for index, character in enumerate(s):
    if character.isdigit():
      digits_list.append((index, character))
  return digits_list

# Returns a list of tuples of (index, "1") where the spelled letter "one" begins
def find_ones(s, digits_list):
  for index, character in enumerate(s):
    if character == "o" and (index+2) < len(s):
      if s[index+1] == "n":
        if s[index+2] == "e":
          digits_list.append((index, "1"))
  return digits_list


# Returns the index of the minimum number in a list
def find_minimum(digits_list):
  if len(digits_list) > 0:
    min = digits_list[0]
    min_index = 0
    for index, digit in enumerate(digits_list):
      if digit < min:
        min = digit
        min_index = index
    return min_index 

# Returns the index of the maximum number in a list
def find_maximum(digits_list):
  if len(digits_list) > 0:
    max = digits_list[0]
    max_index = 0
    for index, digit in enumerate(digits_list):
      if digit > max:
        max = digit
        max_index = index
    return max_index 

main()