#!/usr/bin/env python3

"""Game logic even-game."""

import prompt
from random import randint


def even_check():
    """
    Rules message. Show question. Check user answer.
    Feedback message.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        rand_num = randint(1, 100)
        print(f'Question: {rand_num}')
        answer = prompt.string('Your answer: ').lower()
        if answer != 'yes' and answer != 'no':
            print("Please use only 'yes' or 'no'.")
            break
        elif rand_num % 2 == 0 and answer == 'yes':
            print('Correct!')
            counter += 1
        elif rand_num % 2 != 0 and answer == 'no':
            print('Correct!')
            counter += 1
        elif rand_num % 2 != 0 and answer == 'yes':
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            break
        elif rand_num % 2 == 0 and answer == 'no':
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            break

    if counter == 3:
        print('Congratulations, ' + name)
    else:
        print("Let's try again, " + name)
