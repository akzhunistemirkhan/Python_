# Концом последовательности является любое отрицательное число.
i = int(input())
total = 0
while i >= 0:
    total += i
    i+=1
    i = int(input())
print(total)

#2
n = int(input())
a = 0
while n == abs(n): # такое сравнение ))
    a += n
    n = int(input())
print(a)