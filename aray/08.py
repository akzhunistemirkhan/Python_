from random import randint
a =  [randint(1,100) for i in range(10)]
b = [randint(1,100) for i in range(10)]
c = set()
d = dict()
for i in a:
    d[i] = d.get(i,0)+1
for i in d.keys():
    if d[i] == 1:
        c.add(i)
ans = set()
for i in c:
    if i not in b:
        ans.add(i)
print('“Random list1 is',a,'"')
print('“Random list2 is',b,'"')
print('“Unique numbers in list1 are ',ans,'that do not appear in list 2”','"')

