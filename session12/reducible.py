def create_word_list():
    """ Create list of all words
    """
    word_list = []
    fin = open("session12/words.txt")
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list

def is_reducible(str):
    """ Checks whether a word remains a valid English word, as you remove its letters one at a time"
    """
    word_children = [str] # Creates list, initial term is the word
    for str in word_children:
        for i in range(len(str)):
            if (str[:i]+str[i+1:]) in word_list: # For every word, checks whether any letter can be removed and still is a word
                word_children.append(str[:i]+str[i+1:]) # If so, adds word to string
    # print(word_children) # Uncomment if you want to check progress/method
    return len(word_children[-1]) == 1 # Returns true if word can be reduced to one letter
    
def find_longest_reducible():
    """ Checks for longest reducible word
    """
    d = {}
    for word in word_list:
        if is_reducible(word):
            d[word] = len(word) # If work is reducible, added to dictionary = {word:length}
    return max(d, key=d.get) # Returns key with largest value (i.e. longest work)

word_list = create_word_list() # I know it's bad form to leave outside a function, but runs quicker than if in both functions
print(find_longest_reducible())
# Might take a while! (Eventual) output: "complecting"
# I know these can be done more efficiently, and perhaps with printing the reduction path, I just need more class practice 