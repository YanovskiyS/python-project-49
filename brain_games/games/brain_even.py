#!/usr/bin/env python3
from brain_games.engine import run_game
from random import randint


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_data_for_round():
    question = randint(1, 10)
    if is_even(question) is True:
        correct_answer = 'yes'
    else:
        correct_answer = "no"
    return [question, correct_answer]


run_game(RULE, get_data_for_round)
