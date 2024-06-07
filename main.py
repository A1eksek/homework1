a = int(input("Укажите начало диапазона"))
b = int(input("Укажите конец диапазона"))

for i in range(a, b+1):
    if i == 2:
        print(i)
        if i == 3:
            print(i)
    if (not i % 2 ==0) and (not i % 3 ==0) and (not i % 5 ==0):
        print(i)

i = 1
while i < 11:
    j = 1
    while j < 11:
        print(i, '*', j, '=', i*j, sep='', end='\t')
        j += 1
    i += 1
    print()

a = int(input("Укажите начало диапазона"))
b = int(input("Укажите конец диапазона"))
for i in range (a, b+1):
    for j in range(1, 11):
        print(i, '*', j, '=', i * j, sep='', end='\t')
    print()