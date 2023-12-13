#!/usr/bin/env python3
from brain_games.games.calculator import RULE
from brain_games.games.calculator import get_data_for_round
from brain_games.engine import run_game


def main():
    run_game(RULE, get_data_for_round)


if __name__ == '__main__':
    main()
