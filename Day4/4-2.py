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

  count = 0
  card_total = 0

  # Holds the number of each scratchcard; start with 1 of each (199 total)
  card_counts = []
  for i in range(199):
    card_counts.append(1)

  # Iterate over each scratchcard in the scratchcard data
  for index, scratchcard in enumerate(scratchcard_data):
    winning_numbers = 0

    print("Examining scratchcard:", scratchcard)
    # See if any number on the scratchcard is also found in the winning numbers
    for number in scratchcard[1]:
      if number in scratchcard[0]:
        winning_numbers += 1
    print("This card had", winning_numbers, "winning numbers.")

    # Increase the number in card_counts[index+x] by 1 for each x in range(1, winning_numbers+1)
    for copy in range(card_counts[index]):
      for x in range(1, winning_numbers+1):
        card_counts[index+x] += 1

    # Increase the count of scratchcards checked off
    count += 1

  # Add up all the cards
  card_total = 0
  for item in card_counts:
    card_total += item

  print("The total number of scratchcards you ended up with is:", card_total)
  
main()