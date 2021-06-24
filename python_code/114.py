#проверка на уникальность
n = int(input())
a = list(map(int,input().split()))
for i in range(n-1):
    for j in range(i+1,n):
        if a[i] == a[j]:
            print("NO")
            quit()
print("YES")