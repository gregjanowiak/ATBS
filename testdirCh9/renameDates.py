#! /usr/bin/env python3
import shutil, os, re

# create a regex to match with american date format
datePattern = re.compile(r'''
    ^(.*?)  # all text before the date
    ((0|1)?\d)- # one or two digits for the month
    ((0|1|2|3)?\d)  # one or two digits for the day
    ((19|20)\d\d)   # four digits for year, starting with 19 or 20
    (.*?)$  # all text after the date
''', re.VERBOSE)

# loop through files in working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    if mo == None:
        continue

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # form the new euro filename
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # get the full, absolute file paths
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    print('Renaming file %s to %s...' % (amerFilename,euroFilename))
    # shutil.move(amerFilename, euroFilename)
