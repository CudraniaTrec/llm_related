#Write a python function to calculate the product of the unique numbers in a given list.
def unique_product(list_data):
    temp = list(set(list_data))
    p = 1
    for i in temp:
        p *= i
    return p