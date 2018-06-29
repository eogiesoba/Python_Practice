# Assign the first element of weather to first_element and display it using the print() function.
# Assign the last element of weather to last_element and display it using the print() function.
# Weather has been loaded in.
first_element = weather[0]
print(first_element)

last_element = weather[364]
print(last_element)

# Assign the value 1 to the key Aquaman in a new dictionary named superhero_ranks.
# Assign the value 2 to the key Superman in superhero_ranks.
superhero_ranks = {}
superhero_ranks["Aquaman"] = 1
superhero_ranks["Superman"] = 2

# Look up FDR in president_ranks and assign the result to a new variable fdr_rank.
# Look up Lincoln in president_ranks and assign the result to a new variable lincoln_rank.
# Look up Aquaman in president_ranks and assign the result to a new variable aquaman_rank.
president_ranks = {} #a new dictionary has just been defined as presiden_ranks
president_ranks["FDR"] = 1
president_ranks["Lincoln"] = 2
president_ranks["Aquaman"] = 3

fdr_rank = president_ranks["FDR"]
lincoln_rank = president_ranks["Lincoln"]
aquaman_rank = president_ranks["Aquaman"]


# Create a dictionary named animals with the following keys and values:
# The key 7 corresponding to the value raven.
# The key 8 corresponding to the value goose.
# The key 9 corresponding to the value duck.
# Create a dictionary named times with the following keys and values:
# The key morning corresponding to the value 9.
# The key afternoon corresponding to the value 14.
# The key evening corresponding to the value 19.
# The key night corresponding to the value 23.
random_values = {"key1": 10, "key2": "indubitably", "key3": "dataquest", 3: 5.6}
print(random_values)
animals = {
    7: "raven",
    8: "goose",
    9: "duck"
}
times = {
    "morning": 9,
    "afternoon": 14,
    "evening": 19,
    "night": 23
}


# Add the key Ann and value 85 to the dictionary students.
# Replace the value for the key Tom with 80.
# Add 5 to the value for the key Jim.
students = {
    "Tom": 60,
    "Jim": 70
}
students["Ann"] = 85
students["Tom"] = 80
students["Jim"] = students["Jim"] + 5


# Check whether jupiter is a key in planet_numbers, and assign the resulting Boolean value to jupiter_found.
# Check whether earth is a key in planet_numbers, and assign the resulting Boolean value to earth_found.
planet_numbers = {"mercury": 1, "venus": 2, "earth": 3, "mars": 4}
jupiter_found = "jupiter" in planet_numbers
earth_found = "earth" in planet_numbers


# Append any names in planet_names that are longer than 5 characters to long_names. 
# Otherwise, append the names to short_names.
planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Uranus"]
short_names = []
long_names = []

for planet in planet_names:
    if len(planet) > 5:
        long_names.append(planet)
    else:
        short_names.append(planet)
print(long_names)
print(short_names)



# Count the number of times that each element occurs 
# in the list named pantry that appears in the code block below. You'll need to:
# Create an empty dictionary named pantry_counts.
# Loop through each item in pantry.
# If the item appears in pantry_counts, add 1 to the value in pantry_counts for the item's key.
# Otherwise, add the item to pantry_counts as a key, with the value 1.
# When finished, each item in pantry will have its own key in pantry_counts, 
# and its value will be the number of times the item appears in pantry.
pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]
pantry_counts = {}
for food in pantry:
    if food in pantry_counts:
        pantry_counts[food] = pantry_counts[food] + 1
    else:
        pantry_counts[food] = 1
print(pantry_counts)



# Count how many times each type of weather occurs in the weather list, 
# and store the results in a new dictionary called weather_counts.
weather_counts = {}
for wType in weather:
    if wType in weather_counts:
        weather_counts[wType] = weather_counts[wType] + 1
    else: 
        weather_counts[wType] = 1
print(weather_counts)  