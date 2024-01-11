import numpy as np

arr = np.random.randint(1, 10, size=100)
arr1 = arr[arr > 7]
percent = arr1.size / arr.size * 100

print(percent)