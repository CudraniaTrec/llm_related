#Write a python function to check whether any value in a sequence exists in a sequence or not.
def overlapping(list1,list2):  
    for i in range(len(list1)): 
        for j in range(len(list2)): 
            if(list1[i]==list2[j]): 
                return True
    return False