"""
Tic Tac Toe Player
"""

import math
import numpy as np

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # raise NotImplementedError

    # Count the number of X's and O's on the board
    # X gets first move, so if count is even, it's X's turn
    count = 0
    for row in board:
        for cell in row:
            if cell == X or cell == O:
                count += 1

    if count % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # raise NotImplementedError


    # All possible actinos are the empty cells on the board
    actions = []
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                actions.append((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # raise NotImplementedError

    
    # Make a deep copy of the board
    new_board = []
    for row in board:
        new_board.append(row.copy())

    # Check if action is valid
    if new_board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid action! The cell is not empty.")

    # Make move
    new_board[action[0]][action[1]] = player(board)
    return new_board
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # raise NotImplementedError

    
    # Checking Rows
    for row in board:
        if len(set(row))==1 and row[0] != EMPTY:
            return row[0]
        
    
    #Checking diagonals
    # using set to check if all elements are the same (set stores value once)
    # checking for (0,0),(1,1),(2,2)
    if len(set([board[i][i] for i in range(len(board))]))==1 and board[0][0] != EMPTY:
        return board[0][0]
    
    #checking for (0,2),(1,1),(2,0
    if len(set([board[i][len(board)-i-1] for i in range(len(board))]))==1 and board[0][len(board)-1] != EMPTY:
        return board[0][len(board)-1]


    # Checking Columns
    board_T = np.transpose(board)
    for row in board_T:
        if len(set(row))==1 and row[0] != EMPTY:
            return row[0]

        


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # raise NotImplementedError

    if winner(board):
        return True

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == None:
                return False

    return True       


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # raise NotImplementedError

    if winner(board) != None:
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # raise NotImplementedError
    # MinMax Search Algorithm 

    current_player = player(board)

    if current_player == 'X':
        value = -math.inf
        for action in actions(board):
            new_value = min_value(result(board, action))
            if new_value > value:
                value = new_value
                optimal_action = action
    else:
        value = math.inf
        for action in actions(board):
            new_value = max_value(result(board, action))
            if new_value < value:
                value = new_value
                optimal_action = action

    return optimal_action


def max_value(board):
    if terminal(board):
        return utility(board)
    
    value = -math.inf
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value


def min_value(board):
    if terminal(board):
        return utility(board)
    
    value = math.inf
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value
