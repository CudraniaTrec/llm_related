
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''

    if not lst:
        return []

    sorted_lst = sorted(lst)
    result = []
    left, right = 0, len(sorted_lst) - 1

    while left <= right:
        if left == right:
            result.append(sorted_lst[left])
        else:
            result.append(sorted_lst[left])
            result.append(sorted_lst[right])
        left += 1
        right -= 1

    return result
def check(candidate):

    # Check some simple cases
    assert candidate([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert candidate([5, 6, 7, 8, 9]) == [5, 9, 6, 8, 7]
    assert candidate([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert candidate([5, 6, 7, 8, 9, 1]) == [1, 9, 5, 8, 6, 7]
    assert candidate([5, 5, 5, 5]) == [5, 5, 5, 5]

    # Check some edge cases that are easy to work out by hand.


check(strange_sort_list)