from random import randint


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_data_for_round():
    question = randint(1, 10)
    right_answer = 'yes' if is_prime(question) else "no"
    return (question, right_answer)
