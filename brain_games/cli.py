#! /usr/bin/env python

"""Логика игры будет описана здесь."""

import prompt


def welcome_user():
    """
    Выдает приветственное сообщение.
    Задает вопрос о имени пользователя -
    Пользователь вводит сообщение с клавиатуры. Приветсвует юзера по имени
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


if __name__ == '__main__':
    welcome_user()
