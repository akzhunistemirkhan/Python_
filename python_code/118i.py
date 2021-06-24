n = int(input())
a = list(map(int,input().split()))
b = sorted(a,key=int)
num = True
for i in range(n):
    if a[i] != b[i]:
        num = False
if num: 
    print("Interesting")
else:
    print("Not interesting")