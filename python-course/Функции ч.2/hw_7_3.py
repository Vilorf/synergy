from functools import reduce

user_list = [4, 76, 2, 31, 5, 16, 94, 143, 27, 58]

def getMax(x, y):
    if x > y:
        return x
    else:
        return y 

maximum = reduce(getMax, user_list)

print(maximum)