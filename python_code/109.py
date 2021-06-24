#номер максимального элемента массива
n = int(input())
a = list(map(int,input().split()))
max_num = a[0]
b = 0
for i in range(n):
    if a[i]> max_num:
        max_num = a[i]
        b = i
print(b+1)       