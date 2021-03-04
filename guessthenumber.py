#Program where you have to guess a number

import random #premade python package for functions

def guess(x):  # Our guess function with one parameter
    random_number = random.randint(1,x) #use randint to return a number between 1 and the parameter
    guess = 0 #initial guess
    while guess != random_number:  # main loop to determine your guess
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low')
        elif guess > random_number:
            print('Sorry, guess again. Too high')
    
    print(f'Yay! Congrats, you have guessed the number {random_number}!') #Final output after the game has been won

guess(10)