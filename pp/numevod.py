n = int(input())
a = list(map(int,input().split()))
count_ev = 0
count_odd = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
        count_ev += 1
    if a[i] % 2 != 0:
        count_odd += 1
print(count_ev, count_odd)
