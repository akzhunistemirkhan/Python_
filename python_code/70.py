#количества различных элементов
a = input().split()
for i in range(0,len(a)):
    n_map = set(a)
count = 0
for i in range(0,len(n_map)):
        count += 1
print(count)