"""Problem Set 3, Problem 3 - Printing Out all Available Letters.

Next, implement the function getAvailableLetters that takes in one parameter - a list of letters,
lettersGuessed. This function returns a string that is comprised of lowercase English letters - all
lowercase English letters that are not in lettersGuessed.

Example Usage:
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getAvailableLetters(lettersGuessed))
abcdfghjlmnoqtuvwxyz

Note that this function should return the letters in alphabetical order, as in the example above.

For this function, you may assume that all the letters in lettersGuessed are lowercase.

Hint: You might consider using string.ascii_lowercase, which is a string comprised of all lowercase letters.
"""

import string


# pylint: disable=C0103
def getAvailableLetters(lettersGuessed):
    """Return a string that is comprised of lowercase English letters.

    Args:
        lettersGuessed (str): a list of letters

    Returns:
        list: a list of letters
    """
    alphabeth = string.ascii_lowercase
    availableLetters = ""
    for letter in alphabeth:
        if not (letter in lettersGuessed):
            availableLetters += letter

    return availableLetters
