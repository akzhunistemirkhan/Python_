#1
def maximum(a,b,c):
    if a >= b:
        if c >= a:
            return c 
        else:
            return a 
    else:
        if c >= b:
            return c 
        else:
            return b
a,b,c = map(int,input().split())
print(maximum(a,b,c))                            

#2
def function(a):
    sum = 0
    for i in a:
        sum += i
    return sum
a = list(map(int,input().split()))    
print(function(a))

#3
def function(a):
    sum = 1
    for i in a:
        sum *= i
    return sum
a = list(map(int,input().split()))    
print(function(a))

#4
def reverse(a):
    return a[::-1]
a = input()
print(reverse(a))    

#5
def factorial(a):
    if a == 1:
        return 1
    return a*factorial(a-1)
a = int(input())
print(factorial(a))       

#6
def function(a,b,n):
    if n>=a and n<=b:
        return True
    else:
        return False
a,b,n = map(int,input().split())
if function(a,b,n):
    print('YES')
else:
    print('NO')
    
#8
def f(a):
    b = list()
    for i in a:
        if i not in b:
            b.append(i)
    return b
a = list(map(int,input().split()))
print(f(a))

#9
def isPrime(a):
    if a<=1:
        return False
    for i in range(2,a):
        if a%i==0:
            return False
    return True
a = int(input())
if isPrime(a):
    print("Prime")
else:
    print("Not prime")
    
#10
def func(a):
    for i in a:
        if i%2==0:
            print(i,end=' ')
a = list(map(int,input().split()))
func(a)

#12
def palindrom(a):
    b = a[::-1]
    for i in range(len(a)):
        if b[i]!=a[i]:
            return False
    return True
a = input()
if palindrom(a):
    print("YES")
else:
    print("NO"
          
#15
def sort(a):
    a.sort()
    print(*a,sep="-")
a = input().split("-")   
sort(a)
    
#16
def function(a):
    for i in range(0,31):
        b = i**2
        a.append(b)
        print(b,end=" ")
a=list()  
function(a)     
 


