def lyrics_count(word_list):
    d = dict()
    for word in word_list:
        d[word] = d.get(word, 0) + 1
    return d

f = open("session11/queen_don't_stop_me_now.txt")
lyrics = f.read().lower().replace(",", " ").replace("-", " ").split()

h = lyrics_count(lyrics)
# print(h)

from operator import itemgetter
print(sorted(h.items(), key=itemgetter(1), reverse=True))