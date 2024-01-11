import pandas as pd

data = {
    "Name": pd.Series(["Иван", "Петр", "Алексей"]),
    "Surname": pd.Series(["Иванов", "Петров", "Алексеев"]),
    "Patronymic": pd.Series(["Иванович", "Петрович", "Алексеевич"]),
    "Email": pd.Series(["ivanoff@mail.ru", "petr@mail.ru", "alex@mail.ru"])
}

df = pd.DataFrame(data)
print(df)