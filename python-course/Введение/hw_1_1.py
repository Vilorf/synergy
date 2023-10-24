num = float(input("Введите число: "))
round_num = int(input("Число округления: "))

print(f"Число {num} округлилось до {round_num} знаков после запятой: ", round(num, round_num))