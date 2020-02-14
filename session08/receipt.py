def cost(str):
    """ Cost of a string if a = $1, b = $2 etc
    """
    cost = 0
    str = str.replace(" ","") # Removes space-character from count (otherwise would be ord("32")-96 = -64)
    for i in range(len(str)):
        cost += ord(str[i])-96
    return cost

def receipt(*item):
    """You walk into a store where each item is priced according to the letters in its name: 'a' costs \$1, 'b' is \$2, and so on. Write a program that prints a receipt for this wacky store
    """
    longest = max(len(x) for x in item)
    total = 0
    for i in range(len(item)):
        total += cost(item[i])
        print(f"{item[i]:{8+longest}s}${cost(item[i]):>6.2f}")
    print(f"-"*(15+longest))
    space = " "
    print(f"Total {space*(2+longest)}${total:>6.2f}")

receipt("bananas", "rice", "paprika", "potato chips")
# receipt("bananas", "rice", "paprika")
# receipt("bananas", "rice", "paprika", "potato chips", "twinnings earl grey teabags")
print(ord(" "))