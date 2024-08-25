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

