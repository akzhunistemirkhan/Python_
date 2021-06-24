# 1 10 => 2  [от а до b куб число последн цифра 4 или 9 count]
1) 
a=int(input())
b=int(input())
count=0
for i in range(a,b+1):
    if (i**3)%10==4:
        count += 1
    if (i**3)%10==9:
        count += 1
print(count)  

2)
a, b, count = int(input()), int(input()), 0
for i in range(a, b + 1):
    if i**3 % 10 in [4, 9]:
        count += 1
print(count)
3)
import math
a, b = int(input()), int(input())
counter = 0
for i in range(a, b + 1):
    if math.pow(i, 3) % 10 == 4 or math.pow(i, 3) % 10 == 9:
        counter += 1
print(counter)