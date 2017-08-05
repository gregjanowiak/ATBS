# use pyperclip to copy and paste strings
import pyperclip, re

# input('Copy the desired text to the clipboard, then press Enter.')

# create a regex object (ISMS Ref, Annex Ref)
AnnexRegex = re.compile(r'([A](\.\d{1,2}\.\d\.\d))')

# find all matches of both regexes
text = str(pyperclip.paste()) # string pasted from the clipboard
matches = [] # empty list
for groups in AnnexRegex.findall(text):
    matches.append(groups[0])

# format the matched strings into a single string for pasting
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Found the following ISO 27001 Annex References:')
    print('\n'.join(matches))
else: # display a message if no matches were found
    print('Could not find any ISO 27001 Annex References.')
