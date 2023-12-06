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
  distinct_number = False
  valid_part_num = False

  # Iterate through the rows of the schematic
  for row_index, row in enumerate(engine_schematic):
    # Iterate through the columns of each row
    for col_index, col in enumerate(row):

      # If the character at that column is a digit, and it's the first time we're seeing a digit set,
      if col.isdigit() and not distinct_number:

        # Update the distinct number flag to show we're starting a new analysis of a number
        distinct_number = True
        # Also flag it with a Boolean that will update to True if it's found to be a valid part number
        valid_part_num = False
        # Then start a container string to concatenate all the digits
        number_string = col

        valid_part_num = find_nearby_symbols(engine_schematic, row_index, col_index)

      # If the character at that column is a digit, and it's NOT the first time we're seeing a digit set,
      elif col.isdigit() and distinct_number:
        # Go ahead and add that digit to the number string
        number_string += col
        # Then run through all the same checks, if it wasn't already found to be valid
        # (since this will overwrite the value otherwise)
        if not valid_part_num:
          valid_part_num = find_nearby_symbols(engine_schematic, row_index, col_index)

      # Do these whether it's a distinct number or not
      if col.isdigit():
        if col_index < 139:
          # If there's not another digit after this, do post-checks
          if not engine_schematic[row_index][col_index+1].isdigit():
            ## Post-checks
            if valid_part_num == True:
              # If the next item in the row isn't a digit, we're done. 
              # Compute the final number
              final_number = int(number_string)
              sum += final_number
              # Set the "distinct number" flag back to False
              distinct_number = False
              # Set the "valid part number" flag back to False
              valid_part_num = False
            else:
              # clear the number string
              number_string = ""
        
        # Special case for where a number ends at the end of the row - don't check for next digit
        elif col_index == 139:
          ## Post-checks
          if valid_part_num == True:
            # Compute the final number
            final_number = int(number_string)
            sum += final_number
            # Set the "distinct number" flag back to False
            distinct_number = False
            # Set the "valid part number" flag back to False
            valid_part_num = False
          else:
            # clear the number string
            number_string = ""

  print("The sum of all part numbers is:", sum)

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