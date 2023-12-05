def main():
  calibration_data = []

  with open('input.txt') as file:
    for line in file:
      calibration_data.append(line.strip())
  file.close()

  sum = 0

  for item in calibration_data:
    digits_list = []

### Tbd, functions

main()