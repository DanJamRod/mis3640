import word_list

def has_duplicates(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[i] == list[j+i+1]:
                return True
    return False

print(has_duplicates(["a", "b", "c", "d", "e", "f", "g", "h"]))
print(has_duplicates(["a", "b", "c", "d", "e", "f", "g", "h", "a"]))
# print(has_duplicates(word_list.word_list())) # This one may take a while!