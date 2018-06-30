# Read movie_metadata.csv into a list of lists and assign to movie_data.
# Open and read the file movie_metadata.csv into a string variable.
# Split the data into rows on the newline character ("\n").
# Create an empty list, movie_data.
# Loop through each row, and split each row into a list on the comma character (","), and append it to movie_data.
# Display the first 5 lists in movie_data using the print() function.
f = open("movie_metadata.csv", 'r')
data = f.read()
rows = data.split('\n')
movie_data = []

for row in rows:
    split_row = row.split(",")
    movie_data.append(split_row)

print(movie_data[0:4])


# Write a function, with a definition, name, argument(s), body and return value, that returns a list containing the names of the movies in movie_data. This function is expected to behave similar to first_elt(), but for multiple lists.

# Give the function a name that describes what it does; first_elts() is a good example, but feel free to be creative.
# Declare an empty list.
# Use a for loop to extract the first element of each list, and append these elements to the empty list.
# Return the list.
# Assign the returned list to movie_names.

# Display the first 5 elements of movie_names using the print() function.
def get_movies(input_list):
    first_elts = []
    for x in input_list:
        movie_name = x[0]
        first_elts.append(movie_name)
    return first_elts

movie_names = get_movies(movie_data)
print(movie_names[1:5])
