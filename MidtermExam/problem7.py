"""Midterm Exam, Problem 7.

Write a function called score that meets the specifications below.
"""


# pylint: disable=C0103
def score(word, f):
    """Get score based on following.

    1) Score for each letter is its location in the alphabet (a=1 ... z=26)
       times its distance from start of word.
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.

    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters.
       The first parameter to f is the highest letter score,
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the
           score for 'adD' is 12

    Args:
       word (str): string of length > 1 of alphabetical characters (upper and lowercase)
       f (func): a function that takes in two int arguments and returns an int

    Returns:
       Int: the score of word as defined by the method.
    """
    listScore = []
    for i, char in enumerate(word):
        scoreOfWord = (ord(char.lower()) - 96) * i
        listScore.append(scoreOfWord)

    listScore.sort(reverse=True)
    listScore = listScore[:2]
    return f(listScore[0], listScore[1])
