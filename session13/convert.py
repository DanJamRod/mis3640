# #string to list to string
# s = "Daniel"
# l = list(s)
# print(l)
# s = ("".join(l))
# print(s)

# # list to dict to list
# list = list("Daniel")
# d = {}
# for letter in list:
#     d[letter] = d.get(letter, 0) + 1
# print(d)
# list = []
# for letter,freq in d.items():
#     list.extend([letter] * freq)
# print(list)

# # list to tuples to list
# list = list("Daniel")
# tuple = tuple(list)
# print(tuple)
# list = list(tuple)
# print(list)

# # list to set to list
# list = list("Daniel")
# set = set(list)
# list = list(set)

# # string to set to string
# string = "Daniel"
# set = set(string)
# list = list(set)

# # string to dict to string
# string = "Daniel"
# d = {}
# for letter in string:
#     d[letter] = d.get(letter, 0) + 1
# s = ''
# for letter, freq in d.items():
#     s += letter * freq

# # string to tuple to string
# string = "Daniel"
# tuple = tuple(string)
# string = ""
# string = "".join(tuple)

# # tuple to set to tuple
# tuple = tuple("Daniel")
# set = set(tuple)
# tuple = tuple(set)

# # dict to tuple
# tuple = tuple(d.keys()) # or .values() or .items()

# # dict to set
# set(d.keys()) # or .values() or .items()

# # string, list, dict
# s = "Daniel"
# a = [1, 2, 3, 4, 5, 6]
# list = list(zip(s, a))
# dict = dict(zip(s, a))