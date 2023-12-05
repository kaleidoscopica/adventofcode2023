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
    digits_list = find_twos(item, digits_list)
    digits_list = find_threes(item, digits_list)
    digits_list = find_fours(item, digits_list)
    digits_list = find_fives(item, digits_list)
    digits_list = find_sixes(item, digits_list)
    digits_list = find_sevens(item, digits_list)
    digits_list = find_eights(item, digits_list)
    digits_list = find_nines(item, digits_list)

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

# Returns a list of tuples of (index, "2") where the spelled letter "two" begins
def find_twos(s, digits_list):
  for index, character in enumerate(s):
    if character == "t" and (index+2) < len(s):
      if s[index+1] == "w":
        if s[index+2] == "o":
          digits_list.append((index, "2"))
  return digits_list

# Returns a list of tuples of (index, "3") where the spelled letter "three" begins
def find_threes(s, digits_list):
  for index, character in enumerate(s):
    if character == "t" and (index+4) < len(s):
      if s[index+1] == "h":
        if s[index+2] == "r":
          if s[index+3] == "e":
            if s[index+4] == "e":
              digits_list.append((index, "3"))
  return digits_list

# Returns a list of tuples of (index, "4") where the spelled letter "four" begins
def find_fours(s, digits_list):
  for index, character in enumerate(s):
    if character == "f" and (index+3) < len(s):
      if s[index+1] == "o":
        if s[index+2] == "u":
          if s[index+3] == "r":
            digits_list.append((index, "4"))
  return digits_list

# Returns a list of tuples of (index, "5") where the spelled letter "five" begins
def find_fives(s, digits_list):
  for index, character in enumerate(s):
    if character == "f" and (index+3) < len(s):
      if s[index+1] == "i":
        if s[index+2] == "v":
          if s[index+3] == "e":
            digits_list.append((index, "5"))
  return digits_list

# Returns a list of tuples of (index, "6") where the spelled letter "six" begins
def find_sixes(s, digits_list):
  for index, character in enumerate(s):
    if character == "s" and (index+2) < len(s):
      if s[index+1] == "i":
        if s[index+2] == "x":
          digits_list.append((index, "6"))
  return digits_list

# Returns a list of tuples of (index, "7") where the spelled letter "seven" begins
def find_sevens(s, digits_list):
  for index, character in enumerate(s):
    if character == "s" and (index+4) < len(s):
      if s[index+1] == "e":
        if s[index+2] == "v":
          if s[index+3] == "e":
            if s[index+4] == "n":
              digits_list.append((index, "7"))
  return digits_list

# Returns a list of tuples of (index, "8") where the spelled letter "eight" begins
def find_eights(s, digits_list):
  for index, character in enumerate(s):
    if character == "e" and (index+4) < len(s):
      if s[index+1] == "i":
        if s[index+2] == "g":
          if s[index+3] == "h":
            if s[index+4] == "t":
              digits_list.append((index, "8"))
  return digits_list

# Returns a list of tuples of (index, "9") where the spelled letter "nine" begins
def find_nines(s, digits_list):
  for index, character in enumerate(s):
    if character == "n" and (index+3) < len(s):
      if s[index+1] == "i":
        if s[index+2] == "n":
          if s[index+3] == "e":
            digits_list.append((index, "9"))
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