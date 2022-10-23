"""Problem Set 4, Problem 6 - Playing a Game.

A game consists of playing multiple hands. We need to implement one final function to complete our word-game program.
Write the code that implements the playGame function. You should remove the code that is currently uncommented in the
playGame body. Read through the specification and make sure you understand what this function accomplishes. For the
game, you should use the HAND_SIZE constant to determine the number of cards in a hand.

Testing: Try out this implementation as if you were playing the game. Try out different values for HAND_SIZE with
your program, and be sure that you can play the wordgame with different hand sizes by modifying only the variable
HAND_SIZE.
"""

from ProblemSet4 import playHand
from ProblemSet4.lib import HAND_SIZE, dealHand, loadWords


# pylint: disable=C0103
def playGame(wordList):
    """Play a game.

    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.

    2) When done playing the hand, repeat from step 1
    """
    while True:
        GAME_STATE = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if GAME_STATE == 'e':
            break

        if GAME_STATE == 'n':
            hand = dealHand(HAND_SIZE)
            handCopy = hand.copy()
            playHand(hand, wordList, HAND_SIZE)

        elif GAME_STATE == 'r':
            try:
                hand = handCopy.copy()
                playHand(hand, wordList, HAND_SIZE)
            except UnboundLocalError:
                print('You have not played a hand yet. Please play a new hand first!')

        else:
            print('Invalid command.')


def main():
    """Initialize the playGame."""
    wordList = loadWords()
    playGame(wordList)


if __name__ == '__main__':
    main()
