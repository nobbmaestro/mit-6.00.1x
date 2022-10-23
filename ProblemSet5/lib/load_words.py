"""LoadWords."""


def load_words(file_name):
    """Load words.

    Args:
        file_name (string): the name of the file containing the list of words to load

    Returns:
        list: a list of valid words. Words are strings of lowercase letters.
    """
    # print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    # print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list
