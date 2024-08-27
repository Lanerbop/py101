# A FUNCTION THAT RETURNS THE SUM OF TWO NUMBERS

# START

# GET num1 and num2
# PRINT num1 + num2

def sum_(num1, num2):
    return num1 + num2

# FUNCTION TAKES LIST OF STRINGS AND RETURNS CONCATENATION

# START

# GET list of strings
# PRINT join strings on ""

def concatenate_strings(lst):
    return "".join(lst)

# print(concatenate_strings(["Hello", "World", "!"]))

# START

# GET list of integers
# SET array = []
# iterate through list
# for index % 2 == 0, add integer to array
# PRINT array

# def every_other(lst):
#     result = []
#     index = 0
#     while index < len(lst):
#         if index % 2 == 0:
#             result.append(lst[index])
        
#         index += 1

#     return result

# print(every_other([1, 2, 3, 4, 5, 6]))

# determine the index of the 3rd occurence of a character in a string
# return index, else none

# START

# GET string
# GET character

# SET string = list(string) 
# SET counter = 0
# FOR index in list(string):
#     IF list(string)[index] == character:
#         counter += 1
#     IF counter == 3:
#         return index
# RETURN None

# take two lists of numbers and return result of merging the lists
# elements of first list should become elements of even indexes
# elements of second list should become elements at odd indexes

# START

# GET list 1
# GET list 2

# SET function merge(list1, list2):
# SET new_list = []
# FOR item1, item2 in zip(list1, list2)
#     new_list.append(item1)
#     new_list.append(item2)
# PRINT new_list