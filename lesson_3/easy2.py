# QUESTION 1

# numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

# reverse_numbers = list(reversed(numbers))
# reverse_numbers_2 = numbers[::-1]

# print(reverse_numbers_2)

# QUESTION 2

# numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

# number1 = 8  # False (not in numbers)
# number2 = 95 # True (in numbers)

# print(number1 in numbers)
# print(number2 in numbers)

# QUESTION 3

# print(42 in range(10,101))
# print(42 in range(100,101))

# QUESTION 4

# numbers = [1, 2, 3, 4, 5]

# del numbers[2]

# print(numbers)

# QUESTION 5

# numbers = [1, 2, 3, 4]
# table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

# print(isinstance(numbers, list))
# print(isinstance(table, list))

# QUESTION 6

# title = "Flintstone Family Members"

# centered_title = title.center(40)

# QUESTION 7

# statement1 = "The Flintstones Rock!"
# statement2 = "Easy come, easy go."

# print(statement1.count("t"))
# print(statement2.count("t"))

# QUESTION 8

# ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}

# print("Spot" in ages.keys())

# QUESTION 9 -> didnt know update function

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
additional_ages = {'Marilyn': 22, 'Spot': 237}

ages.update(additional_ages)

print(ages)