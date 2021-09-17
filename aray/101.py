def gcd(a,b):
    for i in range(1,min(a,b)):
        if a%i==0 and b%i==0:
            return i
a = int(input())
b = int(input())
print(gcd(a,b))
    


