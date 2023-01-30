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
