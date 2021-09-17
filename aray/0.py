a,b = set(map(int,input().split()))
b = set(map(int,input().split()))
for i in range(a,b+1):
    print(*sorted(i.union(b)))