"""Problem Set 4, Problem 4 - Hand Length.

We are now ready to begin writing the code that interacts with the player. We'll be implementing the playHand function.
This function allows the user to play out a single hand. First, though, you'll need to implement the helper
calculateHandlen function, which can be done in under five lines of code.
"""


# pylint: disable=C0103
def calculateHandLen(hand):
    """Return the length (number of letters) in the current hand.

    Args:
        hand (dict): dictionary (string -> int)

    Returns:
        int: length of the hand
    """
    length = 0
    for char in hand:
        length += hand.get(char)

    return length
