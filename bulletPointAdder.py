#! /usr/bin/env python3

import pyperclip

# paste text from clipboard
text = pyperclip.paste()

# do something to it
lines = text.split('\n')
for i in range(len(lines)): # loop through all indices in the lines list
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

# copy the new text to the clipboard
pyperclip.copy(text)
