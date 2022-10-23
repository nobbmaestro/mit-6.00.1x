"""Problem Set 4, Problem 7 - You and your Computer.

Now that your computer can choose a word, you need to give the computer the option to play. Write the code that
re-implements the playGame function. You will modify the function to behave as described below in the function's
comments. As before, you should use the HAND_SIZE constant to determine the number of cards in a hand. Be sure to
try out different values for HAND_SIZE with your program.
"""

from ProblemSet4 import playHand
from ProblemSet4.lib import HAND_SIZE, compPlayHand, dealHand, loadWords


# pylint: disable=C0103
def playGame(wordList):
    """Play a game.

    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet.
          Please play a new hand first!"

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    while True:
        GAME_STATE = input('\nEnter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if GAME_STATE == 'e':
            break

        if GAME_STATE == 'n':
            hand = dealHand(HAND_SIZE)
            handCopy = hand.copy()

        elif GAME_STATE == 'r':
            try:
                hand = handCopy.copy()

            except UnboundLocalError:
                print('\nYou have not played a hand yet. Please play a new hand first!')

        else:
            print('Inproblem7.valid command.')

        PLAYER_SETTINGS = input('\nEnter u to have yourself play, c to have the computer play: ')

        if PLAYER_SETTINGS == 'u':
            playHand(hand, wordList, HAND_SIZE)

        elif PLAYER_SETTINGS == 'c':
            compPlayHand(hand, wordList, HAND_SIZE)

        else:
            print('Invalid command.')


def main():
    """Initialize the playGame."""
    wordList = loadWords()
    playGame(wordList)


if __name__ == '__main__':
    main()
