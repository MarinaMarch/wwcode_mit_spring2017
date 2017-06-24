# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 13:35:36 2017

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



def get_available_letters(letters_guessed):  
    available_letters = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available_letters = available_letters + letter    
    return available_letters

    

def get_unique_letters(secret_word):   
    letters = []
    for letter in secret_word:
        if letter not in letters:
            letters.append(letter)            
    return len(letters)



def match_with_gaps(my_word, other_word):   
    my_word = my_word.replace(' ','')
    other_word = other_word.replace(' ','')    
    if len(my_word) != len(other_word):
        return False    
    my_word_list = list(my_word)
    other_word_list = list(other_word)    
    i = 0
    for letter in my_word_list:
        if letter != '*':
            if my_word_list.count(letter) != other_word_list.count(letter):
                return False
            if letter != other_word_list[i]:
                return False
        i += 1    
    return True



def show_possible_matches(my_word):  
    matches = False
    match_list = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            match_list.append(word)
            matches = True    
    if matches:
        print("Possible word matches are:")
        print(' '.join(match_list))
    else:
        print("No matches found")
        
        

def get_unique_letters(secret_word):    
    letters = []
    for letter in secret_word:
        if letter not in letters:
            letters.append(letter)            
    return len(letters)



def hangman_with_hints(secret_word):
    print("Welcome to the game Hangman!") 
    warnings_remaining = 3
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", warnings_remaining, "warnings left.")    
    letters_guessed = []
    guesses_remaining = 6    
    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
        print ("-------------")
        print("You have", guesses_remaining, "guesses left")
        print("Available letters:", get_available_letters(letters_guessed))    
        guess = input("Please guess a letter: ")        
        if guess == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        else:
            if not str.isalpha(guess):
                print( "Oops! That is not a valid letter.")
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    print("You have " + str(warnings_remaining) + " warnings left.")
                else:
                    guesses_remaining -= 1
                    print("You have no warnings left so you lose one guess:")
            else:
                guess = str.lower(guess)                
                if guess in letters_guessed:
                    print("Oops! You've already guessed that letter.")
                    if warnings_remaining > 0:
                        warnings_remaining -= 1
                        print ("You have " + str(warnings_remaining) + " warnings left.")
                    else:
                        guesses_remaining -= 1
                        print("You have no warnings left so you lose one guess.")
                else:
                    letters_guessed.append(guess)
                    if guess in secret_word:
                        print( "Good guess:", get_guessed_word(secret_word, letters_guessed))
                    else:
                        if guess in 'aeuio':
                            guesses_remaining -= 2
                        else:
                            guesses_remaining -= 1                        
                        print("Oops! That letter is not in my word:" , get_guessed_word(secret_word, letters_guessed))
    
    print ("-------------")
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        total_score = guesses_remaining * get_unique_letters(secret_word)
        print("Your total score for this game is:", total_score)
    else:
        print("Sorry, you ran out of guesses. The word was else.")


if __name__ == "__main__":
        
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
input("Press the enter key to exit.")    