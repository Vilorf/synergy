a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

nok = int()
for i in range(1, a * b + 1):
    if i % a == 0 and i % b == 0:
        nok = i
        break

print(f"Наименьшее общее кратное чисел {a} и {b} - {i}")