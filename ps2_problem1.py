# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 17:11:42 2017

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

wordlist = load_words()

guesses = 0
number_letters = 0
secret_word = choose_word(wordlist)
word = []
 
while number_letters < len(secret_word) and guesses < 7:
    letter = input("Enter the lettr: ")
    if letter in secret_word: 
        print("You are on the right track, this letter is in the word!")
        number_letters += 1
        word += letter
        print(''.join([char if char in word else ' _ ' for char in secret_word]))    
        if number_letters==len(secret_word):
                    print("You win!")
    elif letter is not secret_word: 
        guesses += 1
        print("You did not guess.")
        if guesses == 7:         
            print("Game over!", end = " " )
            print("The word was: ", secret_word)
            
            
    





















