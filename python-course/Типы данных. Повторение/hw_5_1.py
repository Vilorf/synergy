n = int(input("Количество городов, которые вы хотите вывести: "))
cities = []

for i in range(n):
    cities.append(input("Введите город: "))

print(len(cities) - len(set(cities)), "города повторяются")