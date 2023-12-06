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
  part_number = False

  # Iterate through the rows of the schematic
  for row_index, row in enumerate(engine_schematic):
    # Iterate through the columns of each row
    for col_index, col in enumerate(row):

      print("Evaluating:", col)

      # If the character at that column is a digit, and it's the first time we're seeing a digit set,
      if col.isdigit() and not distinct_number:

        # Update the distinct number flag to show we're starting a new analysis of a number
        distinct_number = True
        # Also flag it with a Boolean that will update to True if it's found to be a valid part number
        part_number = False
        # Then start a container string to concatenate all the digits
        number_string = ""

        ### VALID PART NUMBER CHECKS
        if col_index > 0:
          ## CHECK LEFT
          if not row[col_index-1].isdigit() and not row[col_index-1] == ".":
            part_number = True
        if col_index < 139:
          ## CHECK RIGHT
          if not row[col_index+1].isdigit() and not row[col_index+1] == ".":
            part_number = True

        if row_index > 0:
          ## CHECK ABOVE-LEFT
          if col_index > 0:
            if not engine_schematic[row_index-1][col_index-1].isdigit() and not engine_schematic[row_index-1][col_index-1] == ".":
              part_number = True
          ## CHECK ABOVE
          if not engine_schematic[row_index-1][col_index].isdigit() and not engine_schematic[row_index-1][col_index] == ".":
            part_number = True
          ## CHECK ABOVE-RIGHT
          if col_index < 139:
            if not engine_schematic[row_index-1][col_index+1].isdigit() and not engine_schematic[row_index-1][col_index+1] == ".":
              part_number = True
        
        if row_index < 139:
          ## CHECK BOTTOM-LEFT
          if col_index > 0:
            if not engine_schematic[row_index+1][col_index-1].isdigit() and not engine_schematic[row_index+1][col_index-1] == ".":
              part_number = True
          ## CHECK BOTTOM
          if not engine_schematic[row_index+1][col_index].isdigit() and not engine_schematic[row_index+1][col_index] == ".":
            part_number = True
          ## CHECK BOTTOM-RIGHT
          if col_index < 139:
            if not engine_schematic[row_index+1][col_index+1].isdigit() and not engine_schematic[row_index+1][col_index+1] == ".":
              part_number = True
      
        ## Post-checks
        if part_number == True:
          # If it was found to be a valid part number, add the digit to the container string
          number_string += col

          # If the next item in the row isn't a digit, we're done. 
          # Check the digit after it to see if we're at the end of the number
          if col_index < 139:
            # Cast the number string to int and add it to the sum
            if not engine_schematic[row_index][col_index+1].isdigit():
              final_number = int(number_string)
              sum += final_number
              # Set the "distinct number" flag back to False
              distinct_number = False
              # Set the "part number" flag back to False
              part_number = False

  print("The sum of all part numbers is:", sum)

main()