a, b = map(int,input().split())
c = input().split()
for i in range(a, b+1):
    s= i.intersection(c)
print(s, end=' ')