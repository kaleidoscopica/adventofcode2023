def main():
  scratchcard_data = []

  with open('input.txt') as file:
    for line in file:
      # Remove newlines and whitespace
      new_line = line.strip()
      # Remove the "Card [Number]: " part
      colon = new_line.index(':')
      new_line = new_line[colon+2:]
      # Create a sublist for the winning numbers, and each scratchcard's numbers
      new_line = [[int(x.strip()) for x in y.split()] for y in new_line.split('|')]
      scratchcard_data.append(new_line)
  file.close()

  point_total = 0

  # Iterate over each scratchcard in the scratchcard data
  for scratchcard in scratchcard_data:
    points = 0
    winning_numbers = []

    print("Examining scratchcard:", scratchcard)
    # See if any number on the scratchcard is also found in the winning numbers
    for number in scratchcard[1]:
      if number in scratchcard[0]:
        winning_numbers.append(number)
    print("This card's winning numbers are:", winning_numbers)

    # Point calculation
    # The first winning match is worth one point, and each match after that doubles the points
    if len(winning_numbers) == 1:
      points = 1
    elif len(winning_numbers) > 1:
      points = 2**(len(winning_numbers)-1)
    print("Adding", points, "points to the total!")

    # Add the points to the point total
    point_total += points

  print("The total points of these scratchcards is:", point_total)

main()