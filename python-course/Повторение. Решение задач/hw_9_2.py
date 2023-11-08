num = int(input("До какого числа программа будет находить простые числа: "))
simple_num = []

for i in range(2, num + 1):
    simple = True
    for j in range(2, i):
        if i % j == 0:
            simple = False
            break            
            
    if simple:
        simple_num.append(i)

print(simple_num)