from brain_games.engine import run_game
from random import randint


RULE = 'What is the result of the expression?'


def calc_expresion(first_num, sign, second_num):
    match sign:
        case '+':
            return first_num + second_num
        case '-':
            return first_num - second_num
        case '*':
            return first_num * second_num


def get_data_for_round():
    FIRST_NUM = randint(1, 15)
    SECOND_NUM = randint(1, 15)
    SIGNS = ['+', '-', '*']
    SIGN = SIGNS[randint(0, 2)]
    QUESTION = f'{FIRST_NUM} {SIGN} {SECOND_NUM}'
    RIGHT_ANSWER = str(calc_expresion(FIRST_NUM, SIGN, SECOND_NUM))
    return [QUESTION, RIGHT_ANSWER]


run_game(RULE, get_data_for_round)
