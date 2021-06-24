n = int(input())
a = list(map(int,input().split()))
i = int(0)
for i in range(0,n):
    a[i] = a[i-1]  
print(*a)