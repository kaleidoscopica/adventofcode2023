def main():
  with open('input.txt') as file:
    # Read in only the first line to create the list of seeds
    new_line = file.readline().strip()
    colon = new_line.index(':')
    new_line = new_line[colon+2:]
    seeds = [int(x.strip()) for x in new_line.split()]
    # Split each pair of seed numbers into a sublist in the form of [seedstart, range]
    seeds = [seeds[i:i+2] for i in range(0, len(seeds), 2)]

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

    # Sort each map by its source numbers, so that they're in ascending order
    seed_to_soil_map = sorted(seed_to_soil_map, key=lambda x: int(x[1]))
    soil_to_fertilizer_map = sorted(soil_to_fertilizer_map, key=lambda x: int(x[1]))
    fertilizer_to_water_map = sorted(soil_to_fertilizer_map, key=lambda x: int(x[1]))
    water_to_light_map = sorted(soil_to_fertilizer_map, key=lambda x: int(x[1]))
    light_to_temperature_map = sorted(soil_to_fertilizer_map, key=lambda x: int(x[1]))
    temperature_to_humidity_map = sorted(soil_to_fertilizer_map, key=lambda x: int(x[1]))
    humidity_to_location_map = sorted(soil_to_fertilizer_map, key=lambda x: int(x[1]))

  file.close()

  locations = []

  # Loop through seeds, find each one's location
  for seedgroup in seeds:
    start = seedgroup[0]
    seedrange = seedgroup[1]
    for x in range(start, start+seedrange+1):
      soil_dest = find_soil_mapping(start, seed_to_soil_map)
      fertilizer_dest = find_fertilizer_mapping(soil_dest, soil_to_fertilizer_map)
      water_dest = find_water_mapping(fertilizer_dest, fertilizer_to_water_map)
      light_dest = find_light_mapping(water_dest, water_to_light_map)
      temperature_dest = find_temperature_mapping(light_dest, light_to_temperature_map)
      humidity_dest = find_humidity_mapping(temperature_dest, temperature_to_humidity_map)
      location = find_location_mapping(humidity_dest, humidity_to_location_map)
      locations.append(location)

  print("The smallest location is", min(locations))

## Functions
# Given a seed and seed-to-soil map, returns the soil destination of the seed
def find_soil_mapping(seed, seed_to_soil_map):
  for map in seed_to_soil_map:
    found_map = False
    dest = int(map[0])
    source = int(map[1])
    range = int(map[2])
    if source <= seed <= source+range:
      difference = seed-source
      found_map = True
      break
  
  if found_map == True:
    return dest+difference
  else:
    return seed

    
# Given a soil location and soil-to-fertilizer map, returns the fertilizer destination of the seed
def find_fertilizer_mapping(soil_src, soil_to_fertilizer_map):
  for map in soil_to_fertilizer_map:
    found_map = False
    dest = int(map[0])
    source = int(map[1])
    range = int(map[2])
    if source <= soil_src <= source+range:
      difference = soil_src-source
      found_map = True
      break
  
  if found_map == True:
    return dest+difference
  else:
    return soil_src

# Given a fertilizer location and fertilizer-to-water map, returns the water destination of the seed
def find_water_mapping(fert_src, fertilizer_to_water_map):
  found_map = False
  for map in fertilizer_to_water_map:
    dest = int(map[0])
    source = int(map[1])
    range = int(map[2])
    if source <= fert_src <= source+range:
      difference = fert_src-source
      found_map = True
      break
  
  if found_map == True:
    return dest+difference
  else:
    return fert_src

# Given a water location and water-to-light map, returns the light destination of the seed
def find_light_mapping(water_src, water_to_light_map):
  found_map = False
  for map in water_to_light_map:
    dest = int(map[0])
    source = int(map[1])
    range = int(map[2])
    if source <= water_src <= source+range:
      difference = water_src-source
      found_map = True
      break
  
  if found_map == True:
    return dest+difference
  else:
    return water_src

# Given a light location and soil-to-fertilizer map, returns the temperature destination of the seed
def find_temperature_mapping(light_src, light_to_temperature_map):
  found_map = False
  for map in light_to_temperature_map:
    dest = int(map[0])
    source = int(map[1])
    range = int(map[2])
    if source <= light_src <= source+range:
      difference = light_src-source
      found_map = True
      break
  
  if found_map == True:
    return dest+difference
  else:
    return light_src

# Given a temperature location and soil-to-fertilizer map, returns the humidity destination of the seed
def find_humidity_mapping(temp_src, temperature_to_humidity_map):
  found_map = False
  for map in temperature_to_humidity_map:
    dest = int(map[0])
    source = int(map[1])
    range = int(map[2])
    if source <= temp_src <= source+range:
      difference = temp_src-source
      found_map = True
      break
  
  if found_map == True:
    return dest+difference
  else:
    return temp_src

# Given a humidity location and humidity-to-location map, returns the location destination of the seed
def find_location_mapping(humidity_src, humidity_to_location_map):
  found_map = False
  for map in humidity_to_location_map:
    dest = int(map[0])
    source = int(map[1])
    range = int(map[2])
    if source <= humidity_src <= source+range:
      difference = humidity_src-source
      found_map = True
      break
  
  if found_map == True:
    return dest+difference
  else:
    return humidity_src

main()