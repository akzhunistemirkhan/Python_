# Концом последовательности является любое число не делящееся на 7
49
2401
4809
# 0       => 49
# 2          2401
# 10         4809
# 100          0
a = int(input())
while a%7 == 0:
    print(a)
    a =int(input())

#2
n = int(input())
while not n % 7:
    print(n)
    n = int(input())