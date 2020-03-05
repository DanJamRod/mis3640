def sumall(*nums):
    """ Takes any number of arguments and returns their sum
    """
    sum = 0
    for num in nums: # For every number, add it to the sum
        sum += num
    return sum

print(sumall(1))
print(sumall(1,2))
print(sumall(1,2,3))