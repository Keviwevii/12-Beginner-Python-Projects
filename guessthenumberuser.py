#inverted program of guess the number where the computer guesses

import random #premade python package for functions

def computer_guess(x): #Our main function with one parameter for our highest number
    low = 1   #declare our lowest and highest variables for range
    high = x
    feedback = '' 
    while feedback != 'c': #c means correct
        if low != high: #we need to cover if the low and high are equal
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?').lower() #feeback will change any input to lower to check conditions
        if feedback == 'h':   #The highest or lowest needs to change depending on feedback
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly') #Final output statements once correct

computer_guess(73)