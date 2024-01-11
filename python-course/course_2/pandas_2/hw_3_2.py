import pandas as pd

csv = pd.read_csv('Customers.csv', delimiter=";")

filter1 = csv[(csv["Age"] < 30) & (csv["Income"] < 30000)]
filter2 = csv[(csv["Profession"] == "Lawyer") & (csv["Work Experience"] > 5)]
print(f"{filter1}\n------------------------\n{filter2}")