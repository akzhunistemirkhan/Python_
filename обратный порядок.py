a = input()
b = list(a)
b.reverse()
i=int(0)
for i in b:
    print(i)

# 12345 => 5
#          4
#          3
#          2
#          1

#2
n = int(input())
while n:
    print(n % 10)
    n //= 10

#3
num = int(input()) 
while num != 0:
    print(num % 10)    
    num = num // 10

#4
[print(i) for i in input()[::-1]]

#5
print( *reversed( input()), sep = '\n' )           
