a =  [int(i) for i in input().split()]
b = []
sum = 0
for i in a: 
    if a.count(i) == 1:
        b.append(i)
for j in b:
    sum +=j
print(sum)