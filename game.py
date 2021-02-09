# game.py
import random

print("Rock, Paper, Scissors, Shoot!")


print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

# ask for input

#user_choice variable name is from Mairead Higgins in class
user_choice = input("Please choose either 'rock', 'paper', or 'scissors'")
print(user_choice)
print(f"You chose: {user_choice}")


# sim comp input
round_options = ['rock', 'paper', 'scissors']
computer_choice = random.choice(round_options)
print(f"The computer chose: {computer_choice}")

exit()


# determine who won
print("-------------------")
print("Oh, the computer won. It's ok.")
print("-------------------")
print("Thanks for playing. Please play again!")