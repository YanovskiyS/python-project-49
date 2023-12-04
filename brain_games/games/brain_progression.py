from brain_games.engine import run_game
from random import randint


RULE = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def create_random_progression(fist_element, step):
    PROGRESSION = []
    i = fist_element
    while len(PROGRESSION) <= PROGRESSION_LENGTH:
        PROGRESSION.append(i)
        i = i + step
    return PROGRESSION


def get_data_for_round():
    FIRST_ELEMENT = randint(1, 10)
    STEP = randint(1, 10)
    LIST_WITH_PROGRESSION = create_random_progression(FIRST_ELEMENT, STEP)
    HIDDEN_index = randint(0, 9)
    NUMBER_FOR_ANSWER = LIST_WITH_PROGRESSION[HIDDEN_index]
    LIST_WITH_PROGRESSION[HIDDEN_index] = '..'
    ANSWER = str(NUMBER_FOR_ANSWER)
    PROGRESSION = ' '.join(str(el) for el in LIST_WITH_PROGRESSION)
    return [PROGRESSION, ANSWER]


run_game(RULE, get_data_for_round)
