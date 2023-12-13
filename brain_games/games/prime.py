from random import randint


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num < 1:
        return False
    d = 2
    while d * d <= num and num % d != 0:
        d += 1
    return d * d > num


def get_data_for_round():
    question = randint(1, 10)
    right_answer = 'yes' if is_prime(question) else "no"
    return [question, right_answer]
