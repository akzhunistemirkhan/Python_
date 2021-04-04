#Сумма факториалов   3 => 9  [1=1][2=2][3=6] => 1+2+6=9
import math
n= int(input())
sum=0
for i in range(1,n+1):
    b=math.factorial(i)
    sum += b
print(sum)

n = int(input())
a = 1
b = 0
for i in range(1, n + 1):
    a *= i
    b += a
print(b)
