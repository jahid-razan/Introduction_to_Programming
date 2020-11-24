from check_inputs import print_sleep
from colorama import Fore, Back, Style, init
init(autoreset=True)


# this file implements the game_rules-
# Paper beats rock; rock beats scissors; scissors beat paper.

def rock_first(human_player, computer):
    """
    This function indicates the game rule when
    human_player chooses 'rock' as the move.
    If the computer chooses 'scissors' human wins.
    If the computer also chooses 'rock' the result is a tie.
    If the computer choose 'paper' it goes to the 'else'
    logic and the computer wins.

    input: string, human_player and computer moves
    output: string, returns the result that declares the winner
            between the the human player and the computer.
            The match can be a tie when both the players
            select the same move.
    """

    if human_player == 'rock':

        # if the human player select rock then this logic is activated
        if computer == 'scissors':
            print_sleep('You have won!')
            return 'You have won!'
        elif computer == 'rock':
            print_sleep('**It\'s a TIE**')
            return '**TIE**'
        else:
            print('Computer has won!')
            return 'Computer has won!'


def paper_first(human_player, computer):
    """
    This function indicates the game rule when
    human_player choose 'paper' as the move.
    If the computer chooses 'rock' human wins.
    If the computer also chooses 'paper' the result
    is a tie. if the computer choose 'scissors'
    it goes to the 'else' logic and the computer wins.

    input: string, human_player and computer moves
    output: string, returns the result that declares
            the winner between the the human player
            and the computer. The match can be a tie
            when both players select the same move.
    """

    if human_player == 'paper':
        # if the human player select paper then this logic is activated
        if computer == 'rock':
            print_sleep('You have won!')
            return 'You have won!'
        elif computer == 'paper':
            print_sleep('**It\'s a TIE**')
            return '**TIE**'
        else:
            print_sleep('Computer has won!')
            return 'Computer has won!'


def scissors_first(human_player, computer):
    """
    This function indicates the game rule when
    human_player chooses 'scissors' as the move.
    If the computer chooses 'paper' human wins.
    If the computer also chooses 'scissors'
    the result is a tie.
    if the computer choose 'rock' then it goes
    to the 'else' logic and the computer wins.

    input: string, human_player and computer moves
    output: string, returns the result that declares the winner between the
            the human player and the computer.
            The match can be a tie when both the players
            select the same move.
    """

    if human_player == 'scissors':
        # if the human player select scissors then
        # this logic is activated
        if computer == 'paper':
            print_sleep('You have won!')
            return 'You have won!'
        elif computer == 'scissors':
            print_sleep('**TIE**')
            return '**TIE**'
        else:
            print_sleep('Computer has won!')
            return 'Computer has won!'


def announce_winner(your_total_wins, total_computer_wins):
    """
    This function decalres the winner.
    The total human win indicated by 'your_total_wins' and
    the total computer wins is indicated by 'total_computer_wins'.
    The player with larger number of wins is declared as the winner.
    Incase of an equal score the result is a tie.
    """

    if your_total_wins > total_computer_wins:
        print("")
        print_sleep(
            Fore.YELLOW +
            'Wow!, Congratulations! You have been victorious!'
            ' This is some achievement!')

    elif your_total_wins == total_computer_wins:
        print("")
        print_sleep(
            Fore.GREEN +
            'The over result is a Tie, that\'s stil a formidable result!')

    else:
        print("")
        print_sleep(Fore.BLUE + 'Overall result: '
                    'Computer wins, better luck next time!')


def compete(response, human_player, computer, win_count):
    """
    This function lets the two input of human user and
    the computer to compete against each other
    by using the rock_first, paper_first and scissors_first
    options. At the end of the competition it appends
    the results in the 'win_count' list for three
    possible moves. The first logic appends the result
    when the human move is 'rock'.
    The second logic appends the result
    when the  human move is 'paper'.
    The third logic appends the result
    when the human move is 'scissors'.

    input: string- human_player and computer
           list- win_count

    """

    if human_player == 'rock':
        win_count.append(rock_first(human_player, computer))

    elif human_player == 'paper':
        win_count.append(paper_first(human_player, computer))

    else:
        win_count.append(scissors_first(human_player, computer))


def win_update(response, win_count):
    '''
    This function counts the win in each round
    based on the response of the computer player
    and the human player.It appends the text- 'You have won!'
    when the human wins and the text 'Computer has won'
    when the computer wins in the 'win_count' list.
    It also updates the total win by each player and prints,
    the updated later at the end of each round.

    '''

    your_total_wins = win_count.count('You have won!')
    total_computer_wins = win_count.count('Computer has won!')
    print_sleep(
        Fore.CYAN +
        f'Out of {response} rounds you have won: {your_total_wins}')
    print_sleep(Fore.YELLOW + f'Computer has won: {total_computer_wins}')
    print("")


def total_win_counter(response, win_count):
    '''
    This function counts the win in each round based
    on the response of the computer player and
    the human player.It appends the text-'You have won!'
    when the human wins and the text 'Computer has won'
    when the computer wins in the 'win_count' list.
    '''

    your_total_wins = win_count.count('You have won!')
    total_computer_wins = win_count.count('Computer has won!')
    return your_total_wins, total_computer_wins


def welcome_message():
    print_sleep('Welcome to the rock, paper and scissors game!')
    print_sleep('You can select the number of'
                ' rounds you want to play.')
    print_sleep('You can play between 1 to 99 rounds in each game')
    print_sleep('You can select one of moves from- rock, paper and'
                ' scissors.')
    print_sleep('You can also select one of the four computer players.')
    print_sleep('To select the RandomPlayer, please type- random.')
    print_sleep('To select the FixedPlayer, please type- fixed.')
    print_sleep('To select the ReflectPlayer, please type- reflect.')
    print_sleep('ReflectPlayer however is not available on the first round.')
    print_sleep('To select the CyclePlayer, please type- cycle.')
    print_sleep('In this game: paper beats rock'
                ' rock beats scissors, scissors beat paper.')
