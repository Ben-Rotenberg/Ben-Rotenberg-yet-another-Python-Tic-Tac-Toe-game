
import random


def display_board(board):
    print('\n'*100)
    print(board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    print('-------------')
    print(board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('-------------')
    print(board[1] + '  |  ' + board[2] + '  |  ' + board[3])


def player_input():
    ''' OUTPUT = (Player 1 marker , layer 2 marker) '''

    marker = 'o'
    while not (marker =='X' or marker =='O'):
        marker = input('Player 1: Choose X or O').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


def place_marker (board, marker, position):
    board[position] = marker

def win_check(board, marker):
    return ((board[7] == board[8] == board[9] == marker) or
            (board[4] == board[5] == board[6] == marker) or
            (board[1] == board[2] == board[3] == marker) or
            (board[1] == board[4] == board[7] == marker) or
            (board[2] == board[5] == board[8] == marker) or
            (board[3] == board[5] == board[9] == marker) or
            (board[1] == board[5] == board[9] == marker) or
            (board[3] == board[5] == board[7] == marker))

def chooos_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check (board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False

    return True


def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board,position):
        try:
            position = int(input('Choose a position: (1-9)'))
        except ValueError:
            pass
    return position


def replay():
   return input('Do you want to play again? Enter Y or N: ').lower().startswith('y')


print('Welcome to Tic Tac Toe')

while True:
    the_board = [' '] * 10

    player1_marker, player2_marker = player_input()

    turn = chooos_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? Y  or n').upper()
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won!!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break