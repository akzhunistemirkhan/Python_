a,b = int(input()),int(input())
for i in range(a,b+1):
    if a < b:
        print(i)     
for i in range(a,b-1,-1):
    if a > b:
        print(i)
if a == b:
    print(a)

#2
n, m = int(input()), int(input())
if n < m:
    for i in range(n, m + 1):
        print(i)
else:
    for i in range(n, m - 1, -1):
        print(i)
#3
m, n = int(input()), int(input())
k = 1 - 2 * (m > n)
for i in range(m, n + k, k):
    print(i)
