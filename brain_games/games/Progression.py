from random import randint


RULE = 'What number is missing in the progression?'


def get_data_for_round():
    fist_element = randint(1, 10)
    step = randint(1, 10)
    list_with_progression = list(range(fist_element, step * 10, step))
    hidden_index = randint(0, 9)
    number_for_answer = list_with_progression[hidden_index]
    list_with_progression[hidden_index] = '..'
    answer = str(number_for_answer)
    progression = ' '.join(str(el) for el in list_with_progression)
    return [progression, answer]
