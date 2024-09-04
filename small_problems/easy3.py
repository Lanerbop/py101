# REPEAT YOURSELF

# input will be a string and a positive integer
# output will be the string print on the same # of lines as integer

# main data structure will be string

# define repeat to take a string and integer
# use a for loop to print the string up to integer range

# def repeat(my_string, times_repeated):
#     for _ in range(times_repeated):
#         print(my_string)

# repeat('Hello', 3)

# ddaaiillyy ddoouubbllee -> somewhat hard. still solved though

# input will be a string that may contain consecutive characters
# output will be a string with consecutive characters crunched to 1 character

# main data structure will be strings

# define crunch to take string as its argument
# create a new string
# for old string, check if character and character next to it are the same
# if they are not the same, add the character to new string

# def crunch(my_string):
#     if my_string:
#         my_list = [my_string[0]]

#         for char in my_string:
#             if char != my_list[-1]:
#                 my_list.append(char)
#         return "".join(my_list)

#     else: # string is empty
#         return ""
        

# # These examples should all print True
# print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
# print(crunch('4444abcabccba') == '4abcabcba')
# print(crunch('ggggggggggggggg') == 'g')
# print(crunch('abc') == 'abc')
# print(crunch('a') == 'a')
# print(crunch('') == '')

# BANNERIZER -> too verbose. didn't do further exploration

# input will be a string
# output will be string encased in box

# main data type will be string

# number of hyphens is length of string + 2. starting and ending plus sign
# than can be used for top and bottom border
# number of rows inside box or pipes needed is height of text + 2

# def print_in_box(my_string):
#     hyphens_needed = "-" * (len(my_string)) + 2 * "-"
#     top_bottom_border = "+" + hyphens_needed + "+"
#     space_needed = " " * (len(my_string)) + 2 * " "
#     above_bottom_text = "|" + space_needed + "|"
#     string_line = "| " + my_string + " |"
#     print(top_bottom_border)
#     print(above_bottom_text)
#     print(string_line)
#     print(above_bottom_text)
#     print(top_bottom_border)

# print_in_box('To boldly go where no one has gone before.')

# STRINGS STRINGS

# input will be a positive integer
# output will be a string of alternating integers of length int starting with '1'

# main data structure is a string

# define stringy to take an integer as input
# use range function to go through integers until inputted integer
# use if even, print 1, else print 0

# def stringy(integer):
#     my_string = ""
#     for index in range(integer):
#         digit = "1" if index % 2 == 0 else "0"
#         my_string += digit
#     return my_string

# print(stringy(6) == "101010")           # True
# print(stringy(9) == "101010101")        # True
# print(stringy(4) == "1010")             # True
# print(stringy(7) == "1010101")          # True

# RIGHT TRIANGLES -> too confusing

# input will be a positive integer
# output will be a right triangle with height of int on right side

# main data structure is a string

# define function triangle to take an integer as its parameter
# line will have length of integer
# use for loop to remove one space from each line and replace with *

# def triangle(height):
#     line = " " * height
#     for index in range(height):
#         line = " " * (height - 1) + ("*" * (index + 1))
#         print(line)
#         height -= 1

# triangle(5)
# triangle(9)

# def triangle(height):
#     for num in range(1, height + 1):
#         spaces = height - num
#         stars = num
#         print(f"{" " * spaces}{"*" * stars}")

# triangle(5)
# triangle(9)

# MADLIBS

# noun = input("Enter a noun: ")
# verb = input("Enter a verb: ")
# adjective = input("Enter an adjective: ")
# adverb = input("Enter an adverb: ")

# print(f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!")

# DOUBLE DOUBLES

# input is an integer
# output for double numbers is the double number, otherwise it's the num * 2

# main data structure is int

# check if number's length is odd, if so, multiply by 2
# now working with even numbers
# check if left side of num == right side of num, if so, return num
# else return num * 2

# def twice(my_num):
#     my_num = str(my_num)
#     slicing_index = len(my_num) // 2
#     if len(my_num) % 2 == 1:
#         return int(my_num) * 2
#     elif my_num[:slicing_index] == my_num[slicing_index:]:
#         return int(my_num)
#     else:
#         return int(my_num) * 2

# print(twice(37) == 74)                  # True
# print(twice(44) == 44)                  # True
# print(twice(334433) == 668866)          # True
# print(twice(444) == 888)                # True
# print(twice(107) == 214)                # True
# print(twice(103103) == 103103)          # True
# print(twice(3333) == 3333)              # True
# print(twice(7676) == 7676)              # True

# GRADE BOOK

# input will be 3 integers representing grades on assignments
# output will be the letter grade corresponding to the average of assignments

# main data structure will be int

# get 3 grades
# calculate average
# use if statement to check for each letter category
# for corresponding category, return letter grade

# def get_grade(grade1, grade2, grade3):
#     average_grade = (grade1 + grade2 + grade3) / 3
#     if 100 >= average_grade >= 90:
#         return 'A'
#     elif 90 > average_grade >= 80:
#         return 'B'
#     elif 80 > average_grade >= 70:
#         return 'C'
#     elif 70 > average_grade >= 60:
#         return 'D'
#     else:
#         return 'F'

# print(get_grade(95, 90, 93) == "A")      # True
# print(get_grade(50, 50, 95) == "D")      # True

# CLEAN UP THE WORDS

# input will be a messy string
# output will be a string with all non alphanumeric characters
# replaced by spaces with only 1 consecutive space max

# main data type will be string

# initialize an empty string
# use a for loop to iterate through each character in string
# if the character is alphanumeric, add character to new string
# if character is not alphanumeric, check if last character in
# new string is a space. if it is, continue loop, if not, add a space
# return new string

# def clean_up(messy_string):
#     new_string = ""

#     for character in messy_string:
#         if character.isalpha():
#             new_string += character
#         elif len(new_string) == 0 or new_string[-1] != " ":
#             new_string += " "
    
#     return new_string

# print(clean_up("---what's my +*& line?") == " what s my line ")
# print(clean_up("---what's my +*& line?"))
# # True

#  WHAT CENTURY IS THAT? -> wayyy too verbose

# input is integer representing year
# output will be the century ending with 'st' 'nd' and such

# main data structure will be integers for categorization
# and then strings for output

# first, find number value of century.
# if last two digits end with '00' // 100
# if not, // 100 + 1
# then find suffix
# first check length of century string. if len == 1,
# use special suffix for 1 2 and 3, then use th for rest
# for len != 1, check if endswith 11-19, then use th for all
# for rest, use th



def century(year):
    year_string = str(year)

    teens = ('11', '12', '13', '14', '15', '16', '17', '18', '19')
    if year_string.endswith('00'):
        century = year // 100
    else:
        century = year // 100 + 1
    
    century_string = str(century)

    if len(century_string) == 1:
        if century_string.endswith("1"):
            century_string += "st"
        elif century_string.endswith("2"):
            century_string += "nd"
        elif century_string.endswith("3"):
            century_string += "rd"
        else:
            century_string += "th"
    elif century_string.endswith(teens):
        century_string += "th"
    else:
        if century_string.endswith("1"):
            century_string += "st"
        elif century_string.endswith("2"):
            century_string += "nd"
        elif century_string.endswith("3"):
            century_string += "rd"
        else:
            century_string += "th"
    
    return century_string


print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True