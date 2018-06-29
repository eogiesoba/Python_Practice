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



