#популяция Напишите программу, которая предсказывает размер популяции организмов.
#  Программа должна выводить размер популяции в каждый день, начиная с 11 и заканчивая nn-м днем.
# 10          1 10.0
# 50   =>     2 15.0
# 6           3 22.5
#             4 33.75
#             5 50.625
#             6 75.9375
#мой код 1)
a,b,c = int(input()),int(input()),int(input())
print('1',float(a))
for i in range(c-1):
    a = a+a*b/100
    print(i+2,a)

#2й код
m, p, n = int(input()), int(input()) * 0.01 + 1, int(input())
for i in range(n):
    print(i + 1, m)
    m = m * p

#3
m, p, n = int(input()), int(input()), int(input())
for i in range(n):
    print(i + 1, m)
    m *= 1 + p / 100

#4
m, p, n = int(input()), int(input()), int(input())
for i in range(1,n + 1):
    print(i, m)
    m += (m / 100) * p
