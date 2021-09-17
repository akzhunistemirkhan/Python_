a, b = map(int, input().split())
c = [int(i) for i in input().split()]
d = []
for i in range(a, b+1):
    d.append(i)
num = list(set(d) - set(c))
print(*sorted(num))