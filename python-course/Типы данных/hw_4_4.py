user_str = input("Введите текст: ")
double = input("Введите символ, вхождение которого надо удвоить: ")

new_str = user_str.replace(double, double * 2)
print(new_str)