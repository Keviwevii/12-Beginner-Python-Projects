import random

def play():  #Our main function that asks for choices and has outputs
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])
    print(f'Your choice is {user} and the computer has chosen {computer}')

    if user == computer:
        return "It's a tie!"

    # r > s, s > p, p > r
    if is_win(user,computer): #Calls our is_win functino with user and computer as arguments
        return 'You won!'

    return 'You lost!'

def is_win(player,opponent): 
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r') :
        return True

print(play())