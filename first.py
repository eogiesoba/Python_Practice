# ---------------------------------------------------
# This demo program shows off how elegant Python is!
# Written by Efosa Ogiesoba 2023
# Anyone may freely copy or modify this program.
# ---------------------------------------------------

print(16 - 2 * 5 // 3 + 1)    # This is the integer division operator
print(7 % 3)     # This is the remainder or modulus operator
print(18.0 // 4)

print(type(34)) #This will use the native fuction type() to determine what type of data type 34 isgit 

print('''"Oh no", she exclaimed, "Ben's bike is broken!"''') #Triple quoted strings can even span multiple lines:

print("""This is a string statement
      that is going to extend
      for up to 3 lines of code""")

#Discrete Mathematical Test
for n in range(10 ** 4):
    if n % 13 == 0 and n % 100 == 15:
        print(n)

#This code below will get the number of characters in rv
rv = """Once upon a midnight dreary, while I pondered, weak and weary,
    Over many a quaint and curious volume of forgotten lore,
    While I nodded, nearly napping, suddenly there came a tapping,
    As of some one gently rapping, rapping at my chamber door.
    'Tis some visitor, I muttered, tapping at my chamber door;
    Only this and nothing more."""

num_chars = len(rv)

#Input from user text code, collect 2 input values then convert to int values
#then finally add them

current_time_str = input("what is the current time (in hours 0-23)?")
wait_time_str = input("How many hours do you want to wait")

current_time_int = int(current_time_str)
wait_time_int = int(wait_time_str)

final_time_int = current_time_int + wait_time_int

final_answer = final_time_int % 24

print(final_time_int)
