# removes all 0s from the list
def clean_lst(lst):
  clean_lst = []
  for el in lst:
    if el != 0:
      clean_lst.append(el)
  return clean_lst

# converts a dictionary to a string of duplicates
def dict_to_str(dict):
  s = ''
  for key in dict:
    for _ in range(0, dict[key]):
      s += key
  return s

# sorts the either lowercase or upercase or num at a time
def sort_alpha_num(input):
  lst = [0]*130
  sorted_lst = []
  lst_dict = []
  for i in input:
    if type(lst[ord(i)]) is dict:
      lst[ord(i)][i] += 1
    else:
      lst[ord(i)] = {i: 1}
  lst_dict = clean_lst(lst)

  # list of duplicates
  for dic in lst_dict:
    sorted_lst.append(dict_to_str(dic))
  
  return ''.join(sorted_lst)

# sorts the string of numbers such that odd is ahead of even
def odd_ahead_even(input):
  even, odd = [], []
  sorted_lst = sort_alpha_num(input)
  for i in sorted_lst:
    if int(i) % 2 == 0:
      even.append(i)
    else:
      odd.append(i)
  return ''.join(odd) + ''.join(even)

# sorts th alphanumeric characters in the string
def sort(input):
  lower, uper, num = [], [], []
  for i in input:
    if i.isalpha() and i.islower():
      lower.append(i)
    elif i.isalpha() and i.isupper():
      uper.append(i)
    else:
      num.append(i)
  return sort_alpha_num(lower) + sort_alpha_num(uper) + odd_ahead_even(num)


if __name__ == '__main__':
  input = input()
  print(sort(input))



