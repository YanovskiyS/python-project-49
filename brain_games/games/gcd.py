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
    first_num = randint(1, 30)
    second_num = randint(1, 30)
    question = f'{first_num} {second_num}'
    right_answer = str(find_gcd(first_num, second_num))
    return [question, right_answer]
