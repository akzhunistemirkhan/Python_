n = int(input())
a = list(map(int,input().split()))
b = list(set(a))
num = False
for i in range(n):
    if a[i] == b[i]:
        num = True
        break
    else: 
        num = False   
        break   
if num == True:
    print("YES")  
else:    
    print("NO")    