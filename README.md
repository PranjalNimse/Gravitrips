# Gravitrips
-----------------------------------------------------------------------------------------------------------------------
Project 1 for 'foundations of artificial intelligence' course: Gravitrips(also known as connect 4)
-----------------------------------------------------------------------------------------------------------------------
NAME: Pranjal Nimse
-----------------------------------------------------------------------------------------------------------------------
DESCRIPTION :

For the project, I have implemented the gravitrips (also known as connect 4) game using minimax, alpha beta pruning
and cutting off strategy for predicting the next possible move in gravitrips game.

What's different?
--> The game continues until either human player wins or computer player wins. If the board if full before that, it is
    a draw. If a player has placed 4 discs on either horizontally, vertically or diagonally, that player is declared as
    the winner.
-----------------------------------------------------------------------------------------------------------------------
STRUCTURE OF THE CODE :

The game uses two python files called gravitrips.py and GravitripsGame.py.

gravitrips.py file has functions to perform basic operations like taking user inputs and set up the gameboard and
call the AI algorithm to predict next moves.

GravitripsGame.py file has the function to perform the AI algorithms and also calculate the evaluation function.

The algorithm is implemented in the function aiPlay() and it uses minimax with alpha-beta pruning and cutting
off strategy.
-----------------------------------------------------------------------------------------------------------------------
HOW TO RUN THE CODE:

Run the gravitrips.py file.

Terminal command: $python gravitrips.py
-----------------------------------------------------------------------------------------------------------------------

EVALUATION FUNCTION : (FOR APPLYING CUT OFF STRATEGY)

We have implemented a evaluation function for depth limited minimax in order to calculate the utility value which will
be used by the algorithm to determine the next best possible move.
The computer will choose the highest utility value it finds while calculating and it will choose the corresponding
column to play its next move.
Firstly it will check if it can get consecutive fours, then threes and lastly twos.
Here we calculate the number of possible fours, threes and twos that the human can make and subtract them from
the opponent.

utility_value = (my_fours * 10 + my_threes * 5 + my_twos * 2)- (comp_fours *10 + comp_threes * 5 + comp_twos * 2).
Once the utility values are calculated, the column which has the highest corresponding value is chosen and then
the move is played.
---------------------------------------------------------------------------------------------------------------------
