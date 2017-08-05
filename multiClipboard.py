#! /usr/bin/env python3

# Usage:
#       multiClipboard.py save <keyword> - Saves clipboard to the keyword
#       multiClipboard.py list - Loads all keywords to the clipboard
#       multiClipboard.py <keyword> - Loads keyword to the clipboard

import pyperclip, shelve, sys

mcbShelf = shelve.open('mcb')

def clearShelf():
    choice = input('This will clear your saved clips, continue? [yes/no]\n')
    if choice == 'yes':
        mcbShelf.clear()
        print('Clips cleared.')
    else:
        print('Clips not cleared.')

# execute script actions based on arguments
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print('Clipboard content saved to keyword %s' % str(sys.argv[2]))
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print('List of keywords loaded to clipboard.')
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print('Content from %s loaded to clipboard.' % str(sys.argv[1]))
    elif sys.argv[1].lower() == 'clear':
        clearShelf()

mcbShelf.close()
