from brain_games.engine import run_game
from random import randint


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_data_for_round():
    question = randint(1, 10)
    correct_answer = 'yes' if is_even(question) else 'no'
    return [question, correct_answer]


run_game(RULE, get_data_for_round)
