import random
from check_inputs import valid_move

moves = ['rock', 'paper', 'scissors']  # the three moves of the game


class Player:

    """
    The Player class always returns 'rock' as the computer
    move. This Player class is used as the base class for
    all other moves.

    """

    def move(self):
        return 'rock'


class FixedPlayer(Player):

    """
     The FixedPlayer class is a subclass of the Player class.
     It always return 'rock' when gets called.
     """

    pass


class RandomPlayer(Player):
    """
    The 'RandomPlayer' class is a subclass of the Player class.
    It choses one of the moves from 'rock', 'paper', 'scissors'
    in a random basis as a computer move.
    """

    def move(self):
        self.move = random.choice(moves)
        return self.move


class ReflectPlayer(Player):

    """
    The 'ReflectPlayer' class is a subclass of the Player class.
    It stores the humanplayer move from the previous round
    remembers it. And when gets called the stored human move
    is then becomes the computer move of that round.

    """

    def __init__(self, store):
        self.store = store

    def move(self):
        return ''.join(self.store)


class CyclePlayer(Player):

    """
    The 'CyclePlayer' class is a subclass of the Player class.
    It cycles through the three moves 'rock', 'paper'
    and 'scissors'. Once a move is slected it is stored
    in the memory so that in the next move it is not
    selected again. Once all the three moves have been
    selected the memory list is cleared and restart.

    """

    def move(self, memory):
        self.memory = memory

        while True:
            if "paper" not in self.memory:
                self.memory.append('paper')
                return 'paper'

            elif "scissors" not in self.memory:
                self.memory.append('scissors')
                return 'scissors'

            elif "rock" not in self.memory:
                self.memory.append('rock')
                return 'rock'

            else:
                self.memory.clear()


class HumanPlayer(Player):

    """
    The 'HumanPlayer' class is a subclass of the Player class.
    Here, the move options is changed and it lets the player
    to choose one of the moves from 'rock', 'paper' & 'scissors'.

    The 'HumanPlayer' can also select the computerplayers.
    By typing 'random' the humanplayer can select the RandomPlayer.
    Likewise, FixedPlayer can be chosen by typing 'fixed',
    CyclePlayer can be chosen by typing 'cycle',
    and ReflectPlayer can be chosen by typing 'reflect' to
    choose the previous computer move.

    ReflectPlayer option is not available in the first round
    since there is no computer move available in the first round.
    However, the move can be selected after the first round
    in a game that is more than 1 round.

    If the user selects the ReflectPlayer option in the first
    round, a message pops us that says the move is not available
    in this round and to select any other move.


    """

    def move(self, cycle_memory, stored_computer_move):
        self.choice = valid_move('Select your move:')
        self.memory = cycle_memory
        self.stored_computer_move = stored_computer_move

        if self.choice == 'cycle':
            return CyclePlayer().move(cycle_memory)

        elif self.choice == 'random':
            return RandomPlayer().move()

        elif self.choice == 'fixed':
            return FixedPlayer().move()

        elif self.choice in moves:
            return self.choice

        elif self.choice == 'reflect':
            if len(stored_computer_move) == 0:

                while True:

                    print('\'ReflectPlayer\' option is not '
                          'available in the first round.')

                    return HumanPlayer().move(cycle_memory,
                                              stored_computer_move)

            else:
                return ReflectPlayer(stored_computer_move).move()
