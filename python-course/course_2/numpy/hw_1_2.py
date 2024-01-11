import numpy as np

count = 0
for i in range(1000):
    arr = np.random.randint(1, 10, size=100)
    arr1 = arr[arr > 7]
    percent = arr1.size / arr.size * 100
    if percent == 20:
        count += 1

print(f"Количество операций, когда процент чисел больше 7 составлял 20% - {count} из 1000")