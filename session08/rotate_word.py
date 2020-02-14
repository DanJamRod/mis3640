def letter_cypher(letter, n):
    """ Ceaser cypher moving letter down the alphabet by n places
    """
    if ord("a") <= ord(letter) <= ord("z"):
        return (ord(letter) + n - ord("a")) % 26 + ord("a")
    elif ord("A") <= ord(letter) <= ord("Z"):
        return (ord(letter) + n - ord("A")) % 26 + ord("A")
    else:
        return ord(letter)

def rotate_word(str, n):
    """ Ceaser cypher moving string down the alphabet by n places
    """
    deciphered = ""
    for i in range(len(str)):
        deciphered += (chr(letter_cypher(str[i],n))) 
    return deciphered
        
# print(rotate_word("Cheer", 7))
# print(rotate_word("Melon", -10))
print(rotate_word("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.",2))
# print(rotate_word("map", 2))