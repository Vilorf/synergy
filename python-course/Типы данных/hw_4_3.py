user_str = input("Введите набор чисел: ")
n = int(input("Введите степень возведения чисел: "))

split_str = user_str.split(" ")

print([int(i) ** n for i in split_str])