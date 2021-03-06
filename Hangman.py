# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/Users/FrankFamily/Downloads/ProblemSet4/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    isGuessed = True
    isLetterGuessed = False
    for char in secretWord:
        for letter in lettersGuessed:
            if char == letter:
                isLetterGuessed = True
        if isLetterGuessed == False:
            isGuessed = False
        isLetterGuessed = False
    return isGuessed



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    answer = ''
    letterUsed = False
    for char in secretWord:
        for letter in lettersGuessed:
            if char == letter:
                letterUsed = True
        if letterUsed == True:
            answer += char
        else:
            answer += '_ '
        letterUsed = False
    return answer



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = ''
    letterUsed = False
    for char in string.ascii_lowercase:
        for letter in lettersGuessed:
            if char == letter:
                letterUsed = True
        if letterUsed == False:
            availableLetters += char
        letterUsed = False
    return availableLetters
    

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
    state = 0
    numberOfGuessesLeft = 8
    guessedLetters = []
    userInput = ''
    letterAlreadyGuessed = False
    letterIsCorrect = False
    
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print('-------------')
    while state == 0:
        print('You have ' + str(numberOfGuessesLeft) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(guessedLetters)),
        userInput = str(raw_input('Please guess a letter: ')),
        
        for char in guessedLetters:
            char = tuple(char)
            if userInput == char:
                letterAlreadyGuessed = True
                break
        if letterAlreadyGuessed == True:
            print('Oops! You\'ve already guessed that letter: ' + getGuessedWord(secretWord, guessedLetters))
        else:
            guessedLetters += userInput
            for char in secretWord:
                char = tuple(char)
                if userInput == char:
                    print('Good guess: ' + getGuessedWord(secretWord, guessedLetters))
                    letterIsCorrect = True
                    break
            if letterIsCorrect == False:
                print('Oops! That letter was not in my word: ' + getGuessedWord(secretWord, guessedLetters))
                numberOfGuessesLeft -= 1
        letterIsCorrect = False
        letterAlreadyGuessed = False
        
        if isWordGuessed(secretWord, guessedLetters) == True:
            state = 1
        if numberOfGuessesLeft == 0:
            state = 2
            
        print('------------')
    if state == 1:
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was ' + 'secretWord' + '.')


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)