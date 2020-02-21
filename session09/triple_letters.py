def how_many_triples(word):
    """ Calculates how many triple letter sequences in a string
    """
    sum_triple_letters = 0
    for i in range (len(word)-2):
        if word[i] == word[i+1] == word [i+2]:
            sum_triple_letters += 1
    return sum_triple_letters

# print(how_many_triples("aaabbbcccdddeee"))
# print(how_many_triples("abbbccddde"))

def triple_letters():
    f = open('session09/words.txt')
    triple_letter_words = 0
    for word in f:
        if how_many_triples(word.strip()) >= 1:
            triple_letter_words += 1
            print(word.strip()) 
    return triple_letter_words

print(triple_letters())