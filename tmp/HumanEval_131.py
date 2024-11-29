
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    product = 1
    has_odd = False
    
    for digit in str(n):
        d = int(digit)
        if d % 2 != 0:
            product *= d
            has_odd = True
            
    return product if has_odd else 0
    product = 1
    has_odd = False
    for digit in str(n):
        d = int(digit)
        if d % 2 != 0:
            product *= d
            has_odd = True
    return product if has_odd else 0
    product = 1
    has_odd = False
    for digit in str(n):
        d = int(digit)
        if d % 2 != 0:
            product *= d
            has_odd = True
    return product if has_odd else 0
def check(candidate):

    # Check some simple cases
    assert candidate(5) == 5
    assert candidate(54) == 5
    assert candidate(120) ==1
    assert candidate(5014) == 5
    assert candidate(98765) == 315

    # Check some edge cases that are easy to work out by hand.


check(digits)