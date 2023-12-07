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

  for line in scratchcard_data:
    print(line)

main()