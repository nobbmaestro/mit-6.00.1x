"""IsWord."""


# pylint: disable=W1401
def is_word(word_list, word):
    """Determine if word is a valid word, ignoring capitalization and punctuation.

    Args:
        word_list (list): list of words in the dictionary.
        word (string): a possible word.

    Returns:
        bool: True if word is in word_list, False otherwise

    Example:
        >>> is_word(word_list, 'bat') returns
        True
        >>> is_word(word_list, 'asdf') returns
        False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")  # noqa: W605
    return word in word_list
