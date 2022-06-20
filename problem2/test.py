from itertools import groupby

# L = [("a", 1), ("a", 2), ("b", 3), ("b", 4)]

# key_func = lambda x: x[0]

# for key, group in groupby(L, key_func):
#     print(key + " :", list(group))

# a_list = [("Animal", "cat"), 
#           ("Animal", "dog"), 
#           ("Bird", "peacock"), 
#           ("Bird", "pigeon")]
  
  
# an_iterator = groupby(a_list, lambda x : x[0])
  
# for key, group in an_iterator:
#     key_and_group = {key : list(group)}
#     print(key_and_group)

L = ["a", "a", "b", "b"]


for key, group in groupby(L):
    print(key + " :", list(group))