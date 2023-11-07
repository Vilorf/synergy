user_str = input("Введите текст: ")

str_split = user_str.split()

# на этом заканчиваю свое сочинение. поставьте пятерку, Мария Ивановна! я очень старалась!

for i in range(len(str_split)):
    if str_split[i][-1] in ".!?" and i + 1 < len(str_split):
        str_split[i + 1] = str_split[i + 1].replace(str_split[i + 1][0], str_split[i + 1][0].upper())
    elif i == 0:
        str_split[i] = str_split[i].replace(str_split[i][0], str_split[i][0].upper())

str_join = " ".join(str_split)
print(str_join)