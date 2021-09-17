#1
import math
n = int(input())
print(math.factorial(n))
# n!=1⋅2⋅3⋅…⋅n
# 3 => 6

#2
n = int(input())
count = 1
for i in range(1, n + 1):
    count *= i
print(count)

#3
fact = lambda n: 1 if n == 0 else n * fact(n - 1)
print(fact(int(input())))

#4
n = int(input())
res = 1
i = 2
while i <= n:
    res *= i
    i += 1
print(res)