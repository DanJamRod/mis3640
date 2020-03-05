def anagram(str):
    """ List all anagrams of a word
    """
    word_list = []
    fin = open("session10/words.txt")
    for line in fin:
        word = line.strip()
        word_list.append(word)
    anagrams = []
    for word in word_list:
        if sorted(word) == sorted(str):
            anagrams.append(word)
    return anagrams

def print_anagrams(*str):
    """ Puts multiple strings' anagrams into a dictionary, prints in order of most anagrams
    """
    d = {}
    for str in str:
        d[tuple(anagram(str))] = len(list(anagram(str))) # List of anagrams is key, number of anagrams is value
    for anagram_list in sorted(d, key=d.get, reverse=True): # Orders dictionary, and prints anagrams 
        print(anagram_list)

print_anagrams("deltas", "retainers", "generating", "resmelts")