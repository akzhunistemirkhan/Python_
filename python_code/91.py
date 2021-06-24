#макс и  мин числа 8945 => Максимальная цифра равна 9
#                          Минимальная цифра равна 4
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

a =input()
b = list(a)
print('Максимальная цифра равна',max(b))
print('Минимальная цифра равна',min(b))

n, x, m = int(input()), -1, 10
while n:
    x = max(x, n % 10)
    m = min(m, n % 10)
    n //= 10
print('Максимальная цифра равна', x)
print('Минимальная цифра равна', m)

