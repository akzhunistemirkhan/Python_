#самый близкий по величине к  данному числу.
n=int(input())
a=list(map(int,input().split()))
k=int(input())
min = abs(k - a[0])
near = a[0]
for i in range(n):
    
    if min > abs(k - a[i]):
        near = a[i]
        min = abs(k - a[i])
print(near)        