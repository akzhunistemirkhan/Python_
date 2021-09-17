#φ0=1, φ1=1, φn=φn-1+φn-2
# 3 => 3

n = int(input())
if n == 0:
    a = 1
if n == 1:
    b = 1
a,b = 1,1
for i in range(2,n+1):
    a, b = b, a+b
print(b)

