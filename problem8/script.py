def alphaEncoding(string):
  s = ''
  for letter in string:
    if letter.isalpha():
      s += str(ord(letter) - 96)
      continue
    s += letter
  return s

print(alphaEncoding(input("Enter input: ")))