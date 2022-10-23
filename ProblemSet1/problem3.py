"""Problem Set 1, Problem 3.

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print
>>> Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
>>> Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this
problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem
after you've had a break and cleared your head.
"""

import string


# pylint: disable=C0103
def find_longest_substring_in_string(s):
    """Return the longest substring of s in which the letters occur in alphabetical order.

    Args:
        s (str): string of chars.

    Returns:
        str: longest string.
    """
    temp = substring = s[0]
    list_of_substrings = []
    longest_substring = 0

    for char in s[1:]:
        if string.ascii_lowercase.index(temp) <= string.ascii_lowercase.index(char):
            substring += char
            temp = char
        else:
            list_of_substrings.append(substring)
            if len(substring) > len(list_of_substrings[longest_substring]):
                longest_substring = list_of_substrings.index(substring)
            substring = temp = char

    list_of_substrings.append(substring)
    return list_of_substrings[longest_substring]
