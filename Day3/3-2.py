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
        # Find its gear ratio
        # (If find_gear_ratio doesn't find exactly two adjacent parts, it just returns 0)
        gear_ratio = find_gear_ratio(engine_schematic, row_index, col_index)
        sum += gear_ratio

  print("The sum of all the gear ratios is:", sum) # not 175!


# Checks the surrounding area of an asterisk for nearby part numbers.
# If exactly two parts are found, returns their gear ratio,
# (The gear ratio is the result of multiplying them together),
# Otherwise returns 0
def find_gear_ratio(engine_schematic, row_index, col_index):
  number_string = ""
  number_list = []
  top_left = False
  top = False
  top_right = False
  bottom_left = False
  bottom = False
  bottom_right = False

  # Now we need to check potentially three units to the left of the *,
  # three units to the right of the *,
  # seven units above the *, and seven units below the *

  if col_index > 0:
    ## CHECK ONE LEFT
    if engine_schematic[row_index][col_index-1].isdigit():
      # Check the unit to the left of that one to see how big the number is
      if col_index > 1 and engine_schematic[row_index][col_index-2].isdigit():
        # Check the unit to the left of that one also
        if col_index > 2 and engine_schematic[row_index][col_index-3].isdigit():
          number_string = engine_schematic[row_index][col_index-3] + engine_schematic[row_index][col_index-2] + engine_schematic[row_index][col_index-1]
          number_list.append(int(number_string))
        elif col_index > 2:
          number_string = engine_schematic[row_index][col_index-2] + engine_schematic[row_index][col_index-1]
          number_list.append(int(number_string))
      elif col_index > 1:
        number_string = engine_schematic[row_index][col_index-1]
        number_list.append(int(number_string))

  if col_index < 139:
    ## CHECK ONE RIGHT
    if engine_schematic[row_index][col_index+1].isdigit():
      # Check the unit to the right of that one to see how big the number is
      if col_index < 138 and engine_schematic[row_index][col_index+2].isdigit():
        # Check the unit to the right of that one also
        if col_index < 137 and engine_schematic[row_index][col_index+3].isdigit():
          number_string = engine_schematic[row_index][col_index+1] + engine_schematic[row_index][col_index+2] + engine_schematic[row_index][col_index+3]
          number_list.append(int(number_string))
        elif col_index < 137:
          number_string = engine_schematic[row_index][col_index+1] + engine_schematic[row_index][col_index+2]
          number_list.append(int(number_string))
      elif col_index < 138:
        number_string = engine_schematic[row_index][col_index+1]
        number_list.append(int(number_string))

  if row_index > 0:
    ## CHECK ABOVE-LEFT
    if col_index > 0:
      if engine_schematic[row_index-1][col_index-1].isdigit():
        top_left = True
        # Hold this for later, we'll see if the top three units are all their own number first
    ## CHECK ABOVE
    if engine_schematic[row_index-1][col_index].isdigit():
      top = True

      # If the top position is a digit but the top-left isn't,
      if top_left == False:
        # Check the one to the right of the top
        pass # Hold this for later maybe

    ## CHECK ABOVE-RIGHT
    if col_index < 139:
      if engine_schematic[row_index-1][col_index+1].isdigit():
        top_right = True
        # evaluate more later

    # If all three top slots are filled, this is a part number
    if top_left and top and top_right:
      number_string = engine_schematic[row_index-1][col_index-1] + engine_schematic[row_index-1][col_index] + engine_schematic[row_index-1][col_index+1]
      number_list.append(int(number_string))

    # If only the top left is filled, need to see what is before it
    elif top_left and not top:
      # Check the unit to the left of that one to see how big the number is
      if col_index > 1 and engine_schematic[row_index-1][col_index-2].isdigit():
        # Check the unit to the left of that one also
        if col_index > 2 and engine_schematic[row_index-1][col_index-3].isdigit():
          number_string = engine_schematic[row_index-1][col_index-3] + engine_schematic[row_index-1][col_index-2] + engine_schematic[row_index-1][col_index-1]
          number_list.append(int(number_string))
        elif col_index > 2:
          number_string = engine_schematic[row_index-1][col_index-2] + engine_schematic[row_index-1][col_index-1]
          number_list.append(int(number_string))
      elif col_index > 1:
        number_string = engine_schematic[row_index-1][col_index-1]
        number_list.append(int(number_string))
    
    # If the top left and top are filled, but the top right isn't, check just one to their left
    elif top_left and top and not top_right:
      # Check the unit to the left of that one to see how big the number is
      if col_index > 1 and engine_schematic[row_index-1][col_index-2].isdigit():
        number_string = engine_schematic[row_index-1][col_index-2] + engine_schematic[row_index-1][col_index-1] + engine_schematic[row_index-1][col_index]
        number_list.append(int(number_string))
      elif col_index > 1:
        number_string = engine_schematic[row_index-1][col_index-1] + engine_schematic[row_index-1][col_index]
        number_list.append(int(number_string))

    # If the top and top right are filled, but the top left isn't, check just one to their right
    elif top_right and top and not top_left:
      # Check the unit to the right of that one to see how big the number is
      if col_index < 138 and engine_schematic[row_index-1][col_index+2].isdigit():
        number_string = engine_schematic[row_index-1][col_index] + engine_schematic[row_index-1][col_index+1] + engine_schematic[row_index-1][col_index+2]
        number_list.append(int(number_string))
      elif col_index < 138:
        number_string = engine_schematic[row_index-1][col_index] + engine_schematic[row_index-1][col_index+1]
        number_list.append(int(number_string))

    # If only the top right is filled, need to see what comes after it
    elif top_right and not top:
      # Check the unit to the right of that one to see how big the number is
      if col_index < 138 and engine_schematic[row_index-1][col_index+2].isdigit():
        # Check the unit to the right of that one also
        if col_index < 137 and engine_schematic[row_index+1][col_index+3].isdigit():
          number_string = engine_schematic[row_index-1][col_index+1] + engine_schematic[row_index-1][col_index+2] + engine_schematic[row_index-1][col_index+3]
          number_list.append(int(number_string))
        elif col_index < 137:
          number_string = engine_schematic[row_index-1][col_index+1] + engine_schematic[row_index-1][col_index+2]
          number_list.append(int(number_string))
      elif col_index < 138:
        number_string = engine_schematic[row_index-1][col_index+1]
        number_list.append(int(number_string))

  if row_index < 139:
    ## CHECK BOTTOM-LEFT
    if col_index > 0:
      if engine_schematic[row_index+1][col_index-1].isdigit():
        bottom_left = True

    ## CHECK BOTTOM
    if engine_schematic[row_index+1][col_index].isdigit():
      bottom = True

    ## CHECK BOTTOM-RIGHT
    if col_index < 139:
      if engine_schematic[row_index+1][col_index+1].isdigit():
        bottom_right = True

    # If all three bottom slots are filled, this is a part number
    if bottom_left and bottom and bottom_right:
      number_string = engine_schematic[row_index+1][col_index-1] + engine_schematic[row_index+1][col_index] + engine_schematic[row_index+1][col_index+1]
      number_list.append(int(number_string))
    
    # If only the bottom left is filled, need to see what is before it
    elif bottom_left and not bottom:
      # Check the unit to the left of that one to see how big the number is
      if col_index > 1 and engine_schematic[row_index+1][col_index-2].isdigit():
        # Check the unit to the left of that one also
        if col_index > 2 and engine_schematic[row_index+1][col_index-3].isdigit():
          number_string = engine_schematic[row_index+1][col_index-3] + engine_schematic[row_index+1][col_index-2] + engine_schematic[row_index+1][col_index-1]
          number_list.append(int(number_string))
        elif col_index > 2:
          number_string = engine_schematic[row_index+1][col_index-2] + engine_schematic[row_index+1][col_index-1]
          number_list.append(int(number_string))
      elif col_index > 1:
        number_string = engine_schematic[row_index+1][col_index-1]
        number_list.append(int(number_string))
    
    # If the bottom left and bottom are filled, but the bottom right isn't, check just one to their left
    elif bottom_left and bottom and not bottom_right:
      # Check the unit to the left of that one to see how big the number is
      if col_index > 1 and engine_schematic[row_index+1][col_index-2].isdigit():
        number_string = engine_schematic[row_index+1][col_index-2] + engine_schematic[row_index+1][col_index-1] + engine_schematic[row_index+1][col_index]
        number_list.append(int(number_string))
      elif col_index > 1:
        number_string = engine_schematic[row_index+1][col_index-1] + engine_schematic[row_index+1][col_index]
        number_list.append(int(number_string))

    # If the bottom and bottom right are filled, but the bottom left isn't, check just one to their right
    elif bottom_right and bottom and not bottom_left:
      # Check the unit to the right of that one to see how big the number is
      if col_index < 138 and engine_schematic[row_index+1][col_index+2].isdigit():
        number_string = engine_schematic[row_index+1][col_index] + engine_schematic[row_index+1][col_index+1] + engine_schematic[row_index+1][col_index+2]
        number_list.append(int(number_string))
      elif col_index < 138:
        number_string = engine_schematic[row_index+1][col_index] + engine_schematic[row_index+1][col_index+1]
        number_list.append(int(number_string))

    # If only the bottom right is filled, need to see what comes after it
    elif bottom_right and not bottom:
      # Check the unit to the right of that one to see how big the number is
      if col_index < 138 and engine_schematic[row_index+1][col_index+2].isdigit():
        # Check the unit to the right of that one also
        if col_index < 137 and engine_schematic[row_index+1][col_index+3].isdigit():
          number_string = engine_schematic[row_index+1][col_index+1] + engine_schematic[row_index+1][col_index+2] + engine_schematic[row_index+1][col_index+3]
          number_list.append(int(number_string))
        elif col_index < 137:
          number_string = engine_schematic[row_index+1][col_index+1] + engine_schematic[row_index+1][col_index+2]
          number_list.append(int(number_string))
      elif col_index < 138:
        number_string = engine_schematic[row_index+1][col_index+1]
        number_list.append(int(number_string))

  # Calculate the gear ratio if there are exactly two part numbers in the list
  if len(number_list) == 2:
    gear_ratio = number_list[0] * number_list[1]
  else:
    gear_ratio = 0

  return gear_ratio

main()