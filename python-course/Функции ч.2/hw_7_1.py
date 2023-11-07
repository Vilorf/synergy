list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

summ = list(map(lambda el1, el2: el1 + el2, list1, list2))

print(summ)