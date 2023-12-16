from random import randint, choice
from operator import add, sub, mul


RULE = 'What is the result of the expression?'
OPERATIONS = [('+', add), ('-', sub), ('*', mul)]


def get_data_for_round():
    first_num = randint(1, 15)
    second_num = randint(1, 15)
    symbol, operation = choice(OPERATIONS)
    question = f'{first_num} {symbol} {second_num}'
    right_answer = str(operation(first_num, second_num))
    return (question, right_answer)
