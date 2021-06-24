#         1
# 3 =>    2 3
#         4 5 6
n = int(input())
total = 0
for i in range(1,n+1):
    for j in range(i):
        total += 1
        print(total,end=' ')
    print()