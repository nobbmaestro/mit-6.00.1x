"""Problem Set 1, Problem 2.

Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl',
then your program should print following
>>> Number of times bob occurs is: 2
"""


# pylint: disable=C0103
def bob_in_string_count(s):
    """Return the number of times the string 'bob' occurs in s.

    Args:
        s (str): string of chars.

    Returns:
        int: number of bobs in s.
    """
    numBob = 0
    for i in range(len(s) - 2):
        temp = s[i] + s[i + 1] + s[i + 2]
        if temp == 'bob':
            numBob += 1

    return numBob
