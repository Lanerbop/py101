import json
import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

with open('rps_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f"==> {message}")

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

    while choice not in VALID_CHOICES:
        prompt(MESSAGES["choose_invalid"])
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(choice, computer_choice)

    while True:
        prompt(MESSAGES["play_again_question"])
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        prompt("That's not a valid choice")

    if answer[0] == 'n':
        break
