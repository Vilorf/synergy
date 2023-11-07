# После долгих, холодных дней пришла весна. Светит и греет солнце.
# слеПо гидолх, лодхоных нейд лашпри навес. веСтит и регет соцелн.

text = input("Введите текст: ")
anagram = input("Введите анаграмму: ")

text = text.split()
anagram = anagram.split()

for i in range(len(text)):
    if len(text[i]) == len(anagram[i]) and set(text[i]) == set(anagram[i]):
        continue
    else:
        print("Второй текст не является анаграммой")
        exit()

print("Второй текст является анаграммой")