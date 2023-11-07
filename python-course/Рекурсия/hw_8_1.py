list1 = [81, 15, 18, 46, 64, 85, 74, 8, 20]
list2 = [14, 5, 83, 99, 11, 66, 98, 30, 58, 77, 99, 82, 75, 63]

def getMax(user_list):
    if len(user_list) == 1:
        return user_list[0]

    mx = user_list.pop()
    cur = user_list.pop()

    if cur > mx:
        user_list.append(cur)
        return getMax(user_list)
    else:
        user_list.append(mx)
        return getMax(user_list)

print(getMax(list1))
print(getMax(list2))