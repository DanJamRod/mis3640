def pronounced_dict():
    """ Returns dictionary of words and pronunciations
    """
    pronounced_list = dict()
    f_2 = open("session11/c06d.txt")
    pronounced_list = f_2.read().splitlines()
    pronounced_dict = dict()
    for i in range(len(pronounced_list)):
        pronounced_dict[pronounced_list[i].split(' ')[0]] = pronounced_list[i].split(' ')[2:]
    return pronounced_dict

def triple_word(str):
    """ Checks whether removing the first letter, and removing the second letter (but not the first) of a word are both also unique words
    """
    return str[1:] in pronounced_dict() and (str[0] + str[2:]) in pronounced_dict() and str[0] != str[1] # Without str[0] != str[1], cartalk_homophone() outputs for example AARON, ARON, and ARON all have the phonetic pronunciation ['EH1', 'R', 'AH0', 'N'] 

def homophone(str1, str2):
    """ Checks if two words in pronounced_dict are homophones
    """
    return pronounced_dict()[str1] == pronounced_dict()[str2]

def cartalk_homophone_check(str):
    """ Boolean for: When you remove the first letter, the remaining letters form a homophone of the original word, that is a word that sounds exactly the same. Replace the first letter, that is, put it back and remove the second letter and the result is yet another homophone of the original word.
    """
    str1 = str[1:]
    str2 = str[0] + str[2:]
    if homophone(str1, str2) == True and homophone(str, str1) == True and homophone(str, str2) == True:
        print(f"{str}, {str1}, and {str2} all have the phonetic pronunciation {pronounced_dict()[str]}")

def cartalk_homophone():
    """ Check if any words from pronounced_dict() fulfil the cartalk_homophone_check
    """
    for word in pronounced_dict():
        if len(word) == 5:
            if triple_word(word) == True:
                cartalk_homophone_check(word)

cartalk_homophone()

# Takes a while to run, so output:
# SCENT, CENT, and SENT all have the phonetic pronunciation ['S', 'EH1', 'N', 'T']

# I'm under no illusions of this being an efficient method (i.e. I know there will be better ways to do this),
# but I don't know much coding so I just tried to break the problem down into smaller ones for the sake of my
# understanding, even if that means it's slow/clunky code
