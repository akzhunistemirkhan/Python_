import sys
def txt(x):
    return (-x[0], x[1])
a = (str(sys.stdin.read()).split())
b = {}
for i in a:
    b[i] = b.get(i, 0) + 1
b = [(x, y) for y, x in b.items()]
b.sort(key=txt)
for i in range(len(b)):
    print(b[i][1])