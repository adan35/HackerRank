import math

def encryption(a):
  result = ""
  a = a.replace(" ", "")
  sqr = math.sqrt(len(a)).real
  floor = math.floor(sqr)
  ceil = math.ceil(sqr)
  for i in range(ceil):
    count = i
    for _ in range(floor+1):
      if count >= len(a):
        break
      result += a[count]
      count += ceil
    result += ' '
  return result

input = input()
print(encryption(input))