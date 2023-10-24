user_str = input("Введите текст: ")

while "(" in user_str:
    a = user_str.find("(")
    b = user_str.find(")")

    print(user_str[a+1:b])
    user_str = user_str[b+1:]