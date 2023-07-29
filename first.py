# ---------------------------------------------------
# This demo program shows off how elegant Python is!
# Written by Efosa Ogiesoba 2023
# Anyone may freely copy or modify this program.
# ---------------------------------------------------

print(2 * 5 // 3 )    # This is the integer division operator
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