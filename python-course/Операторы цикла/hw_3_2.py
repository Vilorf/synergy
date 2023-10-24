num = int(input("Введите число: "))
fac = 1

for i in range(2, num + 1):
    fac *= i

print(f"Факториал числа {num} равен: {fac}")