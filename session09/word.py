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
    flag = True
    for letter in required:
            if letter not in word:    
                flag = False
    return flag

# print(uses_all("hello", "helo"))
# print(uses_all("hello", "h"))
# print(uses_all("hello", "world"))


def find_words_using_all_vowels():
    """
    return the number of the words that use all the vowel letters
    """
    f = open('session09/words.txt')
    num_all_vowels = 0
    for word in f:
        if uses_all(word.strip(),"aeiou") == True:
            num_all_vowels += 1
            print(word.strip()) 
    return num_all_vowels

# print('The number of words that use all the vowels:', find_words_using_all_vowels())


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    flag = True
    for i in range(len(word.strip())-1):
        if ord(word[i]) > ord(word[i+1]):
            flag = False
    return flag

# print(is_abecedarian('abcdef'))
# print(is_abecedarian('abcdefa'))


def find_abecedarian_words():
    """
    returns the number of abecedarian words
    """
    f = open('session09/words.txt')
    num_abecedarian = 0
    for word in f:
        if is_abecedarian(word.strip()) == True:
            num_abecedarian += 1
            print(word.strip()) 
    return num_abecedarian

# print('The number of words that are abecedarian:', find_abecedarian_words())


def is_abecedarian_using_recursion(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    if ord(word[0]) > ord(word[1]):
        return False
    word = word[1:]
    if len(word) == 1:
        return True
    return is_abecedarian_using_recursion(word)

# print(is_abecedarian_using_recursion('abcdef'))
# print(is_abecedarian_using_recursion('abcdefa'))


def is_abecedarian_using_while(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    flag = True
    i = 0
    while i < len(word.strip())-2:
        i += 1
        if ord(word[i]) > ord(word[i+1]):
            flag = False
    return flag

# print(is_abecedarian_using_while('abcdef'))
# print(is_abecedarian_using_while('abcdefa'))

# import timeit
# word = "abcdefa"
# print(f"The time taken for is_abecedarian('abcdefa') <for-loop>      to return 1 million times is {timeit.timeit('is_abecedarian(word)','from __main__ import is_abecedarian, word', number=1000000)}")
# print(f"The time taken for is_abecedarian_using_recursion('abcdefa') to return 1 million times is {timeit.timeit('is_abecedarian_using_recursion(word)','from __main__ import is_abecedarian_using_recursion, word', number=1000000)}")
# print(f"The time taken for is_abecedarian_using_while('abcdefa')     to return 1 million times is {timeit.timeit('is_abecedarian_using_while(word)','from __main__ import is_abecedarian_using_while, word', number=1000000)}")
# # For-loop ~ 1.1s
# # Recursion ~ 1.6s (+45%) 
# # While ~ 1.4s (+27%)