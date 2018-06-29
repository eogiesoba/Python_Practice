#You now have a list of lists assigned to nested_list, where each inner list contains string elements. 
#The second element (the estimated number of people with that name) in each list is a decimal value that you should convert to a float.
#By converting these values to floats, you'll be able to perform computations on them and analyze the data.
print(nested_list[0:5])
numerical_list = []

for x in nested_list:
    name = x[0] #this will assign the value of the element at index 0 of in x to the variable name
    value = float(x[1]) #This will convert the string into a float and assign that value the variable value
    numerical_list.append([name,value]) # This will append the list into the list numerical_list. Hence list of lists.
    
print(numerical_list[0:4])


#---------------------------------------------------------------------------------------------------->

#The data set contains first names shared by at least 100 people. 
#Let's limit it those shared by at least 1,000 people.
# The last value is ~100 people
numerical_list[len(numerical_list)-1]
thousand_or_greater = []

for x in numerical_list:
    if x[1] >= 1000:
        thousand_or_greater.append(x[0])
        
print(thousand_or_greater)
    
