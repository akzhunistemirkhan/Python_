a = int(input())
N = int(input())
k = int(2) 
for k in range(a, N+1):
 
    prime = True
    
    for i in range(2, k):
        if k%i == 0:
            prime = False
            break
 
    if prime:
        print(k)

    
    