
def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''

    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        return sum(1 for char in txt if char.islower() and (ord(char) - ord('a')) % 2 == 1)
    if ',' in txt:
        return txt.split(',')
    return sum(1 for c in txt if c.islower() and (ord(c) - ord('a')) % 2 != 0)
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        return sum(1 for char in txt if char.islower() and (ord(char) - ord('a')) % 2 == 1)
    if ',' in txt:
        return txt.split(',')
    return sum(1 for c in txt if c.islower() and (ord(c) - ord('a')) % 2 == 1)
def check(candidate):

    assert candidate("Hello world!") == ["Hello","world!"]
    assert candidate("Hello,world!") == ["Hello","world!"]
    assert candidate("Hello world,!") == ["Hello","world,!"]
    assert candidate("Hello,Hello,world !") == ["Hello,Hello,world","!"]
    assert candidate("abcdef") == 3

check(split_words)