from random import randint


RULE = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def get_data_for_round():
    start = randint(1, 10)
    step = randint(1, 10)
    end = start + step * PROGRESSION_LENGTH

    progression = list(range(start, end, step))

    hidden_index = randint(0, 8)
    number_for_answer = progression[hidden_index]
    progression[hidden_index] = '..'

    answer = str(number_for_answer)
    progression = ' '.join(str(el) for el in progression)
    return (progression, answer)
