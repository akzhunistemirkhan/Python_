#3 строки в случайном порядке. Напишите программу, которая выясняет
# можно ли из длин этих строк построить возрастающую арифметическую прогрессию.
#abc
#a          =>   YES
#abcde
a,b,c = len(input()),len(input()),len(input())
if (2*b-c-a)*(2*c-b-a)*(2*a-b-c) == 0:
    print('YES')
else:
    print("NO")

#2
a, b ,c = input(), input(), input()
a = len(a)
b = len(b)
c = len(c)
max_a = max(a, b, c)
min_a = min(a, b, c)
a2 = (a + b + c) - (max_a + min_a)
d = max_a - a2
if a2 == min_a + d:
    print('YES')
else:
    print('NO')

#3
a, b, c = input(), input(), input()
x, y, z = len(a), len(b), len(c)
n1, n3 = max(x, y, z),  min(x, y, z)
n2 = 0
if n3 < x < n1:
    n2 = x
elif n3 < y < n1:
    n2 = y
elif n3 < z < n1:
    n2 = z
if n1 - n2 == n2 - n3:
    print('YES')
else:
    print('NO')