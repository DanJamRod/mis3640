# See triple_letters.py for function showing that there are no triple letter sequence words in words.txt, or the function below would not work 

def how_many_doubles(word):
    """ Calculates how many double letter sequences in a string
    """
    sum_double_letters = 0
    for i in range (len(word)-1):
        if word[i] == word[i+1]:
            sum_double_letters += 1
    return sum_double_letters

# print(how_many_doubles("aabbccddee"))
# print(how_many_doubles("abbcdde"))

def cartalk():
    f = open('session09/words.txt')
    double_letter_words = 0
    for word in f:
        if how_many_doubles(word.strip()) >= 3 :
            double_letter_words += 1
            print(word.strip()) 
    return double_letter_words

print(cartalk())