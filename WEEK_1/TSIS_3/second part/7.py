import sys
sys.setrecursionlimit(10**7)
def count(s):
    x[s] += 1
    if(s in b):
        return
    count(tree[s])
tree, x, b = {}, {}, []
n = int(input())
for i in range(n - 1):
    a = input().split()
    if a[1] not in tree.values() and a[1] not in tree.keys():
        b.append(a[1])
        x.update({a[1]:0})
    tree.update({a[0]:a[1]})
    x.update({a[0]:0})
    count(a[1])
y = sorted(x.keys())
for i in y:
    print(i, x[i])