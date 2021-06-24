n = int(input())
a = list(map(int, input().split()))
count=0
for i in range(len(a)):
    b = a[i]%10
    c = (a[i]%100)//10
    d = a[i] // 100
    
    if d == 0:
        count+=1
    elif c == 0:
        count+=1
    elif b == 0:
        count+=1
print(count)