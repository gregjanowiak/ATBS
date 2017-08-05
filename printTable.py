#! /usr/bin/env python3

tableData = [['apples','oranges','cherries'],
             ['Alice','Bob','Chuck'],
             ['dogs','cats','hamsters']]

def printTable(listInput):
    for i in listInput:
        print(' '.join(map(str, i[0:])))

printTable(tableData)
