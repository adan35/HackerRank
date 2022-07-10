
def iszero(string):
  sum_near_zero = int(string[0])
  result = " "
  for i in range(1, len(string)):
    num = int(string[i])
    # check if sum_near_zero - num is closer than zero or sum_near_zero + num
    if abs(sum_near_zero - num) < abs(sum_near_zero + num):
      sum_near_zero -= num
      result += "-"
    else:
      sum_near_zero += num
      result += "+"
  return result if sum_near_zero == 0 else "Not Possible"

exp = input("Enter expression: ")
print(iszero(exp))