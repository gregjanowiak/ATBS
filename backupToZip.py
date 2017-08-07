#! /usr/bin/env python3

# backs up folder and contents to zip file, filename increments

import zipfile, os, shutil

def backupToZip(folder):
    folder = os.path.abspath(folder) # folder var equals abspath of parameter

    number = 1 # start naming at 1

    while True: # loop forever until break
        # zipFilename is basename of param folder, plus next number, .zip
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename): # if name doesn't exist yet, break
            break
        number += 1 # otherwise increment number by 1

    print('Creating %s...' % (zipFilename))
    # make backupZip a zipfile with name just created in loop, write mode
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    for foldername, subfolders, filenames in os.walk(folder): # walk dir tree
        print('Adding files in %s to compressed backup...' % (foldername))
        backupZip.write(foldername) # write each folder to backupZip

        for filename in filenames: # add all files to backupZip
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername,filename))

    backupZip.close()
    print('Done.')

backupToZip('~/Desktop/testBackup')
# shutil.move(os.path.abspath(zipFilename),'/Users/GregJanowiak/Desktop')
