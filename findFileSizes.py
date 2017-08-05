import os

totalFileSize = 0

for filename in os.listdir('/Users/blend/BoringStuff/practice_files'):
    totalFileSize += os.path.getsize(os.path.join('/Users/blend/BoringStuff/practice_files', filename))

print(totalFileSize)
