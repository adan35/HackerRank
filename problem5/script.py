import re

def validate_postal_codes(string):
    pattern1 = r"^[1-9][0-9]{5,5}$"
    pattern2 = r"(\d)(?=\d\1)"
    if re.match(pattern1, string):
        if len(re.findall(pattern2, string)) < 1:
            return True
    return False

print(validate_postal_codes("552523"))