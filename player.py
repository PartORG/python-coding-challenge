def get_move(b, player):
    """get move from player, b = current board status
       player = current player
       returns the chosen field as int
    """
    chosen_field = int(input("Enter a field number from 1 - 9: ")) - 1 
    # -1 to have the right index for the board list
    return chosen_field


def check_valid_move(b, chosen_field):
    """ confirm if chosen field is already occupied
    """
    if b[chosen_field] == " ":
        return True
    else:
        return False


def switch_player(player): 
    """This function switches fom (current) player one to another player"""
    if player == "x":
        return "o"
    else:
        return "x"