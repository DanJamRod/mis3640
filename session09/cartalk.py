def triple_double(word):
    """ Boolean for whether there are 3 consecutive double letters
    """
    triple_double = False
    for i in range (len(word)-5):
        if word[i] == word[i+1] and word[i+2] == word[i+3] and word[i+4] == word[i+5] :
            triple_double = True
    return triple_double

# print(triple_double("aabbccddee"))
# print(triple_double("abbcdde"))

def cartalk():
    """ List any words in words.txt with 3 consecutive double letters, and the count
    """
    f = open('session09/words.txt')
    triple_double_words = 0
    for word in f:
        if triple_double(word.strip()) == True:
            triple_double_words += 1
            print(word.strip()) 
    return triple_double_words

print(cartalk())