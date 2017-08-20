#! /usr/bin/env python3

# tabulates population and num of census tracts per county

import openpyxl, pprint

print('Opening workbook...')

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}

# TODO: Fill in countyData

print('Reading rows...')
for row in range(2, sheet.max_row + 1):
    # each row holds data for one tracts
    state = sheet['B' + str(row)].value
    county = sheet['C' +str(row)].value
    pop = sheet['D' + str(row)].value

    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)

# open a new text file and write countydata to it
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')
