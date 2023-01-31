# tech201_datatypes_and_operators
tech201_datatypes_and_operators

# Data types

Numeric - Ints, Floats, Longs, complex  

String - Text of any type  

Boolean - True or False  

Operators  

Arithmetic operators  

+, -, *, /  

Comparison operators    

 - > 
 - <  
 - ==  
 - !=  
 - >= greater than or equal to  
 - <=  

# Implementing numeric types

Ints

a = 24  
b = 16  

print(a + b) # 40  
print(a > b) # True  
print(a < b) # False  

Floats  
FloatNum = 1.356  
IntNum = 4  
print(FloatNum + IntNum)  

# Theres no limit to the size of decimal, but python will round things up

one_third = 1 / 3  
print(one_third) # 0.3333333333333333  
print(one_third * 3) # 1.0  


# Strings
#
# Single_quotes = 'Look! Single quotes'
# Double_quotes = "Look! Double quotes"
#
# print(Single_quotes)
# print(Double_quotes)
#
# string_failure = 'I said 'Wow!'' , error
#
# escape_example = 'I said \'Wow\''   # by using forward slash we can use ''
# print(escape_example)
#
# quote_in_quote = 'I said "Wow!"'
# print(quote_in_quote)
# reverse_quote = "I said 'Wow!'"
# print(reverse_quote)
#
# String slicing
#
# Everything in code starts with 0 not 1
#
# H e l l o   w o r l  d  !
#
# 0 1 2 3 4 5 6 7 8 9 10 11
# -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# Hw = "Hello world!"
# print(Hw[7:]) # orld! of this string get everything from 7 and after
# print(Hw[7:9])  # or, output will include 7 it doesn't include 9
# print(Hw[-5:]) # orld!
# print(Hw[:5]) # Hello
# print(Hw[0:5]) # Hello
#
# String methods
#
# strip()
#
# white_space = "lot's of space at the end           "
# print(len(white_space)) # 36
# print(len(white_space.strip())) #25
#
# A few more
#
# example_text = "Here's some text with lot's or text"
#
# Count a substring within a string
# How many times does a word occur in a string
# print(example_text.count("text"))
#
# Make everything lowercase
# print(example_text.lower())
# print(example_text.upper())
#
# Capitalise things
# print(example_text.capitalize())
#
# Replace characters/text
# print(example_text.replace("with" , ","))
#
# Concatenation
# a = "here "
# b = "more "
# c = "much more"
# print(a + b + c)
#
# Casting
#
# x = 2
# y = 5.4
# z = " there's a number 25.4 unless we put a space!"
#
# print(x + y + z), lets turn our ints into strings
#
# print(str(x) + ", " + str(y) + z)
#
# string to numeric
#
# int_string = "6"
#
# print(float(int_string))
# print(type(float(int_string)))
#
# F-strings
# format things without casting all the time
#
# name = "Lassie"
# years = 7
# height_cm = 60.2
#
# print(f"{name} is {years} years old and {height_cm}cm tall")
#
# F-strings allow us to use methods/evaluations too
#
# name = "Snoopy"
# years = 52
#
# print(f"{name.upper()} is {years * 7} years old in dog years!!!!")
#
# F-strings to specify precision in rounding and decimals
#
# pi = 3.14159265359
#
# print(f"Pi to 3 decimal places: {pi:.3f}") # 3.142
# print(f"Pi to 3 decimal places: {pi:.5f}") # 3.14159
#
# score = 16
# max_score = 26
#
# print(f"You scored {score/max_score}") # 0.6153846153846154
# print(f"You scored {score/max_score:%}") # 61.538462%
# print(f"You scored {score/max_score:.2%}")  # 61.54%
# print(f"You scored {score/max_score:.0%}") # 62%



# Booleans

# True or False
# Make sure to capitalise True and False
# a = True
# b = False
# use comparison operators
# print(a == b) # False
# print(a != b) # True
# print(a >= b) # True is greater than false
# print(a >= True) # True, because a is equal to True
# print(b <= False) # True, b is = to False or b is lass than a

# print(True and False) # False, True and True will return True everything else will return False
# print(False and True) # False
# print(False or True) # True, because of or True is available

# Booleans are useful for quickly checking he state of something, and making a decision based on that state.
# The other area Booleans are really useful for are validating data types

# Booleans with data types

# hi = "Hello world!"
#
# print(hi.isalpha()) # False
# isalpha checks if everything is alphanumeric

# print(hi.islower()) # False
# islower checks if everything is lowercase
# print(hi.isupper()) # False
# isupper checks if everything is uppercase
# print(hi.endswith("!")) # True
# Check what string ends with
# print(hi.startswith("Hello")) # True
# # Check what string starts with, Case sensitive

# x = 0
# y = 10
# z = -15
# print(bool(x)) # 0 is considered always False
#
# print(bool(y)) # True positive numbers is true
#
# print(bool(z)) # True, minus numbers are also true

# None

# None == Null in a lot of other languages

# print(bool(None)) # False, None is always False

# x = None

# print(x == False) # False,
# print(x == True) # False,

# None, True and False are independent None != True or False

# Checking if a variable is None

# print(x == None) # direct comparison - this can be a problem in more complex situations

# print(x is None) # Best practice for checking is something 'is None

# print(type(x)) # <class 'NoneType'>


