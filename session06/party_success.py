def party_success(cigars, is_weekend):
    """
    When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
    """
    if cigars<=40:
        return False
    elif is_weekend:
        return True
    elif cigars <=60:
        return True
    else: return False

print(party_success(30,False))
print(party_success(50,False))
print(party_success(70,False))
print(party_success(70,True))
print(party_success(30,True))