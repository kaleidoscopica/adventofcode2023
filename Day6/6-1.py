def main():
  race_times = []
  race_distances = []

  with open('input.txt') as file:
    # Read in the race times to a list
    first_line = file.readline()
    race_times = first_line.strip().split()
    race_times.pop(0)
    race_times = [int(x) for x in race_times]
    # Read in the race distances to a second list
    second_line = file.readline()
    race_distances = second_line.strip().split()
    race_distances.pop(0)
    race_distances = [int(x) for x in race_distances]
  file.close()

  races = [[], [], [], []]
  for i in range(len(race_times)):
    for button_hold_time in range(race_times[i]):
      # The amount of time available for traveling is the distance minus the time you hold the button
      travel_time = race_times[i] - button_hold_time
      # Then the distance you can travel is the travel time left available, multiplied by the speed (=button hold time)
      travel_distance = travel_time * button_hold_time
      # So if the travel distance is greater than the current record, you've beat the record - add it to that race's sublist
      if travel_distance > race_distances[i]:
        races[i].append(travel_distance)

  print("The number of ways to win race 1:", len(races[0]))
  print("The number of ways to win race 2:", len(races[1]))
  print("The number of ways to win race 3:", len(races[2]))
  print("The number of ways to win race 4:", len(races[3]))
  print("The number of available ways to win multiplied together is", len(races[0])*len(races[1])*len(races[2])*len(races[3]))

main()