WORDLIST_FILENAME = "ProblemSet4/lib/given_data/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    if len(wordList) == 1:
        wordList = wordList_helper(wordList)
    print("  ", len(wordList), "words loaded.")
    inFile.close()
    return wordList

def wordList_helper(wordList):
    return list(wordList[0].split(' '))