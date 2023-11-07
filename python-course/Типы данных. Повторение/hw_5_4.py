algebra = input("Фамилии школьников, решивших задачу по алгебре: ")
geometry = input("Фамилии школьников, решивших задачу по геометрии: ")
trigonometry = input("Фамилии школьников, решивших задачу по тригонометрии: ")

# Иванов Петров Сидоров Михайлов
# Иванов Михайлов
# Сидоров Михайлов

algebra = algebra.split()
geometry = geometry.split()
trigonometry = trigonometry.split()

wunderkind = [i for i in [j for j in algebra if j in geometry] if i in trigonometry]

if (wunderkind):
    wunderkind.sort()
    print(" ".join(wunderkind))
else:
    print("Все три задачи никто не решил")