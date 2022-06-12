# Problem Set 3, Problem 4 - The Game
#
# Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. 
# This starts up an interactive game of Hangman between the user and the computer. Be sure you take advantage of 
# the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the 
# previous part.
#
# Hints:
# You should start by noticing where we're using the provided functions (at the top of ps3_hangman.py) to load 
# the words and pick a random one. Note that the functions loadWords and chooseWord should only be used on your 
# local machine, not in the tutor. When you enter in your solution in the tutor, you only need to give your 
# hangman function.
#
# Consider using lower() to convert user input to lower case. For example:
#   guess = 'A'
#   guessInLowerCase = guess.lower()
#
# Consider writing additional helper functions if you need them!
#
# There are four important pieces of information you may wish to store:
#   1. secretWord: The word to guess.
#   2. lettersGuessed: The letters that have been guessed so far.
#   3. mistakesMade: The number of incorrect guesses made so far.
#   4. availableLetters: The letters that may still be guessed. Every time a player guesses a letter, the guessed 
#      letter must be removed from availableLetters (and if they guess a letter that is not in availableLetters, you 
#      should print a message telling them they've already guessed that - so try again!).

from ProblemSet3.lib import loadWords, chooseWord
from ProblemSet3 import isWordGuessed, getGuessedWord, getAvailableLetters

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')

    lettersGuessed = []
    guesses = 8
    while True:
        print('-------------')
        print('You have ' + str(guesses) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ')

        while len(guess) != 1 or not(guess.isalpha()):
            print('Provide only a letter!')
            guess = input('Please guess a letter: ')

        if guess in lettersGuessed:
            print('Oops! You\'ve already guessed that letter: ' + getGuessedWord(secretWord, lettersGuessed))
        elif not(guess in secretWord):
            lettersGuessed.append(guess.lower())
            print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
            guesses -= 1
        else:
            lettersGuessed.append(guess.lower())
            print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))

        if isWordGuessed(secretWord, lettersGuessed):
            print('------------')
            print('Congratulations, you won!')
            break

        elif guesses == 0:
            print('------------')
            print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
            break

def main():
    wordlist = loadWords()
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)

if __name__ == '__main__':
    main()