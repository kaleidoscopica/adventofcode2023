def main():
  card_data = []

  with open('input.txt') as file:
    for line in file:
      # Remove newlines and whitespace
      new_line = line.strip()
      # Make each line a list containing the hand at index 0, and the bet at index 1
      new_line = [x.strip() for x in new_line.split()]
      card_data.append(new_line)
  file.close()

  for hand in card_data:
    pass

  print(card_data[0])

  point_total = 0

main()