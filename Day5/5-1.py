def main():
  with open('input.txt') as file:
    # Read in only the first line to create the list of seeds
    new_line = file.readline().strip()
    colon = new_line.index(':')
    new_line = new_line[colon+2:]
    seeds = [int(x.strip()) for x in new_line.split()]

    # Read in the rest of the file, to then create individual lists of mappings (skip empty lines)
    rest_of_file = [line.strip() for line in file.readlines() if line != '\n']
    # Grab the seed-to-soil map
    seed_to_soil_map = [line.split() for line in rest_of_file[1:33]]
    # Grab the soil-to-fertilizer map
    soil_to_fertilizer_map = [line.split() for line in rest_of_file[34:69]]
    # Grab the fertilizer-to-water map
    fertilizer_to_water_map = [line.split() for line in rest_of_file[70:97]]
    # Grab the water-to-light map
    water_to_light_map = [line.split() for line in rest_of_file[98:115]]
    # Grab the light-to-temperature map
    light_to_temperature_map = [line.split() for line in rest_of_file[116:158]]
    # Grab the temperature-to-humidity map
    temperature_to_humidity_map = [line.split() for line in rest_of_file[159:196]]
    # Grab the humidity-to-location map
    humidity_to_location_map = [line.split() for line in rest_of_file[197:]]
  file.close()

  print(humidity_to_location_map)

main()