# use pyperclip to copy and paste strings
import pyperclip, re

input('Copy the desired text to the clipboard, then press Enter.')

# create two regex objects (email, phone)
emailRegex = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+       # username
                        @                       # at symbol
                        [a-zA-Z0-9.-]+          # domain name
                        (\.[a-zA-Z]{2,4})    # domain top level
)''', re.VERBOSE)

phoneRegex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?            # area code
                        (\s|\.|-)                     # separator
                        (\d{3})                       # first 3 digits
                        (\s|\.|-)                     # separator
                        (\d{4})                       # last 4 digits
                        (\s*(x|ext\.|ext)(\d{2,5}))    # extension (if applicable)
)''', re.VERBOSE)

# find all matches of both regexes
text = str(pyperclip.paste()) # string pasted from the clipboard
matches = [] # empty list
for groups in phoneRegex.findall(text): #
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# format the matched strings into a single string for pasting
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Found the following emails and phone numbers:')
    print('\n'.join(matches))
else: # display a message if no matches were found
    print('Could not find any emails or phone numbers.')
