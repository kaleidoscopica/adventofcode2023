def main():
  engine_schematic = []

  with open('input.txt') as file:
    for line in file:
      line = line.strip()
      row = []
      for character in line:
        row.append(character)
      engine_schematic.append(row)
  file.close()

  sum = 0

  # Iterate through the rows of the schematic
  for row_index, row in enumerate(engine_schematic):
    # Iterate through the columns of each row
    for col_index, col in enumerate(row):

      # If the character at that column is a *,
      if col == '*':
        sum += 1

  print("The sum of all the gear ratios is:", sum)

# Checks the surrounding area of a digit for nearby special characters
# Returns True if special characters were found, otherwise, returns False
def find_nearby_symbols(engine_schematic, row_index, col_index):
  valid_part_num = False

  if col_index > 0:
    ## CHECK LEFT
    if not engine_schematic[row_index][col_index-1].isdigit() and not engine_schematic[row_index][col_index-1] == ".":
      valid_part_num = True
  if col_index < 139:
    ## CHECK RIGHT
    if not engine_schematic[row_index][col_index+1].isdigit() and not engine_schematic[row_index][col_index+1] == ".":
      valid_part_num = True

  if row_index > 0:
    ## CHECK ABOVE-LEFT
    if col_index > 0:
      if not engine_schematic[row_index-1][col_index-1].isdigit() and not engine_schematic[row_index-1][col_index-1] == ".":
        valid_part_num = True
    ## CHECK ABOVE
    if not engine_schematic[row_index-1][col_index].isdigit() and not engine_schematic[row_index-1][col_index] == ".":
      valid_part_num = True
    ## CHECK ABOVE-RIGHT
    if col_index < 139:
      if not engine_schematic[row_index-1][col_index+1].isdigit() and not engine_schematic[row_index-1][col_index+1] == ".":
        valid_part_num = True
  
  if row_index < 139:
    ## CHECK BOTTOM-LEFT
    if col_index > 0:
      if not engine_schematic[row_index+1][col_index-1].isdigit() and not engine_schematic[row_index+1][col_index-1] == ".":
        valid_part_num = True
    ## CHECK BOTTOM
    if not engine_schematic[row_index+1][col_index].isdigit() and not engine_schematic[row_index+1][col_index] == ".":
      valid_part_num = True
    ## CHECK BOTTOM-RIGHT
    if col_index < 139:
      if not engine_schematic[row_index+1][col_index+1].isdigit() and not engine_schematic[row_index+1][col_index+1] == ".":
        valid_part_num = True
        # Check the digit after it to see if we're at the end of the number

  return valid_part_num

main()