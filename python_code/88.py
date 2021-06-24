#Асимптотическое приближение  (1+1/2+1/3+...+1/n) - ln(n)  [ln(n) = log(n)]
#10 => 0.6263831609
import math
n = int(input())
num = 0
for i in range(1,n+1):
    num += 1/i
print(num - math.log(n))