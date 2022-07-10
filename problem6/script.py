def asciisort(string):
    return ''.join(sorted(string, key=lambda x: ord(x)))

print(asciisort("bbccdefbbaa"))