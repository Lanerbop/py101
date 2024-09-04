# QUESTION 1

# yes, there will be an indexing error

# QUESTION 2

# str1 = "Come over here!"  # True
# str2 = "What's up, Doc?"  # False

# print(str1.endswith("!"))
# print(str2.endswith("!"))

# QUESTION 3

# famous_words = "seven years ago..."

# new_famous_words = "Four score and " + famous_words
# new2_famous_words = f"Four score and {famous_words}"
# print(new_famous_words)
# print(new2_famous_words)

# QUESTION 4 -> did not need lower method

# munsters_description = "the Munsters are CREEPY and Spooky."
# # => 'The munsters are creepy and spooky.'
# new_munsters_description = munsters_description.capitalize()
# print(new_munsters_description)

# munsters_description = "The Munsters are creepy and spooky."
# print(munsters_description.swapcase())

# QUESTION 6 -> too verbose



# str1 = "Few things in life are as important as house training your pet dinosaur."
# str2 = "Fred and Wilma have a pet dinosaur named Dino."

# print('Dino' in str1)
# print('Dino' in str2)

# QUESTION 7

# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]

# # flintstones.append("Dino")

# flintstones.extend(['Dino', 'Hoppy'])

# print(flintstones)

# QUESTION 8 -> too verbose

# advice = "Few things in life are as important as house training your pet dinosaur."
# # Expected output:
# # Few things in life are as important as

# print(advice.split("house")[0])

# QUESTION 10 -> too verbose

advice = "Few things in life are as important as house training your pet dinosaur."

# advice = advice.replace('important', 'urgent')

print(advice.replace('important', 'urgent'))