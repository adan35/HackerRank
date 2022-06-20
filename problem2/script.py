from itertools import groupby

def compressed_string(string):
    L = list(string)
    for key, group in groupby(L):
      print((len(list(group)), int(key)), end=' ')

if __name__ == "__main__":
  input = input()
  compressed_string(input)