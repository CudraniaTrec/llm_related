#Write a python function to find the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers.
def difference(n) :  
    S = (n*(n + 1))//2;  
    res = S*(S-1);  
    return res;  