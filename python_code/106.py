#встречается ли заданное число x в данном массиве.
n = int(input())
a = list(map(int,input().split()))
k = int(input())
num = False
for i in range(n):
    if a[i]==k:
        num = True
        break
if num == True:
    print("YES")
else:
    print("NO")    
        