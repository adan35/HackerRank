from collections import Counter

def pairs(k, arr):
  dic = Counter(arr)
  count = 0
  for key in dic:
    if dic[key-k]:
      count += 1
  return count

k = int(input("Enter k: "))
nums = input("Enter nums with spaces in between: ").rstrip().split()
arr = list(map(int, nums))
print(pairs(k, arr))

