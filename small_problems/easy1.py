# ISN'T IT ODD

# The input is an integer.
# The output is a boolean. 
# The output return True when odd, false otherwise.

# Mainly working with integer data type.

# Take the absolute value of the integer.
# Check if the integer is odd by using % == 1
# Output True if true

# my solution - too verbose

# def is_odd(integer):
#     abs_integer = abs(integer)
#     return True if abs_integer % 2 == 1 else False

# better solution

# def is_odd(integer):
#     return abs(integer) % 2 == 1

# print(is_odd(5) ) # true
# print(is_odd(-5)) # true
# print(is_odd(6) ) # false
# print(is_odd(-6)) # false
# print(is_odd(0) ) # false

# ODD NUMBERS

# output is odd numbers from 1-99 inclusive

# data type is int

# use a for loop with range stepping to print each number.

# for number in range(1,100, 2):
#     print(number)

# further exploration for user specifying start and end values

# starting_value = int(input("What number would you like to start at? "))
# ending_value = int(input("What number would you like to end at? "))

# for integer in range(starting_value, ending_value + 1):
#     if integer % 2 == 1:
#         print(integer)

# EVEN NUMBERS

# output is all even numbers from 1-99 inclusive, each
# printed on seperate lines

# data type is integer

# use for loop to iterate through range
# for each iteration, check if integer is even using %
# if %, print integer

# for integer in range(1, 100):
#     if integer % 2 == 0:
#         print(integer)

# iterate through just even numbers

# use range stepping and start at 2. print each iteration

# for integer in range(2,100, 2):
#     print(integer)

# HOW BIG IS THE ROOM

# The input is a string of the length and width of a room
# in meters.
# The output is the room's area in both square meters
# and square feet.

# Data type is float

# Take input of length and width of a room. 
# Turn input into a float. 
# Calculate square meters of room by multiplying l * w 
# Use conversion rate to get square feet
# print square meters and square feet


# msmt_type = input("Are you using meters or feet? ")
# length = float(input("What is the length of the room? "))
# width = float(input("What is the width of the room? "))

# if msmt_type == 'meters':
#     sq_m = length * width
#     sq_ft = sq_m * 10.7639
# elif msmt_type == 'feet':
#     sq_ft = length * width
#     sq_m = sq_ft / 10.7639
    

# print(f"The room's area is {sq_m:.2f} square meters, which is"
#       f" {sq_ft:.2f} square feet.")



# area_of_room(0, 50)  # 0sm, 0sf
# area_of_room(50, 0)  # 0sm, 0sf
# area_of_room(5, 10)
# area_of_room(1, 1)   # 1sm, 10.7639 sf

# TIP CALCULATOR

# Input will be the bill and the tip percentage. 
# Output will be the tip and the total.

# The main data structure will be a float.

# Ask what the bill is, then ask what the tip percentage is 
# convert the input into a float
# Calculate the tip by multiplying bill * percentage / 100
# Calculate the total by adding the bill to the tip
# print the tip and total

# bill = float(input("What is the bill? "))
# percentage = float(input("What is the tip percentage? "))

# tip = bill * percentage / 100
# total = bill + tip

# print(f"The tip is ${tip:.2f}.")
# print(f"The total is ${total:.2f}.")

# SUM OR PRODUCT OF CONSECUTIVE INTEGERS

# Input will be an integer greater than 0 and either "s" or "p"
# Output will different for either s or p. s will represent
# the sum of all numbers from 1 to the integer where 
# p will represent the product

# main data type will be integers

# ask user to enter an integer greater than 0
# ask user to enter s or p with s being sum and p product
# create 2 functions s and p
# s will iterate through range from 1 to s + 1
# for each iteration, add integer to the sum
# for p, loop through range from 1 to s + 1
# for each iteration, multiply by integer

# prompt1 = "Please enter an integer greater than 0: "
# prompt2 = 'Enter "s" to compute the sum, or "p" to compute the product. '
# my_integer = int(input(prompt1))
# s_or_p = input(prompt2).replace(" ", "")

# def sum():
#     sum = 0
#     for integer in range(1, my_integer + 1):
#         sum += integer
#     return sum

# def product():
#     product = 1
#     for integer in range(1, my_integer + 1):
#         product *= integer
#     return product


# if s_or_p == "s":
#     print(f"The sum of the integers between 1 and {my_integer} is "
#           f"{sum()}")
# elif s_or_p == "p":
#     print(f"The product of the integers between 1 and {my_integer} is "
#           f" {product()}")
# else:
#     print("Invalid input. Please try again.")

# SHORT LONG SHORT

