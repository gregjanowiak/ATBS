myPets = ['Zophie', 'Pooka', 'Fat-tail']

while len(myPets) > 0:
    print('Guess a pet name:')
    name = input()

    if name not in myPets:
        print('I don\'t have a pet named ' + name)
    else:
        print(name + ' is my pet.')
        myPets.remove(name)

print('No pets left to guess.')
