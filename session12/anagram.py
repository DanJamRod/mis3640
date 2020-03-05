from itertools import permutations

def make_word_list():
    """Reads lines from a file and builds a list using append.
    returns: list of strings
    """
    word_list = []
    fin = open("session10/words.txt")
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def in_bisect(word_list, word):
    """Checks whether a word is in a list using bisection search.
    Precondition: the words in the list are sorted
    word_list: list of strings
    word: string
    """
    flag = False
    first = 0
    last = len(word_list)
    while flag == False and first <= last:
        middle = int((first + last)/2)
        if middle == len(word_list):
            return False
        elif word_list[middle] == word:
            return True
        elif word < word_list[middle]:
            last = middle - 1
        else:
            first = middle + 1
    return False

def anagram(*str):
    """ Reads a word list from a file and prints all the sets of words that are anagrams
    """
    list = str
    d = dict()
    for str in list:
        anagram_list = [''.join(p) for p in permutations(str)] # Creates list of all permutations of letters in str
        for i in range(len(anagram_list) - 1): # Checks whether duplicate values, removes if so
            for j in range(len(anagram_list) - i - 1):
                if anagram_list[i] == anagram_list[i+j+1]:
                    anagram_list.remove(anagram_list[i])
                    i -= 1   
        anagram_list = [word for word in anagram_list if word in make_word_list()] # Removes permutations that aren't words
        d[tuple(anagram_list)] = len(anagram_list) # Creates a dictionary storing words and how many anagrams
    for anagram_list in sorted(d, key=d.get, reverse=True): # Orders dictionary, and prints anagrams 
        print(anagram_list)
    
anagram("felt", "tar")
# anagram("deltas", "retainers", "generating", "resmelts")