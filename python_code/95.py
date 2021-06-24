#Напишите программу, которая вычисляет сумму всех его делителей.
# 10 => 18
# 3 => 4
n = int(input())
sum = 0
for i in range(1,n+1):
    if n%i == 0:
        sum += i
    print(sum)