# This is a "guess the number" game
import random

print('Hello. What is your name?')
name = input()

print('Well, ' + str(name) + ', I am thinking of a number between 1 and 20')

number = random.randint(1, 20)
guesses_taken: int

for guesses_taken in range(1, 7):
    print('Take a guess')
    guess = input()

    print_script = 'Guess ' + str(guesses_taken) + ' of 7. Your guess is too'

    if guess < number:
        print(print_script + ' low')
    elif guess > number:
        print(print_script + ' high')
    else:
        print("Ya did good bucko, nice job!")
        break
    print('You took ' + str(guesses_taken) + ' guesses')
