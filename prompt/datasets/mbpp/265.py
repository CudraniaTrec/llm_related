#Write a function that takes in a list and an integer n and splits a list for every nth element, returning a list of the resulting lists.
def list_split(S, step):
    return [S[i::step] for i in range(step)]