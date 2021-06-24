n = int(input())
a = list(map(int,input().split()))
max = a[0]
min = a[0]
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
    else:
        min = a[i]
print(max, min)
print(max - min)

