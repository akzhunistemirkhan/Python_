n = int(input())
a = list(range(1,n+ 1)) + list(range(n-1,0,-1))
for i in a:
    print('*'*i)