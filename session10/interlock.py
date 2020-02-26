from inlist import make_word_list, in_bisect


def interlock(word_list, word):
    """Checks whether a word contains two interleaved words.
    word_list: list of strings
    word: string
    """
    word_1 = word[::2]
    word_2 = word[1::2]
    return in_bisect(word_list, word_1) and in_bisect(word_list, word_2)

def interlock_general(word_list, word, n):
    """Checks whether a word contains n interleaved words.
    word_list: list of strings
    word: string
    n: number of interleaved words
    """
    for i in range(n):
        word_x = word[i::n]
        if in_bisect(word_list, word_x) == False:
            return False
    return True


if __name__ == "__main__":
    word_list = make_word_list()

    # for word in word_list:
    #     if interlock(word_list, word):
    #         print(word, word[::2], word[1::2])

    for word in word_list:
        if interlock_general(word_list, word, 3):
            print(word, word[0::3], word[1::3], word[2::3])

    # for word in word_list:
    #     if interlock_general(word_list, word, 6):
    #         print(word, word[0::6], word[1::6], word[2::6], word[3::6], word[4::6], word[5::6])