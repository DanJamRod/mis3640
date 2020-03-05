def most_frequent(str):
    """ Takes a string and prints the first n letters in decreasing order of frequency
    """
    str = ''.join(x for x in str if x.isalpha()).lower() # removes punctuation, space/line breaks, and upper-case from string
    d = dict()
    for letter in str: # For every letter in the text, start the count at 0 and add 1 every time it appears
        d[letter.lower()] = d.get(letter.lower(), 0)
        d[letter.lower()] += 1
    d_sum = sum(d.values()) # Calculates sum of values (i.e. how many letters in text)
    for letter in sorted(d, key=d.get, reverse=True): # Prints dictionary in order of word frequency
        print(f"{letter} - {100 * d[letter] / d_sum:.2f}%") # Prints letter and %frequency

english = open("session12/english_text_1984.txt").read()
french = open("session12/french_text_les_miserables_tome_I.txt").read()
german = open("session12/german_text_der_tod.txt").read()

# most_frequent("Mr. Jock, TV quiz PhD, bags few lynx")
# most_frequent("Hello, world!")
most_frequent(english)
# most_frequent(french)
# most_frequent(german)