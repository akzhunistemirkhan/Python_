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