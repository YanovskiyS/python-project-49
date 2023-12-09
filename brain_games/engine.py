import prompt


NUMBER_OF_ROUNDS = 3


def run_game(rules, get_round_data):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(rules)

    for i in range(NUMBER_OF_ROUNDS):
        [number_for_question, right_answer] = get_round_data()
        print('Question:', number_for_question)
        answer = prompt.string('Your answer: ')

        if answer == right_answer:
            print('Correct')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'."
                  f"\nLet's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')
