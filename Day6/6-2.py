def main():
  with open('input.txt') as file:
    # Read in the race time to a variable (flatten out all the spaces)
    first_line = file.readline()
    first_line.replace(" ", "").strip()
    print(first_line)
    race_time = 57726992
    race_distance = 291117211762026

    # Read in the race distances to a second list
    second_line = file.readline()
    second_line.replace(" ", "").strip()
  file.close()

  races = []
  for button_hold_time in range(race_time):
    # The amount of time available for traveling is the distance minus the time you hold the button
    travel_time = race_time - button_hold_time
    # Then the distance you can travel is the travel time left available, multiplied by the speed (=button hold time)
    travel_distance = travel_time * button_hold_time
    # So if the travel distance is greater than the current record, you've beat the record - add it to that race's sublist
    if travel_distance > race_distance:
      races.append(travel_distance)

  print("The number of available ways to win multiplied together is", len(races))

main()