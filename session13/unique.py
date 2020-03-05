def unique(str):
    unique = []
    for i in range(len(str)):
        if str[i] not in unique:
            unique.append(str[i])
    return unique

print(unique("bookkeeper"))
print(sorted(set("bookkeeper")))

s1 = {1, 2, 3}
s2 = {2, 3, 4}

print(s1 & s2)
print(s1 | s2)
print(s1.difference(s2))
print(s2.difference(s1))