def check_win(board, player):
    """
    Check if the player has a winning combination.

    :param board: Current board status list.
    :param player: Player symbol to check for a win.
    """

    # Define all possible winning combinations
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # winning rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # winning columns
        (0, 4, 8), (2, 4, 6)              # winning diagonals
    ]

    # for a, b, c in wins:
    #     if board[a] == player and board[b] == player and board[c] == player:
    #         return True
    # return False
    
    # Go through each winning combination and check if the player occupies all three positions
    return any(board[a] == board[b] == board[c] == player for a, b, c in wins)


def check_draw(board):
    """
    Check if the board is full.

    :param board: Current board status list.
    """

    # Check if the board is full
    return " " not in board