import sys

counter = 0

print('Enter a number')

try:
    number = int(input('> '))
except ValueError:
    print('Please enter an integer.')

def collatz(number):
    global counter

    while number != 1:
        if number % 2 == 0:
            number = number / 2
            counter += 1
            print(int(number))
        elif number % 2 == 1:
            number = 3 * number + 1
            counter += 1
            print(int(number))
    print('Collatz sequence complete.\nIterations: {}'.format(counter))

collatz(number)
