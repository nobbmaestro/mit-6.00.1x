"""ChooseWord."""

import random


# pylint: disable=C0103
def chooseWord(wordlist):
    """
    Wordlist (list): list of words (strings).

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
