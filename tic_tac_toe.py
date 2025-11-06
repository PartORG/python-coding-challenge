import board as b
import player as pl 
import logic

def main():
    board = b.create_empty_board()
    player = "x"

    while True:
        b.show_board(board)
        move = pl.get_move(board, player)

        if pl.check_valid_move(board, move):
            b.make_move(board, player, move)

            if logic.check_win(board, player):
                b.show_board(board)
                print(f"Player {player} wins!")
                break

            elif logic.check_draw(board):
                b.show_board(board)
                print("It's a draw!")
                break

            player = pl.switch_player(player)
        else:
            print("Invalid move. Choose a different field.")


# Tic-tac-toe game
if __name__ == "__main__":
    main()