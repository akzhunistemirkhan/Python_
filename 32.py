#столько символов «+», сколько делителей у этого числа.
#         1+
#         2++
#  5   => 3++
#         4+++
#         5++
n = int(input())
for i in range(1,n+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    print(i,'+'*count,sep='')

n = int(input())
for i in range(1,n+1):
    print(i,end="")
    for j in range(1,i+1):
        if i % j == 0:
            print("+",end="")
    print()    
print()            
