def getFormatName(name, surname, patronymic, age):
    return f"{surname} {name} {patronymic} {age} г.р. зарегистрирован"

print(getFormatName("Иван", "Иванов", "Иванович", 1973))