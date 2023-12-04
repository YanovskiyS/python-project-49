from brain_games.engine import run_game
from random import randint


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    d = 2
    while d * d <= num and num % d != 0:
        d += 1
    return d * d > num


def get_data_for_round():
    QUESTION = randint(1, 20)
    RIGHT_ANSWER = 'yes' if is_prime(QUESTION) else "no"
    return [QUESTION, RIGHT_ANSWER]


run_game(RULE, get_data_for_round)
