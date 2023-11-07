def getMax(a, b, c=0):
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c

    return maximum

print(getMax(5, 12, 45))
print(getMax(81, 3))