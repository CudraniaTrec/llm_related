
def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """

    if n > m:
        return -1
    total_sum = sum(range(n, m + 1))
    count = m - n + 1
    avg = round(total_sum / count)
    return bin(avg)
    if n > m:
        return -1
    total_sum = sum(range(n, m + 1))
    count = m - n + 1
    avg = round(total_sum / count)
    return bin(avg)
    if n > m:
        return -1
    total_sum = sum(range(n, m + 1))
    count = m - n + 1
    avg = round(total_sum / count)
    return bin(avg)
def check(candidate):

    # Check some simple cases
    assert candidate(1, 5) == "0b11"
    assert candidate(7, 13) == "0b1010"
    assert candidate(964,977) == "0b1111001010"
    assert candidate(996,997) == "0b1111100100"
    assert candidate(560,851) == "0b1011000010"


    # Check some edge cases that are easy to work out by hand.


check(rounded_avg)