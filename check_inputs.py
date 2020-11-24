import time
from colorama import Fore, Back, Style

# the moves list contains the three moves of the game
valid_moves = [
    'rock',
    'paper',
    'scissors',
    'random',
    'cycle',
    'fixed',
    'reflect']


def valid_move(string):
    """
    This function checks whether the move is valid. That is the user
    needs to select one of the options from 'rock', 'paper','scissors',
    'random', 'fixed' and 'reflect'.
    To select the RandomPlayer move - the user types 'random.
    To select the FixerdPlayer move - the user types  'fixed'.
    To select the CyclePlayer move - the user types  'cycle'.
    Otherwise, this function prompt the user back with a message to select
    a valid option and continues until the user selects a valid move.
    input: string
    output: string
    """

    move = input(string)
    while True:
        # checks if the input string is one of the items
        # in the moves list
        if move in valid_moves:
            return move
        else:
            # if the input string is not in the moves list
            # it prints the statement below and returns
            # to the beginning of the program and ask the
            # user for a valid move- that is one
            # from rock, paper and scissors
            print('Please select one from rock, paper, scissors'
                  ' random, reflect and cycle.')
            return valid_move(string)


def valid_round(string):
    """
    This function checks whether the user has selected a valid
    number for the number of rounds he wants to play.
    That is, any number of rounds between 1 and 99.
    Otherwise this function prompt the user back with a message to select
    a valid number of round and continues until the user selects a valid round.
    input: string
    output: string
    """

    # forms a list of numbers with number 1 to 99
    round_play = map(str, list(range(1, 100)))
    response = input(string)
    while True:
        # checks if the input is in the round_play list
        if response in round_play:
            return response
        else:
            # if the input string is not in the round_play list
            # it prints the statement below and returns
            # to the beginning
            print('Please select any number from from: 1 to 99')
            return valid_round(string)


def print_sleep(s):
    """
    This funtion prints the input and delays the program for the specific
    amount of time specified in the sleep function.
    input: string
    """

    print(s)
    # the time pause is 01 second
    time.sleep(1)
