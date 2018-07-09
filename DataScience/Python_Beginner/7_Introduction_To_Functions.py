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


# Write a function named is_usa() that checks whether or not a movie was made in the United States.
# Check the movie_metadata.csv file to see which column corresponds to the nationality of the movie. Don't forget to subtract one to find the true index of the column in the list.
# Use an if statement to check the right column of the list with the word "USA". The equality operation is case sensitive, so make sure to get the capitilization right.
# Return True if the condition is met, and False otherwise.
# Try it with a few movies in movie_data.
# Call it on wonder_woman and store the result in wonder_woman_usa.
wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(movie):
    if movie[6] == "USA":
        return True
    else:
        return False
wonder_woman_usa = is_usa(wonder_woman)


# -Write a function index_equals_str() that takes in three arguments: a list, 
# an index and a string, and checks whether that index of the list is equal to that string.
# -Call the function with a different order of the inputs, using named arguments.
# -Call the function on wonder_woman to check whether or not 
# it is a movie in color, store it in wonder_woman_in_color, and print the value.
wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]
def is_usa(input_lst):
    if input_lst[6] == "USA":
        return True
    else:
        return False

def index_equals_str(lst,index,string):
    if lst[index] == string:
        return True
    else:
        return False

index_equals_str(index=6,lst=wonder_woman,string="USA")
wonder_woman_in_color = index_equals_str(wonder_woman,2,"Color")


# Write a function named feature_counter() that combines the logic of the index_equals_str() and counter() functions.
# Use this to find out how many of the movies were made in USA, and store the value in num_of_us_movies.
def index_equals_str(input_lst,index,input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False

def counter(input_lst,header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        num_elt = num_elt + 1
    return num_elt

def feature_counter(input_list,index,input_str,header_row):
    num_elt = 0
    if header_row == True:
        input_list = input_list[1:len(input_list)]
    for each in input_list:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt

# Write a summary_statistics() function that will take movie_data as input, 
# and output a dictionary that will give useful numbers from the data.
# Define summary_statistics() with one argument, an input list.
# Use the feature_counter() with the relevant arguments to count the following properties,
# and make them equal to the corresponding variables.
# Assign the number of movies made in Japan to num_japan_films.
# Assign the number of movies in color to num_color_films.
# Assign the number of movies in English to num_films_in_english.
# Create a dictionary that associates the keys (japan_films,color_films,films_in_english),
# with the corresponding variables.
# Return the dictionary.
# Call the function with movie_data as its input, and store its value in summary.
def feature_counter(input_lst,index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt

def summary_statistics(input_lst):
    num_japan_films = feature_counter(input_lst,6,"Japan",True)
    num_color_films = feature_counter(input_lst,2,"Color",True)
    num_films_in_english = feature_counter(input_lst,5,"English",True)
    movie_stats = {}
    movie_stats["japan_films"] = num_japan_films
    movie_stats["color_films"] = num_color_films
    movie_stats["films_in_english"] = num_films_in_english
    return movie_stats

summary = summary_statistics(movie_data)
    
# Edit the default code and fix the errors:
# Access the first element in lives (instead of the fifth),
# and assign it to a new variable first_life.
# Use the read() method to read the file story.txt into a string named story.
# Use the split() method to split the story variable into strings seperated 
# by spaces and assign the result to split_story.
# Display first_life and story.
first_life = lives[0]
story = open("story.txt").read()
split_story = story.split(" ")
print(first_life)
print(story)