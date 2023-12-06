import re

def main():
  game_data = []

  with open('input.txt') as file:
    for line in file:
      # Remove newlines and whitespace
      new_line = line.strip()
      # Remove the "Game [Number]: " part
      colon = new_line.index(':')
      new_line = new_line[colon+2:]
      # Create a sublist for each set within a game, and each color within a set
      new_line = [[x.strip() for x in y.split(',')] for y in new_line.split(';')]
      game_data.append(new_line)
  file.close()

  sum = 0

  # Iterate through each game, through each set, and examine each cube
  for game in game_data:
    # Reset stats for each game
    possible = True
    red = 0
    green = 0
    blue = 0
    power = 0

    for set in game:
      for cube in set:
        number, color = cube.split()
        if color == "red":
          if int(number) > red:
            red = int(number)
        elif color == "green":
          if int(number) > green:
            green = int(number)
        elif color == "blue":
          if int(number) > blue:
            blue = int(number)

    # Calculate the power at the end of each game
    power = red * blue * green
    # Add each game's power to the sum total
    sum += power


  print("The power of all games is:", sum)

main()