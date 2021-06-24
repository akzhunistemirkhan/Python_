#четные элементы 1 2 2 3 3 4 => 2 2 4
a = input().split()
for i in range(0,len(a)):
    if int(a[i])%2==0:
        print(a[i],end=' ')