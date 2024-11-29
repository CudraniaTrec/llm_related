def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    result = []
    for char in s:
        if char.isalpha():
            # Shift the character by 4 positions
            new_char = chr(((ord(char) - ord('a') + 4) % 26) + ord('a')) if char.islower() else \
                           chr(((ord(char) - ord('A') + 4) % 26) + ord('A'))
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)
    result = []
    for char in s:
        if char.isalpha():
            new_char = chr(((ord(char) - ord('a') + 4) % 26) + ord('a')) if char.islower() else \
                            chr(((ord(char) - ord('A') + 4) % 26) + ord('A'))
            result.append(new_char)
    return ''.join(result)
    result = []
    for char in s:
        if char.isalpha():
            new_char = chr(((ord(char) - ord('a') + 4) % 26) + ord('a')) if char.islower() else \
                           chr(((ord(char) - ord('A') + 4) % 26) + ord('A'))
            result.append(new_char)
    return ''.join(result)
def check(candidate):

    # Check some simple cases
    assert candidate('hi') == 'lm', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('asdfghjkl') == 'ewhjklnop', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('gf') == 'kj', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('et') == 'ix', "This prints if this assert fails 1 (good for debugging!)"

    assert candidate('faewfawefaewg')=='jeiajeaijeiak', "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.


check(encrypt)