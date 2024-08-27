import json

# ask user for the first number
# ask user for the second number
# ask user what operation to perform
# perform the operation
# print to terminal

LANGUAGE = 'en'

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def messages(message, lang='en'):
    return MESSAGES[lang][message]

prompt(messages('welcome'))

while True:

    prompt(messages('first_number'))
    number1 = input()
    while invalid_number(number1):
        prompt(messages('invalid_number'))
        number1 = input()

    prompt(messages('second_number'))
    number2 = input()
    while invalid_number(number2):
        prompt("Hmm.. that doesn't look like a valid number.")
        number2 = input()

    prompt(messages('operation'))
    operation = input()
    while operation not in ["1", "2", "3", "4"]:
        prompt(messages('must_choose'))
        operation = input()

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    prompt(f"The result is: {output}")

    prompt("Would you like to perform another operation? y/n")
    another_one = input()
    while another_one not in ["y", "n"]:
        prompt("Please type y to do another calculation or "
               "n to exit Calculator.")
        another_one = input()

    if another_one == "n":
        break
