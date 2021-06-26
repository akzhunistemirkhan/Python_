v = {}
for i in range(int(input())):
    a = input().split()
    v.update({a[0]:a[1]})
x = input()
if x in v.keys():
    print(v[x])
else:
    for i in v.keys():
        if v[i] == x:
            print(i)