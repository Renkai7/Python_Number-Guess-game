#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

correct_number = random.randint(1, 100)
game_over = False

print(logo)
print("Welcome to the Number Guessing Game!")
print("I\'m thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


if difficulty == "easy":
  total_life = 10
elif difficulty == "hard":
  total_life = 5

print(correct_number)

def check_guess(guess, answer):
  if guess > answer:
    print("Too high.")
  elif guess < answer:
    print("Too low.")

  if total_life == 0:
    print("You've run out of guesses, you lose.")

while not game_over:

  print(f"You have {total_life} attempts remaining to guess the number.")
  user_guess = int(input("Make a guess: "))
  
  if user_guess == correct_number:
    print("That's correct! Congrats!")  
    game_over = True
  else:
    total_life -= 1
    check_guess(user_guess, correct_number)

  if total_life == 0:
    game_over = True
    