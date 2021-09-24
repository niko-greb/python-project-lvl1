#!/usr/bin/env python3

"""Логика игры будет описана здесь."""

import prompt


def welcome_user():
    """
    Greeting message. Ask name. Greetings by name.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


if __name__ == '__main__':
    welcome_user()
