a = input().split()
for n in range(0,len(a)):
    a[0], a[-1] = a[-1],a[0]
    a[1], a[-2] = a[-2],a[1]
print(*a)
