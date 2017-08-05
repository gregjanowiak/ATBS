import pprint

message = 'Hello, world!!!!!'
count = {}

for character in message:
    count.setdefault(character, 0) # if character is not in count, then add character and set value to 0
    count[character] += 1

print(pprint.pformat(count))
