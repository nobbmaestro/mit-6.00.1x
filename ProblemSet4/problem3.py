"""Problem Set 4, Problem 3 - Valid Words.

At this point, we have written code to generate a random hand and display that hand to the user. We can also
ask the user for a word (Python's input) and score the word (using your getWordScore). However, at this point
we have not written any code to verify that a word given by a player obeys the rules of the game. A valid word
is in the word list; and it is composed entirely of letters from the current hand.
Implement the isValidWord function.

Testing: Make sure the test_isValidWord tests pass. In addition, you will want to test your implementation by
calling it multiple times on the same hand - what should the correct behavior be? Additionally, the empty string
('') is not a valid word - if you code this function correctly, you shouldn't need an additional check for this
condition.

Fill in the code for isValidWord in ps4a.py and be sure you've passed the appropriate tests in test_ps4a.py
before pasting your function definition here.
"""
# pylint: disable=R0401
from ProblemSet4.lib import getFrequencyDict


# pylint: disable=C0103
def isValidWord(word, hand, wordList):
    """Check the validity of the word.

    Return True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    Args:
        word (str): string (lowercase letters)
        hand (dict): dictionary (string -> int)
        wordList (list): list of lowercase strings

    Returns:
        list: wordList, list of lowercase strings
    """
    if len(word) == 0:
        return False

    if word not in wordList:
        return False

    Freq = getFrequencyDict(word)
    try:
        for char in Freq:
            if not (hand.get(char) >= Freq.get(char)):
                return False

        return True

    except TypeError:
        return False
