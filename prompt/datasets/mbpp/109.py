#Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.
def odd_Equivalent(s,n): 
    count=0
    for i in range(0,n): 
        if (s[i] == '1'): 
            count = count + 1
    return count 