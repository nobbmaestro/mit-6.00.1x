"""LoadWords."""

WORDLIST_FILENAME = "ProblemSet3/lib/words.txt"


# pylint: disable=C0103
def loadWords():
    """
    Return a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    # print("  ", len(wordlist), "words loaded.")
    return wordlist
