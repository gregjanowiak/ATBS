import random

secretNumber = random.randint(1, 20)

print('I am thinking of a number between 1 and 20.')

for guessesTaken in range(1, 6):
    print('Take a guess:')
    guess = int(input('> '))

    if guess > secretNumber:
        print('Too high')
    elif guess < secretNumber:
        print('Too low')
    else:
        break

if guess == secretNumber:
    print('Good job! You got the number in {} guesses'.format(guessesTaken))
else:
    print('Sorry, the number I was thinking of was {}'.format(secretNumber))
