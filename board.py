def create_empty_board():      ##function for creating empty boards
    return [" "]*9

def show_board(b):
    print(f"{b[0]}|{b[1]}|{b[2]}\n-+-+-\n{b[3]}|{b[4]}|{b[5]}\n-+-+-\n{b[6]}|{b[7]}|{b[8]}")

def make_move(b, player, field):
    """This function locates the player's symbol into the chosen board field"""
    b[field] = player       
