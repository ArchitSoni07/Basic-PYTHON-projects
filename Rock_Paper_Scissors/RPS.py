import random

def play():
    user = input("Choose between 'rock', 'paper' and 'scissors':  ")
    computer = random.choice(['rock','paper','scissors'])
    print(f'You chose {user} and the computer chose {computer}')
    if user == computer:
        return 'It\'s a tie'

    if is_win(user,computer):
        return 'You Won!!!!!'

    return 'Lost!!!'

def is_win(player,opponent):
    if(player == 'r' and opponent == 's') or \
    (player == 's' and opponent == 'p') or \
    (player == 'p' and opponent == 'r'):
        return True 

print(play())