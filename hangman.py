#import random and string library and our words list from words.py
import random
from words import words
import string

def get_valid_word(words): #choose a word from our imported list
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman(): 
    word = get_valid_word(words)
    word_letters = set(word)  #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guesssed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ',' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word] #shows the letter if it has been guessed or not
        print('Current word: ', ' '.join(word_list))

        user_letter  = input('Guess a letter: ').upper()
        if user_letter in  alphabet - used_letters: # if the character input is in the string alphabet
            used_letters.add(user_letter)
            if user_letter in word_letters: #if the character input is in the word set (the word to guess)
                word_letters.remove(user_letter)

            else: 
                lives = lives - 1 #takes away a life if wrong
                print('Letter is not in word.')

        elif user_letter in used_letters: #Character has already been used
            print('You have already used that character. Please try again.')
        
        else: #character is not valid
            print('You did not type in a valid character.')
    
    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word, '.')
    else:
        print('You guessed the word', word, '!!')

#start the program by calling the function
hangman()