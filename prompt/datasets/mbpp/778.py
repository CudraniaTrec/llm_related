#Write a function to pack consecutive duplicates of a given list elements into sublists.
from itertools import groupby
def pack_consecutive_duplicates(list1):
    return [list(group) for key, group in groupby(list1)]