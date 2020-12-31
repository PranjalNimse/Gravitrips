from pip._vendor.distlib.compat import raw_input

from GravitripsGame import GravitripsGame


def start_playing(board, next_player):
    board.count_score()
    board.check_winner()
    if board.win_value == 1:
        print("You won!")
        return
    elif board.win_value == 2:
        print("Computer won!")
        return

    board.display_gameboard()
    print('Score ==> Your score = %d, Computer score = %d\n' % (board.player1Score, board.player2Score))

    if next_player == 'human':
        while True:

            try:
                userMove = int(input("Your turn. \n Enter the column number from 1 to 7 where you want to play : "))
            except ValueError:
                print("Invalid choice. Try again!")
            if not 0 < userMove < 8:
                print("Column number not valid. Enter again!")
                continue
            if not board.playPiece(userMove - 1):
                print("Column number: %d is full. Try other column." % userMove)
                continue

            print("You made a move in column number:: " + str(userMove))
            board.display_gameboard()
            board.count_score()
            board.check_winner()
            if board.win_value == 1:
                print("You won!")
                print("Game Over")
                return
            elif board.win_value == 2:
                print("Computer won!")
                print("Game Over")
                return

            if board.getPieceCount() == 42:
                print("The game is a Tie !")
                print("Game Over")
                break
            else:
                print("Computer is making a decision for next " + str(board.depth) + " steps...")
                board.change_move()
                board.aiPlay()
                board.display_gameboard()
                board.count_score()
                board.check_winner()
                if board.win_value == 1:
                    print("You won!")
                    print("Game Over")
                    return
                elif board.win_value == 2:
                    print("Computer won!")
                    print("Game Over")
                    return
                print('Score ==> Your score = %d, Computer score = %d\n' % (board.player1Score, board.player2Score))

    else:
        board.count_score()
        board.check_winner()
        if board.win_value == 1:
            print("You won!")
            print("Game Over")
            return
        elif board.win_value == 2:
            print("Computer won!")
            print("Game Over")
            return

        else:
            board.aiPlay()
            board.display_gameboard()
            print('Scores ==> Your score = %d, Computer score = %d\n' % (board.player1Score, board.player2Score))
            start_playing(board, 'human')


if __name__ == "__main__":

    playing = True
    while playing:
        try:
            gameboard = GravitripsGame()
            gameboard.current_move = 1
            gameboard.checkPieceCount()
            # hard-coded depth value. Can also be taken as user input if required
            gameboard.depth = 3
            # prompts user to make a move first
            # Player 1 = human and Player 2 = computer
            start_playing(gameboard, 'human')

            while True:
                try:
                    option = raw_input("Do you want to play again? (Y/N)")
                except ValueError:
                    print
                    "Please input a correct value. Try again."
                    continue
                if option == 'Y' or option == 'y':
                    break
                elif option == 'N' or option == 'n':
                    playing = False
                    break
                else:
                    print("Please enter Y or N (yes or no).")
        except:
            print("Something went wrong! Try playing again.")
