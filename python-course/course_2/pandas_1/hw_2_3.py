import pandas as pd

data = {
    "Name": pd.Series(["Иван", "Петр", "Алексей", "Владимир", "Олег"]),
    "Surname": pd.Series(["Иванов", "Петров", "Алексеев", "Владимиров", "Олегов"]),
    "Patronymic": pd.Series(["Иванович", "Петрович", "Алексеевич", "Владимирович", "Олегович"]),
    "Email": pd.Series(["ivanoff@mail.ru", "petr@mail.ru", "alex@mail.ru", "vlad@mail.ru", "oleg@mail.ru"])
}

df = pd.DataFrame(data)

df.to_csv("file.csv")