"""Problem Set 3, Problem 1 - Is the Word Guessed.

Please read the Hangman Introduction before starting this problem. We'll start by writing 3 simple functions that
will help us easily code the Hangman problem. First, implement the function isWordGuessed that takes in two
parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a boolean - True
if secretWord has been guessed (ie, all the letters of secretWord are in lettersGuessed) and False otherwise.

Example Usage:
>>> secretWord = 'apple'
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(isWordGuessed(secretWord, lettersGuessed))
False

For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.
"""


# pylint: disable=C0103
def isWordGuessed(secretWord, lettersGuessed):
    """Check if word is already gueased.

    Args:
        secretWord (str): the word the user is guessing
        lettersGuessed (list): what letters have been guessed so far

    Returns:
        bool: True if all the letters of secretWord are in lettersGuessed
    """
    for letter in secretWord:
        if (letter in lettersGuessed) is False:
            return False
    return True
