#Write a function to find the number of elements that occurs before the tuple element in the given tuple.
def count_first_elements(test_tup):
  for count, ele in enumerate(test_tup):
    if isinstance(ele, tuple):
      break
  return (count) 