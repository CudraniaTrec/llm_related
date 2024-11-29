def split_Arr(arr, n):
    return arr[n:] + arr[:n]
assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
assert split_Arr([1,2,3,4],1) == [2,3,4,1]
assert split_Arr([0,1,2,3,4,5,6,7],3) == [3,4,5,6,7,0,1,2]