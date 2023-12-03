from brain_games.engine import run_game
from random import randint


RULE = 'Find the greatest common divisor of given numbers.'


def find_gcd(num1, num2):
    x = num1
    y = num2
    while y != 0:
        temp = y
        y = x % y
        x = temp
    return x


def get_data_for_round():
    FIRST_NUMBER = randint(1, 30)
    SECOND_NUM = randint(1, 30)
    QUESTION = f'{FIRST_NUMBER} {SECOND_NUM}'
    RIGHT_ANSWER = str(find_gcd(FIRST_NUMBER, SECOND_NUM))
    return [QUESTION, RIGHT_ANSWER]


run_game(RULE, get_data_for_round)
