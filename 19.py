#четные индексы  1 2 3 4 5 => 1 3 5
a = input().split()
for i in range(0,len(a)):
    if i % 2 == 0:
        print(a[i],end=' ')
