def main():
  with open('input.txt') as file:
    # Read in the race time to a variable (and flatten out all the spaces)
    race_time = file.readline()
    race_time = race_time.replace("Time:", "").strip()
    race_time = int(race_time.replace(" ", ""))
    # Read in the race distance to a second variable (and flatten out all the spaces)
    race_distance = file.readline()
    race_distance = race_distance.replace("Distance:", "").strip()
    race_distance = int(race_distance.replace(" ", ""))
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

  print("The number of available ways to win multiplied together is:", len(races))

main()