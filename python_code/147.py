a = input().split(' ')
for i in range(1,10):
    cnt = 0
    for j in a:
        if int(j) == i:
            cnt += 1
    print(cnt,end=' ')
print()    