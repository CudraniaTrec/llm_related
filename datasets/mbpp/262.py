#Write a function that takes in a list and an integer L and splits the given list into two parts where the length of the first part of the list is L, and returns the resulting lists in a tuple.
def split_two_parts(list1, L):
    return list1[:L], list1[L:]