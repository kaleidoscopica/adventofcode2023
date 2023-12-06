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

  red = 12
  green = 13
  blue = 14
  sum = 0
  game_id = 1

  for game in game_data:
    possible = True
    for set in game:
      for cube in set:
        number, color = cube.split()
        if color == "red":
          if int(number) > red:
            possible = False
        elif color == "green":
          if int(number) > green:
            possible = False
        elif color == "blue":
          if int(number) > blue:
            possible = False

    # at the end of all the sets in the game, see if all cubes from all sets passed the possibility check
    if possible == True:
      # if the game was possible, add its Game ID to the sum total
      sum += game_id
    
    # increment the game ID
    game_id += 1


  print("The sum of the game IDs is:", sum)

main()