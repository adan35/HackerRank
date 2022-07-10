import re

def insert_dashes(string):
  pattern = r"(?<=[13579])(?=[13579])"
  return re.sub(pattern, '\1-\2', string)

s = input("Enter input: ")
print(insert_dashes(s))