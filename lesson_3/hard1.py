# QUESTION 1 -> wrong

# the second returns none because the dictionary is not on the same line

# QUESTION 2

# it prints {'first': [1, 2]}

# QUESTION 3 -> wrong

# A becomes one is ["one"], and so on
# B same
# one is two, two is three, three is one will be printed

# QUESTION 4

# def is_an_ip_number(str):
#     if str.isdigit():
#         number = int(str)
#         return 0 <= number <= 255
#     return False

# def is_dot_separated_ip_address(input_string):
#         dot_separated_words = input_string.split(".")
#         if len(dot_separated_words) != 4:
#              return False

#         while len(dot_separated_words) > 0:
#             word = dot_separated_words.pop()
#             if not is_an_ip_number(word):
#                 return False

#         return True

# QUESTION 5

# there is a name error because greeting was never initialized