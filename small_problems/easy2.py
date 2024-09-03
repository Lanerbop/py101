# WELCOME STRANGER -> was easy

# input will be a list with unknown num of elements that product a name
# plus a dictionary with 2 keys for title and occupation
# output will be a greeting with person's full name and title

# data structure -> string

# first, inititialize variable name
# name will be the list joined with a space
# then initialize variable title
# plumber will be an f string -> the map at key title then occupation
# use f string to return greeting

# def greetings(name, dict):
#     name = " ".join(name)
#     title_and_job = f"{dict["title"]} {dict["occupation"]}"
#     return f"Hello {name}! Nice to have a {title_and_job} around."



# greeting = greetings(
#     ["John", "Q", "Doe"],
#     {"title": "Master", "occupation": "Plumber"},
# )
# print(greeting)

# GREETING A USER -> easy

# input will be a person's name, either with or without a '!'
# output will be a greeting, or shouted greeting if '!' is appended

# data structure will be a string

# initialize variable name
# if last character of name is '!' use screaming greeting

# name = input("Hi. What is your name? ")
# name = name.strip()
# if name[-1] == '!':
#     name = name.upper()
#     print(f"HELLO {name} WHY ARE WE YELLING?")
# else:
#     print(f"Hello {name}.")

# MULTIPLY TWO NUMBERS -> easy

def multiply(num1, num2):
    return num1 * num2

# print(multiply(5, 3) == 15)  # True

# SQUARING AN ARGUMENT -> easy

# def square(num1):
#     return multiply(num1, num1)

# print(square(5) == 25)   # True
# print(square(-8) == 64)  # True

# power to n further exploration -> little bit harder but okay

# def power_to(num1, exponent):
#     result = 1
#     for _ in range(1, exponent + 1):
#         result = multiply(num1, result)
#     return result

# print(power_to(5, 3))

# FLOATING POINT ARITHMETIC -> good. try match case next time

# def prompt(my_string):
#     print(f"==> {my_string}")

# prompt("Enter the first number: ")
# num1 = float(input())
# prompt("Enter the second number: ")
# num2 = float(input())

# prompt(f"{num1} + {num2} = {num1 + num2}")
# prompt(f"{num1} - {num2} = {num1 - num2}")
# prompt(f"{num1} * {num2} = {num1 * num2}")
# prompt(f"{num1} / {num2} = {num1 / num2}")
# prompt(f"{num1} // {num2} = {num1 // num2}")
# prompt(f"{num1} % {num2} = {num1 % num2}")
# prompt(f"{num1} ** {num2} = {num1 ** num2}")

# def calculate(first, second, operator):
#     match operator:
#         case '+': return first + second
#         case '-': return first - second
#         case '*': return first * second
#         case '/': return first / second
#         case '//': return first // second
#         case '%': return first % second
#         case '**': return first ** second

# first_float = float(input("==> What is your first number?\n"))
# second_float = float(input("==> What is your second number?\n"))
# for operator in ['+', '-', '*', '/', '//', '%', '**']:
#     operation = f"{first_float} {operator} {second_float}"
#     result = f"{calculate(first_float, second_float, operator)}"
#     print(f"==> {operation} = {result}")

# THE END IS NEAR BUT NOT HERE -> easy

# input will be a string of at least 2 words
# output will be the next to last word of that string

# primary data type will be strings

# define penultimate to take string as argument
# initialize list of words variable
# list of words = split string into words using split method
# return list of words at index -2 to get penultimate

# def penultimate(sentence):
#     words = sentence.split()
#     return words[-2]

# # These examples should print True
# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")

# further exploration

# input is a sentence of any length of words
# output will be the middle word of a sentence

# edge cases
# even # of words
# one word
# no words

# main data structure will be strings

# def function middle word that takes sentence as an argument
# if sentence is empty, return ""
# initialize words
# words = split on whitespace to get each word in a list
# if len  of words is 1, return word[0]
# if len of words is even, return words[len of words / 2 - 1]
# if len of words is odd, return words[len of words // 2]

# def middle_word(sentence=""):
#     if bool(sentence) == False:
#         return ""
#     words = sentence.split()
#     if len(words) == 1:
#         return words[0]
#     if len(words) % 2 == 0:
#         return words[int(len(words) / 2) - 1]
#     if len(words) % 2 == 1:
#         return words[len(words) // 2]

# print(middle_word())                           # ""
# print(middle_word("Hi"))                       # "Hi"
# print(middle_word("hi there how's it going"))  # "how's"
# print(middle_word("hi there how's it"))        # "there"

# EXCLUSIVE OR ->

# inputs will be 2 values
# output will be a boolean. if only 1 is truthy and 1 is falsy -> true else -> false

# define xor to take 2 expressions
# check bool of both expressions
# if A is truthy and B is falsy or vice versa, return True
# else false

# def xor(ex1, ex2):
#     ex1 = bool(ex1)
#     ex2 = bool(ex2)
#     if ex1 == True and ex2 == False:
#         return True
#     if ex1 == False and ex2 == True:
#         return True
#     else:
#         return False

# print(xor(5, 0) == True)
# print(xor(False, True) == True)
# print(xor(1, 1) == False)
# print(xor(True, True) == False)

# ODD LISTS -> easy w some troubleshooting

# input will be a list with n elements
# output will be a the list with only the odd elements

# main data structure is list

# return list[1:-1:2]

# def oddities(lst):
#     return lst[0:len(lst) + 1:2]

# print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
# print(oddities([1, 2, 3, 4]) == [1, 3])        # True
# print(oddities(["abc", "def"]) == ['abc'])     # True
# print(oddities([123]) == [123])                # True
# print(oddities([]) == [])                      # True

# HOW OLD IS TEDDY?

# import random

# name = input("What's your name? \n")
# if name == "":
#     name = "Teddy"

# age = random.randint(20, 100)

# print(f"{name} is {age} years old!")

# WHEN WILL I RETIRE -> didn't use datetime for current year

# from datetime import datetime

# age = int(input("What is your age? "))
# retirement_age = int(input("At what age would you like to retire? "))
# current_year = datetime.now().year

# years_until_retirement = retirement_age - age
# year_of_retirement = current_year + years_until_retirement

# print(f"It's {current_year}. You will retire in {year_of_retirement}.")
# print(f"You have only {years_until_retirement} years of work to go!")

# GET MIDDLE CHARACTER -> messy indexing

# input will be a non-empty string
# output will be the middle character if odd, or the two middle if even

# data structure will be strings

# define center_of function to take string as argument

# if length of string is odd, return character at index
# length of string // 2 
# if string is even, return character at index slice
# [length of string // 2]:length of string // 2 + 2]

# def center_of(my_string):
#     if len(my_string) % 2 == 1:
#         center_index = len(my_string) // 2
#         return my_string[center_index]
#     if len(my_string) % 2 == 0:
#         left_index = (len(my_string) // 2) - 1
#         return my_string[left_index:left_index + 2]

# print(center_of('I Love Python!!!') == "Py")    # True
# print(center_of('Launch School') == " ")        # True
# print(center_of('Launchschool') == "hs")        # True
# print(center_of('Launch') == "un")              # True
# print(center_of('Launch School is #1') == "h")  # True
# print(center_of('x') == "x")                    # True

# ALWAYS RETURN NEGATIVE

# input will be number
# output will be negative of the absolute value of that number

# main data structure is float

# def negative(num):
#     num = abs(num)
#     return -1 * num

# print(negative(5) == -5)      # True
# print(negative(-3) == -3)     # True
# print(negative(0) == 0)       # True