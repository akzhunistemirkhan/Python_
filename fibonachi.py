#1, 1, 2, 3, 5, 8, 13,  21, 34, 55, 89..
# 1 => 1     5 => 1 1 2 3 5    22 => 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711
n = int(input())
for i in range(1,n+1):
    if i <= 2:
        n = 1
        a = 1 
        b = 1
    if i > 2:
        n = a+b
        a = b
        b = n
    print(n, end=' ')

#2
n = int(input())
a, b = 1, 1
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b

#3
fib1 = fib2 = 1
n = int(input())
if n < 2:
    print(fib1)
else:
    print(fib1, end=' ')
    print(fib2, end=' ')
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')

#4
f, s = 0, 1
for i in range(int(input())):
    f, s = s, f + s
    print(f, end=' ')