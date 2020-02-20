def find_long_words():
    """
    prints only the words with more than 20 characters
    """
    f = open('session09/words.txt')
    for line in f:
        if len(line.strip()) > 20:
            print(line.strip())

# find_long_words()


def has_no_e(word):
    """
    returns True if the given word doesn’t have the letter "e" in it
    """
    return not "e" in word.lower()

# print(has_no_e('Babson'))
# print(has_no_e('EA sports'))

def find_words_no_e():
    """
    returns the percentage of the words that don't have the letter "e"
    """
    f = open('session09/words.txt')
    num_no_e = 0
    num_words = 0
    for word in f:
        num_words += 1
        if has_no_e(word.strip()) == True:
            num_no_e += 1
            print(word.strip()) 
    return num_no_e/num_words

# perc_no_e = find_words_no_e()
# print(f'The percentage of the words with no "e" is {perc_no_e*100:.2f}%.')


def avoids(word, forbidden):
    """
    returns True if the given word does not use any of the forbidden letters
    """
    for letter in word:
        if letter in forbidden:
            return False
    return True

# print(avoids('Babson', 'abcde'))
# print(avoids('Boston', 'xyz'))


def find_words_no_vowels():
    """
    returns the percentage of the words that don't vowel letters
    """
    f = open('session09/words.txt')
    num_no_vowels = 0
    num_words = 0
    for word in f:
        num_words += 1
        if avoids(word.strip(),"aeiou") == True:
            num_no_vowels += 1
            print(word.strip()) 
    return num_no_vowels/num_words

# perc_no_vowel = find_words_no_vowels()
# print(f'The percentage of the words without vowel letters is {perc_no_vowel*100:.2f}%.')


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the list.
    """
    for letter in word:
        if letter not in available:
            return False
    return True 

# print(uses_only('Babson', 'aBbsonxyz'))
# print(uses_only('college', 'aBbsonxyz'))


def find_words_only_use_planets():
    f = open('session09/words.txt')
    num_only_use_planets = 0
    for word in f:
        if uses_only(word.strip(),"planets") == True:
            num_only_use_planets += 1
            print(word.strip()) 
    return num_only_use_planets

# print('Number of words that use only letters from "planet" is', find_words_only_use_planets())


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    pass


# please write test cases


def find_words_using_all_vowels():
    """
    return the number of the words that use all the vowel letters
    """
    pass


# print('The number of words that use all the vowels:', find_words_using_all_vowels())


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    pass


# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))


def find_abecedarian_words():
    """
    returns the number of abecedarian words
    """
    pass


# print(find_abecedarian_words())


def is_abecedarian_using_recursion(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    pass


# print(is_abecedarian_using_recursion('abcdef'))


def is_abecedarian_using_while(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    pass