# input would be 2 strings 
# output would be a string of the shorter + longer + shorter

# Main data type will be strings

# create an if statement if len of string1 > string2 and vice versa
# if len of string1 > string2, return string1 + string2 + string1
# else: do the opposite
# return concatendated string

# def short_long_short(string1, string2):
#     if len(string1) > len(string2):
#         return string2 + string1 + string2
#     else:
#         return string1 + string2 + string1


# print(short_long_short("", "banana") == "banana")        # True
# print(short_long_short('abc', 'defgh') == "abcdefghabc") # True
# print(short_long_short('abcde', 'fgh') == "fghabcdefgh") # True
# print(short_long_short('', 'xyz') == "xyz")              # True

# LEAP YEARS PART 1

# input is an integer > 0 that represents a year
# output is a booleon that returns true if year is a leap year

# main data structure is an int

# use match/case on year
# check if year is divisible by 400 -> true
# check if year is divisible by 100, but not 400 -> false
# check if year is divisible by 4, but not 100 -> true
# else -> false

# def is_leap_year(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     else:
#         return year % 4 == 0
    
# # These examples should all print True
# print(is_leap_year(1) == False)
# print(is_leap_year(2) == False)
# print(is_leap_year(3) == False)
# print(is_leap_year(4) == True)
# print(is_leap_year(1000) == False)
# print(is_leap_year(1100) == False)
# print(is_leap_year(1200) == True)
# print(is_leap_year(1300) == False)
# print(is_leap_year(1751) == False)
# print(is_leap_year(1752) == True)
# print(is_leap_year(1753) == False)
# print(is_leap_year(1800) == False)
# print(is_leap_year(1900) == False)
# print(is_leap_year(2000) == True)
# print(is_leap_year(2023) == False)
# print(is_leap_year(2024) == True)
# print(is_leap_year(2025) == False)

# LEAP YEARS PART 2

# gregorian_adaptation = {
#     "ES": 1582,
#     "PT": 1582,
#     "FR": 1582,
#     "IT": 1582,
#     "GB": 1752,
#     "SE": 1753,
#     "JP": 1873,
# }

# def is_leap_year(year, country_code="GB"):
#     if year < gregorian_adaptation[country_code]: # Julian leap year
#         return year % 4 == 0
#     else: # Gregorian leap year
#         if year % 400 == 0:
#             return True
#         elif year % 100 == 0:
#             return False
#         else:
#             return year % 4 == 0
        
# # These examples should all print True
# print(is_leap_year(1) == False)
# print(is_leap_year(2) == False)
# print(is_leap_year(3) == False)
# print(is_leap_year(4) == True)
# print(is_leap_year(1000) == True)
# print(is_leap_year(1100) == True)
# print(is_leap_year(1200) == True)
# print(is_leap_year(1300) == True)
# print(is_leap_year(1751) == False)
# print(is_leap_year(1752) == True)
# print(is_leap_year(1753) == False)
# print(is_leap_year(1800) == False)
# print(is_leap_year(1900) == False)
# print(is_leap_year(2000) == True)
# print(is_leap_year(2023) == False)
# print(is_leap_year(2024) == True)
# print(is_leap_year(2025) == False)

# MULTIPLES OF 3 AND 5

# input will be an integer
# output will be the sum of all numbers between 1 and integer
# that are multiples of 3 and 5

# main data structure is integer

# initialize a sum
# loop through each number from 1 to integer + 1
# for each iteration, add number to sum if it is a multiple of 3 or 5
# return the sum

# def multisum(max_integer):
#     sum = 0
#     for integer in range(3, max_integer + 1):
#         if integer % 3 == 0 or integer % 5 == 0:
#             sum += integer
    
#     return sum



# # These examples should all print True
# print(multisum(3) == 3)
# print(multisum(5) == 8)
# print(multisum(10) == 33)
# print(multisum(1000) == 234168)
# print(multisum(2) == 0)

# UTF-16 STRING VALUE

# input is a string
# output is sum of utf-16 values of each character in the string

# mainly working with strings and integers

# initialize a sum
# iterate through each character in the string
# for each iteration, add value of ord to sum
# return sum

# def utf16_value(string):
#     sum_ = 0
#     for character in string:
#         sum_ += ord(character)
    
#     return sum_



# # These examples should all print True
# print(utf16_value('Four score') == 984)
# print(utf16_value('Launch School') == 1251)
# print(utf16_value('a') == 97)
# print(utf16_value('') == 0)

# # The next three lines demonstrate that the code
# # works with non-ASCII characters from the UTF-16
# # character set.
# OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
# print(utf16_value(OMEGA) == 937)
# print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)