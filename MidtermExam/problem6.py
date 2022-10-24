"""Midterm Exam, Problem 6.

Write a function to flatten a list. The list contains other lists, strings, or ints. For example,
[[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).
"""


def flatten(list_of_lists):
    """Flatten the list a list.

    Args:
        list_of_lists (list): list of lists

    Returns:
        list: Returns a copy of aList, which is a flattened version of aList
    """
    flatten_list = []
    for element in list_of_lists:
        if isinstance(element, list):
            flatten_list.extend(flatten(element))

        else:
            flatten_list.append(element)

    return flatten_list
