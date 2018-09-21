from IPython.display import clear_output
#index board and print it out
def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)
display_board(test_board)
display_board(test_board)

#write function to take input and assign to x or o

def player_input():

    # Keep asking player 1 to choose x or O

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or ): ').upper()
    if marker =='X':

        return ('X','O')
    else:
        return ('O','X')

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1,player2)

def place_marker(board, marker, position):

    board[position] = marker
