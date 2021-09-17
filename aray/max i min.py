# 26670     Максимальная цифра равна 7
#           Минимальная цифра равна 0
a =input()
b = list(a)
print('Максимальная цифра равна',max(b))
print('Минимальная цифра равна',min(b))

#2
n, x, m = int(input()), -1, 10
while n:
    x = max(x, n % 10)
    m = min(m, n % 10)
    n //= 10
print('Максимальная цифра равна', x)
print('Минимальная цифра равна', m)

#3
n = int(input())
minimum = 9
maximum = 0
while n > 0:
    x = n % 10
    if x < minimum:
        minimum = x
    if x > maximum:
        maximum = x
    n = n // 10
print('Максимальная цифра равна', maximum)
print('Минимальная цифра равна', minimum)

#4
n = int(input())
max_n = n%10
min_n = max_n
while n != 0:
    if n % 10 > max_n:
        max_n = n % 10
    if min_n > n % 10:
        min_n = n % 10
    n = n//10
print('Максимальная цифра равна', max_n)
print('Минимальная цифра равна', min_n)