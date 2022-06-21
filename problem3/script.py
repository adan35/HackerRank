import re

def validate_card_num(string):
  # check for the very first number
  pattern1 = r"^4|5|6"
  # check if there are dashes at right places
  pattern2 = r"(\d{4})(-?)(\d{4})(\2\d{4}){2}"
  # check for repeated numbers within 16 digits
  pattern3 = r"((\d)(?!\2{3})){16}$"

  flag = True
  if re.match(pattern1, string):
    if re.match(pattern2, string):
      string = string.replace("-", "")
      if re.match(pattern3, string):
          flag = False
          print("Valid")

  if flag:
    print("Invalid")

if __name__ == "__main__":
  N = int(input())
  for i in range(N):
    string = input()
    validate_card_num(string)