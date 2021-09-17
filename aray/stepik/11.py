# 3  => ***
#       **
#       *

a = int(input())
for a in reversed(range(a+1)):
    print(a*'*')


n = int(input())
for i in range(n):
    print('*' * n)
    n -= 1

a = int(input())
for i in range (a):
    print('*' * (a - i))