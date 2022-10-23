"""DealHand."""
import random


# pylint: disable=C0103
def dealHand(n):
    """Return a random hand containing n lowercase letters.

    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    # pylint: disable=C0415
    from ProblemSet4.lib import CONSONANTS, VOWELS

    hand = {}
    numVowels = n // 3

    for _ in range(numVowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for _ in range(numVowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand
