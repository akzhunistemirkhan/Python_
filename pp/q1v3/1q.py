a = list(map(int,input()))
count = 0
for i in range(len(a)):
    if a[i] == a[i]:
        count += 1
print(count)