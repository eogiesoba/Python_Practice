#Because our data is in a CSV file, we'll need to read the file in before we can work with it. 
#In an earlier mission, we read a CSV file into a list, and we'll do the same here.
f = open("la_weather.csv", 'r')
data = f.read()
rows = data.split('\n')
weather_data = []
for row in rows:
    split_row = row.split(",")
    weather_data.append(split_row)

print(weather_data)


# Loop over each row in weather_data.
# Append the second item in each row to the weather list.
# When complete, weather should contain each value from the Type of Weather column.
# weather_data has already been read in automatically to make things easier.
# weather = []
for x in weather_data:
    value = x[1]
    weather.append(value)
print(weather)


# Count the number of items in weather. You can accomplish this by:
# Looping over each element in weather.
# Adding 1 to count for each element.
# When finished, count should equal the number of items in weather.
count = 0
for x in weather:
    count = count + 1
print(count)


# Slice the weather list to remove the header.
# The slice should only remove the first element in the list.
# Assign the slice to new_weather.
new_weather = weather[1:]


# Use the in statement to check whether the value cat is in the list animals,
# and assign the result to cat_found.
# Use the in statement to check whether the value space_monster is in the list animals, 
# and assign the result to space_monster_found.
animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]
cat_found = "cat" in animals
space_monster_found = "space_monster" in animals

# Loop through each item in the weather_types list.
# Check whether the item occurs in the new_weather list.
# Append the result of the check to weather_type_found.
# At the end, weather_type_found should be a list of Boolean values.
weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []
for x in weather_types:
    value = x in new_weather
    weather_type_found.append(value)

print(weather_type_found)
