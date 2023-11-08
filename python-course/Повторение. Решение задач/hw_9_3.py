num = int(input("Введите число у которого хотите найти делители: "))
dividers = []

for i in range(1, num + 1):
    if num % i == 0:
        dividers.append(i)

print(f"Делители числа {num} - {dividers}")