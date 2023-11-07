user_list = list(range(1, 100))

finded = list(filter(lambda i: i % 12 == 0 or i % 13 == 0, user_list))

print(finded)