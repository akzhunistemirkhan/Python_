n = int(input())
a = list(map(int, input().split()))
sum = 0
average = 0
for i in range(len(a)):
    sum += a[i]
    average = sum/n
print('Average:', average)
print('Sum:', sum)