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
        if middle == len(word_list): # To fix error in interlock.py caused by zayin -> zyn as zyn would be after zymurgy(last entry)
            return False
        elif word_list[middle] == word:
            return True
        elif word < word_list[middle]:
            last = middle - 1
        else:
            first = middle + 1
    return False

if __name__ == "__main__":
    word_list = make_word_list()

    for word in ["aa", "alien", "allen", "zymurgy"]:
        print(word, "in list", in_bisect(word_list, word))