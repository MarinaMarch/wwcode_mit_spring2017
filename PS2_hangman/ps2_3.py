# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 18:47:53 2017

@author: marina
"""
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):   
    correct = 0
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            correct += 1
            if correct == len(secret_word):
                return True
        else:
            return False


def get_guessed_word(secret_word, letters_guessed):    
    string = ""
    for i in secret_word:
        if i in letters_guessed:
            string += i
        else:
            string += '*'
    return string
guesses = 6
number_letters = 0
secret_word = choose_word(wordlist)

word = []



def get_available_letters(letters_guessed): 
  
    not_guessed = list(string.ascii_lowercase) 
    for i in letters_guessed:
        not_guessed.remove(i)
    return ("".join(not_guessed))

def warnings_left(warnings_remaining, guesses_remaining):
   
    if warnings_remaining > 0:
        warnings_remaining -= 1
       
    else:
        guesses_remaining -= 1
    return (warnings_remaining, guesses_remaining)

def get_unique_letters(secret_word):    
    letters = []
    for letter in secret_word:
        if letter not in letters:
            letters.append(letter)
            
    return len(letters)

def hangman(secret_word):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", str(len(secret_word)), "letters long.")
    print ("-------------")
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    while  guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
        print ("You have",str(guesses_remaining),"guesses left.")
        print ("Available letters:",get_available_letters(letters_guessed))
        guess=str(input("Please guess a letter: "))
        guess=guess.lower()
        while len(guess) > 1 or not guess.isalpha():
            warnings_remaining, guesses_remaining = warnings_left(warnings_remaining, guesses_remaining)
            print ("Oops! That is not a valid letter. You have: ",warnings_remaining, 'warnings remaining.')
            guess=str(input("Please, enter a letter: ")).lower()
            
        if guess not in letters_guessed:
            letters_guessed.append(guess)
            if guess in secret_word:
                print ("Good guess:")               
            elif guess in 'aeuio':
                guesses_remaining -= 2
                print ("Oops! That letter is not in my word")
            else:
                guesses_remaining -= 1
                print ("Oops! That letter is not in my word")
              
               
        else:
            warnings_remaining, guesses_remaining = warnings_left(warnings_remaining, guesses_remaining)
            print ("Oops! You've already guessed that letter:",warnings_remaining, 'warnings remaining')
        print (get_guessed_word(secret_word, letters_guessed))
        print ("------------")
    if is_word_guessed(secret_word, letters_guessed):
        print ("Congratulations, you won!")
        total_score = guesses_remaining * get_unique_letters(secret_word)
        print("Your total score for this game is:", total_score)
    else:
        print ("Sorry, you ran out of guesses. The word was", str(secret_word))

secret_word = choose_word(wordlist)
hangman(secret_word)
input("Press the enter key to exit.")






























        