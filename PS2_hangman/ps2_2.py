# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 19:10:49 2017

@author: marina
"""
import random
import string
#
#WORDLIST_FILENAME = "words.txt"
#
#
#def load_words():
#    """
#    Returns a list of valid words. Words are strings of lowercase letters.
#    
#    Depending on the size of the word list, this function may
#    take a while to finish.
#    """
#    print("Loading word list from file...")
#    # inFile: file
#    inFile = open(WORDLIST_FILENAME, 'r')
#    # line: string
#    line = inFile.readline()
#    # wordlist: list of strings
#    wordlist = line.split()
#    print("  ", len(wordlist), "words loaded.")
#    return wordlist
#
#
#
#def choose_word(wordlist):
#    """
#    wordlist (list): list of words (strings)
#    
#    Returns a word from wordlist at random
#    """
#    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
#wordlist = load_words()
#
secret_word= 'apple'
letters_guessed= ['e', 'i', 'k', 'p', 'r', 's'] 


def is_word_guessed(secret_word, letters_guessed):   
    correct = 0
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            correct += 1
            if correct == len(secret_word):
                return True
        else:
            return False
is_word_guessed(secret_word, letters_guessed)

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
#secret_word = choose_word(wordlist)
word = []
print(get_guessed_word(secret_word, letters_guessed))



def get_available_letters(letters_guessed): 
  
    not_guessed = list(string.ascii_lowercase) 
    for i in letters_guessed:
        not_guessed.remove(i)
    return ("".join(not_guessed))
print(get_available_letters(letters_guessed))
    
   
