from random import randint


RULE = 'Find the greatest common divisor of given numbers.'


def find_gcd(num1, num2):
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return num1


def get_data_for_round():
    first_num = randint(1, 30)
    second_num = randint(1, 30)
    question = f'{first_num} {second_num}'
    right_answer = str(find_gcd(first_num, second_num))
    return (question, right_answer)
