def product(*nums):
    """ Takes any number of arguments and returns their product
    """
    product = 1
    for num in nums: # For every number, multiply it to the product
        product *= num
    return product

print(product(1))
print(product(1,2))
print(product(1,2,3))