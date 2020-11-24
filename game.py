# Import necessary python moduels and functions from
# other files
import random
from check_inputs import valid_round, print_sleep
from game_rules import compete, welcome_message
from players import HumanPlayer, FixedPlayer
from players import RandomPlayer, ReflectPlayer, CyclePlayer
from game_rules import win_update, total_win_counter, announce_winner
from colorama import Fore, Back, Style, init
init(autoreset=True)


def first_move(
        response,
        first_move_options,
        win_count,
        memory,
        cycle_memory,
        stored_computer_move):
    """
    If the user decides to play a single round
    then this function gets selected. In the first move
    the human and computer player can not select the
    'ReflectPlayer' option.

    After both the players give their move, the result
    is announced and the winner is declared.

    """
    print_sleep(Fore.YELLOW + 'You have chosen to play a single round.')
    print("")
    human_player = HumanPlayer().move(cycle_memory, stored_computer_move)
    print("")
    print_sleep(f"You select: {human_player}")
    computer = random.choice(first_move_options)
    print_sleep(f"Computer selects: {computer}")
    compete(response, human_player, computer, win_count)
    win_update(response, win_count)
    your_total_wins, total_computer_wins = total_win_counter(
        response, win_count)
    announce_winner(your_total_wins, total_computer_wins)


def other_moves(response, stored_items, store, win_count, memory,
                cycle_memory, all_moves, first_move_options,
                stored_computer, stored_computer_move):
    """
    If the user decides to play more than one round
    then this function gets selected. In the first move
    the human and computer player can not select the
    'ReflectPlayer' option.

    After the first round the 'ReflectPlayer' is available.
    Both the computer move and the humaplayer move is stored
    and passed for the next move.

    At each round the winner is declared and the win number is
    updated.

    This function continues until all the rounds are finished.
    At the end of all the rounds  the result is announced
    and the winner is declared.

    """

    for rounds in range(int(response)):
        print("")
        print_sleep(f'This is round: {rounds+1}')

        if rounds == 0:
            # takes the human move
            human_player = HumanPlayer().move(cycle_memory,
                                              stored_computer_move)
            print("")
            # prints the human move
            print_sleep(f"You select: {human_player}")
            # stores all the human moves
            stored_items.append(human_player)
            # takes the computer move
            computer = random.choice(first_move_options)
            # stores all the computer moves moves
            stored_computer.append(computer)
            # prints the computer move
            print_sleep(f"Computer selects: {computer}")
            # call the competes function and the result is decided
            compete(response, human_player, computer, win_count)
            # total_number of win is updated
            win_update(response, win_count)
            total_win_counter(response, win_count)

        else:
            # the latest computer move used when the humanplayer
            # uses the ReflectPlayer
            stored_computer_move = stored_computer[rounds - 1]
            human_player = HumanPlayer().move(cycle_memory,
                                              stored_computer_move)
            print("")

            print_sleep(f"You select: {human_player}")
            stored_items.append(human_player)
            store = stored_items[rounds - 1]

            computer = random.choice(all_moves)
            stored_computer.append(computer)
            print(f"Computer selects: {computer}")

            compete(response, human_player, computer, win_count)
            win_update(response, win_count)
            total_win_counter(response, win_count)

    your_total_wins, total_computer_wins = total_win_counter(
        response, win_count)
    announce_winner(your_total_wins, total_computer_wins)


class Game:

    '''
    The Game class lets the player choose a single round
    and when the user gives 1 as the number of the round
    the single_round gets selected.

    When the user selects more then one round the method
    multiple_rounds gets selected.

    The game should each player's move method once
    in each round, to get that player's move.
    After each round, it stores the human and computer
    move that can be used in the ReflectPlayer both
    by the humanplayer and the computer.

    The ReflectPlayer option is not available in the
    first move. The humanplayer can select his inputs
    or can also select any of the computer player.

    The game displays the results after each round,
    including each player's score.
    At the end, the final score is displayed and the player
    with higher total win is decaled as the victorious. The game
    continues until all the rounds are finished.


    '''

    def __init__(self):
        # initalization of all the lists that
        # will be used inside the Game class
        self.stored_items = []  # stores all the items of the human player
        self.store = []  # stores the last human move
        self.stored_computer = []  # stores all the items of the computer
        self.stored_computer_move = []  # stores the last computer move
        self.win_count = []  # store all the wins for each player
        self.memory = []  # stores all the moves of the CyclePlayer

        # stores all the moves of the CyclePlayer
        # inside the HumanPlayer
        self.cycle_memory = []

        # containts all the moves for the first round
        self.first_move_options = [FixedPlayer().move(),
                                   RandomPlayer().move(),
                                   CyclePlayer().move(self.memory)]

        # containts all the moves
        self.all_moves = [FixedPlayer().move(),
                          RandomPlayer().move(),
                          ReflectPlayer(self.store).move(),
                          CyclePlayer().move(self.memory)]

        # print the welcome message and rules
        welcome_message()
        print("")
        print("Let's start!")

        # user response to select the number of rouds
        self.response = valid_round(
            'Please select the number of rounds you want to'
            ' play.\nPlease Select a number between 1-99: ')

    def single_round(self):
        """
        If the human player decides to play
        1 round then this logic is
        implemented.

        """
        if (int(self.response)) == 1:
            first_move(self.response, self.first_move_options,
                       self.win_count, self.memory,
                       self.cycle_memory,
                       self.stored_computer_move)

    def multiple_rounds(self):
        """
        If the human player decides to play multiple rounds
        then this logic is implemented.
        """
        if int(self.response) > 1:
            other_moves(
                self.response,
                self.stored_items,
                self.store,
                self.win_count,
                self.memory,
                self.cycle_memory,
                self.all_moves,
                self.first_move_options,
                self.stored_computer,
                self.stored_computer_move)

    def play(self):

        # can play single and multiple rounds
        self.single_round()
        self.multiple_rounds()


# the game begins
Game().play()
