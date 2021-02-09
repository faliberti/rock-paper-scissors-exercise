# game.py
import random

import os

from dotenv import load_dotenv
load_dotenv()
USER_NAME = os.getenv("USER_NAME", default="Player One") 
print(f"PLAYER: '{USER_NAME}'")

print("Rock, Paper, Scissors, Shoot!")


print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

# ask for input

#user_choice variable name is from Mairead Higgins in class
user_choice = input("Please choose either 'rock', 'paper', or 'scissors'")
print(user_choice)
print(f"You chose: {user_choice}")

# create round options list
round_options = ['rock', 'paper', 'scissors']

# validate the user selection

user_choice = user_choice.lower()

if user_choice not in round_options:
    print("OOPS, please choose a valid option and try again")
    exit()  

# sim comp input
computer_choice = random.choice(round_options)
print(f"The computer chose: {computer_choice}")
print("-------------------")

# determine who won
# This code is based on Prof. Rossetti's on slack.
if user_choice == "scissors":
    if computer_choice == "scissors":
        print("Oh, it's a tie.")
    elif computer_choice == "rock":
        print("Oh, the computer won. It's ok.")
    elif computer_choice == "paper":
        print("Oh, you won! Nice job.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Oh, you won! Nice job.")
    elif computer_choice == "paper":
        print("Oh, it's a tie.")
    elif computer_choice == "scissors":
        print("Oh, the computer won. It's ok.")
elif user_choice == "rock":
    if computer_choice == "paper":
        print("Oh, the computer won. It's ok.")
    elif computer_choice == "scissors":
        print("Oh, you won! Nice job.")
    elif computer_choice == "rock":
        print("Oh, it's a tie.")
else:
    print("OOPS SOMETHING WENT WRONG.")

print("-------------------")

# End game message
print("Thanks for playing. Please play again!")



