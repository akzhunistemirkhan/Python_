a = list(map(int,input().split()))
num = 0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] == a[j]:
            num += 1
print(num)            