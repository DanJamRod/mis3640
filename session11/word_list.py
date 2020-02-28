def word_list():
    """
    Returns list of words in a dictionary
    """
    word_list = dict()
    f = open("session11/words.txt")
    word_list = f.read().split()
    return word_list

# print("hello" in word_list())
# print("helo" in word_list())