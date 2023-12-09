from brain_games.engine import run_game
from random import randint


RULE = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def create_random_progression(fist_element, step):
    progression = []
    i = fist_element
    while len(progression) <= PROGRESSION_LENGTH:
        progression.append(i)
        i = i + step
    return progression


def get_data_for_round():
    fist_element = randint(1, 10)
    step = randint(1, 10)
    list_with_progression = create_random_progression(fist_element, step)
    hidden_index = randint(0, 9)
    number_for_answer = list_with_progression[hidden_index]
    list_with_progression[hidden_index] = '..'
    answer = str(number_for_answer)
    progression = ' '.join(str(el) for el in list_with_progression)
    return [progression, answer]


run_game(RULE, get_data_for_round)
