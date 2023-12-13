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
    first_num = randint(1, 15)
    second_num = randint(1, 15)
    signs = ['+', '-', '*']
    sign = signs[randint(0, 2)]
    question = f'{first_num} {sign} {second_num}'
    right_answer = str(calc_expresion(first_num, sign, second_num))
    return [question, right_answer]
