"""Midterm Exam, Problem 5.

Write a Python function that returns a list of keys in aDict that map to integer values that are unique
(i.e. values appear exactly once in aDict). The list of keys you return should be sorted in increasing order.
(If aDict does not contain any unique values, you should return an empty list.)

This function takes in a dictionary and returns a list.
"""


# pylint: disable=C0103
def uniqueValues(aDict):
    """Return a list of keys in aDict that map to integer values that are unique.

    Args:
        aDict (dict): list of ints

    Returns:
        list: list of keys
    """
    listOfKeys = []

    for key in aDict.keys():
        uniqueCount = 0
        for value in aDict.values():
            if aDict[key] == value:
                uniqueCount += 1

        if uniqueCount == 1:
            listOfKeys.append(key)

    return sorted(listOfKeys)
