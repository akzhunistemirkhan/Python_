a = input().split()
for i in range(1,len(a),2):
    if int(a[i]) % 2 != 0:
        a[i-1],a[i] = a[i],a[i-1]
print(a[i],end=' ')    
