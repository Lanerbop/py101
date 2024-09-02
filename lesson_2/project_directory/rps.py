import json
import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
VALID_PREFIXES = ('r', 'p', 'sc', 'l', 'sp')
player_win_counter = 0
computer_win_counter = 0

with open('rps_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f"==> {message}")

def choice_abbreviation_reassign_to_choice():
    global choice
    if choice.startswith("r"):
        choice = VALID_CHOICES[0]
    elif choice.startswith("p"):
        choice = VALID_CHOICES[1]
    elif choice.startswith("sc"):
        choice = VALID_CHOICES[2]
    elif choice.startswith("l"):
        choice = VALID_CHOICES[3]
    elif choice.startswith("sp"):
        choice = VALID_CHOICES[4]

def increment_wins(player, computer):
    global player_win_counter
    global computer_win_counter
    if ((player == "rock" and computer == "scissors") or
        (player == 'rock' and computer == 'lizard') or
        (player == "paper" and computer == "rock") or
        (player == 'paper' and computer == 'spock') or
        (player == 'scissors' and computer == 'lizard') or
        (player == "scissors" and computer == "paper") or
        (player == 'lizard' and computer == 'paper') or
        (player == 'lizard' and computer == 'spock') or
        (player == 'spock' and computer == 'rock') or
        (player == 'spock' and computer == 'scissors')):
        player_win_counter += 1
    elif ((computer == "rock" and player == "scissors") or
        (computer == 'rock' and player == 'lizard') or
        (computer == "paper" and player == "rock") or
        (computer == 'paper' and player == 'spock') or
        (computer == 'scissors' and player == 'lizard') or
        (computer == "scissors" and player == "paper") or
        (computer == 'lizard' and player == 'paper') or
        (computer == 'lizard' and player == 'spock') or
        (computer == 'spock' and player == 'rock') or
        (computer == 'spock' and player == 'scissors')):
        computer_win_counter += 1

def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")

    if ((player == "rock" and computer == "scissors") or
        (player == 'rock' and computer == 'lizard') or
        (player == "paper" and computer == "rock") or
        (player == 'paper' and computer == 'spock') or
        (player == 'scissors' and computer == 'lizard') or
        (player == "scissors" and computer == "paper") or
        (player == 'lizard' and computer == 'paper') or
        (player == 'lizard' and computer == 'spock') or
        (player == 'spock' and computer == 'rock') or
        (player == 'spock' and computer == 'scissors')):
        prompt("You win!")
    elif ((computer == "rock" and player == "scissors") or
        (computer == 'rock' and player == 'lizard') or
        (computer == "paper" and player == "rock") or
        (computer == 'paper' and player == 'spock') or
        (computer == 'scissors' and player == 'lizard') or
        (computer == "scissors" and player == "paper") or
        (computer == 'lizard' and player == 'paper') or
        (computer == 'lizard' and player == 'spock') or
        (computer == 'spock' and player == 'rock') or
        (computer == 'spock' and player == 'scissors')):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while (choice not in VALID_CHOICES
            and not choice.startswith(VALID_PREFIXES)):
        prompt(MESSAGES["choose_invalid"])
        choice = input()

    choice_abbreviation_reassign_to_choice()

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(choice, computer_choice)
    increment_wins(choice, computer_choice)

    if player_win_counter == 3:
        prompt("Player got 3 wins!")
        break
    if computer_win_counter == 3:
        prompt("Computer got 3 wins!")
        break

    while True:
        prompt(MESSAGES["play_again_question"])
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        prompt("That's not a valid choice")

    if answer[0] == 'n':
        break
