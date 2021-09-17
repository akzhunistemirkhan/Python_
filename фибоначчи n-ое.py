#a0 = 0, a1 = 1, ak = ak-1 + ak-2   найти N-е число Фибоначчи
#3 => 2

n = int(input())
if n == 0:
    print(0)
else:
    a,b = 0,1
    for i in range(2, n+1):
        a, b = b, a+b
    print(b)



