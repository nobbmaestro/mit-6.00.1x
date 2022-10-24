"""Midterm Exam, Problem 4.

Write a Python function that returns the sublist of strings in aList that contain fewer than 4 characters.
For example, if aList = ["apple", "cat", "dog", "banana"], your function should return: ["cat", "dog"]

This function takes in a list of strings and returns a list of strings. Your function should not modify aList.
"""


# pylint: disable=C0103
def lessThan4(aList):
    """Return the sublist of strings in aList that contain fewer than 4 characters.

    Args:
        aList (list): a list of strings

    Returns:
        list: sublist of strings in aList that contain fewer than 4 characters
    """
    sublist = []
    for element in aList:
        if len(element) < 4:
            sublist.append(element)
    return sublist
