import random
y = int(input('Input a Upper Limit Number: '))
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess > random_number:
            print('Guess Lower :)')
        elif guess < random_number:
            print('Guess Higher :)')
    print('Congrats!!!!! You Guessed Right')


print('Imagine a number in your mind and let the Computer guess it!!!!! Fun, right?')
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'CORRECT':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'Is {guess} too High (HIGH), too low (LOW), or correct (CORRECT): ')
        if feedback == 'HIGH':
            high = guess-1
        elif feedback == 'LOW':
            low = guess + 1

    print(f'Hurray!!!!! The Computer guessed your number {guess} correctly!!')


print(guess(y))
print(computer_guess(250))