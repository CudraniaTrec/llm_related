def move_zero(lst):
    non_zero = [x for x in lst if x != 0]
    zero_count = lst.count(0)
    return non_zero + [0] * zero_count
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
assert move_zero([2,3,2,0,0,4,0,5,0]) == [2,3,2,4,5,0,0,0,0]
assert move_zero([0,1,0,1,1]) == [1,1,1,0,0]