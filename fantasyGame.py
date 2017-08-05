bag = {'arrow':5,'coin':100, 'dagger':1,'torch':2,'rope':0}
satchel = {'arrow':2,'coin':500, 'dagger':1,'torch':0,'rope':1}

def displayInventory(inventory):
    global bag
    global satchel

    total = 0
    if inventory == 'bag':
        print('Inventory:')
        for k, v in bag.items():
            print(str(v) + ' ' + str(k))
            total += v
        print('Total number of items: ' + str(total))
        return 'bag'
    elif inventory == 'satchel':
        print('Inventory:')
        for k, v in satchel.items():
            print(str(v) + ' ' + str(k))
            total += v
        print('Total number of items: ' + str(total))
        return 'satchel'

def addToInventory(selection):
    global bag, satchel
    coins = ['coin','coin','coin','coin','coin']

    if selection == 'bag':
        selection = bag
    elif selection == 'satchel':
        selection = satchel

    for i in coins:
        selection['coin'] += 1
    displayInventory(selection) # bug: displays correct inventory but not updated

inv = input('What inventory do you want to check? (bag/satchel)\n> ')
displayInventory(inv)

add = input('Would you like to deposit 5 coins to an inventory? (bag/satchel)\n> ')
if add == 'Y':
    addToInventory(displayInventory(inv))
else:
    print('Okay, your list is unchanged.')
