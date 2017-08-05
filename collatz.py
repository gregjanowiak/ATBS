counter = 0

def collatzSequence(number):
    global counter

    if number % 2 == 0:
        result = number / 2
        counter += 1
        return result
    elif number % 2 == 1:
        result = 3 * number + 1
        counter += 1
        return result

while True: # loops the try/except statement until n is an integer
    try:
        n = int(input('Enter a number: '))
        break # breaks out of the loop if n is an integer
    except ValueError:
        print('Enter an integer value')

while n != 1:
    n = collatzSequence(n)
    print(int(n))

print("Done. Total iterations = {}".format(counter))
