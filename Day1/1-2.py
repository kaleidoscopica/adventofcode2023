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

main()