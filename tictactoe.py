"""
Tic Tac Toe Player
"""

import math
import copy

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

    if board == initial_state():
        return X

    Xc = 0
    Oc = 0
    for i in board:
        Xc += i.count("X")
        Oc += i.count("O")
    if Oc < Xc:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    set1 = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] is EMPTY:
                set1.add((i, j))
    return set1


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)
    # Check if the given action is valid
    if action[0] not in range(0, 3) or action[1] not in range(0, 3) or board[action[0]][action[1]] is not None:
        raise Exception("Invalid")
    # insert the action and return the new board
    board_copy[action[0]][action[1]] = player(board)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (board[0][0] == board[0][1] == board[0][2]) or (board[0][0] == board[1][0] == board[2][0]):
        if board[0][0] == "X":
            return X
        elif board[0][0] == "O":
            return O
    elif (board[1][0] == board[1][1] == board[1][2]) or (board[0][1] == board[1][1] == board[2][1])\
            or (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
        if board[1][1] == "X":
            return X
        elif board[1][1] == "O":
            return O
    elif (board[2][0] == board[2][1] == board[2][2]) or (board[0][2] == board[1][2] == board[2][2]):
        if board[2][2] == "X":
            return X
        elif board[2][2] == "O":
            return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True

    # Terminal if all cells have been filled
    all_moves = [cell for row in board for cell in row]
    if not any(move == EMPTY for move in all_moves):
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == "X":
        return 1
    elif win == "O":
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    global best_move
    if terminal(board):
        return None
    if player(board) == X:
        actions_set = actions(board)
        best_version = -math.inf
        for i in actions_set:
            result_board = result(board, i)
            max_version = min_value(result_board)
            if max_version > best_version:
                best_version = max_version
                best_move = i

    elif player(board) == O:
        actions_set = actions(board)
        best_version = math.inf
        for i in actions_set:
            result_board = result(board, i)
            min_version = max_value(result_board)
            if min_version < best_version:
                best_version = min_version
                best_move = i
    return best_move


def min_value(board):
    """
    Returns the minimum utility of the current board.
    """

    if terminal(board):
        return utility(board)

    v = math.inf
    actions_set = actions(board)
    for i in actions_set:
        v = min(v, max_value(result(board, i)))
    return v


def max_value(board):
    """
    Returns the maximum utility of the current board.
    """

    if terminal(board):
        return utility(board)

    v = -math.inf
    actions_set = actions(board)
    for move in actions_set:
        v = max(v, min_value(result(board, move)))
    return v
