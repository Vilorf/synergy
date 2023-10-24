num = int(input("Введите число до которого будет проверяться кратность: "))

for i in range(num):
    if (i % 7 == 0):
        print(f"Число {i} кратно 7")
    else: continue