
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """

    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)
    return sum(lst[i] for i in range(len(lst)) if i % 2 == 0 and lst[i] % 2 != 0)
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)
def check(candidate):

    # Check some simple cases
    assert candidate([5, 8, 7, 1])    == 12
    assert candidate([3, 3, 3, 3, 3]) == 9
    assert candidate([30, 13, 24, 321]) == 0
    assert candidate([5, 9]) == 5
    assert candidate([2, 4, 8]) == 0

    # Check some edge cases that are easy to work out by hand.


check(solution)