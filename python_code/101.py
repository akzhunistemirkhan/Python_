n = int(input())
a = list(map(int,input().split()))
a = set()
for i in range(1,n+1):
    for j in range(0,n+1):
        print(i, a[j])    