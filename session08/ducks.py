prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter in "OQ":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)