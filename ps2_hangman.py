# Program Solving with Python/Intro to Competitive Programming, Fall 2021
# Eternal University, Baru Sahib
# Cite: John Guttag. 6.00SC Introduction to Computer Science and Programming. Spring 2011. Massachusetts Institute of Technology: MIT OpenCourseWare, https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011. License: Creative Commons BY-NC-SA.
#
#
# Problem Set 2
# Hangman
#
#
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME)
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

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
print("Welcome")
def Hangman_game(): 
    choosed_word = choose_word(wordlist)
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(choosed_word)) +' letters long.')
    number_of_guess = len(choosed_word) * 2
    gusses = ''
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    while(number_of_guess !=0):
        print('-------------')
        print('You have '+ str(number_of_guess) +' guesses left.')
        print('Available letters: ',''.join(letters))
        letter = input("Please guess a letter: ")        
        gusses = gusses +letter.lower()
        word = ''
        for char in choosed_word:
            if char in gusses:
               word = word + char + ' '
            else:
                word = word + '- ' 
        print('')           
        if letter in choosed_word:
           print('Good guess:',word)
           if letter in letters:
              letters.remove(letter) 
           if word.replace(' ','') == choosed_word:
               return True    
        else:
            print('Oops! That letter is not in my word:' ,word)
            if letter in letters:
                letters.remove(letter)
            number_of_guess = number_of_guess - 1  
    print("you loose")
    print('word was',choosed_word)        


if Hangman_game():
    print("Congratulation, you won!")
    
        
    
    
