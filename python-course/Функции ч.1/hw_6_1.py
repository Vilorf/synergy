def isPalindrom(str):
    str = "".join(str.lower().split())
    str_reverse = str[::-1]
    return str == str_reverse

print(isPalindrom("hello"))
print(isPalindrom("tamat"))
print(isPalindrom("Искать такси"))