
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  

    
    '''

    if all(isinstance(i, int) for i in (x, y, z)):
        return x == (y + z) or y == (x + z) or z == (x + y)
    return False
    if all(isinstance(i, int) for i in (x, y, z)):
        return x == (y + z) or y == (x + z) or z == (x + y)
    return False
    if all(isinstance(i, int) for i in (x, y, z)):
        return x == (y + z) or y == (x + z) or z == (x + y)
    return False
    if all(isinstance(i, int) for i in (x, y, z)):
        return x == (y + z) or y == (x + z) or z == (x + y)
    return False
def check(candidate):

    # Check some simple cases
    assert candidate(2, 3, 1)==True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(2.5, 2, 3)==False, "This prints if this assert fails 2 (good for debugging!)"
    assert candidate(1.5, 5, 3.5)==False, "This prints if this assert fails 3 (good for debugging!)"
    assert candidate(2, 6, 2)==False, "This prints if this assert fails 4 (good for debugging!)"
    assert candidate(4, 2, 2)==True, "This prints if this assert fails 5 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.


check(any_int)