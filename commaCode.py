x = []

def commaCode(listVal):
    result = ''
    for i in listVal:
        if listVal.index(i) == len(listVal) - 1:
            result += ', and ' + i
        elif listVal.index(i) == 0:
            result += i
        else:
            result += ', ' + i
    print(result)

while True:
    print('Enter the name of an animal (Or enter nothing to stop):')
    name = input()
    if name == '':
        break
    x += [name]

commaCode(x)
